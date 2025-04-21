# Fruit-Image-Classification
CNN-based image classification project for distinguishing between fruits, arrows and humans.

# 🍎 CNN Image Classification – Fruits, Humans & Arrows

This project uses a **Convolutional Neural Network (CNN)** to classify images into **6 types of fruits**, **humans**, and **3 types of arrows**. It demonstrates the effectiveness of deep learning in handling multi-class image classification tasks.

## 🧠 Objective

To build and train a CNN model that can identify and classify:

- 🍌 6 types of fruits  
- 🧍‍♀️ Humans  
- ➡️ 3 types of arrows (e.g., left, right, and up)

## 🛠️ Technologies Used

- Python
- TensorFlow / Keras
- NumPy
- Matplotlib
- OpenCV (optional, for image handling)

## 🗂️ Dataset

The dataset includes labeled images for:
- Fruits: e.g., apple, banana, orange, etc.
- Human class: images of people
- Arrows: images of left, right, and up arrows

Each image is resized and normalized before being fed into the CNN model.

## 🔍 Methodology

1. **Data Preprocessing**  
   - Resize and normalize images  
   - Split dataset into training and validation sets  

2. **CNN Architecture**  
   - Convolutional Layers  
   - Pooling Layers  
   - Flatten Layer  
   - Dense Layers with Softmax output for multi-class classification  

3. **Training the Model**  
   - Loss Function: Categorical Cross-Entropy  
   - Optimizer: Adam  
   - Evaluation Metric: Accuracy  

4. **Evaluation**  
   - Evaluate model performance on unseen validation data  
   - Plot accuracy/loss graphs  

## 📈 Results

The trained CNN model achieves good classification accuracy across all categories. Sample prediction outputs show successful differentiation between fruit types, human figures, and directional arrows.

## 🚀 Future Improvements

- Add more image categories for broader classification  
- Implement real-time classification using a webcam  
- Optimize the model with deeper architectures or transfer learning  
- Deploy the model with a web or mobile interface  

## 📎 License

This project is developed for educational and demonstration purposes.

