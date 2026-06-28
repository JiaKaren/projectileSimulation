# Projectile Motion Simulator - Streamlit Conversion Plan

## Overview
Convert the command-line projectile motion simulator into a modern, interactive Streamlit web app with drag-and-drop ball interface for intuitive input control.

---

## Phase 1: Project Setup & Dependencies
**Duration:** 1-2 hours  
**Objective:** Establish the foundation for Streamlit development

### Tasks:
- [ ] Install required dependencies
  - `streamlit` - Web framework
  - `matplotlib` - Plotting (compatible with Streamlit)
  - `plotly` - Modern interactive charts (alternative/supplement to matplotlib)
  - `numpy` - Numerical calculations (optional optimization)
  
- [ ] Create new file structure:
  - `app.py` - Main Streamlit application
  - `physics_engine.py` - Core physics calculations (refactored from simulation.py)
  - `ui_components.py` - Reusable UI components and styling
  - `requirements.txt` - Dependency list
  
- [ ] Configure Streamlit settings (`.streamlit/config.toml`)
  - Set theme to modern/light mode
  - Configure layout (wide mode)
  - Set custom color scheme

### Deliverables:
- Streamlit project structure initialized
- All dependencies installed and tested
- Configuration file ready

---

## Phase 2: Refactor Physics Engine
**Duration:** 1-2 hours  
**Objective:** Extract and optimize physics calculations for reusability

### Tasks:
- [ ] Create `physics_engine.py`:
  - Extract `solve_projectile()` function
  - Return structured data (dict/dataclass) with all calculations:
    - Velocity components (v0x, v0y)
    - Time to apex, total flight time
    - Maximum height
    - Range/horizontal distance
    - Trajectory points (x, y coordinates for plotting)
  
- [ ] Add helper functions:
  - `generate_trajectory_points(v0x, v0y, t_total, intervals=100)` - Generate trajectory coordinates
  - `calculate_metrics()` - Return all physics metrics as structured data
  
- [ ] Add input validation:
  - Velocity range: 0.1 - 100 m/s
  - Angle range: 0 - 90 degrees
  - Error handling with meaningful messages

### Deliverables:
- Clean, modular physics engine
- Testable functions with clear inputs/outputs
- Input validation ready

---

## Phase 3: Create Base Streamlit App Structure
**Duration:** 1-2 hours  
**Objective:** Build the main app skeleton with layout

### Tasks:
- [ ] Set up `app.py` basic structure:
  - Streamlit page configuration (title, icon, layout)
  - Page layout with columns/containers
  - Import physics engine
  
- [ ] Create layout sections:
  - Header: App title and description
  - Sidebar or left column: Input controls (placeholder)
  - Main content: Results display area (placeholder)
  - Footer: Information/credits
  
- [ ] Add basic styling:
  - Custom CSS for modern look (clean fonts, spacing, colors)
  - Responsive design for different screen sizes
  - Dark/Light mode support (optional)
  
- [ ] Test app runs without errors:
  - `streamlit run app.py`
  - Basic layout visible

### Deliverables:
- Functional Streamlit app template
- Clean layout structure
- Basic styling in place

---

## Phase 4: Implement Interactive Slider Controls (Baseline)
**Duration:** 1-2 hours  
**Objective:** Add traditional slider inputs before implementing drag interface

### Tasks:
- [ ] Add Streamlit sliders to sidebar:
  - Initial velocity slider (0.1 - 100 m/s, step 0.5)
  - Launch angle slider (0 - 90°, step 1)
  - Add helpful labels and descriptions
  
- [ ] Implement real-time calculation:
  - Use Streamlit session state to track values
  - Update calculations on slider change
  - Add debouncing if needed for performance
  
- [ ] Display physics breakdown:
  - Show velocity components
  - Display time metrics (apex time, flight time)
  - Show maximum height and range
  - Format numbers with proper units
  
- [ ] Add result cards/metrics:
  - Use Streamlit columns for metric display
  - Style with background colors
  - Include icons/emojis for visual appeal

### Deliverables:
- Working slider controls
- Real-time physics calculations
- Formatted results display

---

## Phase 5: Add Matplotlib/Plotly Visualization
**Duration:** 1-2 hours  
**Objective:** Render trajectory graphs in Streamlit

### Tasks:
- [ ] Create trajectory visualization:
  - Plot projectile path (curved trajectory line)
  - Mark apex point with annotation
  - Mark landing point with annotation
  - Add grid and axis labels
  
- [ ] Implement with Plotly for interactivity:
  - Interactive hover information
  - Zoom and pan capabilities
  - Legend with trajectory details
  - Professional styling
  
- [ ] Add plot customization:
  - Adjustable grid visibility
  - Different color schemes
  - Responsive sizing
  
- [ ] Display using `st.plotly_chart()` or `st.pyplot()`
  - Select best performance option
  - Ensure smooth updates

### Deliverables:
- Interactive trajectory plot
- Professional visualization
- Real-time plot updates with slider changes

---

## Phase 6: Design Drag-and-Drop Ball Interface
**Duration:** 2-3 hours  
**Objective:** Create custom draggable ball component for intuitive input

### Tasks:
- [ ] Design the drag interface concept:
  - Horizontal bar representing angle (0-90°)
  - Vertical bar representing velocity (0-100 m/s)
  - Ball positioned at intersection point
  - Visual feedback on hover/drag
  
- [ ] Implement using Streamlit components:
  - **Option A**: Use `streamlit-drawable-canvas` for custom drawing
  - **Option B**: Use `streamlit-elements` for interactive components
  - **Option C**: Use JavaScript with Streamlit custom components (advanced)
  - **Option D**: Use HTML/CSS/JavaScript with `st.components.v1` (custom component)
  
- [ ] Create helper functions:
  - `render_drag_interface()` - Main drag component
  - `convert_position_to_values()` - Map ball position to physics values
  - `render_ball_at_position()` - Visualize ball position
  
- [ ] Add visual elements:
  - Animated ball with shadow
  - Axis labels (angle, velocity)
  - Grid or tick marks
  - Smooth drag animation

### Deliverables:
- Functional drag-and-drop interface concept
- Position-to-value conversion logic
- Selected component library implementation

---

## Phase 7: Integrate Drag Interface with Physics Engine
**Duration:** 1-2 hours  
**Objective:** Connect drag interaction to calculations

### Tasks:
- [ ] Bind drag position to physics values:
  - Map ball X position to angle (0-90°)
  - Map ball Y position to velocity (0.1-100 m/s)
  - Real-time calculation updates
  
- [ ] Synchronize with sliders:
  - Moving ball updates slider values (one-way or two-way)
  - Sliders can also move ball position
  - No conflicts or race conditions
  
- [ ] Add input constraints:
  - Keep ball within valid bounds
  - Snap to grid (optional)
  - Visual feedback on boundaries
  
- [ ] Implement smooth transitions:
  - Animation when values change
  - Responsive feedback

### Deliverables:
- Drag interface fully functional
- Physics values updated in real-time
- Synchronized with other controls

---

## Phase 8: Enhance UI/UX - Modern Design
**Duration:** 2-3 hours  
**Objective:** Polish the interface for professional appearance

### Tasks:
- [ ] Apply modern design principles:
  - Clean typography (sans-serif fonts)
  - Consistent color palette (2-3 main colors)
  - Ample whitespace
  - Subtle shadows and borders
  
- [ ] Organize information hierarchy:
  - Hero section with title/description
  - Input controls clearly visible
  - Results prominently displayed
  - Supplementary info in collapsible sections
  
- [ ] Add interactive elements:
  - Hover effects on buttons/controls
  - Smooth transitions and animations
  - Loading indicators for heavy calculations
  - Success/info messages
  
- [ ] Implement responsive design:
  - Mobile-friendly layout
  - Touch-friendly controls
  - Adaptive column widths
  
- [ ] Add visual polish:
  - Icons for different metrics
  - Color-coded result cards
  - Gradient backgrounds (subtle)
  - Professional color scheme

### Deliverables:
- Modern, polished UI
- Responsive design
- Professional appearance
- Enhanced user experience

---

## Phase 9: Add Advanced Features
**Duration:** 2-4 hours  
**Objective:** Include extra functionality for better user engagement

### Tasks:
- [ ] Trajectory comparison:
  - Save multiple trajectories
  - Display multiple paths on same graph
  - Compare metrics side-by-side
  
- [ ] Interactive physics explanations:
  - Collapsible sections explaining each calculation
  - Formula display with variable substitution
  - Educational annotations on graph
  
- [ ] Export capabilities:
  - Download trajectory data (CSV)
  - Save plot as image (PNG/PDF)
  - Share configuration link
  
- [ ] Animation features:
  - Play animation of projectile motion
  - Slow-motion replay
  - Show velocity vectors during flight
  
- [ ] Unit conversion:
  - Support for different units (ft/s, km/h, etc.)
  - Automatic conversion display

### Deliverables:
- Comparison feature working
- Export functionality available
- Educational content integrated
- Animation system (if included)

---

## Phase 10: Testing & Optimization
**Duration:** 2-3 hours  
**Objective:** Ensure reliability and performance

### Tasks:
- [ ] Functional testing:
  - Test all slider ranges
  - Verify physics calculations accuracy
  - Test drag interface responsiveness
  - Check edge cases (0°, 90°, extreme velocities)
  
- [ ] Performance optimization:
  - Profile app with Streamlit's built-in tools
  - Optimize calculations if needed
  - Cache heavy computations with `@st.cache_data`
  - Monitor memory usage
  
- [ ] Cross-browser testing:
  - Test on Chrome, Firefox, Safari
  - Verify responsive design
  - Check drag interface on different browsers
  
- [ ] User acceptance testing:
  - Get feedback on UI/UX
  - Verify intuitive navigation
  - Test on different screen sizes
  
- [ ] Documentation:
  - Add code comments and docstrings
  - Create user guide (in-app help)
  - Document physics formulas used

### Deliverables:
- Verified functionality
- Optimized performance
- Comprehensive documentation
- Ready for deployment

---

## Phase 11: Deployment & Distribution
**Duration:** 1-2 hours  
**Objective:** Make app publicly accessible

### Tasks:
- [ ] Choose deployment platform:
  - Streamlit Cloud (easiest, free tier available)
  - Heroku (with Procfile configuration)
  - AWS/Azure/GCP (more complex)
  - Docker containerization (optional)
  
- [ ] Prepare for deployment:
  - Finalize `requirements.txt`
  - Create `.streamlit/config.toml` for production
  - Set up environment variables if needed
  - Add `README.md` with usage instructions
  
- [ ] Deploy application:
  - Push to GitHub repository
  - Deploy via chosen platform
  - Configure custom domain (if desired)
  - Test deployed version
  
- [ ] Monitor and maintain:
  - Check error logs
  - Monitor performance metrics
  - Update dependencies regularly
  - Gather user feedback

### Deliverables:
- Application deployed and live
- Publicly accessible URL
- Monitoring in place
- Update process documented

---

## Implementation Timeline

| Phase | Tasks | Est. Duration | Status |
|-------|-------|---------------|--------|
| 1 | Project Setup | 1-2 hours | ⬜ |
| 2 | Physics Engine Refactor | 1-2 hours | ⬜ |
| 3 | Base App Structure | 1-2 hours | ⬜ |
| 4 | Slider Controls | 1-2 hours | ⬜ |
| 5 | Visualization | 1-2 hours | ⬜ |
| 6 | Drag Interface Design | 2-3 hours | ⬜ |
| 7 | Drag Integration | 1-2 hours | ⬜ |
| 8 | UI/UX Enhancement | 2-3 hours | ⬜ |
| 9 | Advanced Features | 2-4 hours | ⬜ |
| 10 | Testing & Optimization | 2-3 hours | ⬜ |
| 11 | Deployment | 1-2 hours | ⬜ |
| **TOTAL** | | **18-28 hours** | |

---

## Technology Stack

### Frontend
- **Streamlit** - Web framework and UI
- **Plotly** - Interactive charts
- **Streamlit Components** - Drag interface implementation
- **HTML/CSS/JavaScript** - Custom styling and interactions

### Backend
- **Python 3.8+** - Core language
- **Math library** - Physics calculations
- **NumPy** (optional) - Advanced numerical operations

### Deployment
- **Streamlit Cloud**, **Heroku**, or **Docker**
- **GitHub** - Version control

---

## Key Features Summary

✨ **Modern UI**: Clean, minimalist design with professional styling  
🎯 **Interactive Controls**: Sliders for precise input  
🎮 **Drag Interface**: Intuitive ball-on-bar input method  
📊 **Real-time Visualization**: Interactive trajectory plots  
🧮 **Physics Breakdown**: Step-by-step calculations  
📱 **Responsive Design**: Works on desktop and mobile  
📈 **Advanced Features**: Comparison, export, animation  
🚀 **Deployment Ready**: Easy cloud deployment  

---

## Success Criteria

- ✅ App successfully converts physics inputs to trajectory calculations
- ✅ Drag interface is intuitive and responsive
- ✅ UI is modern, clean, and user-friendly
- ✅ Results are accurate and clearly displayed
- ✅ App performs smoothly with no lag
- ✅ Mobile-responsive design works on all devices
- ✅ Application is deployed and publicly accessible

---

## Notes & Considerations

- **Drag Interface Library**: Phase 6 requires selecting appropriate component library. `streamlit-elements` or custom HTML component recommended.
- **Physics Accuracy**: Ensure all calculations match AP Physics C curriculum standards.
- **Performance**: Use Streamlit's caching mechanisms to optimize frequent calculations.
- **Accessibility**: Consider WCAG compliance for drag interface.
- **Browser Compatibility**: Test drag interface extensively on different browsers.
