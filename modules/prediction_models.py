import numpy as np
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
import pickle
import os

def load_or_create_model(model_path, model_type='random_forest'):
    """
    Load a model from disk or create a new one if it doesn't exist.
    
    Args:
        model_path (str): Path to the model file
        model_type (str): Type of model to create if loading fails
        
    Returns:
        object: Loaded or created model
    """
    try:
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
        print(f"Model loaded from {model_path}")
        return model
    except (FileNotFoundError, EOFError):
        print(f"Model not found at {model_path}, creating new model")
        if model_type == 'random_forest':
            model = RandomForestRegressor(n_estimators=100, random_state=42)
        elif model_type == 'gradient_boosting':
            model = GradientBoostingRegressor(n_estimators=100, random_state=42)
        else:
            raise ValueError(f"Unknown model type: {model_type}")
        
        # Ensure directory exists
        os.makedirs(os.path.dirname(model_path), exist_ok=True)
        
        return model

def predict_virality(features, model_path='models/trained/virality_predictor.pkl'):
    """
    Predict virality score based on features and parameters.
    
    Args:
        features (pd.DataFrame): Feature matrix
        model_path (str): Path to the model file
        
    Returns:
        float: Predicted virality score (0-100)
    """
    # For demonstration, we'll use a simple rule-based approach with simulated ML
    # In production, you would use a properly trained model
    
    model = load_or_create_model(model_path)
    
    # Simple mock prediction for demonstration
    # In a real app, this would use the loaded model
    base_score = 50
    
    # Weight each feature based on importance
    feature_weights = {
        'mean_growth': 20,
        'momentum': 15,
        'mean_acceleration': 10,
        'growth_volatility': 5
    }
    
    score_adjustment = 0
    for feature, weight in feature_weights.items():
        if feature in features:
            # Normalize the feature value to a -1 to 1 range
            normalized_value = np.clip(features[feature].values[0] / 0.5, -1, 1)
            score_adjustment += normalized_value * weight
    
    final_score = np.clip(base_score + score_adjustment, 0, 100)
    return final_score

def predict_trend_duration(features, model_path='models/trained/trend_duration.pkl'):
    """
    Predict the expected duration of a trend in days.
    
    Args:
        features (pd.DataFrame): Feature matrix
        model_path (str): Path to the model file
        
    Returns:
        int: Predicted trend duration in days
    """
    model = load_or_create_model(model_path)
    
    # Simple mock prediction for demonstration
    base_duration = 14  # Base duration in days
    
    # Adjust based on growth and volatility
    if 'mean_growth' in features and 'growth_volatility' in features:
        growth = features['mean_growth'].values[0]
        volatility = features['growth_volatility'].values[0]
        
        # Higher growth = potentially longer trend
        growth_factor = 1 + (growth * 5)
        
        # Higher volatility = potentially shorter trend
        volatility_factor = 1 - (volatility * 2)
        
        duration = base_duration * growth_factor * volatility_factor
        
        # Constrain to reasonable range
        duration = np.clip(duration, 3, 30)
        return int(round(duration))
    
    return base_duration