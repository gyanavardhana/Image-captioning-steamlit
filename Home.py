import streamlit as st
from PIL import Image
import base64

# Function to load image and convert to base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Load images
infosys_image = get_base64_image("static/infosys.jpg")
springboard_image = get_base64_image("static/Spring.png")
surf_image = get_base64_image("static/surf.jpg")
workflow_image = get_base64_image("static/workflow.png")
extraction_image = get_base64_image("static/extraction.png")
context_image = get_base64_image("static/Context.jpg")
example_image = get_base64_image("static/Example.jpg")
xray_image = get_base64_image("static/xray.jpg")
travel_guide_image = get_base64_image("static/travel-guide.jpg")
cctv_image = get_base64_image("static/cctv1.jpg")

# Load custom CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("styles.css")

# Streamlit application
def main():
    # Navbar
    st.sidebar.success("Select a Usecase above.")
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

    # Body content
    st.markdown(
        f"""
        <div class="bg-gray-800 text-white px-4 py-8">
          <div class="container mx-auto">
            <h2 class="text-2xl font-bold mb-4">Image Captioning</h2>
            <img src="data:image/jpeg;base64,{surf_image}" alt="Sample" class="h-auto mb-4 rounded-lg shadow-lg"/>
            <h3 class="text-xl font-semibold mb-2">Caption: Surfer surfing the sea</h3>
            <p class="text-lg mb-6">
              Image captioning is an advanced technology that bridges the gap
              between computer vision and natural language processing. It involves
              generating descriptive and contextually relevant text captions for
              images, enabling machines to understand and articulate visual
              content in human language.
            </p>
            <h3 class="text-xl font-semibold mb-2">How Does Image Captioning Work?</h3>
            <img src="data:image/jpeg;base64,{workflow_image}" alt="Sample" class="h-auto mb-4 rounded-lg shadow-lg"/>
            <h3 class="text-xl font-semibold mb-2">Basic workflow of Image Captioning</h3>
            <p class="text-lg mb-4">
              Image captioning systems leverage deep learning models, particularly
              convolutional neural networks (CNNs) for image feature extraction
              and recurrent neural networks (RNNs) or transformers for language
              generation. The process involves:
            </p>
            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-3 mb-5">
              <div class="col-span-1">
                <img src="data:image/jpeg;base64,{extraction_image}" alt="Extraction" class="h-80 w-full rounded-lg shadow-lg"/>
              </div>
              <div class="col-span-1">
                <img src="data:image/jpeg;base64,{context_image}" alt="Context" class="h-80 w-full rounded-lg shadow-lg"/>
              </div>
              <div class="col-span-1">
                <img src="data:image/jpeg;base64,{example_image}" alt="Example" class="h-80 w-full rounded-lg shadow-lg"/>
              </div>
            </div>
            <ul class="list-disc list-inside mb-4">
              <li>
                Feature Extraction: Analyzing the image to identify objects,
                actions, and scenes using a pre-trained CNN.
              </li>
              <li>
                Contextual Understanding: Integrating the extracted features into
                an RNN or transformer model to understand the relationships and
                context within the image.
              </li>
              <li>
                Caption Generation: Producing a coherent and contextually accurate
                textual description based on the visual analysis.
              </li>
            </ul>
            <h3 class="text-xl font-semibold mb-2">Applications of Image Captioning</h3>
            <ul class="list-disc list-inside mb-4 space-y-2">
              <li>
                Accessibility: Enhancing accessibility for visually impaired
                individuals by providing textual descriptions of images.
              </li>
              <li>
                Content Management: Automating the tagging and categorization of
                images in large databases.
              </li>
              <li>
                E-commerce: Enriching product listings with automatic
                descriptions.
              </li>
              <li>
                Social Media: Automatically generating captions for user-uploaded
                images.
              </li>
              <li>
                Surveillance and Security: Analyzing and describing surveillance
                footage.
              </li>
            </ul>
          </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Use Cases section with three cards
    st.markdown(
        f"""
        <div class="bg-gray-800 text-white py-8">
          <div class="container mx-auto px-4">
            <h2 class="text-2xl font-bold mb-4 text-center">Use Cases</h2>
            <div class="card-container">
              <div class="card" onclick="window.location.href='/travel'">
                <img src="data:image/jpeg;base64,{travel_guide_image}" alt="Travel Guide"/>
                <h3>Travel Guide</h3>
                <p>Automatically describing landmarks and scenic spots in travel photos, enriching travel guides and blogs with informative captions.</p>
              </div>
              <div class="card" onclick="window.location.href='/xray'">
                <img src="data:image/jpeg;base64,{xray_image}" alt="X-Ray Captioning"/>
                <h3>X-Ray Captioning</h3>
                <p>Generating detailed and accurate captions for medical x-ray images, aiding in diagnostic processes and medical reporting.</p>
              </div>
              <div class="card" onclick="window.location.href='/cctv'">
                <img src="data:image/jpeg;base64,{cctv_image}" alt="CCTV Analysis"/>
                <h3>CCTV Analysis</h3>
                <p>Analyzing CCTV camera footage to detect and describe activities and events, enhancing security monitoring and incident response.</p>
              </div>
            </div>
          </div>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
