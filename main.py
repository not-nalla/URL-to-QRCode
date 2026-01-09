import qrcode

url=input("Enter the URL:")
filepath="C:\\Users\\vighn\\OneDrive\\Desktop\\qrcodeee.png"

qr = qrcode.QRCode()
qr.add_data(url)
qr.make(fit=1)

image = qr.make_image()
image.save(filepath)
print("QR Generated Succesfully!!!!")