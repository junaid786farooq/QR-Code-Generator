# Programe of generating OR Code.

import qrcode

def generate_QRcode(text, file_name="qr_code.png"):
    
    # Create a QRCode object with specified parameters
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4
        )
    
    # Add the input text to the QR code and optimize its fit.
    qr.add_data(text)
    qr.make(fit=True)

    # Create an image from the QR code with specified colors and save it as "qrimg001.png".
    img = qr.make_image(fill_color = "black", back_color = "white")
    img.save(file_name)
    print(f"QR code generated and saved as {file_name}")
    img.show()  # This will open the QR code image


# Check if the script is run directly, and if so, prompt the user for input, generate the QR code.
if __name__ == "__main__":
    url = input("Enter url for QR_Code: ")
    generate_QRcode(url)
    print(f"(: Check Image for QR Code of --> {url} :)")