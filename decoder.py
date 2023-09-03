import cv2

qrDetector = cv2.QRCodeDetector()


file = input('Enter Qr code file name with extension: ')
reading = cv2.imread(file)

val, points, straight_qrcode = qrDetector.detectAndDecode(reading)

print('The Decoded Data is: ' + val)
