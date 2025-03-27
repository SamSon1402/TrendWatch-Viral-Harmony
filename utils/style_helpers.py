import streamlit as st

def load_custom_css():
    """
    Load custom CSS for the application to create a futuristic interface.
    """
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

def create_spinner_with_message(message):
    """
    Create a custom loading spinner with message.
    
    Args:
        message (str): Message to display with spinner
    """
    return st.spinner(message)

def apply_card_style(title, value, description):
    """
    Generate HTML for a styled metric card.
    
    Args:
        title (str): Card title
        value (str): Main metric value
        description (str): Description text
        
    Returns:
        str: HTML for the styled card
    """
    return f"""
    <div class='metric-card'>
        <h3 style='margin:0;font-size:16px;'>{title}</h3>
        <p style='font-size:28px;margin:10px 0;color:#BD4DE6;'>{value}</p>
        <p style='font-size:12px;margin:0;'>{description}</p>
    </div>
    """