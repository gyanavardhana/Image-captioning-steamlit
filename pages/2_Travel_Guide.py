import streamlit as st
import base64

# Function to load image and convert to base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Define the model metrics
model_metrics = [
    {"metric": "Accuracy", "value": "90%"},
    {"metric": "Precision", "value": "88%"},
    {"metric": "Recall", "value": "92%"},
    {"metric": "F1 Score", "value": "90%"},
]

infosys_image = get_base64_image("static/infosys.jpg")
springboard_image = get_base64_image("static/Spring.png")

# Load custom CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("styles.css")
# Streamlit application
def travel_guide_page():
    # Navbar
    st.markdown(
        f"""
        <div class="navbar">
            <img src="data:image/jpeg;base64,{infosys_image}" class="avatar" alt="Infosys" onclick="window.location.reload()"/>
            <img src="data:image/jpeg;base64,{springboard_image}" class="avatar" alt="Springboard" style="width: 60px; height: 60px;"/>
            <div>
                <h1>Image Captioning Project</h1>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("## Overview")
    st.write(
        """
        Travel guide captioning involves automatically describing landmarks and scenic spots in travel photos,
        enriching travel guides and blogs with informative captions.
        """
    )

    st.write("## Data Preprocessing")
    st.write(
        """
        Data preprocessing steps involve cleaning and preparing the travel images and associated text
        data for model training.
        """
    )

    st.write("## Image Preprocessing")
    st.write(
        """
        Image preprocessing techniques include resizing, normalization, and augmentation to enhance
        the quality and consistency of input images for the captioning model.
        """
    )

    st.write("## Model Metrics")
    st.write("### Model Performance Metrics")
    st.write(
        """
        The table below shows the performance metrics of the travel guide captioning model.
        """
    )

    # Display metrics in a table
    st.table(model_metrics)

# Main function to run the Streamlit app
if __name__ == "__main__":
    travel_guide_page()
