# DermNet - A Skin Disease Prediction Website

This project is a web application for predicting skin diseases using a Convolutional Neural Network (CNN) model. The frontend is built with React.js, while the backend is powered by Flask. The CNN model has been trained on a dataset of skin disease images.

## Home Page
![App Screenshot](./Dermnet%201.png)

## Upload Page
![App Screenshot](./Dermnet%202.png)

![App Screenshot](./Dermnet%203.png)

## Prediction Page
![App Screenshot](./Dermnet%204.png)

## Inspiration
"Turning a Negative Experience into Positive Change"

In the face of challenges, innovation can emerge that transforms negative experiences into powerful catalysts for positive change. The unfortunate incident of a person being falsely predicted and administered cancer drugs for years serves as a stark reminder of the critical responsibility that rests upon those venturing into the field of medical technology. While such an incident highlights the potential risks of inaccurate predictions, it also underscores the urgency to develop ethical and accurate solutions in skin disease prediction.
Hence building a skin disease prediction application can be a valuable contribution to the field of healthcare and dermatology. Such an application could help individuals identify potential skin issues early on and encourage them to seek professional medical advice. 


## What It Does
DermNet - A skin disease prediction application that takes dermoscopic and normal images as input and predicts the output for 32 different classes, which involves the use of advanced deep learning techniques and medical knowledge. Here's an overview of how this application works and the additional information it could provides.

**Functionality of the Application:**

• Input of dermoscopic image or normal image.

• Prediction: The application uses a trained convolutional neural network (CNN) model to predict

• Output: Provides the user with a prediction of the skin disease or condition.

• Gives the disease overview

• Provides available medical treatments

• Provides home remedies.


## How we built it
• Imported essential libraries

• Understand the data

• Train Test split

• Train the model using CNN to get better results and faster computation (Intel oneAPI Deep Neural Network (oneDNN))

• Model Fitting

• Attempt to gain maximum accuracy

• Save the model


## What we learned
**Intel oneDNN:** Intel oneDNN (Deep Neural Network Library), is used to efficiently preprocess the input images. This might involve tasks like resizing, normalization, and data augmentation to ensure consistent and meaningful input for the neural network.
We designed and trained a deep learning model using a framework like TensorFlow and Keras. These frameworks can leverage oneDNN's optimized operations for better performance during the training process. oneDNN provides a backend for many popular deep learning frameworks, allowing them to take advantage of hardware acceleration.

**Image Analysis:** Image is analyzed using Convolutional Neural Networks (CNNs) architecture which is the critical component in our skin disease prediction application. CNNs excel in extracting intricate patterns and features from images, making them well-suited for identifying subtle visual cues in skin lesions. 


## Features

- Upload an image of a skin lesion for prediction.
- Get predictions for possible skin diseases based on the uploaded image.
- User-friendly web interface for ease of use.

## Technologies Used

- Frontend: React.js
- Backend: Flask
- Deep Learning: Convolutional Neural Network (CNN)

## Installation and Usage

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/skin-disease-prediction.git
   cd skin-disease-prediction
   ```

2. Set up the backend:

   ```bash
   cd backend
   pip install -r requirements.txt
   python app.py
   ```

3. Set up the frontend:

   ```bash
   cd frontend
   npm install
   npm start
   ```

4. Access the application in your web browser at `http://localhost:3000`.

## Model Details

The skin disease prediction model is a Convolutional Neural Network (CNN) trained on a labeled dataset of skin lesion images. The model has been trained to classify different skin diseases based on these images. More details about the model architecture and training process can be found in [model_training.md](backend/model_training.md).

## Contributing

Contributions are welcome! If you find any issues or want to add new features, please feel free to open an issue or submit a pull request.
