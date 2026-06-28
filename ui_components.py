"""
Reusable UI components and styling utilities for Streamlit app.
"""

import streamlit as st


def init_session_state():
    """Initialize Streamlit session state variables."""
    if "velocity" not in st.session_state:
        st.session_state.velocity = 25.0
    if "angle" not in st.session_state:
        st.session_state.angle = 45.0


def display_metric_card(label: str, value: str, unit: str, color: str = "#1f77b4", icon: str = ""):
    """
    Display a metric card with label, value, and unit.
    
    Args:
        label: Metric name
        value: Formatted value
        unit: Unit of measurement
        color: Card color (hex)
        icon: Optional emoji or icon
    """
    st.markdown(f"""
    <div style="
        background: linear-gradient(135deg, {color}15 0%, {color}05 100%);
        border-left: 4px solid {color};
        padding: 18px;
        border-radius: 8px;
        margin: 8px 0;
        transition: all 0.3s ease;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    ">
        <p style="color: #666; margin: 0; font-size: 0.85em; text-transform: uppercase; font-weight: 600; letter-spacing: 0.5px;">
            {icon} {label}
        </p>
        <p style="color: {color}; margin: 8px 0 0 0; font-size: 2em; font-weight: 700;">
            {value} <span style="font-size: 0.5em; font-weight: 500;">{unit}</span>
        </p>
    </div>
    """, unsafe_allow_html=True)


def display_header():
    """Display the app header with title and description."""
    st.markdown("""
    <div style="text-align: center; padding: 30px 0; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                border-radius: 12px; margin-bottom: 30px; color: white;">
        <h1 style="color: white; margin-bottom: 10px; font-size: 2.5em;">🎯 Projectile Motion Simulator</h1>
        <p style="color: rgba(255,255,255,0.9); font-size: 1.1em; margin: 0; font-weight: 300;">
            Interactive Physics Calculator for AP Physics C
        </p>
        <p style="color: rgba(255,255,255,0.7); font-size: 0.95em; margin: 8px 0 0 0;">
            Explore kinematics with intuitive, real-time visualizations
        </p>
    </div>
    """, unsafe_allow_html=True)


def display_footer():
    """Display footer with information."""
    st.markdown("""
    <hr style="border: none; height: 1px; background: linear-gradient(to right, transparent, #ddd, transparent); margin: 40px 0;">
    <div style="text-align: center; color: #999; font-size: 0.9em; padding: 20px 0;">
        <p style="margin: 5px 0;">
            <strong>Gravitational Acceleration:</strong> g = 9.8 m/s²
        </p>
        <p style="margin: 5px 0;">
            Built with ❤️ for physics education | Streamlit + Plotly
        </p>
        <p style="margin: 10px 0 0 0; font-size: 0.8em; color: #bbb;">
            Accurate to AP Physics C standards • Real-time calculations
        </p>
    </div>
    """, unsafe_allow_html=True)


def apply_custom_css():
    """Apply custom CSS styling to the Streamlit app."""
    st.markdown("""
    <style>
    /* Root styling */
    :root {
        --primary-color: #667eea;
        --secondary-color: #764ba2;
        --accent-color: #f093fb;
        --success-color: #4CAF50;
        --warning-color: #ff7f0e;
        --danger-color: #d62728;
        --light-bg: #f8f9fa;
        --border-color: #e0e0e0;
    }
    
    /* Main container */
    .main {
        max-width: 1200px;
        margin: 0 auto;
        padding: 20px;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #f8f9fa 0%, #e8e9f0 100%);
        padding: 20px;
    }
    
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] {
        padding-left: 0;
        padding-right: 0;
    }
    
    /* Header styling */
    h1, h2, h3 {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-weight: 700;
        letter-spacing: -0.5px;
    }
    
    /* Button styling */
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-weight: 700;
        border-radius: 8px;
        padding: 12px 24px;
        border: none;
        font-size: 1em;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
    }
    
    .stButton > button:active {
        transform: translateY(0);
    }
    
    /* Slider styling */
    .stSlider {
        padding: 15px 0;
    }
    
    .stSlider > div > div > div > div {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        border-radius: 8px;
    }
    
    /* Radio button styling */
    .stRadio > label {
        font-weight: 600;
        font-size: 1em;
    }
    
    /* Input styling */
    .stNumberInput > input {
        border-radius: 8px;
        border: 2px solid var(--border-color);
        padding: 10px 12px;
        transition: all 0.3s ease;
    }
    
    .stNumberInput > input:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    
    /* Metric cards */
    .metric-column {
        background-color: var(--light-bg);
        padding: 15px;
        border-radius: 8px;
        margin: 10px 0;
    }
    
    /* Plotly chart container */
    .plotly-graph-div {
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        margin: 20px 0;
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        font-weight: 600;
        font-size: 1.05em;
    }
    
    [data-testid="stExpander"] {
        border: 1px solid var(--border-color);
        border-radius: 8px;
        background: linear-gradient(135deg, #f8f9fa 0%, #f0f1f8 100%);
    }
    
    /* Markdown styling */
    .markdown-text-container {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Metric display */
    [data-testid="stMetric"] {
        background: linear-gradient(135deg, #f8f9fa 0%, #e8e9f0 100%);
        padding: 15px;
        border-radius: 8px;
        border-left: 4px solid #667eea;
    }
    
    /* Info/Success/Warning boxes */
    .stAlert {
        border-radius: 8px;
        padding: 12px 16px;
    }
    
    /* Column styling */
    .stColumn {
        padding: 0 10px;
    }
    
    /* Scrollbar styling */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #f1f1f1;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #667eea;
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #764ba2;
    }
    
    /* Responsive adjustments */
    @media (max-width: 768px) {
        .main {
            padding: 10px;
        }
        
        h1 {
            font-size: 1.8em;
        }
        
        .stButton > button {
            font-size: 0.9em;
            padding: 10px 20px;
        }
    }
    </style>
    """, unsafe_allow_html=True)


def display_info_box(title: str, content: str, box_type: str = "info"):
    """
    Display an information box with custom styling.
    
    Args:
        title: Box title
        content: Box content
        box_type: 'info', 'success', 'warning', or 'error'
    """
    colors = {
        "info": ("#1f77b4", "#e3f2fd"),
        "success": ("#2ca02c", "#e8f5e9"),
        "warning": ("#ff7f0e", "#fff3e0"),
        "error": ("#d62728", "#ffebee"),
    }
    
    color, bg_color = colors.get(box_type, colors["info"])
    
    st.markdown(f"""
    <div style="
        background-color: {bg_color};
        border-left: 4px solid {color};
        padding: 15px;
        border-radius: 8px;
        margin: 15px 0;
    ">
        <p style="color: {color}; margin: 0; font-weight: 700; font-size: 1em;">
            {title}
        </p>
        <p style="color: #333; margin: 8px 0 0 0; font-size: 0.95em;">
            {content}
        </p>
    </div>
    """, unsafe_allow_html=True)

