import streamlit as st
import os
from agent import run_agent
from file_utils import save_uploaded_file, read_file

WORKSPACE_DIR = "workspace"

st.set_page_config(page_title="Groq AI File Editor")

st.title("📂 Groq AI File Editor")

# Upload section
st.subheader("Upload a File")
uploaded_file = st.file_uploader(
    "Upload a text-based file",
    type=["txt", "md", "json", "py"]
)

if uploaded_file:
    try:
        saved_filename = save_uploaded_file(uploaded_file)
        st.success(f"{saved_filename} uploaded successfully!")
    except Exception as e:
        st.error(str(e))

# List files
files = [
    f for f in os.listdir(WORKSPACE_DIR)
    if os.path.isfile(os.path.join(WORKSPACE_DIR, f))
]

st.subheader("Select File to Edit")
selected_file = st.selectbox("Choose file", files)

if selected_file:
    st.write("### File Preview")
    st.code(read_file(selected_file))

    user_input = st.text_area("Enter instruction")

    if st.button("Run Agent"):
        if user_input:
            try:
                result = run_agent(user_input, selected_file)
                st.success("Result")
                st.code(result)

                st.write("### Updated File Preview")
                st.code(read_file(selected_file))

                with open(os.path.join(WORKSPACE_DIR, selected_file), "rb") as f:
                    st.download_button(
                        "Download Updated File",
                        f,
                        file_name=selected_file
                    )

            except Exception as e:
                st.error(str(e))