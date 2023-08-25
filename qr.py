
from qrcode import QRCode
import qrcode

# QR del video

url = "https://www.google.com"

qr = QRCode(version=1, error_correction=qrcode.ERROR_CORRECT_L, box_size=2, border=2)
qr.add_data(url)
qr.make()

img = qr.make_image()
img.save("img/qr.png")