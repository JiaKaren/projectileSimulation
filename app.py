"""
Streamlit web app for Projectile Motion Simulator.
Interactive physics calculator with modern UI and intuitive controls.
"""

import streamlit as st
import plotly.graph_objects as go
from physics_engine import solve_projectile, get_physics_breakdown
from drag_interface import drag_selector
from ui_components import (
    init_session_state,
    display_metric_card,
    display_header,
    display_footer,
    apply_custom_css,
)

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================

st.set_page_config(
    page_title="Projectile Motion Simulator",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Apply custom styling
apply_custom_css()

# Initialize session state
init_session_state()

# ============================================================================
# MAIN APP
# ============================================================================

# Display header
display_header()

# Create layout: Sidebar for controls, main area for results
col_sidebar, col_main = st.columns([1, 2.5])

# ============================================================================
# SIDEBAR: INPUT CONTROLS
# ============================================================================

with col_sidebar:
    st.markdown("### ⚙️ Input Parameters")
    
    # Toggle between input modes
    input_mode = st.radio(
        "Input Method",
        options=["Sliders", "Drag Interface"],
        help="Choose how to set the launch parameters"
    )
    
    if input_mode == "Sliders":
        # Velocity slider
        st.session_state.velocity = st.slider(
            "Initial Velocity (v₀)",
            min_value=0.1,
            max_value=100.0,
            value=st.session_state.velocity,
            step=0.5,
            help="Launch speed in meters per second (m/s)",
        )
        
        # Angle slider
        st.session_state.angle = st.slider(
            "Launch Angle (θ)",
            min_value=0.0,
            max_value=90.0,
            value=st.session_state.angle,
            step=1.0,
            help="Launch angle in degrees (0-90°)",
        )
    else:
        st.markdown("#### 🎮 Drag the ball to set values")
        st.markdown("*Horizontal (X-axis) = Angle | Vertical (Y-axis) = Velocity*")
        
        # Render drag-style input controls and sync them to session state
        drag_result = drag_selector(
            initial_angle=st.session_state.angle,
            initial_velocity=st.session_state.velocity,
            max_velocity=100.0,
            key="drag_selector"
        )
        st.session_state.velocity = drag_result["velocity"]
        st.session_state.angle = drag_result["angle"]
    
    st.markdown("---")
    
    # Display current values
    st.markdown("#### 📊 Current Values")
    col_v, col_a = st.columns(2)
    with col_v:
        st.metric("Velocity", f"{st.session_state.velocity:.1f} m/s")
    with col_a:
        st.metric("Angle", f"{st.session_state.angle:.1f}°")
    
    st.markdown("---")
    
    # Calculate button
    if st.button("🚀 Calculate Trajectory", use_container_width=True):
        st.session_state.calculate = True
    else:
        if "calculate" not in st.session_state:
            st.session_state.calculate = True

# ============================================================================
# MAIN AREA: RESULTS AND VISUALIZATION
# ============================================================================

with col_main:
    try:
        # Calculate results
        results = solve_projectile(st.session_state.velocity, st.session_state.angle)
        
        # Display key metrics in columns
        metric_col1, metric_col2, metric_col3 = st.columns(3)
        
        with metric_col1:
            display_metric_card(
                "Max Height",
                f"{results.y_max:.2f}",
                "m",
                color="#ff7f0e",
                icon="📈"
            )
        
        with metric_col2:
            display_metric_card(
                "Range",
                f"{results.x_max:.2f}",
                "m",
                color="#2ca02c",
                icon="➡️"
            )
        
        with metric_col3:
            display_metric_card(
                "Flight Time",
                f"{results.t_total:.2f}",
                "s",
                color="#d62728",
                icon="⏱️"
            )
        
        st.markdown("---")
        
        # Create interactive Plotly visualization
        fig = go.Figure()
        
        # Trajectory line
        fig.add_trace(go.Scatter(
            x=results.trajectory_x,
            y=results.trajectory_y,
            mode='lines',
            name='Trajectory',
            line=dict(color='#1f77b4', width=3),
            hovertemplate='<b>Position</b><br>X: %{x:.2f} m<br>Y: %{y:.2f} m<extra></extra>'
        ))
        
        # Apex point
        fig.add_trace(go.Scatter(
            x=[results.x_max / 2],
            y=[results.y_max],
            mode='markers',
            name=f'Apex (Max Height: {results.y_max:.1f} m)',
            marker=dict(color='#ff7f0e', size=12, symbol='star'),
            hovertemplate='<b>Apex</b><br>Height: %{y:.2f} m<br>Distance: %{x:.2f} m<extra></extra>'
        ))
        
        # Landing point
        fig.add_trace(go.Scatter(
            x=[results.x_max],
            y=[0],
            mode='markers',
            name=f'Landing (Range: {results.x_max:.1f} m)',
            marker=dict(color='#2ca02c', size=12, symbol='circle'),
            hovertemplate='<b>Landing</b><br>Distance: %{x:.2f} m<extra></extra>'
        ))
        
        # Update layout
        fig.update_layout(
            title=f"Projectile Motion: v₀ = {results.v0} m/s, θ = {results.angle_degrees}°",
            xaxis_title="Horizontal Distance (meters)",
            yaxis_title="Vertical Distance (meters)",
            hovermode='closest',
            template='plotly_white',
            height=500,
            showlegend=True,
            legend=dict(x=0.02, y=0.98, bgcolor='rgba(255,255,255,0.8)'),
        )
        
        # Add grid
        fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='#e5e5e5')
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#e5e5e5')
        
        # Display plot
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("---")
        
        # Physics breakdown
        with st.expander("📖 View Physics Breakdown", expanded=True):
            st.markdown(get_physics_breakdown(results))
        
        # Additional calculations
        with st.expander("📊 Detailed Metrics"):
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric("Horizontal Velocity (V₀ₓ)", f"{results.v0x:.2f} m/s")
                st.metric("Vertical Velocity (V₀ᵧ)", f"{results.v0y:.2f} m/s")
                st.metric("Time to Apex", f"{results.t_apex:.2f} s")
            
            with col2:
                st.metric("Initial Velocity", f"{results.v0:.2f} m/s")
                st.metric("Launch Angle", f"{results.angle_degrees:.2f}°")
                st.metric("Gravitational Acceleration", "9.8 m/s²")
        
        # Quick facts
        with st.expander("💡 Physics Facts"):
            facts = f"""
            - **45° Angle**: The optimal angle for maximum range (with symmetric launch/landing)
            - **Your Angle**: {'Optimal for range!' if abs(results.angle_degrees - 45) < 5 else 'Different launch characteristics'}
            - **Symmetry**: Time to apex = Total time / 2 ({results.t_apex:.2f}s = {results.t_total:.2f}s / 2)
            - **Zero Velocity Point**: Vertical velocity becomes zero at apex (maximum height)
            - **Horizontal Motion**: No acceleration horizontally (constant velocity of {results.v0x:.2f} m/s)
            """
            st.markdown(facts)
        
        st.markdown("---")
        
    except ValueError as e:
        st.error(f"❌ Error: {str(e)}")

# ============================================================================
# FOOTER
# ============================================================================

display_footer()
