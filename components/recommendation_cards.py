import streamlit as st
from modules.recommendation import generate_artist_recommendations, analyze_potential_collaborations

def render_recommendations(params):
    """
    Render artist recommendations based on analysis.
    
    Args:
        params (dict): Parameters dictionary
    """
    st.markdown("<div class='holographic'>", unsafe_allow_html=True)
    st.subheader("Optimization Recommendations")
    
    # Generate artist recommendations
    artist_recommendations = generate_artist_recommendations(params)
    
    # Display recommendations as numbered list
    for i, rec in enumerate(artist_recommendations):
        st.markdown(f"##### {i+1}. {rec}")
    
    st.markdown("</div>", unsafe_allow_html=True)

def render_collaboration_suggestions(params):
    """
    Render collaboration suggestions for artists.
    
    Args:
        params (dict): Parameters dictionary
    """
    st.markdown("<div class='rotating-border'>", unsafe_allow_html=True)
    st.subheader("Potential Neural Collaborations")
    
    # Get collaboration suggestions
    collaborations = analyze_potential_collaborations(params)
    
    # Display collaborations
    cols = st.columns(len(collaborations))
    for i, col in enumerate(cols):
        with col:
            st.markdown(f"""
            <div class='metric-card' style='text-align:center;'>
                <h3 style='font-size:18px;'>{collaborations[i]}</h3>
                <p style='font-size:14px;margin-top:10px;'>Resonance Match: {int(80 + i * 3)}%</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

def render_case_studies():
    """
    Render case studies of successful trend predictions.
    """
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