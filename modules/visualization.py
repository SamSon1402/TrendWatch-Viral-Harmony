import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

def create_trend_chart(trend_data, genre, metrics):
    """
    Create a trend line chart visualization.
    
    Args:
        trend_data (pd.DataFrame): DataFrame with trend data
        genre (str): Music genre name
        metrics (dict): Metrics dictionary with peak day info
        
    Returns:
        plotly.graph_objects.Figure: Plotly figure object
    """
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
    
    # Customize the plot for a futuristic look
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
    
    # Add annotation for peak day if available
    if 'peak_day' in metrics:
        peak_date = datetime.strptime(metrics['peak_day'], "%b %d").replace(year=today.year)
        peak_data = trend_data[trend_data['date'] == peak_date]
        
        if not peak_data.empty:
            peak_engagement = peak_data['engagement'].iloc[0]
            
            fig.add_annotation(
                x=peak_date,
                y=peak_engagement,
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
    
    return fig

def create_radar_chart(params):
    """
    Create a radar chart for audio feature analysis.
    
    Args:
        params (dict): Parameters dictionary with audio features
        
    Returns:
        plotly.graph_objects.Figure: Plotly figure object
    """
    # Extract parameters
    tempo = params.get('tempo', 120)
    emotional_intensity = params.get('emotional_intensity', 7)
    novelty_factor = params.get('novelty_factor', 0.6)
    neural_connection = params.get('neural_connection', 0.8)
    meme_potential = params.get('meme_potential', 0.7)
    algorithmic_boost = params.get('algorithmic_boost', 7)
    
    # Define categories and values
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
    
    return fig

def create_platform_distribution_chart(platforms):
    """
    Create a bar chart for platform distribution.
    
    Args:
        platforms (dict): Dictionary with platform names and distribution values
        
    Returns:
        plotly.graph_objects.Figure: Plotly figure object
    """
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
    
    return fig