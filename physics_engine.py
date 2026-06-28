"""
Physics engine for projectile motion calculations.
Handles all kinematics computations for AP Physics C curriculum.
"""

import math
from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class ProjectileResults:
    """Structured data containing all projectile motion calculations."""
    v0: float
    angle_degrees: float
    v0x: float
    v0y: float
    t_apex: float
    t_total: float
    y_max: float
    x_max: float
    trajectory_x: List[float]
    trajectory_y: List[float]


def validate_inputs(v0: float, angle_degrees: float) -> Tuple[bool, str]:
    """
    Validate projectile motion inputs.
    
    Args:
        v0: Initial velocity in m/s
        angle_degrees: Launch angle in degrees
    
    Returns:
        Tuple of (is_valid, error_message)
    """
    if v0 < 0.1 or v0 > 100:
        return False, "Velocity must be between 0.1 and 100 m/s"
    if angle_degrees < 0 or angle_degrees > 90:
        return False, "Angle must be between 0 and 90 degrees"
    return True, ""


def generate_trajectory_points(
    v0x: float, v0y: float, t_total: float, g: float = 9.8, intervals: int = 100
) -> Tuple[List[float], List[float]]:
    """
    Generate trajectory points for plotting.
    
    Args:
        v0x: Horizontal velocity component (m/s)
        v0y: Vertical velocity component (m/s)
        t_total: Total flight time (seconds)
        g: Gravitational acceleration (m/s²)
        intervals: Number of data points to generate
    
    Returns:
        Tuple of (x_points, y_points)
    """
    time_steps = [(t_total * i) / (intervals - 1) for i in range(intervals)]
    x_points = [v0x * t for t in time_steps]
    y_points = [v0y * t - 0.5 * g * (t**2) for t in time_steps]
    return x_points, y_points


def solve_projectile(v0: float, angle_degrees: float, g: float = 9.8) -> ProjectileResults:
    """
    Solve projectile motion problem.
    
    Args:
        v0: Initial velocity in m/s
        angle_degrees: Launch angle in degrees
        g: Gravitational acceleration (m/s²), default 9.8
    
    Returns:
        ProjectileResults object with all calculations
    
    Raises:
        ValueError: If inputs are invalid
    """
    is_valid, error_msg = validate_inputs(v0, angle_degrees)
    if not is_valid:
        raise ValueError(error_msg)
    
    # Convert angle to radians
    angle_radians = math.radians(angle_degrees)
    
    # Resolve velocity components
    v0x = v0 * math.cos(angle_radians)
    v0y = v0 * math.sin(angle_radians)
    
    # Calculate time metrics
    t_total = (2 * v0y) / g
    t_apex = t_total / 2
    
    # Calculate height and range
    y_max = (v0y**2) / (2 * g)
    x_max = v0x * t_total
    
    # Generate trajectory points
    trajectory_x, trajectory_y = generate_trajectory_points(v0x, v0y, t_total, g)
    
    return ProjectileResults(
        v0=v0,
        angle_degrees=angle_degrees,
        v0x=v0x,
        v0y=v0y,
        t_apex=t_apex,
        t_total=t_total,
        y_max=y_max,
        x_max=x_max,
        trajectory_x=trajectory_x,
        trajectory_y=trajectory_y,
    )


def get_physics_breakdown(results: ProjectileResults) -> str:
    """
    Generate a formatted physics breakdown explanation.
    
    Args:
        results: ProjectileResults object
    
    Returns:
        Formatted string with step-by-step calculations
    """
    breakdown = f"""
### Physics Breakdown

**1. Velocity Components:**
- V₀ₓ = {results.v0} × cos({results.angle_degrees}°) = **{results.v0x:.2f} m/s**
- V₀ᵧ = {results.v0} × sin({results.angle_degrees}°) = **{results.v0y:.2f} m/s**

**2. Time to Apex:**
- t_apex = V₀ᵧ / g = {results.v0y:.2f} / 9.8 = **{results.t_apex:.2f} seconds**

**3. Total Flight Time:**
- t_total = 2 × t_apex = **{results.t_total:.2f} seconds**

**4. Maximum Height:**
- h_max = V₀ᵧ² / (2g) = {results.v0y:.2f}² / 19.6 = **{results.y_max:.2f} meters**

**5. Horizontal Range:**
- Range = V₀ₓ × t_total = {results.v0x:.2f} × {results.t_total:.2f} = **{results.x_max:.2f} meters**
"""
    return breakdown
