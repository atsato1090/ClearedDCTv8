import streamlit as st
from streamlit_lottie import st_lottie
import requests

# ----------------- PAGE CONFIG -------------------
st.set_page_config(
    page_title="ClearedDCT",
    page_icon="🛫",
    layout="centered",
)

# ----------------- LOAD LOTTIE SAFELY -------------------
def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            st.error(f"Failed to load animation. Status code: {r.status_code}")
            return None
        return r.json()
    except Exception as e:
        st.error(f"Error loading animation: {e}")
        return None

# Aviation clouds animation (new, clean)
clouds_animation = load_lottieurl("https://lottie.host/55e20894-4749-4dbb-ae97-f9f1d49d4790/QEtNUXM94H.json")

# ----------------- PAGE BACKGROUND COLOR -------------------
st.markdown(
    """
    <style>
    .stApp {
        background-color: #e6f0fa;
    }
    .center {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ----------------- CENTERED LOGO -------------------
st.markdown("<div class='center'>", unsafe_allow_html=True)
st.image("logo_loading.png", width=350)  # Increased size for visibility

# ----------------- TITLE -------------------
st.title("ClearedDCT")
st.subheader("Your digital flight plan companion")

# ----------------- LOTTIE ANIMATION -------------------
if clouds_animation:
    st_lottie(clouds_animation, speed=1, height=300, key="clouds")
else:
    st.warning("Cloud animation could not be loaded. Check your internet or the URL.")

# ----------------- ENTER APP BUTTON -------------------
if st.button("🚀 Enter App", use_container_width=True):
    st.switch_page("cleareddct_tabs.py")

st.markdown("</div>", unsafe_allow_html=True)
