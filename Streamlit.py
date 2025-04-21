import streamlit as st
import tensorflow as tf
import numpy as np


#Tensorflow Model Prediction
def model_prediction(test_image):
    model = tf.keras.models.load_model("classify.h5")
    image = tf.keras.preprocessing.image.load_img(test_image,target_size=(64,64))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr]) #convert single image to batch
    predictions = model.predict(input_arr)
    return np.argmax(predictions) #return index of max element

#Sidebar
st.sidebar.title("Dashboard")
app_mode = st.sidebar.selectbox("Select Page",["Home","About Project","Prediction"])

#Main Page
if(app_mode=="Home"):
    st.header("Image Recognition System")
    

#About Project
elif(app_mode=="About Project"):
    st.header("About Project")
    st.subheader("About Dataset")
    st.text("This dataset contains images of the following items:")
    st.code("fruits- banana, apple, kiwi, watermelon, pomegranate, strawberry.")
    st.code("Human pictures and Arrows-[LeftArrows,RightArrows,UpArrows]")
    st.subheader("Content")
    st.text("This dataset contains two folders:")
    st.text("1. train ")
    st.text("2. validation (10% of training images)")

#Prediction Page
elif(app_mode=="Prediction"):
    st.header("Model Prediction")
    test_image = st.file_uploader("Choose an Image:")
    if(st.button("Show Image")):
        st.image(test_image,width=4,use_column_width=True)
    #Predict button
    if(st.button("Predict")):
        st.snow()
        st.write("Our Prediction")
        result_index = model_prediction(test_image)
        #Reading Labels
        with open("labels.txt") as f:
            content = f.readlines()
        label = []
        for i in content:
            label.append(i[:-1])
        st.success("Model is Predicting it's a {}".format(label[result_index]))
