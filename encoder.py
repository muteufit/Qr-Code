import qrcode

data = input('Enter the data: ')
img = qrcode.make(data)
name = input('Enter Qr name: ')+'.jpg'
img.save(name)
