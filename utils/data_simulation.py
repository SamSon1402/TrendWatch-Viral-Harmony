import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def generate_mock_trend_data(days_back=30, forecast_days=14, tempo=120, 
                             emotional_intensity=7, neural_connection=0.8,
                             meme_potential=0.7, algorithmic_boost=7, 
                             novelty_factor=0.6):
    """
    Generate simulated trend data for visualization and testing.
    
    Args:
        days_back (int): Number of historical days to simulate
        forecast_days (int): Number of days to forecast into the future
        tempo (int): Music tempo parameter (affects growth rate)
        emotional_intensity (float): Emotional impact parameter
        neural_connection (float): Audience connection strength
        meme_potential (float): Viral sharing potential
        algorithmic_boost (float): Platform algorithm favorability
        novelty_factor (float): Content uniqueness score
        
    Returns:
        pd.DataFrame: DataFrame with date, engagement, and is_forecast columns
    """
    # Generate dates for historical and forecast data
    past_dates = [datetime.now() - timedelta(days=x) for x in range(days_back, 0, -1)]
    future_dates = [datetime.now() + timedelta(days=x) for x in range(0, forecast_days+1)]
    all_dates = past_dates + future_dates
    
    # Generate historical engagement data with realistic noise
    base_level = 1000 + (tempo * 10)  # Base engagement level
    growth_factor = 200 + (emotional_intensity * 30)  # Daily growth
    
    # Historical data with some randomness
    past_trend = []
    current_value = base_level
    for i in range(len(past_dates)):
        noise = random.randint(-int(current_value * 0.1), int(current_value * 0.1))
        current_value = current_value + growth_factor + noise
        past_trend.append(max(0, current_value))
    
    # Future trend with growth trajectory based on input parameters
    base_projection = past_trend[-1]
    future_growth_factor = (tempo / 100) * (emotional_intensity / 5) * neural_connection * (novelty_factor * 2) * (meme_potential * 3)
    
    # Calculate algorithm boost influence
    algo_influence = algorithmic_boost / 5
    
    # Generate future trend
    future_trend = []
    for i in range(forecast_days + 1):
        # Exponential growth with added variability based on parameters
        day_value = base_projection + (i ** (1.2 + (algo_influence * 0.2))) * future_growth_factor * 200
            
        # Add some randomness
        day_value += random.randint(-int(day_value * 0.05), int(day_value * 0.05))
        future_trend.append(int(day_value))
    
    # Combine past and projected data
    engagement = past_trend + future_trend
    
    # Create dataframe with all data
    df = pd.DataFrame({
        'date': all_dates,
        'engagement': engagement,
        'is_forecast': [False] * len(past_dates) + [True] * len(future_dates)
    })
    
    return df

def generate_platform_distribution(meme_potential, neural_connection, cultural_resonance, 
                                   tempo, synthetic_vocal_pct, celebrity_influence,
                                   emotional_intensity, novelty_factor):
    """
    Generate a simulated platform distribution based on song parameters.
    
    Returns:
        dict: Platform names and their distribution percentages
    """
    platforms = {
        "HoloTok": 0.4 + (meme_potential * 0.6) + (novelty_factor * 0.3) - (cultural_resonance * 0.1),
        "NeuraVerse": 0.2 + (neural_connection * 0.6) + (emotional_intensity * 0.05),
        "SenseStream": 0.15 + (cultural_resonance * 0.4) + (emotional_intensity * 0.03),
        "BrainBeats": 0.1 + (tempo/200 * 0.3) + (synthetic_vocal_pct/100 * 0.2),
        "OmniGroove": 0.05 + (celebrity_influence * 0.3) + (emotional_intensity * 0.02),
        "NeuroClips": 0.1 + (novelty_factor * 0.2) + (meme_potential * 0.15)
    }
    
    # Normalize to sum to 100%
    total = sum(platforms.values())
    platforms = {k: v/total for k, v in platforms.items()}
    
    return dict(sorted(platforms.items(), key=lambda item: item[1], reverse=True))