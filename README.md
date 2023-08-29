# Image to ASCII Art Converter

This simple Python application allows you to convert an image into ASCII art. It uses a predefined set of ASCII characters to represent different shades of gray in the image, resulting in a text-based representation of the image.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed
- The following Python packages installed:
  - `tkinter`: Included in most Python installations, used for the graphical user interface (GUI).
  - `Pillow` (PIL): Used for opening, resizing, and processing images.

You can install `Pillow` using `pip`:
   
    pip install Pillow

## Usage
1. Run the ascii_converter.py script using Python. This will open a graphical user interface (GUI).

2. Click the "Open Image" button to select the image you want to convert to ASCII art. Supported image formats include JPG, JPEG, PNG, GIF, BMP, and TIFF.

3. The application will display the converted ASCII art in a text widget. You can adjust the width and height of the text widget as needed to view the ASCII art.

Optionally, you can save the generated ASCII art to a text file.

## Customization
You can customize the ASCII character set used for shading by modifying the ASCII_CHARS variable in the ascii_converter.py script.

## Example
Here's a simple example of how to run the application:

    python ascii.py
