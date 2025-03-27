import pickle
import os
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from datetime import datetime

def load_model(model_path, default_model_type='random_forest'):
    """
    Load a trained model from disk.
    
    Args:
        model_path (str): Path to the saved model file
        default_model_type (str): Type of model to create if loading fails
        
    Returns:
        object: Loaded model object
    """
    try:
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
        return model
    except (FileNotFoundError, EOFError) as e:
        print(f"Error loading model from {model_path}: {e}")
        return create_default_model(default_model_type)

def save_model(model, model_path):
    """
    Save a model to disk.
    
    Args:
        model (object): Model object to save
        model_path (str): Path where model should be saved
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Ensure directory exists
        os.makedirs(os.path.dirname(model_path), exist_ok=True)
        
        # Save the model
        with open(model_path, 'wb') as f:
            pickle.dump(model, f)
        
        print(f"Model saved to {model_path}")
        return True
    except Exception as e:
        print(f"Error saving model to {model_path}: {e}")
        return False

def create_default_model(model_type='random_forest'):
    """
    Create a new default model of the specified type.
    
    Args:
        model_type (str): Type of model to create
        
    Returns:
        object: Created model object
    """
    if model_type == 'random_forest':
        return RandomForestRegressor(
            n_estimators=100,
            max_depth=10,
            min_samples_split=5,
            min_samples_leaf=2,
            random_state=42
        )
    elif model_type == 'gradient_boosting':
        return GradientBoostingRegressor(
            n_estimators=100,
            learning_rate=0.1,
            max_depth=5,
            random_state=42
        )
    else:
        raise ValueError(f"Unknown model type: {model_type}")

def predict_with_model(model, features, fallback_function=None):
    """
    Make predictions using a model with fallback option.
    
    Args:
        model (object): Model to use for prediction
        features (pd.DataFrame): Feature matrix
        fallback_function (callable, optional): Function to use if model fails
        
    Returns:
        np.ndarray: Prediction results
    """
    try:
        return model.predict(features)
    except Exception as e:
        print(f"Error during prediction: {e}")
        if fallback_function:
            print("Using fallback prediction function")
            return fallback_function(features)
        else:
            # Return a sensible default
            return np.array([0.5] * len(features))

def get_model_info(model):
    """
    Get information about a trained model.
    
    Args:
        model (object): Model object
        
    Returns:
        dict: Dictionary with model information
    """
    model_info = {
        'type': type(model).__name__,
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    
    # Get feature importances if available
    if hasattr(model, 'feature_importances_'):
        model_info['has_feature_importances'] = True
    else:
        model_info['has_feature_importances'] = False
    
    return model_info