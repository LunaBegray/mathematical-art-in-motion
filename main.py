import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider

def create_fractal(size, iterations, time_factor):
    """Generate a time-dependent fractal pattern."""
    x = np.linspace(-2, 2, size)
    y = np.linspace(-2, 2, size)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y
    C = Z * np.exp(1j * time_factor)
    fractal = np.zeros_like(X, dtype=np.float64)

    for _ in range(iterations):
        mask = np.abs(Z) <= 2
        Z[mask] = Z[mask]**2 + C[mask]
        fractal[mask] += 1

    fractal /= fractal.max()
    return fractal

def create_polar_patterns(size, layers, time_factor):
    """Generate evolving polar interference patterns."""
    theta = np.linspace(0, 2 * np.pi, size)
    r = np.linspace(0, 1, size)
    R, Theta = np.meshgrid(r, theta)

    polar = np.zeros_like(R, dtype=np.float64)
    for i in range(1, layers + 1):
        polar += np.sin(i * Theta + time_factor) * np.cos(i * R * 2 * np.pi - time_factor)

    polar = (polar - polar.min()) / (polar.max() - polar.min())
    return polar.T  # Match orientation with fractal

def colorize_art(art, colormap, time_factor):
    """Apply a shifting colormap to the generated art."""
    colored = plt.cm.get_cmap(colormap)((art + np.sin(time_factor)) % 1)
    return (colored[:, :, :3] * 255).astype(np.uint8)

def generate_art(size, iterations, layers, time_factor):
    """Combine fractal and polar patterns into a single dynamic artwork."""
    fractal = create_fractal(size, iterations, time_factor)
    polar = create_polar_patterns(size, layers, time_factor)

    # Combine layers with matching dimensions
    combined = fractal * polar
    return (combined - combined.min()) / (combined.max() - combined.min())

def update(frame, ax, size, iterations, layers, colormap, sliders):
    """Update function for the animation."""
    time_factor = frame * 0.1  # Faster transformations

    # Get values from sliders
    size = int(sliders['size'].val)
    iterations = int(sliders['iterations'].val)
    layers = int(sliders['layers'].val)
    colormap_index = int(sliders['colormap'].val)
    colormap = plt.colormaps()[colormap_index % len(plt.colormaps())]

    art = generate_art(size, iterations, layers, time_factor)
    colored_art = colorize_art(art, colormap, time_factor)

    ax.clear()
    ax.imshow(colored_art)
    ax.axis("off")
    ax.set_title("Mathematical Art in Motion", fontsize=16, color="white")
    ax.figure.set_facecolor("black")

def interactive_art():
    """Main function for interactive and animated art generation."""
    initial_size = 300       # Default resolution of the art
    initial_iterations = 50  # Default iterations for fractal
    initial_layers = 6       # Default number of polar layers
    initial_colormap = 0     # Default colormap index

    # Set up Matplotlib figure
    fig, ax = plt.subplots(figsize=(8, 8))
    fig.subplots_adjust(left=0.25, right=0.95, top=0.95, bottom=0.25)

    # Sliders for parameters
    ax_size = plt.axes([0.05, 0.2, 0.15, 0.03], facecolor='lightgray')
    ax_iterations = plt.axes([0.05, 0.15, 0.15, 0.03], facecolor='lightgray')
    ax_layers = plt.axes([0.05, 0.1, 0.15, 0.03], facecolor='lightgray')
    ax_colormap = plt.axes([0.05, 0.05, 0.15, 0.03], facecolor='lightgray')

    sliders = {
        'size': Slider(ax_size, 'Size', 100, 1000, valinit=initial_size, valstep=50),
        'iterations': Slider(ax_iterations, 'Iterations', 10, 200, valinit=initial_iterations, valstep=10),
        'layers': Slider(ax_layers, 'Layers', 1, 12, valinit=initial_layers, valstep=1),
        'colormap': Slider(ax_colormap, 'Colormap', 0, len(plt.colormaps()) - 1, valinit=initial_colormap, valstep=1)
    }

    # Create animation
    anim = FuncAnimation(
        fig, update, frames=300, interval=50,  # Reduced interval for faster updates
        fargs=(ax, initial_size, initial_iterations, initial_layers, plt.colormaps()[initial_colormap], sliders)
    )

    print("Displaying interactive art with sliders. Close the window to stop.")
    plt.show()

if __name__ == "__main__":
    interactive_art()
