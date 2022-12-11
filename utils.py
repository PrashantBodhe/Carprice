import pickle
import os
import config

model_folder_path = config.MODEL_FOLDER_PATH

if not os.path.exists(model_folder_path):
    os.mkdir(model_folder_path)

def predict_class(Year,Present_Price,Kms_Driven,Seller_Type,Transmission,Owner,Fuel_Diesel,Fuel_Petrol):

    linear_model = pickle.load(open(f'{model_folder_path}/model.pkl','rb'))
    print("linear_model:",linear_model)
    
    prediction = linear_model.predict([[Year,Present_Price,Kms_Driven,Seller_Type,Transmission,Owner,Fuel_Diesel,Fuel_Petrol]])
    print('Predicted Price is:',prediction[0])
    return prediction[0]

# predict_class(2013,4.600,30000,0,0,0,0,1)