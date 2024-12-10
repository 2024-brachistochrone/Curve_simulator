import numpy as np
import plotly.graph_objects as go

# Define the curve
def curve(x):
    return x**2

# Simulation parameters
g = 9.81
dt = 0.01
time_duration = 5
time = np.arange(0, time_duration, dt)

# Initial conditions
x = [0]
v = [0]

# Compute positions
for t in time[1:]:
    slope = 2 * x[-1]  # Derivative of x^2
    angle = np.arctan(slope)
    acceleration = g * np.sin(angle)
    v_new = v[-1] + acceleration * dt
    x_new = x[-1] + v_new * dt
    x.append(x_new)
    v.append(v_new)

# Get y values
y = curve(np.array(x))

# Create frames for animation
frames = [
    go.Frame(
        data=[
            go.Scatter(x=x[:k], y=y[:k], mode="lines+markers", marker=dict(color="red"))
        ]
    )
    for k in range(len(x))
]

# Create the figure
fig = go.Figure(
    data=[go.Scatter(x=[x[0]], y=[y[0]], mode="lines+markers", marker=dict(color="red"))],
    layout=go.Layout(
        xaxis=dict(range=[min(x), max(x)], title="x"),
        yaxis=dict(range=[min(y), max(y)], title="y"),
        title="Ball Rolling Down a Curve",
        updatemenus=[
            dict(
                type="buttons",
                showactive=False,
                buttons=[
                    dict(label="Play", method="animate", args=[None]),
                    dict(label="Pause", method="animate", args=[[None], {"frame": {"duration": 0, "redraw": False}, "mode": "immediate"}]),
                ],
            )
        ],
    ),
    frames=frames,
)

fig.show()
