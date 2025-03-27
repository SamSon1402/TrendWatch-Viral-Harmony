import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def extract_advanced_features(trend_data, audio_params=None):
    """
    Extract advanced features from trend data and audio parameters.
    
    Args:
        trend_data (pd.DataFrame): DataFrame with trend data
        audio_params (dict, optional): Dictionary of audio parameters
        
    Returns:
        pd.DataFrame: DataFrame with engineered features
    """
    if trend_data.empty:
        raise ValueError("Trend data is empty")
    
    features = pd.DataFrame()
    
    # Time series features from trend data
    if 'engagement' in trend_data.columns:
        # Basic trend metrics
        features['recent_engagement'] = [trend_data['engagement'].values[-1]]
        features['max_engagement'] = [trend_data['engagement'].max()]
        features['engagement_growth_pct'] = [(trend_data['engagement'].values[-1] / trend_data['engagement'].values[0]) - 1 
                                             if trend_data['engagement'].values[0] > 0 else 0]
        
        # Calculate trend stability (inverse of volatility)
        if len(trend_data) >= 7:
            volatility = trend_data['engagement'].rolling(window=7).std().mean() / trend_data['engagement'].mean()
            features['trend_stability'] = [1 - min(volatility, 1)]
        else:
            features['trend_stability'] = [0.5]  # Default for short series
    
    # Add audio parameters if provided
    if audio_params:
        for param_name, param_value in audio_params.items():
            # Convert percentage values to 0-1 range
            if param_name in ['tempo']:
                # Normalize tempo to 0-1 range (assuming 60-180 bpm range)
                features[param_name] = [(param_value - 60) / 120 if 60 <= param_value <= 180 else 0.5]
            elif param_name in ['emotional_intensity', 'algorithmic_boost']:
                # Convert 1-10 scale to 0-1
                features[param_name] = [param_value / 10]
            else:
                # Assume other parameters are already in 0-1 range
                features[param_name] = [param_value]
    
    return features

def create_feature_matrix(trend_features, audio_features):
    """
    Combine trend and audio features into a single feature matrix.
    
    Args:
        trend_features (pd.DataFrame): Features extracted from trend data
        audio_features (pd.DataFrame): Features from audio parameters
        
    Returns:
        pd.DataFrame: Combined feature matrix
    """
    # Combine features
    combined = pd.concat([trend_features, audio_features], axis=1)
    
    # Handle any missing values
    combined = combined.fillna(0)
    
    return combined

def normalize_features(features):
    """
    Normalize features for model input.
    
    Args:
        features (pd.DataFrame): Feature matrix
        
    Returns:
        np.ndarray: Normalized features
    """
    scaler = StandardScaler()
    normalized = scaler.fit_transform(features)
    
    return normalized

def create_interaction_features(features):
    """
    Create interaction features to capture relationships between variables.
    
    Args:
        features (pd.DataFrame): Original feature matrix
        
    Returns:
        pd.DataFrame: Feature matrix with interaction terms
    """
    # Create a copy to avoid modifying the original
    enhanced = features.copy()
    
    # Define pairs of features to interact
    interaction_pairs = [
        ('emotional_intensity', 'neural_connection'),
        ('meme_potential', 'novelty_factor'),
        ('tempo', 'emotional_intensity'),
        ('neural_connection', 'meme_potential')
    ]
    
    # Create interaction terms
    for feat1, feat2 in interaction_pairs:
        if feat1 in features.columns and feat2 in features.columns:
            interaction_name = f"{feat1}_x_{feat2}"
            enhanced[interaction_name] = features[feat1] * features[feat2]
    
    return enhanced