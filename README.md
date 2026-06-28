# 🎯 Projectile Motion Simulator

An interactive, modern web application for simulating and visualizing projectile motion problems. Built with Streamlit and Plotly for AP Physics C students and educators.

## Features

✨ **Modern Interface**
- Clean, intuitive UI with gradient designs
- Responsive layout that works on desktop and mobile
- Real-time calculations and visualizations

🎮 **Two Input Methods**
- **Sliders**: Traditional slider controls for precise input
- **Drag Interface**: Interactive ball-on-canvas for intuitive parameter selection

📊 **Interactive Visualizations**
- Real-time trajectory plots with Plotly
- Marked apex and landing points
- Hover information for detailed data

🧮 **Physics Calculations**
- Accurate kinematics computations (AP Physics C standards)
- Step-by-step physics breakdown with formulas
- Detailed metrics and velocity components
- Educational facts and optimal angle suggestions

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup

1. **Navigate to the project directory:**
   ```bash
   cd /home/karen/karenWorks/Python\ Projects/projectileSimulation
   ```

2. **Install dependencies:**
   ```bash
   python -m pip install --upgrade pip setuptools wheel
   python -m pip install --force-reinstall --no-cache-dir -r requirements.txt
   ```

   This will install:
   - **Streamlit** - Web application framework
   - **Plotly** - Interactive charting library
   - **NumPy** - Numerical computing (optional optimization)

## Running the App

### Launch Locally

```bash
streamlit run app.py
```

The app will automatically open in your default browser at `http://localhost:8501`

If it doesn't open automatically, manually visit: **http://localhost:8501**

### Usage

1. **Select Input Method**
   - Choose between "Sliders" or "Drag Interface" from the sidebar
   - Adjust parameters to your desired values

2. **View Results**
   - See real-time calculations and updated trajectory plot
   - Hover over the plot to see detailed coordinates
   - Check metric cards for key values (max height, range, flight time)

3. **Explore Details**
   - Expand "View Physics Breakdown" to see step-by-step calculations
   - Expand "Detailed Metrics" for velocity components and times
   - Expand "Physics Facts" for educational information

## Project Structure

```
projectileSimulation/
├── app.py                       # Main Streamlit application
├── physics_engine.py            # Physics calculations and data structures
├── ui_components.py             # Reusable UI components and styling
├── drag_interface.py            # Drag-and-drop interface component
├── requirements.txt             # Python dependencies
├── IMPLEMENTATION_PLAN.md       # Development roadmap
├── README.md                    # This file
├── .streamlit/
│   └── config.toml             # Streamlit configuration
└── simulation.py               # Original command-line version
```

## How to Use Each Feature

### Using Sliders
1. Move the "Initial Velocity (v₀)" slider from 0.1 to 100 m/s
2. Move the "Launch Angle (θ)" slider from 0° to 90°
3. Watch the trajectory update in real-time
4. View metrics and physics breakdown

### Using Drag Interface
1. Select "Drag Interface" from the input method radio buttons
2. Click and drag the green ball within the canvas
3. X-axis (horizontal) controls angle (0-90°)
4. Y-axis (vertical) controls velocity (0.1-100 m/s)
5. Release to set values
6. View real-time updates

### Understanding the Plot
- **Blue Line**: The projectile's trajectory path
- **Orange Star**: The apex (highest point)
- **Green Circle**: The landing point
- **Hover**: Move cursor over the plot to see coordinates

### Reading the Breakdown
The physics breakdown shows:
1. Velocity components (horizontal and vertical)
2. Time to reach apex
3. Total flight time
4. Maximum height
5. Total horizontal range

## Physics Formulas Used

### Velocity Components
- V₀ₓ = V₀ × cos(θ)
- V₀ᵧ = V₀ × sin(θ)

### Time Calculations
- t_apex = V₀ᵧ / g
- t_total = 2 × t_apex

### Height and Range
- h_max = V₀ᵧ² / (2g)
- range = V₀ₓ × t_total

Where g = 9.8 m/s² (gravitational acceleration)

## Tips for Best Results

✅ **Do**
- Experiment with different velocities and angles
- Try 45° for maximum range
- Compare different trajectories mentally
- Use the drag interface for quick exploration
- Read physics facts for learning

❌ **Don't**
- Exceed 100 m/s initial velocity
- Use angles outside 0-90° range
- Ignore the physics breakdown
- Rush through the calculations

## Keyboard Shortcuts

- **Ctrl+C** in terminal to stop the app
- **R** to refresh the browser and reload app
- **Browser back/forward** to navigate if needed

## Troubleshooting

### App won't start
```bash
# Make sure you're in the correct directory
cd /home/karen/karenWorks/Python\ Projects/projectileSimulation

# Reinstall dependencies
pip install --upgrade streamlit plotly numpy
```

### Drag interface not working
- Ensure JavaScript is enabled in your browser
- Try refreshing the page (F5)
- Switch to "Sliders" mode and back

### Port already in use
```bash
# Use a different port
streamlit run app.py --server.port 8502
```

### Slow performance
- Close other browser tabs
- Reduce browser zoom to 100%
- Clear browser cache

## Future Enhancements

Planned features for future versions:
- 🎬 Animation of projectile motion
- 📈 Multiple trajectory comparison
- 📥 Export data to CSV/PDF
- 🎨 Custom color themes
- 🌍 Air resistance calculations
- 📱 Full mobile app version

## Education

This simulator is designed for:
- AP Physics C students learning kinematics
- Physics teachers demonstrating concepts
- Science educators creating interactive content
- Anyone interested in understanding projectile motion

### Learning Objectives
- Understand velocity decomposition
- Visualize parabolic trajectories
- Calculate flight parameters
- Apply kinematic equations
- Explore optimal launch angles

## Technical Details

### Technologies Used
- **Streamlit**: Web application framework (open-source, Python-based)
- **Plotly**: Interactive visualization library
- **Python 3**: Core programming language
- **HTML/CSS/JavaScript**: Custom interactive components

### Browser Compatibility
- ✅ Chrome/Chromium (recommended)
- ✅ Firefox
- ✅ Safari
- ✅ Edge
- ⚠️ Older versions may have limited drag interface support

### Performance
- Calculations: < 10ms
- Plot rendering: < 100ms
- Drag interface: Real-time (60fps capable)

## Contributing

To contribute improvements:
1. Fork or clone the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit feedback or pull requests

## License

This project is created for educational purposes. Feel free to use, modify, and distribute for learning.

## Support

For issues or questions:
- Review the troubleshooting section
- Check the implementation plan
- Examine the code comments
- Run in verbose mode for debugging

## Acknowledgments

- AP Physics C Curriculum Standards
- Streamlit Documentation
- Plotly Community
- Physics education community

---

**Version**: 1.0.0  
**Last Updated**: June 2026  
**Status**: ✅ Ready for Use

Enjoy exploring projectile motion! 🚀
