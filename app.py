import cv2
import streamlit as st
from PIL import Image
import io
import qrcode
import numpy as np
import cv2



def app():
    st.title("QR Code Generator and Decoder")

    # User input for QR code text
    input_text = st.text_input("Enter text or URL to generate QR Code:")

    # QR code generation
    if st.button("Generate QR Code"):
        if input_text:
            qr = qrcode.make(input_text)

            # Save the image to a bytes buffer
            img_byte_arr = io.BytesIO()
            qr.save(img_byte_arr, format='PNG')
            img_byte_arr = img_byte_arr.getvalue()

            # Display the generated QR code
            st.image(img_byte_arr, caption="Generated QR Code", use_column_width=True)
        else:
            st.error("Please enter text or a URL.")

    # QR code decoding section
    qr_image = st.file_uploader("Upload a QR Code image to decode:", type=["png", "jpg", "jpeg"])

    if qr_image:
        # Read the uploaded image with OpenCV
        img = Image.open(qr_image)
        img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)  # Convert to BGR for OpenCV

        # Decode the QR code
        detector = cv2.QRCodeDetector()
        value, pts, qr_code = detector(img)

        if value:
            st.success(f"Decoded QR Code Text: {value}")
        else:
            st.error("Could not decode the QR code.")
print(cv2.__version__)
if __name__ == "__main__":
    app()
