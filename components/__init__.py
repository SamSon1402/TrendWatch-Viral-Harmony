# This file makes the components directory a Python package
# Import key components to make them available at the package level

from .sidebar import render_sidebar
from .trend_charts import render_trend_chart
from .metrics_display import render_metrics
from .recommendation_cards import render_recommendations

__all__ = [
    'render_sidebar',
    'render_trend_chart',
    'render_metrics',
    'render_recommendations'
]