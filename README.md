# SatelliteCalculator
This Python-based application provides a visual and mathematical simulation of satellite orbits around the Earth. It allows users to input orbital parameters, visualize the resulting orbit on a dynamic canvas, and calculate key physical properties such as orbital velocity and escape velocity.

# Features
Orbital Visualization: View a scaled representation of the Earth, the Moon's orbit, and your custom satellite orbit.

Dynamic Zoom: Zoom in and out on the canvas to inspect orbits at different scales.
Interactive Hover: Hover over the Moon or satellite orbits to see the approximate distance from the center of the Earth in real-time.
Orbital Physics Calculator: Automatically calculates:
Orbital Period (hrs)
Average Orbital Velocity (km/s)
Eccentricity
Average Escape Velocity (km/s)

Custom Orbit Customization: Input Aphelion (longest radius), Perihelion (shortest radius), and the orbital ratio/offset.

# Installation & Requirements
Prerequisites
Python 3.x
Tkinter (usually included with Python)
Pillow (PIL) for image handling


# File Structure
mymain.py: The entry point of the application. Handles the primary UI, orbital logic, and physics calculations.
hover.py: Manages the interactive tooltips and distance measurement lines when interacting with canvas objects.
zoomcanva.py: Contains the logic for scaling the Earth, Moon, and satellite orbits relative to the canvas center.

# How to Use
Start the App: Run python mymain.py.
Initialize: Click the "Start" button on the splash screen.
