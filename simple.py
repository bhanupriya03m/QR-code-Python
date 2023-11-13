import qrcode

data='check now!'

img=qrcode.make(data)

img.save('qr1.png')
