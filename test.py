import qrcode


def create_qrcode(text): 

    qr = qrcode.QRCode()
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black",back_color='white')
    return img 


qr_gen = create_qrcode("test").resize((500,500))
qr_gen.show()

#img = Image.open("img/logo.png")
#print(img.size)
#print(img.mode)

#img_250 = img.resize((250,250))
#img_250.show()
