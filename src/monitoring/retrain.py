# from some_monitoring_library import get_model_performance
from src.model_training.train_model import train_xgboost_model

def monitor_and_retrain(model, X, y):
    performance = get_model_performance(model)
    if performance < 0.85:
        print("Performance below threshold, retraining...")
        new_model = train_xgboost_model(X, y)
        new_model.save_model("model.json")