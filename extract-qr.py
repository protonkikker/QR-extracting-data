from PIL import Image
import imageio
from qreader import QReader
import io

# Read the animated GIF as a series of images
images = imageio.mimread('qr_codes.gif')

# Decode each image as a QR code
reader = QReader()
decoded_data = []
for img in images:
  qr_code = reader.detect_and_decode(image=img)
  decoded_data.append(qr_code)

# Combine the decoded data into the original image data
original_data = ''.join(map(str, decoded_data))

# Convert the binary data back into an image
original_image = Image.open(io.BytesIO(int(original_data, 2).to_bytes((len(original_data) + 7) // 8, byteorder='big')))
original_image.save("cema_reconstructed.png")
