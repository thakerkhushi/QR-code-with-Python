import qrcode
import image

qr = qrcode.QRCode(
    version=15,
    box_size=4,
    border=5
)

data = "https://github.com/thakerkhushi"

qr.add_data(data)
qr.make(fit=True)
image = qr.make_image(fill="black", back_color="white")
image.save("test.png")
