import qrcode
from PIL import Image

qr = qrcode.QRCode(version = 1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)

qr.add_data("https://github.com/Ayushman88")

qr.make(fit=True)

img = qr.make_image(fill_color="#0CD4F3", back_color="#010101")

img.save("Github_web.png")

