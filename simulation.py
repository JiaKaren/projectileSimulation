import math
import matplotlib.pyplot as plt


def solve_projectile(v0, angle_degrees, g=9.8):
    # Convert angle to radians for Python's math functions
    angle_radians = math.radians(angle_degrees)

    # Step 1: Resolve velocity components
    v0x = v0 * math.cos(angle_radians)
    v0y = v0 * math.sin(angle_radians)

    # Step 2: Calculate time of flight (when y = 0)
    # Equation: t = 2 * v0y / g
    t_total = (2 * v0y) / g

    # Step 3: Calculate maximum height (at t_total / 2)
    # Equation: y_max = v0y^2 / (2g)
    y_max = (v0y**2) / (2 * g)
    t_apex = t_total / 2

    # Step 4: Calculate total horizontal range
    # Equation: x = v0x * t_total
    x_max = v0x * t_total

    # Print the step-by-step breakdown
    print("\n" + "=" * 40)
    print("        PHYSICS BREAKDOWN WORK")
    print("=" * 40)
    print(f"1. Break velocity into components:")
    print(f"   v0x = {v0} * cos({angle_degrees}°) = {v0x:.2f} m/s")
    print(f"   v0y = {v0} * sin({angle_degrees}°) = {v0y:.2f} m/s")
    print(f"\n2. Time to reach the apex (peak):")
    print(f"   t_apex = v0y / g = {v0y:.2f} / {g} = {t_apex:.2f} seconds")
    print(f"\n3. Total time in the air:")
    print(f"   t_total = 2 * t_apex = {t_total:.2f} seconds")
    print(f"\n4. Maximum height (Apex):")
    print(
        f"   y_max = (v0y^2) / (2*g) = ({v0y:.2f}^2) / {2*g} = {y_max:.2f} meters"
    )
    print(f"\n5. Total horizontal range:")
    print(
        f"   Range = v0x * t_total = {v0x:.2f} * {t_total:.2f} = {x_max:.2f} meters"
    )
    print("=" * 40)

    # --- PLOTTING THE GRAPH ---
    # Create 100 time intervals from 0 to t_total
    intervals = 100
    time_steps = [
        (t_total * i) / (intervals - 1) for i in range(intervals)
    ]

    # Calculate x and y positions at each time step
    x_points = [v0x * t for t in time_steps]
    y_points = [v0y * t - 0.5 * g * (t**2) for t in time_steps]

    # Plotting
    plt.figure(figsize=(10, 5))
    plt.plot(x_points, y_points, label="Trajectory", color="blue", linewidth=2)

    # Highlight Apex and Landing points
    plt.scatter(
        [x_max / 2],
        [y_max],
        color="red",
        zorder=5,
        label=f"Apex (Max Height: {y_max:.1f}m)",
    )
    plt.scatter(
        [x_max],
        [0],
        color="green",
        zorder=5,
        label=f"Landing (Range: {x_max:.1f}m)",
    )

    # Graph formatting
    plt.title(
        f"Projectile Motion Trajectory (v0 = {v0} m/s, Angle = {angle_degrees}°)"
    )
    plt.xlabel("Horizontal Distance (meters)")
    plt.ylabel("Vertical Distance (meters)")
    plt.axhline(0, color="black", linewidth=0.5, linestyle="--")
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.legend()
    plt.ylim(bottom=0)  # Don't show below ground level
    plt.show()


# --- RUN THE INTERACTIVE PROGRAM ---
print("Welcome to the AP Physics C Projectile Tutor!")
try:
    init_vel = float(input("Enter initial velocity (v0) in m/s: "))
    launch_ang = float(input("Enter launch angle in degrees (0-90): "))

    if 0 <= launch_ang <= 90:
        solve_projectile(init_vel, launch_ang)
    else:
        print("Please enter a realistic angle between 0 and 90 degrees.")
except ValueError:
    print("Please enter valid numbers.")