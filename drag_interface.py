"""
Interactive selector for projectile launch values.
This uses Streamlit-native controls so the app remains stable and works
without needing a custom frontend build.
"""

import streamlit as st


def drag_selector(
    initial_angle: float = 45.0,
    initial_velocity: float = 25.0,
    max_velocity: float = 100.0,
    key: str = None,
) -> dict:
    """Render an interactive control panel for choosing angle and velocity."""
    st.markdown("#### 🎮 Drag-style controls")
    st.caption("Adjust the controls below to set the launch conditions.")

    angle = st.slider(
        "Launch Angle (θ)",
        min_value=0.0,
        max_value=90.0,
        value=float(initial_angle),
        step=1.0,
        key=f"{key}_angle" if key else None,
    )
    velocity = st.slider(
        "Initial Velocity (v₀)",
        min_value=0.1,
        max_value=float(max_velocity),
        value=float(initial_velocity),
        step=0.5,
        key=f"{key}_velocity" if key else None,
    )

    progress = min(100.0, (velocity / max_velocity) * 100.0)
    st.markdown(
        f"""
        <div style="padding: 12px; border-radius: 10px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; margin-top: 8px;">
            <div style="font-size: 0.9em; margin-bottom: 8px;">Current selection</div>
            <div><strong>Angle:</strong> {angle:.1f}°</div>
            <div><strong>Velocity:</strong> {velocity:.1f} m/s</div>
            <div style="margin-top: 8px; height: 10px; background: rgba(255,255,255,0.25); border-radius: 999px; overflow: hidden;">
                <div style="height: 100%; width: {progress:.1f}%; background: #4CAF50; border-radius: 999px;"></div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    return {"angle": angle, "velocity": velocity}
