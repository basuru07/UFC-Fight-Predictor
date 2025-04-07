from django.db import models

class Fighter(models.Model):
    name = models.CharField(max_length=100)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    win_streak = models.IntegerField(default=0)
    lose_streak = models.IntegerField(default=0)
    avg_sig_strikes_landed = models.FloatField(default=0)
    avg_sig_strikes_pct = models.FloatField(default=0)
    avg_takedowns_landed = models.FloatField(default=0)
    avg_takedown_pct = models.FloatField(default=0)
    
    def __str__(self):
        return self.name

class Prediction(models.Model):
    red_fighter = models.ForeignKey(Fighter, related_name='red_fights', on_delete=models.CASCADE)
    blue_fighter = models.ForeignKey(Fighter, related_name='blue_fights', on_delete=models.CASCADE)
    red_odds = models.FloatField()
    blue_odds = models.FloatField()
    predicted_winner = models.CharField(max_length=10)
    prediction_confidence = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.red_fighter.name} vs {self.blue_fighter.name}"
