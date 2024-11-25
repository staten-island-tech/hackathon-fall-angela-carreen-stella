
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Pillow for handling images
import random

# Create the main window
root = tk.Tk()
root.title("Memory Matching Game")

# Define the dimensions of the game board
rows, cols = 4, 4
button_list = []
image_paths = ['path_to_image1.jpg', 'path_to_image2.jpg', 'path_to_image3.jpg', 'path_to_image4.jpg'] * 2  # List of image paths

# Shuffle the images randomly
random.shuffle(image_paths)

# Function to load and display an image
def load_image(image_path):
    img = Image.open(image_path)  # Open image file
    img = img.resize((100, 100))  # Resize image to fit in buttons
    return ImageTk.PhotoImage(img)  # Convert to a format tkinter can handle

# Function to handle button clicks
def on_button_click(index):
    button = button_list[index]
    if not button["state"] == "normal":
        return  # If the button is already matched, do nothing
    
    button.config(image=load_image(image_paths[index]))  # Show the image on the button
    button.image = load_image(image_paths[index])  # Keep a reference to the image

    revealed_buttons.append((index, button))  # Store the revealed button

    if len(revealed_buttons) == 2:
        # Check for match
        idx1, btn1 = revealed_buttons[0]
        idx2, btn2 = revealed_buttons[1]

        if image_paths[idx1] == image_paths[idx2]:
            # If the images match, disable the buttons
            btn1.config(state="disabled")
            btn2.config(state="disabled")
        else:
            # If the images don't match, hide them again after a brief pause
            root.after(1000, hide_buttons, btn1, btn2)

        revealed_buttons.clear()

# Function to hide buttons (if the images don't match)
def hide_buttons(btn1, btn2):
    btn1.config(image="", state="normal")
    btn2.config(image="", state="normal")

# Create the game board
revealed_buttons = []
for i in range(rows):
    row_buttons = []
    for j in range(cols):
        index = i * cols + j
        button = tk.Button(root, width=12, height=6, command=lambda i=index: on_button_click(i))
        button.grid(row=i, column=j)
        row_buttons.append(button)
    button_list.append(row_buttons)

root.mainloop()

from PIL import Image

# Specify the relative path
image_path = 'images/image.jpg'  # Image is inside the 'images' folder

# Open the image
img = Image.open(image_path)

# Display the image
img.show()

# Optionally, save it as PNG
img.save('image_as_png.png', 'PNG')
