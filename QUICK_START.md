# 🚀 Quick Start Guide

## Installation & Launch (30 seconds)

### Step 1: Install Dependencies
```bash
python -m pip install --upgrade pip setuptools wheel
python -m pip install --force-reinstall --no-cache-dir -r requirements.txt
```

### Step 2: Launch the App
```bash
streamlit run app.py
```

### Step 3: Open in Browser
Visit: **http://localhost:8501**

---

## What You'll See

### Main Layout
```
┌─────────────────────────────────────────────────────┐
│        🎯 Projectile Motion Simulator              │
│     Interactive Physics Calculator for AP Physics C │
└─────────────────────────────────────────────────────┘

┌──────────┐  ┌────────────────────────────────────────┐
│ Sidebar  │  │        Main Content Area              │
│          │  │                                        │
│ ⚙️ Input │  │ 📈 Max Height  ➡️ Range  ⏱️ Flight Time│
│ Parameters│  │   12.76 m       69.42 m    2.65 s    │
│          │  │                                        │
│ 🎮 Sliders│  │   [Interactive Trajectory Plot]       │
│ or Drag  │  │                                        │
│          │  │ 📖 Physics Breakdown (expandable)     │
│ 🚀 Calc  │  │ 📊 Detailed Metrics (expandable)      │
│ Button   │  │ 💡 Physics Facts (expandable)        │
└──────────┘  └────────────────────────────────────────┘
```

---

## How to Use

### Option 1: Sliders (Easiest)
1. Drag velocity slider (0.1-100 m/s)
2. Drag angle slider (0-90°)
3. Watch trajectory update in real-time

### Option 2: Drag Interface (Most Fun)
1. Click radio button "Drag Interface"
2. Click and drag the green ball
3. Horizontal movement = angle
4. Vertical movement = velocity

---

## Key Buttons & Controls

| Control | Purpose |
|---------|---------|
| Input Method Radio | Switch between Sliders and Drag |
| Velocity Slider | Set initial launch speed |
| Angle Slider | Set launch angle |
| Calculate Button | Refresh calculations |
| Expandable Sections | View physics breakdown & details |

---

## Example Scenarios

### 🏆 Maximum Range (45°)
- Set angle to 45°
- Set velocity to 50 m/s
- Expected range: ~255 m

### 🎯 Straight Up (90°)
- Set angle to 90°
- Set velocity to 25 m/s
- Expected max height: ~31.9 m
- Expected range: 0 m

### 📉 Shallow Arc (20°)
- Set angle to 20°
- Set velocity to 40 m/s
- Short flight time, long range

---

## Tips & Tricks

✨ **Pro Tips**
- 45° gives maximum range (with same height)
- Try velocities from 10-50 m/s first
- Use drag interface for quick exploration
- Read physics facts for learning insights
- Compare 30° vs 60° (same range!)

⚡ **Performance**
- All calculations are instant
- Smooth real-time updates
- No lag on modern browsers

🎨 **Visual Cues**
- Orange star = apex (highest point)
- Green circle = landing point
- Blue line = trajectory path
- Hover for exact coordinates

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| App doesn't start | Reinstall: `pip install -r requirements.txt` |
| Port 8501 in use | Run: `streamlit run app.py --server.port 8502` |
| Drag interface frozen | Refresh browser (F5) and try again |
| Slow performance | Close browser tabs, reduce zoom |

---

## Physics Formulas at a Glance

```
Velocity Components:    V₀ₓ = V₀ cos(θ)     V₀ᵧ = V₀ sin(θ)
Time to Apex:          t_apex = V₀ᵧ / g
Total Flight Time:     t_total = 2 × t_apex
Maximum Height:        h_max = V₀ᵧ² / (2g)
Range:                 R = V₀ₓ × t_total

g = 9.8 m/s² (gravitational acceleration)
```

---

## Common Questions

**Q: Why does 45° give maximum range?**  
A: The angle balances horizontal and vertical velocity components optimally.

**Q: Can I use different gravity values?**  
A: Currently set to 9.8 m/s² (Earth). Future versions may support customization.

**Q: Is this accurate for AP Physics C?**  
A: Yes! Uses standard kinematic equations without air resistance.

**Q: Can I export data?**  
A: Feature coming soon! For now, you can take screenshots or manually record values.

**Q: Works on phone?**  
A: Yes, but drag interface works better with mouse/trackpad.

---

## Next Steps

After launching:
1. ✅ Try different velocity/angle combinations
2. ✅ Explore the physics breakdown
3. ✅ Compare different trajectories mentally
4. ✅ Use drag interface for intuitive exploration
5. ✅ Read physics facts for learning

---

## Stop the App

Press **Ctrl+C** in the terminal where you ran the app.

---

## Need Help?

- Check the [README.md](README.md) for detailed documentation
- Review [IMPLEMENTATION_PLAN.md](IMPLEMENTATION_PLAN.md) for technical details
- Check code comments in Python files
- Restart the app fresh if issues occur

---

**Ready to explore projectile motion? 🚀 Good luck!**
