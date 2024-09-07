def get_prediction(model, input_data: list):
    """Make a prediction using the loaded model."""
    result = {
        0: "Iris-setosa",
        1: "Iris-versicolor",
        2: "Iris-virginica",
    }

    predections = model.predict([input_data])[0]
    return result[predections]
