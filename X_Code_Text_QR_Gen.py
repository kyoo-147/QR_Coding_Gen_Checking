# Author: mihcuog@AILab
# Contatct: AI-Lab - Smart Things

import qrcode

text_data = input("Please put data:")
utf8_data = text_data.encode('utf-8')

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(utf8_data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

file_name = f"data_QR_Code\qr_code_{text_data}.png"

with open('myDataFile.text', mode='a', encoding='utf-8') as f:
    # Ghi dữ liệu vào cuối tệp
    f.write(text_data+'\n')

img.save(file_name)

img.show()


