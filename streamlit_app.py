import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import time as systime  # For delays

# Streamlit App
st.title("Ball Rolling Down a Curve Simulation (Dynamic)")
st.markdown(
    """
    This simulation shows a ball rolling down a curve based on gravitational acceleration. 
    Adjust the parameters below to see the effect on the ball's motion.
    """
)

# User Inputs
curve_function = st.selectbox(
    "Select a curve type:",
    ["Parabola (y = x^2)", "Sine Wave (y = sin(x))", "Cubic (y = x^3)"]
)

# Define curve and derivative based on selection
if curve_function == "Parabola (y = x^2)":
    curve = lambda x: x**2
    curve_derivative = lambda x: 2 * x
elif curve_function == "Sine Wave (y = sin(x))":
    curve = lambda x: np.sin(x)
    curve_derivative = lambda x: np.cos(x)
elif curve_function == "Cubic (y = x^3)":
    curve = lambda x: x**3
    curve_derivative = lambda x: 3 * x**2

# User-adjustable parameters
g = st.slider("Gravitational acceleration (g)", 1.0, 20.0, 9.81)
dt = st.slider("Time step (dt)", 0.001, 0.1, 0.01)
time_duration = st.slider("Simulation duration (seconds)", 1, 10, 5)

# Time parameters
time = np.arange(0, time_duration, dt)

# Initial conditions
x = [0]  # Initial x position
v = [0]  # Initial velocity

# Simulation
for t in time[1:]:
    slope = curve_derivative(x[-1])  # Slope of the curve at current position
    angle = np.arctan(slope)  # Angle of the slope
    acceleration = g * np.sin(angle)  # Component of gravity along the slope
    v_new = v[-1] + acceleration * dt  # Update velocity
    x_new = x[-1] + v_new * dt  # Update position
    x.append(x_new)
    v.append(v_new)

# Calculate y positions from x
y = curve(np.array(x))

# Set up dynamic visualization
st.write("Visualizing the ball rolling...")

placeholder = st.empty()  # Placeholder for dynamic updates

for i in range(len(x)):
    # Create a new plot for each frame
    fig, ax = plt.subplots(figsize=(10, 6))
    # Plot the curve
    x_curve = np.linspace(min(x), max(x), 500)
    ax.plot(x_curve, curve(x_curve), label="Curve", color="blue")
    # Plot the ball's current position
    ax.plot(x[:i], y[:i], label="Ball path", color="red", linestyle="--")
    ax.scatter(x[i], y[i], color="green", label="Ball", zorder=5, s=100)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Ball Rolling Down a Curve")
    ax.legend()
    ax.grid()
    # Update the Streamlit placeholder
    placeholder.pyplot(fig)
    # Add a delay for animation effect
    systime.sleep(0.01)
