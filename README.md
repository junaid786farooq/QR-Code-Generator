# QR Code Generator

This is a Python program that generates a QR code from a given text input (such as a URL) and saves it as an image file. The program uses the `qrcode` library to create and customize the QR code.

## Features

- Generates a QR code from a given text input.
- Saves the QR code as an image file (default name is `qr_code.png`).
- Displays the QR code image after generating it.

## How to Use

1. **Install Required Libraries:**
   - Ensure you have the `qrcode` library installed. You can install it using pip:
     ```bash
     pip install qrcode[pil]
     ```

2. **Run the Program:**
   - Execute the script in a Python environment.

3. **Input Instructions:**
   - The program will prompt you to enter the text (such as a URL) for which you want to generate a QR code.
   - Enter the desired text and press enter.

4. **Output:**
   - The program will generate a QR code and save it as an image file (`qr_code.png` by default).
   - The QR code image will be displayed automatically.

## Example

Enter url for QR_Code: https://www.linkedin.com/in/junaid786farooq/ <br>
QR code generated and saved as qr_code.png<br>
(: Check Image for QR Code of --> https://www.linkedin.com/in/junaid786farooq/ :) <br>
<br>
![Example Image](qr_code.png)

## Customization

- You can customize the output file name by passing an optional second argument to the `generate_QRcode` function.

## Requirements

- Python 3.x
- `qrcode` library

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contributions
Contributions are welcome! If you have any suggestions, improvements, or bug fixes, feel free to open an issue or submit a pull request.
