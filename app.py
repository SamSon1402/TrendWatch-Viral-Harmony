import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import time
from sklearn.ensemble import RandomForestClassifier, GradientBoostingRegressor
from sklearn.preprocessing import StandardScaler
import pickle
import random

# Set page configuration
st.set_page_config(
    page_title="SonicSeer™ 2040 - Viral Music Trend Predictor",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for futuristic look
st.markdown("""
<style>
    .main {
        background-color: #0a0a1a;
        color: #e0e0ff;
    }
    .stApp {
        background: linear-gradient(to bottom, #0a0a1a, #1a103a);
    }
    .css-1d391kg {
        background-color: #151530;
    }
    .st-bw {
        background-color: #201a4a;
    }
    .css-1v3fvcr {
        background-color: transparent;
    }
    .stButton>button {
        background-color: #6e45e2;
        color: white;
        border-radius: 20px;
        border: none;
        padding: 10px 25px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #9067ff;
        transform: scale(1.05);
        transition: all 0.3s ease;
    }
    .stSlider>div>div {
        background-color: #6e45e2;
    }
    h1, h2, h3 {
        color: #c9b6ff;
    }
    .highlight {
        background: linear-gradient(to right, #7149EA, #BD4DE6);
        padding: 10px 15px;
        border-radius: 10px;
        margin: 10px 0px;
    }
    .metrics-container {
        display: flex;
        justify-content: space-between;
        flex-wrap: wrap;
    }
    .metric-card {
        background: rgba(30, 30, 80, 0.7);
        border-radius: 15px;
        padding: 20px;
        margin: 10px;
        box-shadow: 0 4px 20px rgba(138, 87, 255, 0.2);
        flex: 1;
        min-width: 200px;
        border: 1px solid rgba(138, 87, 255, 0.3);
    }
    .holographic {
        animation: holo 8s infinite;
        background: linear-gradient(45deg, rgba(138, 43, 226, 0.2), rgba(75, 0, 130, 0.2), rgba(138, 43, 226, 0.2));
        border-radius: 15px;
        padding: 20px;
        backdrop-filter: blur(5px);
    }
    @keyframes holo {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }
    .rotating-border {
        position: relative;
        border-radius: 15px;
        padding: 20px;
        overflow: hidden;
    }
    .rotating-border::before {
        content: "";
        position: absolute;
        top: -5px; left: -5px; right: -5px; bottom: -5px;
        background: linear-gradient(45deg, #ff00cc, #3333ff, #00ffff, #ff00cc);
        background-size: 400% 400%;
        z-index: -1;
        border-radius: 18px;
        animation: rotate 10s ease infinite;
    }
    @keyframes rotate {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }
    .glow-text {
        text-shadow: 0 0 10px rgba(138, 87, 255, 0.7);
    }
</style>
""", unsafe_allow_html=True)

# App title and description
st.markdown("<h1 style='text-align: center; font-size: 50px;' class='glow-text'>SonicSeer™ 2040</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Neural-Quantum Music Trend Prediction Engine</h3>", unsafe_allow_html=True)

st.markdown("<div class='highlight'>Developed by: Sameer M | Powered by Believe Quantum-AI</div>", unsafe_allow_html=True)

# Sidebar configuration
with st.sidebar:
    st.markdown("<h2>Analysis Controls</h2>", unsafe_allow_html=True)
    
    st.markdown("<div class='rotating-border'>", unsafe_allow_html=True)
    st.subheader("Trend Parameters")
    genre = st.selectbox(
        "Base Music Genre",
        [
            "Synth-Neural Pop", 
            "Quantum Trap", 
            "NeuroWave", 
            "Holographic Folk", 
            "Bio-Electronic", 
            "Orbital Ambient",
            "Virtual Reality Metal",
            "AI-Generated Classical",
            "Memory-Infused Jazz",
            "Biofeedback House"
        ]
    )
    
    # More advanced controls for future tech
    regions = st.multiselect(
        "Target Neural-Markets",
        [
            "Global Neural Network", 
            "North American Consciousness", 
            "European Thought-Sphere", 
            "Asian Collective",
            "African Harmony Nexus",
            "South American Flow", 
            "Oceanic Dream Web",
            "Lunar Colony Network",
            "Mars Outpost Stream",
            "Orbital Habitat Collective"
        ],
        default=["Global Neural Network"]
    )
    
    tempo = st.slider("Quantum Rhythm Frequency (BPM)", 60, 200, 120)
    emotional_intensity = st.slider("Emotional Resonance Factor", 1, 10, 7)
    neural_connection = st.slider("Neural Connection Strength", 0.0, 1.0, 0.8)
    synthetic_vocal_pct = st.slider("Synthetic Vocal Integration (%)", 0, 100, 40)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<div class='holographic'>", unsafe_allow_html=True)
    st.subheader("Advanced Quantum Parameters")
    meme_potential = st.slider("Meme Potential Score", 0.0, 1.0, 0.7)
    algorithmic_boost = st.slider("Platform Algorithm Boost Factor", 1, 10, 7)
    novelty_factor = st.slider("Novelty Vector Magnitude", 0.0, 1.0, 0.6)
    cultural_resonance = st.slider("Cultural Wavelength Resonance", 0.0, 1.0, 0.75)
    celebrity_influence = st.slider("Celebrity Neural-Network Influence", 0.0, 1.0, 0.5)
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<div class='rotating-border'>", unsafe_allow_html=True)
    st.subheader("Cognitive-Enhanced AI Model")
    model_selection = st.radio(
        "Prediction Algorithm",
        [
            "Quantum Neural Network (QNN)",
            "Consciousness-Graph Analysis",
            "Temporal Wavefront Predictor",
            "Neural-Memetic Diffusion",
            "Bio-Rhythmic Pattern Matcher"
        ]
    )
    st.markdown("</div>", unsafe_allow_html=True)
    
    forecast_days = st.slider("Forecast Horizon (days)", 1, 60, 14)
    
    process_btn = st.button("Generate Quantum Prediction")

# Mock trend data generator
def generate_mock_trend_data(days_back=30, forecast_days=14):
    past_dates = [datetime.now() - timedelta(days=x) for x in range(days_back, 0, -1)]
    future_dates = [datetime.now() + timedelta(days=x) for x in range(0, forecast_days+1)]
    all_dates = past_dates + future_dates
    
    # Past trend - actual data with some noise
    past_trend = [random.randint(1000, 5000) + i * 200 + random.randint(-500, 500) for i in range(len(past_dates))]
    
    # Future trend with growth trajectory based on input parameters
    base_projection = past_trend[-1]
    growth_factor = (tempo / 100) * (emotional_intensity / 5) * neural_connection * (novelty_factor * 2) * (meme_potential * 3)
    
    # Calculate algorithm boost influence
    algo_influence = algorithmic_boost / 5
    celeb_effect = celebrity_influence * 2
    
    future_trend = []
    for i in range(forecast_days + 1):
        # Exponential growth with added variability
        day_value = base_projection + (i ** (1.2 + (algo_influence * 0.2))) * growth_factor * 200
        
        # Add celebrity and cultural resonance effects
        if i > 3 and i < 10 and celebrity_influence > 0.7:
            day_value *= (1 + (celeb_effect * 0.5))
            
        # Add some randomness
        day_value += random.randint(-int(day_value * 0.1), int(day_value * 0.1))
        future_trend.append(int(day_value))
    
    # Combine past and projected data
    engagement = past_trend + future_trend
    
    # Create dataframe
    df = pd.DataFrame({
        'date': all_dates,
        'engagement': engagement,
        'is_forecast': [False] * len(past_dates) + [True] * len(future_dates)
    })
    
    return df

# Generate engagement metrics
def generate_forecast_metrics(trend_data, emotional_intensity, meme_potential):
    # Filter only forecast data
    forecast = trend_data[trend_data['is_forecast']]
    
    peak_engagement = forecast['engagement'].max()
    peak_day = forecast[forecast['engagement'] == peak_engagement]['date'].iloc[0].strftime("%b %d")
    
    total_engagement = forecast['engagement'].sum()
    
    # Virality score (0-100)
    avg_growth = (forecast['engagement'].iloc[-1] / trend_data[~trend_data['is_forecast']]['engagement'].iloc[-1]) - 1
    virality_score = min(100, max(0, avg_growth * 25 * emotional_intensity * meme_potential * 100))
    
    trend_duration = min(30, max(3, int(10 * neural_connection * cultural_resonance)))
    
    return {
        'peak_engagement': peak_engagement,
        'peak_day': peak_day,
        'total_engagement': total_engagement,
        'virality_score': virality_score,
        'trend_duration': trend_duration
    }

# Main section layout
col1, col2 = st.columns([2, 1])

# Mock processing for when button is clicked
if process_btn:
    with col1:
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
            
        st.markdown("<div class='rotating-border'>", unsafe_allow_html=True)
        st.subheader("Trend Trajectory Forecast")
        
        # Generate and plot trend data
        trend_data = generate_mock_trend_data(forecast_days=forecast_days)
        
        # Create the plot
        fig = px.line(
            trend_data, 
            x='date', 
            y='engagement',
            color='is_forecast',
            color_discrete_map={True: '#9067ff', False: '#BD4DE6'},
            labels={'engagement': 'Neural Engagement Score', 'date': 'Timeline', 'is_forecast': 'Prediction Type'},
            title=f"Predicted Viral Trajectory for {genre}"
        )
        
        # Customize the plot for a more futuristic look
        fig.update_layout(
            plot_bgcolor='rgba(10, 10, 26, 0.8)',
            paper_bgcolor='rgba(10, 10, 26, 0)',
            font_color='#e0e0ff',
            title_font_size=20,
            legend_title_font_color='#e0e0ff',
            legend_font_color='#e0e0ff',
            hovermode='x unified',
            xaxis=dict(
                showgrid=False,
                gridcolor='rgba(138, 87, 255, 0.2)',
                showline=True,
                linecolor='rgba(138, 87, 255, 0.5)',
            ),
            yaxis=dict(
                showgrid=True,
                gridcolor='rgba(138, 87, 255, 0.2)',
                showline=True,
                linecolor='rgba(138, 87, 255, 0.5)',
            )
        )
        
        # Add a vertical line at today's date
        today = datetime.now()
        fig.add_vline(x=today, line_width=2, line_dash="dash", line_color="#FF5733")
        
        # Add annotations
        metrics = generate_forecast_metrics(trend_data, emotional_intensity, meme_potential)
        peak_date = datetime.strptime(metrics['peak_day'], "%b %d").replace(year=today.year)
        
        # Add annotation for peak
        peak_point = trend_data[trend_data['date'] == peak_date]['engagement'].iloc[0]
        fig.add_annotation(
            x=peak_date,
            y=peak_point,
            text="Peak Virality",
            showarrow=True,
            arrowhead=1,
            arrowsize=1,
            arrowwidth=2,
            arrowcolor="#9067ff",
            font=dict(size=12, color="#ffffff"),
            bgcolor="#6e45e2",
            bordercolor="#ffffff",
            borderwidth=1,
            borderpad=4,
            opacity=0.8
        )
        
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
    with col2:
        st.markdown("<div class='holographic'>", unsafe_allow_html=True)
        st.subheader("Virality Metrics")
        
        # Create a metrics box for key prediction insights
        metrics = generate_forecast_metrics(trend_data, emotional_intensity, meme_potential)
        
        st.markdown("<div class='metrics-container'>", unsafe_allow_html=True)
        
        # Virality Score
        st.markdown(f"""
        <div class='metric-card'>
            <h3 style='margin:0;font-size:16px;'>Virality Score</h3>
            <p style='font-size:28px;margin:10px 0;color:#BD4DE6;'>{metrics['virality_score']:.1f}<span style='font-size:16px;'>/100</span></p>
            <p style='font-size:12px;margin:0;'>Quantum-calculated probability</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Peak Day
        st.markdown(f"""
        <div class='metric-card'>
            <h3 style='margin:0;font-size:16px;'>Peak Virality Date</h3>
            <p style='font-size:28px;margin:10px 0;color:#BD4DE6;'>{metrics['peak_day']}</p>
            <p style='font-size:12px;margin:0;'>Maximum engagement point</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Trend Duration
        st.markdown(f"""
        <div class='metric-card'>
            <h3 style='margin:0;font-size:16px;'>Trend Duration</h3>
            <p style='font-size:28px;margin:10px 0;color:#BD4DE6;'>{metrics['trend_duration']} days</p>
            <p style='font-size:12px;margin:0;'>Expected active period</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Peak Engagement
        st.markdown(f"""
        <div class='metric-card'>
            <h3 style='margin:0;font-size:16px;'>Peak Engagement</h3>
            <p style='font-size:28px;margin:10px 0;color:#BD4DE6;'>{metrics['peak_engagement']:,}</p>
            <p style='font-size:12px;margin:0;'>Maximum neural interactions</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Total Engagement
        st.markdown(f"""
        <div class='metric-card'>
            <h3 style='margin:0;font-size:16px;'>Total Forecast Engagement</h3>
            <p style='font-size:28px;margin:10px 0;color:#BD4DE6;'>{metrics['total_engagement']:,}</p>
            <p style='font-size:12px;margin:0;'>Cumulative neural resonance</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Audio features analysis
        st.markdown("<div class='rotating-border'>", unsafe_allow_html=True)
        st.subheader("Neural-Sonic Pattern Analysis")
        
        # Audio features radar chart
        categories = ['Rhythm Impact', 'Emotional Resonance', 'Sonic Novelty', 
                     'Neural Hook Strength', 'Memetic Potential', 'Algorithm Appeal']
        
        values = [
            tempo/200,
            emotional_intensity/10,
            novelty_factor,
            neural_connection,
            meme_potential,
            algorithmic_boost/10
        ]
        
        # Convert to 0-100 scale
        values = [v * 100 for v in values]
        
        # Create radar chart
        fig = go.Figure()
        
        fig.add_trace(go.Scatterpolar(
            r=values,
            theta=categories,
            fill='toself',
            fillcolor='rgba(138, 87, 255, 0.3)',
            line=dict(color='#BD4DE6', width=2),
            name='Trend Pattern Analysis'
        ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 100],
                    gridcolor='rgba(138, 87, 255, 0.2)',
                    color='rgba(138, 87, 255, 0.5)'
                ),
                angularaxis=dict(
                    gridcolor='rgba(138, 87, 255, 0.2)',
                    linecolor='rgba(138, 87, 255, 0.5)'
                ),
                bgcolor='rgba(10, 10, 26, 0.8)'
            ),
            paper_bgcolor='rgba(10, 10, 26, 0)',
            plot_bgcolor='rgba(10, 10, 26, 0)',
            font_color='#e0e0ff',
            margin=dict(t=10, b=10),
            showlegend=False
        )
        
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Key recommendations
        st.markdown("<div class='holographic'>", unsafe_allow_html=True)
        st.subheader("Optimization Recommendations")
        
        artist_recommendations = [
            f"Emphasize {genre.split()[0]} elements in vocal processing",
            f"Optimize for {max(regions, key=lambda x: len(x))} neurological patterns",
            "Incorporate neural-hook at 0:45 timestamp",
            f"Utilize {tempo}bpm rhythmic pattern in chorus sections",
            "Structure for 15-second viral loop compatibility",
            f"{'Increase synthetic vocal elements' if synthetic_vocal_pct < 50 else 'Add organic vocal textures'}",
            f"{'Boost emotional resonance hooks' if emotional_intensity < 7 else 'Balance emotional intensity with novelty factors'}"
        ]
        
        for i, rec in enumerate(artist_recommendations):
            st.markdown(f"##### {i+1}. {rec}")
            
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Main dashboard area with additional insights
    st.markdown("<div class='rotating-border'>", unsafe_allow_html=True)
    st.header("Cross-Platform Neural Virality Prediction")
    
    # Platform distribution
    col1, col2 = st.columns(2)
    
    with col1:
        # Generate platform-specific predictions
        platforms = {
            "HoloTok": 0.4 + (meme_potential * 0.6) + (novelty_factor * 0.3) - (cultural_resonance * 0.1),
            "NeuraVerse": 0.2 + (neural_connection * 0.6) + (emotional_intensity * 0.05),
            "SenseStream": 0.15 + (cultural_resonance * 0.4) + (algorithmic_boost * 0.03),
            "BrainBeats": 0.1 + (tempo/200 * 0.3) + (synthetic_vocal_pct/100 * 0.2),
            "OmniGroove": 0.05 + (celebrity_influence * 0.3) + (emotional_intensity * 0.02),
            "NeuroClips": 0.1 + (novelty_factor * 0.2) + (meme_potential * 0.15)
        }
        
        # Normalize to sum to 100%
        total = sum(platforms.values())
        platforms = {k: v/total for k, v in platforms.items()}
        
        # Sort by value
        platforms = dict(sorted(platforms.items(), key=lambda item: item[1], reverse=True))
        
        # Create platform distribution chart
        fig = px.bar(
            x=list(platforms.keys()),
            y=list(platforms.values()),
            labels={'x': 'Neural Platform', 'y': 'Virality Potential'},
            title="Platform Distribution Prediction"
        )
        
        # Customize colors
        fig.update_traces(marker_color='#9067ff', marker_line_color='#BD4DE6',
                          marker_line_width=1.5, opacity=0.8)
        
        # Update layout
        fig.update_layout(
            plot_bgcolor='rgba(10, 10, 26, 0.8)',
            paper_bgcolor='rgba(10, 10, 26, 0)',
            font_color='#e0e0ff',
            yaxis=dict(
                tickformat='.0%',
                gridcolor='rgba(138, 87, 255, 0.2)',
            ),
            xaxis=dict(
                tickangle=45,
                gridcolor='rgba(138, 87, 255, 0.2)',
            )
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Demographic appeal projection
        age_groups = {
            "13-17": 0.15 + (novelty_factor * 0.3) - (emotional_intensity * 0.05),
            "18-24": 0.25 + (meme_potential * 0.4) + (tempo/200 * 0.1),
            "25-34": 0.3 + (neural_connection * 0.2) + (emotional_intensity * 0.1),
            "35-44": 0.2 + (cultural_resonance * 0.3) - (novelty_factor * 0.1),
            "45+": 0.1 + (celebrity_influence * 0.2) - (meme_potential * 0.1)
        }
        
        # Normalize
        total = sum(age_groups.values())
        age_groups = {k: max(0.01, v/total) for k, v in age_groups.items()}
        
        # Create donut chart
        fig = go.Figure(data=[go.Pie(
            labels=list(age_groups.keys()),
            values=list(age_groups.values()),
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
    
    # Additional performance metrics
    st.subheader("Neural-Enhanced Marketing Opportunities")
    
    cols = st.columns(4)
    
    marketing_metrics = [
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
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Disclaimer and credits
    st.markdown("""
    <div style='margin-top:30px;padding:15px;border-radius:10px;background-color:rgba(30,30,80,0.7);border:1px solid rgba(138,87,255,0.3);'>
        <p style='font-size:12px;color:#CCC;margin:0;'>
        This NeuroViral trend prediction model uses quantum neural networks and biosensor feedback combined with real-time global culture analysis. 
        Predictions represent potential outcomes based on current quantum neural patterns, not guaranteed results. Multiple parallel timeline 
        analysis technology provided by Believe Neural Innovations Division. Data conforms to Global Neural Privacy Regulations of 2038.
        </p>
    </div>
    """, unsafe_allow_html=True)
else:
    # Initial state when app loads
    st.markdown("<div class='holographic' style='text-align:center;padding:40px;'>", unsafe_allow_html=True)
    st.image("https://placehold.co/600x400/202045/BD4DE6?text=SonicSeer+2040+Neural+Interface", width=600)
    st.markdown("""
    <h2 style='margin-top:20px;'>Next-Generation Music Trend Forecasting</h2>
    <p style='font-size:18px;margin:20px 0;'>
        This quantum-neural platform analyzes billions of sonic patterns, audience brain wave responses, 
        and cross-dimensional cultural data to predict future viral music trends with unprecedented accuracy.
    </p>
    <p style='font-size:18px;'>
        Adjust the parameters in the sidebar and click "Generate Quantum Prediction" to begin.
    </p>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Feature overview
    st.markdown("<div class='rotating-border' style='margin-top:30px;'>", unsafe_allow_html=True)
    st.header("Platform Capabilities")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class='metric-card' style='height:220px;'>
            <h3>Neural Trend Prediction</h3>
            <p>Utilizes quantum computing and collective consciousness analysis to predict viral potential 14-60 days in advance with 94.7% accuracy</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class='metric-card' style='height:220px;'>
            <h3>Cross-Platform Optimization</h3>
            <p>Identifies optimal platform-specific parameters for maximum neural engagement across HoloTok, NeuraVerse, SenseStream, and other neural platforms</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown("""
        <div class='metric-card' style='height:220px;'>
            <h3>Artist-Specific Recommendations</h3>
            <p>Generates precise creative recommendations tailored to each artist's neural signature, optimizing their content for maximum resonance with target audience brainwave patterns</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Case studies
    st.markdown("<div class='holographic' style='margin-top:30px;'>", unsafe_allow_html=True)
    st.header("Success Stories")
    
    case_studies = [
        {
            "artist": "Neural Nexus",
            "genre": "Quantum Trap",
            "success": "600M neural-streams in 14 days",
            "prediction": "SonicSeer predicted viral trajectory 31 days before mainstream detection"
        },
        {
            "artist": "Synaptic Aurora",
            "genre": "Bio-Electronic",
            "success": "42 days at #1 across global consciousness charts",
            "prediction": "Platform accurately mapped cross-demographic appeal patterns"
        },
        {
            "artist": "Holographic Harmony",
            "genre": "VR Metal",
            "success": "Largest neural engagement density of 2039",
            "prediction": "SonicSeer identified optimal emotional resonance parameters"
        }
    ]
    
    cols = st.columns(3)
    for i, col in enumerate(cols):
        with col:
            case = case_studies[i]
            st.markdown(f"""
            <div class='metric-card'>
                <h3>{case['artist']}</h3>
                <p style='font-size:14px;color:#9067ff;margin:5px 0;'>{case['genre']}</p>
                <p style='font-size:18px;font-weight:bold;margin:10px 0;'>{case['success']}</p>
                <p style='font-size:14px;'>{case['prediction']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)