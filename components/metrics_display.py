import streamlit as st
from modules.visualization import create_radar_chart

def render_metrics(metrics):
    """
    Render the metrics display component.
    
    Args:
        metrics (dict): Dictionary containing trend metrics
    """
    st.markdown("<div class='holographic'>", unsafe_allow_html=True)
    st.subheader("Virality Metrics")
    
    # Create metrics container
    st.markdown("<div class='metrics-container'>", unsafe_allow_html=True)
    
    # Virality Score
    st.markdown(f"""
    <div class='metric-card'>
        <h3 style='margin:0;font-size:16px;'>Virality Score</h3>
        <p style='font-size:28px;margin:10px 0;color:#BD4DE6;'>{metrics.get('virality_score', 0):.1f}<span style='font-size:16px;'>/100</span></p>
        <p style='font-size:12px;margin:0;'>Quantum-calculated probability</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Peak Day
    st.markdown(f"""
    <div class='metric-card'>
        <h3 style='margin:0;font-size:16px;'>Peak Virality Date</h3>
        <p style='font-size:28px;margin:10px 0;color:#BD4DE6;'>{metrics.get('peak_day', 'N/A')}</p>
        <p style='font-size:12px;margin:0;'>Maximum engagement point</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Trend Duration
    st.markdown(f"""
    <div class='metric-card'>
        <h3 style='margin:0;font-size:16px;'>Trend Duration</h3>
        <p style='font-size:28px;margin:10px 0;color:#BD4DE6;'>{metrics.get('trend_duration', 0)} days</p>
        <p style='font-size:12px;margin:0;'>Expected active period</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Peak Engagement
    st.markdown(f"""
    <div class='metric-card'>
        <h3 style='margin:0;font-size:16px;'>Peak Engagement</h3>
        <p style='font-size:28px;margin:10px 0;color:#BD4DE6;'>{metrics.get('peak_engagement', 0):,}</p>
        <p style='font-size:12px;margin:0;'>Maximum neural interactions</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Total Engagement
    st.markdown(f"""
    <div class='metric-card'>
        <h3 style='margin:0;font-size:16px;'>Total Forecast Engagement</h3>
        <p style='font-size:28px;margin:10px 0;color:#BD4DE6;'>{metrics.get('total_engagement', 0):,}</p>
        <p style='font-size:12px;margin:0;'>Cumulative neural resonance</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Audio features radar chart
    st.markdown("<div class='rotating-border'>", unsafe_allow_html=True)
    st.subheader("Neural-Sonic Pattern Analysis")
    
    # Create and display radar chart
    radar_fig = create_radar_chart(metrics)
    st.plotly_chart(radar_fig, use_container_width=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

def render_marketing_metrics(metrics):
    """
    Render additional marketing-related metrics.
    
    Args:
        metrics (dict): Dictionary containing metrics data
    """
    # Get marketing metrics
    from utils.metrics_calculation import generate_marketing_metrics
    
    marketing_metrics = generate_marketing_metrics(
        neural_connection=metrics.get('neural_connection', 0.8),
        emotional_intensity=metrics.get('emotional_intensity', 7),
        meme_potential=metrics.get('meme_potential', 0.7),
        virality_score=metrics.get('virality_score', 50)
    )
    
    st.subheader("Neural-Enhanced Marketing Opportunities")
    
    cols = st.columns(4)
    for i, col in enumerate(cols):
        with col:
            metric = marketing_metrics[i]
            st.markdown(f"""
            <div class='metric-card' style='height:150px;'>
                <h3 style='margin:0;font-size:16px;'>{metric['title']}</h3>
                <p style='font-size:28px;margin:15px 0;color:#BD4DE6;'>{metric['value']}</p>
                <p style='font-size:12px;margin:0;'>{metric['desc']}</p>
            </div>
            """, unsafe_allow_html=True)