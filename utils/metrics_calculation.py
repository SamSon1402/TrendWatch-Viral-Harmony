def generate_forecast_metrics(trend_data, emotional_intensity, meme_potential, 
                             neural_connection, cultural_resonance):
    """
    Calculate prediction metrics based on forecast data.
    
    Args:
        trend_data (pd.DataFrame): DataFrame with trend data
        emotional_intensity (float): Emotional impact parameter
        meme_potential (float): Viral sharing potential
        neural_connection (float): Audience connection strength
        cultural_resonance (float): Cultural relevance score
        
    Returns:
        dict: Dictionary with calculated metrics
    """
    # Filter only forecast data
    forecast = trend_data[trend_data['is_forecast']]
    historical = trend_data[~trend_data['is_forecast']]
    
    # Calculate key metrics
    peak_engagement = forecast['engagement'].max()
    peak_day = forecast[forecast['engagement'] == peak_engagement]['date'].iloc[0].strftime("%b %d")
    
    total_engagement = forecast['engagement'].sum()
    
    # Calculate virality score (0-100)
    if len(historical) > 0 and historical['engagement'].iloc[-1] > 0:
        avg_growth = (forecast['engagement'].iloc[-1] / historical['engagement'].iloc[-1]) - 1
        virality_score = min(100, max(0, avg_growth * 25 * emotional_intensity * meme_potential * 100))
    else:
        virality_score = 50  # Default value if we can't calculate growth
    
    # Calculate expected trend duration
    trend_duration = min(30, max(3, int(10 * neural_connection * cultural_resonance)))
    
    # Return all calculated metrics
    return {
        'peak_engagement': peak_engagement,
        'peak_day': peak_day,
        'total_engagement': total_engagement,
        'virality_score': virality_score,
        'trend_duration': trend_duration
    }

def calculate_demographic_appeal(novelty_factor, meme_potential, tempo, 
                               neural_connection, cultural_resonance, 
                               emotional_intensity, celebrity_influence):
    """
    Calculate demographic appeal distribution based on song parameters.
    
    Returns:
        dict: Age groups and their appeal percentages
    """
    age_groups = {
        "13-17": 0.15 + (novelty_factor * 0.3) - (emotional_intensity * 0.05),
        "18-24": 0.25 + (meme_potential * 0.4) + (tempo/200 * 0.1),
        "25-34": 0.3 + (neural_connection * 0.2) + (emotional_intensity * 0.1),
        "35-44": 0.2 + (cultural_resonance * 0.3) - (novelty_factor * 0.1),
        "45+": 0.1 + (celebrity_influence * 0.2) - (meme_potential * 0.1)
    }
    
    # Normalize and ensure no negative values
    total = sum(age_groups.values())
    age_groups = {k: max(0.01, v/total) for k, v in age_groups.items()}
    
    return age_groups

def generate_marketing_metrics(neural_connection, emotional_intensity, 
                              meme_potential, virality_score):
    """
    Generate marketing opportunity metrics based on trend analysis.
    
    Returns:
        list: List of marketing metric dictionaries
    """
    return [
        {
            "title": "Cognitive Resonance Score",
            "value": f"{int((neural_connection * 1000) + (emotional_intensity * 50)):,}",
            "desc": "Mind-share potential in target demographics"
        },
        {
            "title": "Cross-Platform Synergy",
            "value": f"{int(65 + (meme_potential * 30))}%",
            "desc": "Potential for multi-platform virality"
        },
        {
            "title": "Creator Collaboration Value",
            "value": f"{int(1000 + (virality_score * 400)):,} µ-credits",
            "desc": "Estimated collaboration market value"
        },
        {
            "title": "Neural Stream Conversion",
            "value": f"{int(5 + (neural_connection * 10))}%",
            "desc": "Viral views to sustained listener conversion"
        }
    ]