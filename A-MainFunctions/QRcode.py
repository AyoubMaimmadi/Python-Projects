import qrcode

img = qrcode.make(
    'https://gpabooster.netlify.app/'
)
img.save('myQRcode.png')
img.show()