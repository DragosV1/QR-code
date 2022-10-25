import pyqrcode
import png
from pyqrcode import QRCode 

source = "https://github.com/DragosV1/Projects" # Put between quotation mark the link you want to generate a QR code

url = pyqrcode.create(source)

url.svg("qrcode.svg", scale = 8)
url.png("qrcode.png", scale = 6)
