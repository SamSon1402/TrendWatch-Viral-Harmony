# This file makes the modules directory a Python package
# Import key functions to make them available at the package level

from .data_processing import preprocess_data, extract_features
from .prediction_models import predict_virality, predict_trend_duration
from .visualization import create_trend_chart, create_radar_chart, create_platform_distribution_chart
from .recommendation import generate_artist_recommendations

__all__ = [
    'preprocess_data',
    'extract_features',
    'predict_virality',
    'predict_trend_duration',
    'create_trend_chart',
    'create_radar_chart',
    'create_platform_distribution_chart',
    'generate_artist_recommendations'
]