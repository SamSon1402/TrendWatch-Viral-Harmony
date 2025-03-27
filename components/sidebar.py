import streamlit as st

def render_sidebar():
    """
    Render the application sidebar with all control parameters.
    
    Returns:
        dict: Dictionary containing all parameter values
    """
    with st.sidebar:
        st.markdown("<h2>Analysis Controls</h2>", unsafe_allow_html=True)
        
        # Create a dictionary to store all parameters
        params = {}
        
        st.markdown("<div class='rotating-border'>", unsafe_allow_html=True)
        st.subheader("Trend Parameters")
        
        # Genre selection
        params['genre'] = st.selectbox(
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
        
        # Target markets
        params['regions'] = st.multiselect(
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
        
        # Audio parameters
        params['tempo'] = st.slider("Quantum Rhythm Frequency (BPM)", 60, 200, 120)
        params['emotional_intensity'] = st.slider("Emotional Resonance Factor", 1, 10, 7)
        params['neural_connection'] = st.slider("Neural Connection Strength", 0.0, 1.0, 0.8)
        params['synthetic_vocal_pct'] = st.slider("Synthetic Vocal Integration (%)", 0, 100, 40)
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Advanced parameters section
        st.markdown("<div class='holographic'>", unsafe_allow_html=True)
        st.subheader("Advanced Quantum Parameters")
        
        params['meme_potential'] = st.slider("Meme Potential Score", 0.0, 1.0, 0.7)
        params['algorithmic_boost'] = st.slider("Platform Algorithm Boost Factor", 1, 10, 7)
        params['novelty_factor'] = st.slider("Novelty Vector Magnitude", 0.0, 1.0, 0.6)
        params['cultural_resonance'] = st.slider("Cultural Wavelength Resonance", 0.0, 1.0, 0.75)
        params['celebrity_influence'] = st.slider("Celebrity Neural-Network Influence", 0.0, 1.0, 0.5)
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Model selection
        st.markdown("<div class='rotating-border'>", unsafe_allow_html=True)
        st.subheader("Cognitive-Enhanced AI Model")
        
        params['model_selection'] = st.radio(
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
        
        # Forecast horizon
        params['forecast_days'] = st.slider("Forecast Horizon (days)", 1, 60, 14)
        
        # Process button
        params['process_btn'] = st.button("Generate Quantum Prediction")
        
        return params