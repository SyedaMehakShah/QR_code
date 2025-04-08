import io
import qrcode
import streamlit as st
from pyzbar.pyzbar import decode
from PIL import Image

def app():
    st.title("QR Code Generator & Decoder")

    # Input text for QR code generation
    input_text = st.text_input("Enter text or URL to generate QR Code:")

    # Generate QR Code
    if st.button("Generate QR Code"):
        if input_text:
            # Generate QR code using qrcode library
            qr = qrcode.make(input_text)

            # Save the image to a bytes buffer
            img_byte_arr = io.BytesIO()
            qr.save(img_byte_arr, format='PNG')  # Save the QR code image as PNG into the byte array
            img_byte_arr = img_byte_arr.getvalue()  # Retrieve byte data from the buffer

            # Display the QR code in Streamlit
            st.image(img_byte_arr, caption="Generated QR Code", use_column_width=True)

            # Provide an option to download the QR code
            st.download_button("Download QR Code", data=img_byte_arr, file_name="generated_qr_code.png", mime="image/png")

        else:
            st.error("Please enter some text or URL to generate the QR code.")

    # Option to upload an existing QR code image
    st.header("Decode an Existing QR Code")

    uploaded_file = st.file_uploader("Upload a QR Code image to decode", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        # Open the uploaded image
        img = Image.open(uploaded_file)

        # Decode the QR code using pyzbar
        decoded_objects = decode(img)

        if decoded_objects:
            for obj in decoded_objects:
                decoded_text = obj.data.decode("utf-8")
                st.success(f"Decoded Text/URL: {decoded_text}")
        else:
            st.error("No QR Code found in the uploaded image.")

if __name__ == "__main__":
    app()
