import xgboost as xgb

def prediction(data):
    model_xgb= xgb.XGBRegressor()
    model = r'C:\Users\Léa\OneDrive\ECV-M2\python\pythonVideoGameSales\videoGamesSalesSite\videoGames\model.json'
    model_xgb.load_model(model)
    return model_xgb.predict(data)
