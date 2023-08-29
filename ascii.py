import tkinter as tk
from tkinter import filedialog
from PIL import Image

# Define ASCII characters to represent different shades of gray
ASCII_CHARS = "@%#*+=-:. "

# Function to open an image file and convert it to ASCII art
def convert_image_to_ascii():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif *.bmp *.tiff")])
    
    if not file_path:
        return  # User canceled the file dialog
    
    try:
        img = Image.open(file_path)
    except Exception as e:
        result_text.set("Error: " + str(e))
        return
    
    img = resize_image(img)
    img_gray = image_to_gray(img)
    ascii_art = image_to_ascii(img_gray)
    ascii_art_lines = [ascii_art[i:i + art_width] for i in range(0, len(ascii_art), art_width)]
    
    # Display the ASCII art in the text widget
    ascii_text.delete("1.0", tk.END)
    ascii_text.insert(tk.END, "\n".join(ascii_art_lines))
    result_text.set("Image converted successfully!")

# Function to resize the image
def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width / 1.65
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

# Function to convert grayscale pixel to ASCII character
def gray_to_ascii(gray_value):
    return ASCII_CHARS[gray_value // 25]

# Function to convert image to grayscale
def image_to_gray(image):
    return image.convert("L")

# Function to convert grayscale image to ASCII art
def image_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    for pixel_value in pixels:
        ascii_str += gray_to_ascii(pixel_value)
    return ascii_str

# Create the main window
root = tk.Tk()
root.title("Image to ASCII Art Converter")

# Create a button to open the image file
open_button = tk.Button(root, text="Open Image", command=convert_image_to_ascii)
open_button.pack(pady=10)

# Create a text widget to display the ASCII art with increased width and height
ascii_text = tk.Text(root, wrap=tk.WORD, width=200, height=100)
ascii_text.pack()

# Create a label to display conversion result or error messages
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text)
result_label.pack()

# Define the width of the ASCII art (adjust as needed)
art_width = 100

# Start the GUI main loop
root.mainloop()
