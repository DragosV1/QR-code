import pyqrcode
import png
from pyqrcode import QRCode 




source = "https://github.com/DragosV1/Projects"

url = pyqrcode.create(source)

url.svg("qrcode.svg", scale = 8)
url.png("qrcode.png", scale = 6)