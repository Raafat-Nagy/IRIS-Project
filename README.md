# **IRIS Flower Prediction App**

This repository contains a machine learning project focused on predicting the species of an Iris flower based on its sepal and petal dimensions. The project uses the famous **Iris dataset** and implements a **Streamlit** web app for users to interactively make predictions.

## **Project Structure**

```
IRIS-Project/
│
├── data/
│   └── IRIS.csv
│
├── notebooks/
│   └── IRIS_Classification.ipynb
│
├── models/
│   └── IRIS_Model.pkl
│
├── app/
│   ├── streamlit_app.py
│   ├── images/
│   │   └── iris-flowers.jpg
│   └── utils/
│       ├── __init__.py
│       ├── model_loader.py
│       └── predictor.py
│
└── requirements.txt
```

## **Project Overview**

This project involves:
- **Data Exploration**: Analyzing the Iris dataset to understand its structure and distributions.
- **Model Training**: Training a machine learning model using a **Support Vector Classifier** to predict the species of the flower.
- **Model Deployment**: A Streamlit-based web application that allows users to input the sepal and petal dimensions of an Iris flower and get a predicted species.

### **Features**
- Interactive inputs for flower dimensions (sepal length, sepal width, petal length, petal width).
- Displays the predicted species along with a representative image of the flower.
- Clean and simple user interface powered by **Streamlit**.

## **Running the App**

### **1. Install Dependencies**

Make sure you have Python installed. Then, install the required dependencies by running:

```bash
pip install -r requirements.txt
```

### **2. Run the Streamlit App**

To run the Streamlit app, navigate to the `app/` directory and run the following command:

```bash
streamlit run app/streamlit_app.py
```

This will launch the app in your browser where you can input the sepal and petal dimensions to get a prediction.

### **3. Interact with the App**

Once the app is running, you can:
- Adjust the sliders to set the dimensions of the sepal and petal.
- Click the **"Prediction"** button to view the predicted species and its corresponding image.

## **Model Training**

To retrain the model, refer to the `notebooks/iris_classification.ipynb` notebook, which walks through:
- Data loading and preprocessing.
- Model training using a Support Vector Classifier.
- Saving the trained model as `IRIS_Model.pkl`.

## **Files Explained**

- **`streamlit_app.py`**: The main code for the web app.
- **`model_loader.py`**: Contains the `load_model` function to load the saved model (`IRIS_Model.pkl`).
- **`predictor.py`**: Contains the `get_prediction` function that takes the model and input data to return the predicted species.
- **`images/`**: Contains the images for each predicted species, as well as a general image for IRIS flowers.

## **Dataset**

The Iris dataset (`IRIS.csv`) is used in this project. It contains 150 observations of Iris flowers, each with:
- Sepal length (cm)
- Sepal width (cm)
- Petal length (cm)
- Petal width (cm)
- Species (Setosa, Versicolor, Virginica)

## **Dependencies**

All dependencies are listed in `requirements.txt`. These include:
- **Numpy**: For numerical computations.
- **Pandas**: For data manipulation.
- **Matplotlib**: For plotting graphs and charts.
- **Seaborn**: For data visualization during exploratory data analysis.
- **Scikit-learn**: For training the machine learning model.
- **Streamlit**: For building the interactive web app.
