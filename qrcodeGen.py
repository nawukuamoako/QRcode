!pip install qrcode
import qrcode

# qrcode documentation can be found here: https://pypi.org/project/qrcode/

# Data to be encoded in the QR code
data = "https://github.com/"

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4,)

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
imageName="github.png"
img.save("imageName")

print(f"QR Code generated and saved as {imageName}")
