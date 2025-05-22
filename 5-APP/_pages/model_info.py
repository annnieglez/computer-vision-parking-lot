# _pages/model_info.py

'''Parking Spot Detection App - Model Information Page
This page provides information about the model used for parking spot detection. 
It includes details about the model architecture, dataset, preprocessing steps, and evaluation metrics.
The model is based on MobileNetV2 and is trained to classify parking spots as occupied or empty.
'''	

import streamlit as st

def page():
    st.title("🧠 Model Information")
    
    st.write("""
        This binary classification model is trained to detect if a parking spot is Occupied or Empty.
        
        - 📐 **Input Size**: 224x224 RGB
        - 🔁 **Architecture**: Based on MobilNetV2
        - 🎯 **Output**: 0 (Empty) or 1 (Occupied)
    """)

    st.subheader("📊 Dataset Overview")
    st.markdown("""
    - Overhead images of parking lots that can be found [here](https://drive.google.com/drive/folders/1mxbPv9i2dV00AL-6g2UYNpfK9ASPUcYI?usp=sharing).
    - Balanced dataset with roughly equal examples of empty and occupied spots. 
    - Random variations of lighting and camera position.
    """)

    st.subheader("⚙️ Preprocessing")
    st.markdown("""
    - Images resized to 224x224
    - Normalized pixel values between -1 and 1
    - Spots cropped using connected components on a binary mask
    """)

    st.subheader("🧪 How It Works")
    st.markdown("""
    1. A video is upload with a pre-defined binary mask.
    2. The binary mask identifies parking spot areas.
    3. Each spot is cropped and passed through the model.
    4. The model classifies it as **Occupied** or **Empty**.
    5. Bounding boxes are drawn on the image accordingly.
    """)

    st.subheader("📉 Model Evaluation")
    img_path = os.path.join(os.path.dirname(__file__), "..", "images", "model_performance_chart.png")
    st.image(img_path, width=500)
    st.markdown("""
    - **Precision**: 99.7%  
    - **Recall**: 99.6%  
    - **F1 Score**: 99.6%
    """)

    st.subheader("⚠️ Limitations & Future Work")
    st.markdown("""
    - Currently relies on a static mask — may need dynamic spot detection for new layouts.
    - Future improvements: Fine-tuning on more diverse datasets.
    """)

    st.subheader("🔗 Resources")
    st.markdown("""
    - [📂 Dataset and model](https://drive.google.com/drive/folders/1mxbPv9i2dV00AL-6g2UYNpfK9ASPUcYI?usp=sharing)
    - [🔧 GitHub Repository](https://github.com/annnieglez/computer-vision-parking-lot)
    """)