import xgboost as xgb
from sklearn.model_selection import train_test_split

def train_xgboost_model(X, y):
    model = xgb.XGBClassifier()
    model.fit(X, y)
    return model