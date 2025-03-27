import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def preprocess_data(df):
    """
    Preprocess raw trend data for analysis.
    
    Args:
        df (pd.DataFrame): Raw data frame with trend data
        
    Returns:
        pd.DataFrame: Cleaned and preprocessed data
    """
    # Make a copy to avoid modifying the original
    data = df.copy()
    
    # Ensure datetime format
    if 'date' in data.columns and not pd.api.types.is_datetime64_any_dtype(data['date']):
        data['date'] = pd.to_datetime(data['date'])
    
    # Sort by date
    data = data.sort_values('date')
    
    # Calculate additional metrics
    if 'engagement' in data.columns:
        # Calculate day-over-day growth
        data['growth'] = data['engagement'].pct_change()
        
        # Calculate rolling metrics
        data['rolling_avg_3d'] = data['engagement'].rolling(window=3, min_periods=1).mean()
        data['rolling_avg_7d'] = data['engagement'].rolling(window=7, min_periods=1).mean()
        
        # Calculate acceleration (second derivative)
        data['acceleration'] = data['growth'].pct_change()
    
    # Fill NaN values
    data = data.fillna(method='ffill')
    
    return data

def extract_features(df, window_size=7):
    """
    Extract time series features for predictive modeling.
    
    Args:
        df (pd.DataFrame): Preprocessed trend data
        window_size (int): Window size for rolling features
        
    Returns:
        pd.DataFrame: Feature matrix for modeling
    """
    if len(df) < window_size:
        raise ValueError(f"DataFrame must have at least {window_size} rows for feature extraction")
    
    # Calculate statistical features
    features = pd.DataFrame()
    
    if 'engagement' in df.columns:
        # Time series features
        features['mean_engagement'] = df['engagement'].rolling(window=window_size).mean().values[-1]
        features['std_engagement'] = df['engagement'].rolling(window=window_size).std().values[-1]
        features['max_engagement'] = df['engagement'].rolling(window=window_size).max().values[-1]
        features['min_engagement'] = df['engagement'].rolling(window=window_size).min().values[-1]
        
        # Growth and trend features
        features['mean_growth'] = df['growth'].rolling(window=window_size).mean().values[-1]
        features['growth_volatility'] = df['growth'].rolling(window=window_size).std().values[-1]
        
        # Momentum and acceleration
        features['momentum'] = (df['engagement'].values[-1] / df['engagement'].values[-window_size]) - 1
        features['mean_acceleration'] = df['acceleration'].rolling(window=window_size).mean().values[-1]
    
    return features

def normalize_features(features):
    """
    Normalize features for model input.
    
    Args:
        features (pd.DataFrame): Feature matrix
        
    Returns:
        np.array: Normalized features
    """
    scaler = StandardScaler()
    return scaler.fit_transform(features.values.reshape(1, -1))