# predictor/forms.py
from django import forms
from .models import Fighter

class FighterForm(forms.ModelForm):
    class Meta:
        model = Fighter
        fields = ['name', 'wins', 'losses', 'win_streak', 'lose_streak', 
                  'avg_sig_strikes_landed', 'avg_sig_strikes_pct', 
                  'avg_takedowns_landed', 'avg_takedown_pct']

class PredictionForm(forms.Form):
    red_fighter = forms.ModelChoiceField(queryset=Fighter.objects.all())
    blue_fighter = forms.ModelChoiceField(queryset=Fighter.objects.all())
    red_odds = forms.FloatField(min_value=0.1)
    blue_odds = forms.FloatField(min_value=0.1)
