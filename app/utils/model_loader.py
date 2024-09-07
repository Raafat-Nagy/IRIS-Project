import pickle

def load_model(model_path):
    """Load a saved model from the specified path."""
    with open(model_path, "rb") as file:
        loaded_model = pickle.load(file)

    return loaded_model
