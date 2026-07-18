import qrcode


def create_registration_qr():

    # உங்கள் website link இங்கே மாற்றவும்
    website_link = "https://your-wedding-moy-app.streamlit.app"

    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )

    qr.add_data(website_link)
    qr.make(fit=True)

    qr_image = qr.make_image()

    qr_image.save("registration_website_qr.png")

    print("Website Registration QR Created Successfully")


create_registration_qr()