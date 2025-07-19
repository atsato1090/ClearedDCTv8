import streamlit as st

st.set_page_config(
    page_title="ClearedDCT Landing",
    page_icon="✈️",
    layout="centered"
)

# === Styling for centered logo and button ===
st.markdown(
    """
    <style>
    .logo {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 300px;
    }
    .enter-button {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# === Display centered logo ===
st.image("logo_loading.png", use_container_width=True, output_format="PNG", caption="ClearedDCT", clamp=True)

# === Title ===
st.markdown("<h2 style='text-align: center; font-size: 28px;'>Welcome to ClearedDCT</h2>", unsafe_allow_html=True)

# === ENTER APP button ===
st.markdown("<br>", unsafe_allow_html=True)
centered_button = st.columns(3)
with centered_button[1]:
    if st.button("🚀 Enter App", use_container_width=True):
        st.switch_page("cleareddct_tabs.py")  # Ensure this file name matches your deployed app

# === Optional footer ===
st.markdown("<br><p style='text-align: center; font-size: 14px; color: gray;'>Effortless Flight Plan Management</p>", unsafe_allow_html=True)
