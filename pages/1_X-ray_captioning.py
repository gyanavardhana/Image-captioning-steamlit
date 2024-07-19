import streamlit as st
import pandas as pd
import base64
from transformers import pipeline
from PIL import Image

# Function to load image and convert to base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Define the model metrics
model_metrics = [
    {"metric": "Accuracy", "value": "85%"},
    {"metric": "Precision", "value": "82%"},
    {"metric": "Recall", "value": "88%"},
    {"metric": "F1 Score", "value": "85%"},
]

infosys_image = get_base64_image("static/Infosys.jpg")
springboard_image = get_base64_image("static/Spring.png")
xrayimage = get_base64_image("static/xray.jpg")

# Load custom CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("styles.css")

# Streamlit application
def xray_page():
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
        X-ray captioning involves generating descriptive captions for medical X-ray images to aid in
        diagnostic processes and medical reporting.
        """
    )
    st.markdown(
        f"""
        <div >
            <img src="data:image/jpeg;base64,{xrayimage}" alt="Sample" class="h-auto mb-4 rounded-lg shadow-lg"/>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("## Data Preprocessing")
    st.write(
        """
        Data preprocessing steps involve cleaning and preparing the X-ray images and associated text
        data for model training.
        """
    )

    code = '''
        # Function to preprocess text by cleaning and normalizing
        def preprocess_text(text):
            text = text.lower()
            text = re.sub(r'http\S+|www\S+|ftp\S+', '', text) # removing the links
            text = text.replace('\\n', ' ') # removing the new lines
            text = re.sub(r'\w*\d\w*', '', text) # removing the words containing numbers
            text = re.sub(r'\s+', ' ', text).strip() # removing the spaces
            text = re.sub(r'[^\w\s]', '', text) # removing special characters
            words = text.split()
            stop_words = set(stopwords.words('english'))
            words = [word for word in words if word not in stop_words] # considering only normal words
            stemmer = PorterStemmer()
            words = [stemmer.stem(word) for word in words] # considering the stemmed words
            lemmatizer = WordNetLemmatizer()
            words = [lemmatizer.lemmatize(word) for word in words] #considering the lemmatized words
            text = ' '.join(words)
            return text
    '''

    # Display the code snippet
    st.code(code, language='python')

    # Update the file path
    df = pd.read_csv("static/train_caption_df.csv")
    df1 = df.iloc[:, [1, 2]]
    st.write("### Unprocessed captions data")
    st.dataframe(df1)

    # Display the second dataframe with columns 3 and 4
    df2 = df.iloc[:, [2, 3]]
    st.write("### Processed captions data")
    st.dataframe(df2)

    st.write("## Image Preprocessing")
    st.write(
        """
        Image preprocessing techniques include resizing, normalization, and augmentation to enhance
        the quality and consistency of input images for the captioning model.
        """
    )
    df3 = pd.read_csv('static/test_preprocessed_df.csv')
    st.write("### Processed Images & Captions data")
    st.dataframe(df3)

    st.write("## Model Metrics")
    st.write("### Model Performance Metrics")
    st.write(
        """
        The table below shows the performance metrics of the X-ray captioning model.
        """
    )

    # Display metrics in a table
    st.table(model_metrics)

    # Add image captioning section
    st.write("## Image Captioning")
    st.write(
        """
        Upload an image to generate a caption using the fine-tuned model.
        """
    )

    # Set up the caption pipeline
    caption_pipeline = pipeline("image-to-text", model="nathansutton/generate-cxr")

    # Image upload
    uploaded_image = st.file_uploader('Upload an image', type=["png", "jpg", "jpeg"])

    if uploaded_image is not None:
        # Display the uploaded image
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Button to generate caption
        if st.button("Generate Caption"):
            with st.spinner('Generating caption...'):
                # Generate caption
                captions = caption_pipeline(image)
                # Display the caption
                st.write(captions[0]['generated_text'])

# Main function to run the Streamlit app
if __name__ == "__main__":
    xray_page()
