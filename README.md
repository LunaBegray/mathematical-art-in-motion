# Mathematical Art in Motion

**Mathematical Art in Motion** is a Python-based project that generates dynamic, mesmerizing animations by combining fractals, polar patterns, and colormap transformations. This project is interactive, allowing users to tweak parameters in real-time using sliders for a personalized artistic experience.

---

## Features

- **Fractal Generation:** Create time-dependent fractal patterns with customizable iterations.
- **Polar Patterns:** Add evolving polar interference patterns with multiple layers.
- **Dynamic Colorization:** Apply shifting colormaps to enhance the visual appeal.
- **Real-time Interaction:** Adjust parameters like size, iterations, layers, and colormap using intuitive sliders.
- **Smooth Animations:** Enjoy fluid transitions with continuous updates in the artwork.

---

## Requirements

To run the project, you need the following dependencies installed in your Python environment:

- `numpy`
- `matplotlib`

You can install these using pip:
```bash
pip install numpy matplotlib
```

---

## How to Use

1. **Run the Script:**
   Execute the script in your Python environment:
   ```bash
   python interactive_art.py
   ```

2. **Interactive Controls:**
   - Use the sliders provided in the interface to adjust the following parameters:
     - **Size:** Control the resolution of the art.
     - **Iterations:** Set the depth of fractal calculations.
     - **Layers:** Change the number of polar interference layers.
     - **Colormap:** Choose from a wide range of colormap options.

3. **Explore Visuals:**
   - Watch the animated patterns evolve in real-time.
   - Experiment with different parameter combinations to create unique artwork.

4. **Close the Window:**
   To stop the animation, close the Matplotlib window.

--- 

## Customization

- **Fractal Algorithm:** Modify the `create_fractal` function to explore different fractal types.
- **Polar Patterns:** Adjust the formula in `create_polar_patterns` for new designs.
- **Colormap:** Add or customize colormaps by modifying the `colorize_art` function.

---

## Acknowledgments

- Built with love for mathematical beauty and dynamic visuals.
- Inspired by the interplay of fractals, polar geometry, and color theory.

