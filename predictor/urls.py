from django.urls import path
from .views import HomeView, AddFighterView, MakePredictionView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add-fighter/', AddFighterView.as_view(), name='add_fighter'),
    path('make-prediction/', MakePredictionView.as_view(), name='make_prediction'),
]
