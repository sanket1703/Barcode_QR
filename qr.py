import pyqrcode
from PIL import Image
from pyzbar.pyzbar import decode

# big_code = pyqrcode.create('http://uca.edu')
# big_code.png('test.png')
# big_code.show()



data = decode(Image.open('test.png'))
print(str(data[0].data))


