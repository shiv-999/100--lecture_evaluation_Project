import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array

# Load the saved model
model_path = "C:\\Users\\2020BEC045\\Brain tumor\\model.h5"
model = load_model(model_path)

# Set the class labels
class_labels = ["glioma_tumor", "meningioma_tumor", "pituitary_tumor", "no_tumor"]

def preprocess_image(image, input_shape):
    img = load_img(image, target_size=input_shape[:2])
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Normalize pixel values to [0, 1]
    return img_array

def main():
    st.title("Brain Tumor Classification")

    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        input_image = preprocess_image(uploaded_file, input_shape=(150, 150, 3))
        prediction = model.predict(input_image)
        predicted_class_index = np.argmax(prediction)
        predicted_class = class_labels[predicted_class_index]

        st.subheader("Prediction")
        st.write(f"Class: {predicted_class}")
        st.image(load_img(uploaded_file), caption="Uploaded Image", use_column_width=True)

if __name__ == "__main__":
    main()
