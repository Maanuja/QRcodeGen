
import qrcode
from qrcode.image.svg import SvgPathImage

url = "https://ko-fi.com/studiomeens"

qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)

qr.add_data(url)
qr.make(fit=True)

png = qr.make_image(
    fill_color="black",
    back_color="white"
)
png.save("studio_meens_qr.png")

svg = qr.make_image(
    image_factory=SvgPathImage
)
svg.save("studio_meens_qr.svg")

print("QR codes générés avec succès !")
