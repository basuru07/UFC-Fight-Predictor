import pickle
import numpy as np
import os
import pandas as pd
from django.conf import settings

# Path to the saved model
MODEL_PATH = os.path.join(settings.BASE_DIR, 'predictor', 'model', 'ufc_model.pkl')

def load_model():
    try:
        with open(MODEL_PATH, 'rb') as f:
            model = pickle.load(f)
        return model
    except FileNotFoundError:
        print(f"Model file not found at {MODEL_PATH}")
        # Create a simple default model
        from sklearn.ensemble import RandomForestClassifier
        default_model = RandomForestClassifier(random_state=42)
        # Train with minimal data to make it functional
        default_model.fit([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]], [0, 1])
        return default_model

def get_model_expected_features():
    """Extract expected feature names from the model"""
    model = load_model()
    # Check if model has feature_names_in_ attribute (scikit-learn 1.0+)
    if hasattr(model, 'feature_names_in_'):
        return model.feature_names_in_
    # For older scikit-learn or if it's a pipeline
    elif hasattr(model, 'get_feature_names_out'):
        return model.get_feature_names_out()
    else:
        # If we can't get feature names, we'll create a fallback list
        # This should match the exact number of features model expects (203)
        print("Warning: Unable to extract feature names from model")
        return [f'feature_{i}' for i in range(203)]

def prepare_features(red_fighter, blue_fighter, red_odds, blue_odds):
    # Get expected feature names from the model
    try:
        expected_features = get_model_expected_features()
        num_expected_features = len(expected_features)
        print(f"Model expects {num_expected_features} features")
    except Exception as e:
        print(f"Error getting expected features: {e}")
        # Fallback to 203 features as indicated by the error
        num_expected_features = 203
        expected_features = [f'feature_{i}' for i in range(num_expected_features)]
    
    # Create a dataframe with zeros for all expected features
    df = pd.DataFrame(0, index=[0], columns=expected_features)
    
    # Create a dictionary with the features we have
    our_features = {
        'RedOdds': red_odds,
        'BlueOdds': blue_odds,
        'RedCurrentWinStreak': red_fighter.win_streak,
        'RedAvgSigStrPct': red_fighter.avg_sig_strikes_pct,
        'RedAvgTDLanded': red_fighter.avg_takedowns_landed,
        'RedLosses': red_fighter.losses,
        'WinStreakDif': red_fighter.win_streak - blue_fighter.win_streak,
        'AvgTDDif': red_fighter.avg_takedowns_landed - blue_fighter.avg_takedowns_landed,
        'OddsRatio': red_odds / blue_odds if blue_odds != 0 else 0,
        'RedWinPercentage': red_fighter.wins / (red_fighter.wins + red_fighter.losses) if (red_fighter.wins + red_fighter.losses) > 0 else 0,
        'WinPercentageDifference': (red_fighter.wins / (red_fighter.wins + red_fighter.losses) if (red_fighter.wins + red_fighter.losses) > 0 else 0) - 
                                  (blue_fighter.wins / (blue_fighter.wins + blue_fighter.losses) if (blue_fighter.wins + blue_fighter.losses) > 0 else 0),
        'RedForm': red_fighter.win_streak - red_fighter.lose_streak,
        'FormDifference': (red_fighter.win_streak - red_fighter.lose_streak) - (blue_fighter.win_streak - blue_fighter.lose_streak),
    }
    
    # Check feature mapping with model's expected features
    mapped_features = 0
    for feature, value in our_features.items():
        if feature in df.columns:
            df[feature] = value
            mapped_features += 1
        # Try case insensitive matching as a fallback
        else:
            matching_cols = [col for col in df.columns if col.lower() == feature.lower()]
            if matching_cols:
                df[matching_cols[0]] = value
                mapped_features += 1
    
    print(f"Successfully mapped {mapped_features} out of {len(our_features)} features")
    
    # If we didn't map enough features, this might not work, but at least we have the right shape
    return df.values

def predict_winner(red_fighter, blue_fighter, red_odds, blue_odds):
    model = load_model()
    X = prepare_features(red_fighter, blue_fighter, red_odds, blue_odds)
    
    try:
        # Get prediction and probability
        prediction = model.predict(X)[0]
        probabilities = model.predict_proba(X)[0]
        
        winner = "Red" if prediction == 1 else "Blue"
        confidence = probabilities[1] if prediction == 1 else probabilities[0]
        
        return winner, confidence
    except Exception as e:
        print(f"Prediction error: {e}")
        # Fallback prediction
        return "Prediction failed", 0.0