# predictor/views.py
from django.shortcuts import render, redirect
from django.views import View
from .forms import FighterForm, PredictionForm
from .models import Fighter, Prediction
from .prediction_model import predict_winner

class HomeView(View):
    def get(self, request):
        prediction_form = PredictionForm()
        fighter_form = FighterForm()
        recent_predictions = Prediction.objects.order_by('-created_at')[:5]
        
        return render(request, 'predictor/home.html', {
            'prediction_form': prediction_form,
            'fighter_form': fighter_form,
            'recent_predictions': recent_predictions
        })

class AddFighterView(View):
    def post(self, request):
        form = FighterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
        return render(request, 'predictor/home.html', {'fighter_form': form})

class MakePredictionView(View):
    def post(self, request):
        form = PredictionForm(request.POST)
        if form.is_valid():
            red_fighter = form.cleaned_data['red_fighter']
            blue_fighter = form.cleaned_data['blue_fighter']
            red_odds = form.cleaned_data['red_odds']
            blue_odds = form.cleaned_data['blue_odds']
            
            winner, confidence = predict_winner(red_fighter, blue_fighter, red_odds, blue_odds)
            
            prediction = Prediction(
                red_fighter=red_fighter,
                blue_fighter=blue_fighter,
                red_odds=red_odds,
                blue_odds=blue_odds,
                predicted_winner=winner,
                prediction_confidence=confidence
            )
            prediction.save()
            
            return render(request, 'predictor/result.html', {
                'prediction': prediction,
                'red_fighter': red_fighter,
                'blue_fighter': blue_fighter
            })
        
        return redirect('home')
