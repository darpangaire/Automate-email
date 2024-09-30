import qrcode
def qrCode_generator():
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data('Hello world')
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save('qr.png')
qrCode_generator()