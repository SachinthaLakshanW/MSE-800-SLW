import math

# Polar → Cartesian
r = 3
theta_deg = 60
theta_rad = math.radians(theta_deg)
x = r * math.cos(theta_rad)
y = r * math.sin(theta_rad)
print("Polar → Cartesian:", x, y)

# Cartesian → Polar
x2, y2 = 3, 6
r2 = math.hypot(x2, y2)
#THis function use for pythagorean theorem(x2 + y2 = r2)
theta_deg2 = math.degrees(math.atan2(y2, x2))
# atan2 returns the angle in radians, converting to degrees
print("Cartesian → Polar:", r2, theta_deg2)