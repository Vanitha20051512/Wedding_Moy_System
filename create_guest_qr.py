import qrcode

url = "http://localhost:8501"

img = qrcode.make(url)

img.save("guest_qr.png")

print("Guest QR Code Created Successfully")