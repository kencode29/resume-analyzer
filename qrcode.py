import qrcode
qr_code=qrcode.QRCode(version=3,box_size=16,border=5)
data="hello coding world"
qr_code.add_data(data)
qr_code.make(fit=True)
image=qr_code.make_image(fill_color="black",back_color="white")
image.save("qr.png")
print("QR code generated successfully!!")
