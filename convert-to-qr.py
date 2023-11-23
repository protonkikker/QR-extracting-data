import qrcode
from PIL import Image

# Open the image file
with open("cema.png", "rb") as f:
 image_data = f.read()

# Convert the image data into binary
binary_data = ''.join(format(b, '08b') for b in image_data)

# Split the binary data into several parts
parts = [binary_data[i:i+1000] for i in range(0, len(binary_data), 1000)]

# Save the number of parts to a file
with open("num_parts.txt", "w") as f:
 f.write(str(len(parts)))

# Generate QR codes for each part
for i, part in enumerate(parts):
 qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
 )
 qr.add_data(part)
 qr.make(fit=True)
 img = qr.make_image(fill_color="black", back_color="white")
 img = img.resize((200, 200)) # Resize the QR code to a common size
 img.save(f"qr_code_{i}.png") # Save the QR code as a separate image file
