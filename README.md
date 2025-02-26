Chicken Disease Classification

📸 Screenshots

![Homepage](images/Screensort1.png)

📌 Project Overview

This project is a Chicken Disease Classification System that uses deep learning to predict diseases from images of chickens. The application is built using Flask and provides a REST API for training the model and making predictions.

🚀 Features

🐔 Classifies chicken diseases based on input images

🌐 Flask-based API with endpoints for training and prediction

🖼 Accepts base64-encoded images for inference

🛠 Supports model training via an API call

🔥 CORS enabled for smooth frontend integration

🛠 Tech Stack

Backend: Flask, Flask-CORS

Deep Learning: TensorFlow/Keras or PyTorch (based on your model)

Utilities: NumPy, OpenCV (for image processing)

📂 Project Structure

├── src
│   ├── chicken_diseases_classification
│   │   ├── pipeline
│   │   │   ├── predict.py  # Prediction pipeline
│   │   │   ├── stage_01_data_ingestion.py  # Data ingestion stage
│   │   │   ├── stage_02_prepare_base_model.py  # Model preparation
│   │   │   ├── stage_03_training.py  # Model training
│   │   │   ├── stage_04_evaluation.py  # Model evaluation
│   │   ├── utils
│   │   │   ├── common.py   # Utility functions (decodeImage, etc.)
├── templates
│   ├── index.html  # Frontend UI (if applicable)
├── app.py  # Main Flask app
├── main.py  # Pipeline execution script
├── requirements.txt  # Dependencies
├── README.md  # Project documentation

🛠 Installation & Setup

1️⃣ Clone the Repository

git clone https://github.com/yourusername/chicken-disease-classification.git
cd chicken-disease-classification

2️⃣ Create a Virtual Environment (Optional but Recommended)

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Run the Flask App

python app.py

The API will start at http://0.0.0.0:5000/.

🖥 API Endpoints

➤ Home Page

GET /

Loads the index.html page (if applicable)

➤ Train the Model

POST /train

Triggers the training process using main.py

curl -X POST http://localhost:5000/train

➤ Predict Disease from an Image

POST /predict

Takes a base64-encoded image as input and returns the predicted disease

curl -X POST http://localhost:5000/predict \
    -H "Content-Type: application/json" \
    -d '{"image": "base64_encoded_image_here"}'

🔄 Training Pipeline Execution

The main.py script runs the entire machine learning pipeline in four stages:

1️⃣ Data Ingestion: Loads and processes the dataset.
2️⃣ Prepare Base Model: Sets up the deep learning model architecture.
3️⃣ Training: Trains the model using the dataset.
4️⃣ Evaluation: Evaluates the trained model's performance.

To run the pipeline, execute:

python main.py

📌 TODOs & Future Improvements



📜 License

This project is licensed under the MIT License.

Made with ❤️ by Aryan Thapa

