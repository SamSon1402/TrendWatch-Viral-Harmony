# This file makes the utils directory a Python package
# Import key functions to make them available at the package level

from .data_simulation import generate_mock_trend_data
from .metrics_calculation import generate_forecast_metrics
from .style_helpers import load_custom_css

__all__ = [
    'generate_mock_trend_data',
    'generate_forecast_metrics',
    'load_custom_css'
]