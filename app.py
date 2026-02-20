import streamlit as st
import google.generativeai as genai
from PIL import Image

# Configure Google Generative AI with API key
# Works with both .env files (local) and Streamlit Cloud secrets
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
except FileNotFoundError:
    # Fallback if secrets.toml not found
    from dotenv import load_dotenv
    import os
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=api_key)

# ─────────────────────────────────────────────
# Function to get Gemini response
# ─────────────────────────────────────────────
def get_gemini_response(input_text, image, prompt):
    model = genai.GenerativeModel('gemini-2.5-flash')
    response = model.generate_content([input_text, image[0], prompt])
    return response.text

# ─────────────────────────────────────────────
# Function to read image and prepare for Gemini
# ─────────────────────────────────────────────
def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# ─────────────────────────────────────────────
# Prompt for the Gemini model
# ─────────────────────────────────────────────
input_prompt = """
You are a civil engineer. Please describe the structure in the image and provide details such as its type,

1. Type of structure – Description
2. Materials used – Description
3. Dimensions (if visible) – Description
4. Construction methods – Description
5. Notable features or engineering challenges – Description
6. Estimated age or era of construction (if determinable) – Description
7. Structural condition and maintenance observations – Description
8. Safety considerations – Description

Please be thorough and technical in your analysis, using appropriate civil engineering terminology.
"""

# ─────────────────────────────────────────────
# Initialize Streamlit App
# ─────────────────────────────────────────────
st.set_page_config(page_title="Civil Engineering Insight Studio", page_icon="🏗️")

# Custom CSS for better UI
st.markdown("""
    <style>
    * {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #e8eef7 100%);
        padding: 2rem;
    }
    h1, h2, h3 {
        color: #1a3a52;
        font-weight: 600;
    }
    .stButton>button {
        background: linear-gradient(90deg, #2c6fad 0%, #3a7fbd 100%);
        color: white;
        font-size: 16px;
        font-weight: 600;
        border-radius: 8px;
        padding: 0.7em 2em;
        border: none;
        box-shadow: 0 4px 6px rgba(44, 111, 173, 0.2);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #1a4f80 0%, #2a5fa0 100%);
        box-shadow: 0 6px 12px rgba(26, 79, 128, 0.3);
        transform: translateY(-2px);
    }
    .stButton>button:active {
        transform: translateY(0);
    }
    .stTextInput>div>input {
        border-radius: 8px;
        border: 2px solid #2c6fad;
        padding: 0.7em;
        font-size: 15px;
        transition: all 0.3s ease;
    }
    .stTextInput>div>input:focus {
        border-color: #3a7fbd;
        box-shadow: 0 0 8px rgba(44, 111, 173, 0.3);
    }
    .output-box {
        background-color: #ffffff;
        color: #1a3a52;
        border-left: 5px solid #2c6fad;
        border-radius: 8px;
        padding: 1.5rem;
        margin-top: 1.5rem;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
        line-height: 1.6;
    }
    .stFileUploader>div>div>div {
        border: 2px dashed #2c6fad;
        border-radius: 8px;
        padding: 2rem;
    }
    .stFileUploader>div>button {
        background-color: #2c6fad;
        color: white;
        border-radius: 8px;
    }
    .stImage {
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    hr {
        border: none;
        height: 2px;
        background: linear-gradient(90deg, transparent, #2c6fad, transparent);
        margin: 1.5rem 0;
    }
    </style>
""", unsafe_allow_html=True)

st.header("🏗️ Civil Engineering Insight Studio")
st.markdown("""
    <p style='font-size: 18px; color: #4a7ba7; font-weight: 500; margin-bottom: 10px;'>
    ✨ Analyze civil engineering structures with AI-powered insights
    </p>
""", unsafe_allow_html=True)

st.divider()

# ─── Input Section ───
st.markdown("<h3 style='color: #1a3a52;'>📋 Upload & Analyze</h3>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("<p style='color: #4a7ba7; font-weight: 500;'>Custom Prompt (Optional)</p>", unsafe_allow_html=True)
    input_text = st.text_input("Enter your prompt:", key="input",
                               placeholder="e.g., Identify materials, structural risks, etc.",
                               label_visibility="collapsed")

with col2:
    st.markdown("<p style='color: #4a7ba7; font-weight: 500;'>Select Structure Image</p>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Upload image:", type=["jpg", "jpeg", "png"],
                                     label_visibility="collapsed")

st.divider()

# Display uploaded image
if uploaded_file is not None:
    st.markdown("<h4 style='color: #1a3a52;'>📸 Preview</h4>", unsafe_allow_html=True)
    image = Image.open(uploaded_file)
    st.image(image, use_column_width=True)

st.divider()

# Submit button with better styling
col_btn = st.columns([1, 4])
with col_btn[0]:
    submit = st.button("🚀 Analyze Structure", use_container_width=True)

st.divider()

# ─────────────────────────────────────────────
# On Submit: Process and display response
# ─────────────────────────────────────────────
if submit:
    try:
        with st.spinner("🔄 Analyzing structure..."):
            image_data = input_image_setup(uploaded_file)
            response = get_gemini_response(input_text, image_data, input_prompt)

        st.markdown("<h3 style='color: #1a3a52;'>🏛️ Analysis Report</h3>", unsafe_allow_html=True)
        st.markdown(
            f'<div class="output-box">{response}</div>',
            unsafe_allow_html=True
        )
    except FileNotFoundError:
        st.error("❌ Please upload an image before analyzing.")
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")

# ─── Footer ───
st.divider()
st.markdown(
    "<p style='text-align:center; color: #4a7ba7; font-size: 13px; font-weight: 500;'>"
    "🏗️ Civil Engineering Insight Studio · Powered by Google Gemini 2.5 Flash"
    "</p>",
    unsafe_allow_html=True
)
