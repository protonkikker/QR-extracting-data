import imageio
import numpy as np
from PIL import Image

# Read the number of parts from the file
with open("num_parts.txt", "r") as f:
 num_parts = int(f.read())

# Read the QR codes from the separate files and resize them to a common size
qr_codes = [Image.open(f"qr_code_{i}.png").resize((200, 200)) for i in range(num_parts)]

# Convert the PIL images to NumPy arrays
qr_codes = [np.array(img) for img in qr_codes]

# Create an animated GIF from the QR codes
imageio.mimsave('qr_codes.gif', qr_codes, duration=0.5)
