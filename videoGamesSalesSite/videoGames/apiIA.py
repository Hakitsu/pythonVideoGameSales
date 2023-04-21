import xgboost as xgb
import json

def prediction(data):
    with open(r'C:\Users\Léa\OneDrive\ECV-M2\python\pythonVideoGameSales\videoGamesSalesSite\videoGames\model.json') as mon_fichier:
        model_xgb= xgb.XGBRegressor()
        model = json.load(mon_fichier)
        model_xgb.load_model(model)
        return model_xgb.predict(data)
        
