import streamlit as st
import requests

# Your Imgflip credentials
USERNAME = "ram12356"
PASSWORD = "ram12356"

# Meme templates (name → ID)
meme_templates = {
    "Drake Hotline Bling": "181913649",
    "Distracted Boyfriend": "112126428",
    "Two Buttons": "87743020",
    "Change My Mind": "129242436",
    "Left Exit 12 Off Ramp": "124822590",
    "Expanding Brain": "93895088",
}

st.set_page_config(page_title="😂 AI Meme Generator", layout="centered")

st.title("😂 AI Meme Generator")
st.write("Enter your idea and captions to generate a meme!")

# User input for topic (optional)
topic = st.text_input("🧠 What's the meme about? (optional)")

# Caption inputs — start empty, no suggestions
top_text = st.text_input("🔼 Top Text", value="")
bottom_text = st.text_input("🔽 Bottom Text", value="")

selected_template = st.selectbox(
    "🖼️ Choose a meme template", list(meme_templates.keys())
)

if st.button("🎉 Generate Meme"):
    if top_text.strip() == "" and bottom_text.strip() == "":
        st.error("Please enter at least one caption text.")
    else:
        template_id = meme_templates[selected_template]
        url = "https://api.imgflip.com/caption_image"
        params = {
            "template_id": template_id,
            "username": USERNAME,
            "password": PASSWORD,
            "text0": top_text,
            "text1": bottom_text,
        }
        response = requests.post(url, params=params).json()

        if response["success"]:
            meme_url = response["data"]["url"]
            st.image(meme_url, caption="Here's your meme!", use_column_width=True)
            st.success("✅ Meme generated successfully!")
        else:
            st.error(
                "❌ Failed to generate meme. Check credentials or try again later."
            )

st.caption(
    "🔥 Made by Saurav Raj Aryal and Manjil Shrestha | Powered by Streamlit & Imgflip API"
)
