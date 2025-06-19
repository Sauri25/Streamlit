import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import os
import requests
from io import BytesIO

# Comprehensive meme template library
MEME_TEMPLATES = {
    # Popular Classic Memes
    "Drake Hotline Bling": "https://i.imgflip.com/30b1gx.jpg",
    "Distracted Boyfriend": "https://i.imgflip.com/1bij.jpg",
    "Two Buttons": "https://i.imgflip.com/9vct.jpg",
    "Expanding Brain": "https://i.imgflip.com/1jwhww.jpg",
    "Batman Slapping Robin": "https://i.imgflip.com/9ehk.jpg",
    # Reaction Memes
    "Woman Yelling at Cat": "https://i.imgflip.com/23ls.jpg",
    "Change My Mind": "https://i.imgflip.com/24y43o.jpg",
    "Surprised Pikachu": "https://i.imgflip.com/2kbn1e.jpg",
    # Advice Animals
    "Success Kid": "https://i.imgflip.com/2hgfw.jpg",
    "Bad Luck Brian": "https://i.imgflip.com/2h7i8s.jpg",
    "Overly Attached Girlfriend": "https://i.imgflip.com/2hgfw.jpg",
    # Current Trends
    "Wojak (Feels Guy)": "https://i.imgflip.com/2/1h7in3.jpg",
    # Blank Templates
    "Blank 4-Panel": "https://i.imgflip.com/9vct.jpg",
    "Blank 2-Panel": "https://i.imgflip.com/1bij.jpg",
    # Custom Option
    "Custom Upload": None,
}

# Default font (using Arial, but you can replace with Impact font if available)
try:
    FONT = ImageFont.truetype("arial.ttf", 40)
except:
    FONT = ImageFont.load_default()


def create_meme(image, top_text, bottom_text, text_color="white", stroke_color="black"):
    """Add text to image to create meme"""
    draw = ImageDraw.Draw(image)

    # Calculate text width and position
    image_width, image_height = image.size

    # Add top text
    if top_text:
        top_text_width = draw.textlength(top_text, font=FONT)
        draw.text(
            ((image_width - top_text_width) / 2, 10),
            top_text,
            font=FONT,
            fill=text_color,
            stroke_width=2,
            stroke_fill=stroke_color,
        )

    # Add bottom text
    if bottom_text:
        bottom_text_width = draw.textlength(bottom_text, font=FONT)
        draw.text(
            ((image_width - bottom_text_width) / 2, image_height - 50),
            bottom_text,
            font=FONT,
            fill=text_color,
            stroke_width=2,
            stroke_fill=stroke_color,
        )

    return image


def load_image(image_source):
    """Load image from URL or file upload"""
    if isinstance(image_source, str):  # URL
        response = requests.get(image_source)
        return Image.open(BytesIO(response.content))
    else:  # Uploaded file
        return Image.open(image_source)


def main():
    st.title("📸 Meme Generator App")
    st.write("Create your own memes in seconds!")

    # Sidebar for template selection and customization
    with st.sidebar:
        st.header("Settings")

        selected_template = st.selectbox(
            "Select a meme template", list(MEME_TEMPLATES.keys())
        )

        # File upload if custom selected
        uploaded_file = None
        if selected_template == "Custom Upload":
            uploaded_file = st.file_uploader(
                "Upload your own image", type=["jpg", "jpeg", "png"]
            )
            if not uploaded_file:
                st.warning("Please upload an image to continue")
                return

        # Customization options
        st.header("Customization")
        text_color = st.color_picker("Text Color", "#FFFFFF")
        stroke_color = st.color_picker("Stroke Color", "#000000")

    # Get the selected image
    if selected_template != "Custom Upload":
        image_url = MEME_TEMPLATES[selected_template]
        image = load_image(image_url)
    else:
        image = load_image(uploaded_file)

    with st.columns([1, 5, 1])[1]:
        # Display the template image
        st.image(image, caption="Selected Template", use_container_width=True)

    # Text inputs
    col1, col2 = st.columns(2)
    with col1:
        top_text = st.text_input(
            "Top Text", "", help="Text that appears at the top of the meme"
        )
    with col2:
        bottom_text = st.text_input(
            "Bottom Text", "", help="Text that appears at the bottom of the meme"
        )

    # Generate meme button
    if st.button("Generate Meme", type="primary"):
        if not top_text and not bottom_text:
            st.warning("Please add some text to your meme!")
        else:
            meme_image = create_meme(
                image.copy(),
                top_text,
                bottom_text,
                text_color=text_color,
                stroke_color=stroke_color,
            )
            st.image(
                meme_image, caption="Your Generated Meme", use_container_width=True
            )

            # Download button
            buf = BytesIO()
            meme_image.save(buf, format="PNG")
            byte_im = buf.getvalue()
            st.download_button(
                label="Download Meme",
                data=byte_im,
                file_name="my_meme.png",
                mime="image/png",
                use_container_width=True,
            )


if __name__ == "__main__":
    main()
