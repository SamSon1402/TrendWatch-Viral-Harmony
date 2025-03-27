import streamlit as st
import time
from modules.visualization import create_trend_chart, create_radar_chart, create_platform_distribution_chart
from utils.data_simulation import generate_platform_distribution

def render_trend_chart(trend_data, genre, metrics):
    """
    Render the main trend chart visualization.
    
    Args:
        trend_data (pd.DataFrame): DataFrame with trend data
        genre (str): Music genre
        metrics (dict): Metrics dictionary
    """
    # Show processing animations for futuristic feel
    with st.spinner('Initializing quantum neural pathways...'):
        time.sleep(1.5)
    with st.spinner('Analyzing memetic resonance patterns...'):
        time.sleep(2)
    with st.spinner('Calculating cross-platform harmonic frequencies...'):
        time.sleep(1.5)
    with st.spinner('Integrating neural-collective consciousness data...'):
        time.sleep(2)
    with st.spinner('Generating sensory-enhanced visualization...'):
        time.sleep(1)
    
    # Create container for trend chart
    st.markdown("<div class='rotating-border'>", unsafe_allow_html=True)
    st.subheader("Trend Trajectory Forecast")
    
    # Create and display the trend chart
    fig = create_trend_chart(trend_data, genre, metrics)
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Create container for additional visualizations
    st.markdown("<div class='rotating-border'>", unsafe_allow_html=True)
    st.header("Cross-Platform Neural Virality Prediction")
    
    # Create platform distribution and demographic charts
    col1, col2 = st.columns(2)
    
    with col1:
        # Generate and display platform distribution
        platforms = generate_platform_distribution(
            meme_potential=metrics.get('meme_potential', 0.7),
            neural_connection=metrics.get('neural_connection', 0.8),
            cultural_resonance=metrics.get('cultural_resonance', 0.75),
            tempo=metrics.get('tempo', 120),
            synthetic_vocal_pct=metrics.get('synthetic_vocal_pct', 50),
            celebrity_influence=metrics.get('celebrity_influence', 0.5),
            emotional_intensity=metrics.get('emotional_intensity', 7),
            novelty_factor=metrics.get('novelty_factor', 0.6)
        )
        
        platform_fig = create_platform_distribution_chart(platforms)
        st.plotly_chart(platform_fig, use_container_width=True)
    
    with col2:
        # Generate and display demographic appeal
        from utils.metrics_calculation import calculate_demographic_appeal
        
        demographics = calculate_demographic_appeal(
            novelty_factor=metrics.get('novelty_factor', 0.6),
            meme_potential=metrics.get('meme_potential', 0.7),
            tempo=metrics.get('tempo', 120),
            neural_connection=metrics.get('neural_connection', 0.8),
            cultural_resonance=metrics.get('cultural_resonance', 0.75),
            emotional_intensity=metrics.get('emotional_intensity', 7),
            celebrity_influence=metrics.get('celebrity_influence', 0.5)
        )
        
        # Create demographic donut chart
        import plotly.graph_objects as go
        
        fig = go.Figure(data=[go.Pie(
            labels=list(demographics.keys()),
            values=list(demographics.values()),
            hole=.5,
            marker=dict(
                colors=['#BD4DE6', '#9067ff', '#6e45e2', '#4527a0', '#311b92'],
                line=dict(color='#000000', width=1)
            ),
            textfont=dict(color='white'),
            textinfo='label+percent'
        )])
        
        fig.update_layout(
            title="Demographic Neural Resonance",
            plot_bgcolor='rgba(10, 10, 26, 0)',
            paper_bgcolor='rgba(10, 10, 26, 0)',
            font_color='#e0e0ff',
            showlegend=False,
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("</div>", unsafe_allow_html=True)