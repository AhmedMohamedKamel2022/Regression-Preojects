import joblib
import warnings
warnings.simplefilter(action='ignore')

def preprocess_weather(x) :
    if x  == 'Mist' : 

        return [1, 0, 0]
    
    elif x == 'Rainy' :

        return [0, 1, 0]
        
    elif x == 'Snowy' :
        return [0, 0, 1]
    
    else :
        return [0,0,0]


def weakday_name(x) :
    if x == 'Monday' :
        return [1,0,0,0,0,0]
    
    elif x == 'Saturday' :
        return [0,1,0,0,0,0]
    
    elif x == 'Sunday' :
        return [0,0,1,0,0,0]
    
    elif x == 'Thursday' :
        return [0,0,0,1,0,0]
    
    elif x == 'Tuesday' :
        return [0,0,0,0,1,0]
    
    elif x == 'Wednesday' :
        return [0,0,0,0,0,1]
    
    else :
        return [0,0,0,0,0,0]


def month_name(x):
    if x == 'August':
        return [1,0,0,0,0,0,0,0,0,0,0]
    elif x == 'December':
        return [0,1,0,0,0,0,0,0,0,0,0]
    elif x == 'February':
        return [0,0,1,0,0,0,0,0,0,0,0]
    elif x == 'January':
        return [0,0,0,1,0,0,0,0,0,0,0]
    elif x == 'July':
        return [0,0,0,0,1,0,0,0,0,0,0]
    elif x == 'June':
        return [0,0,0,0,0,1,0,0,0,0,0]
    elif x == 'March':
        return [0,0,0,0,0,0,1,0,0,0,0]
    elif x == 'May':
        return [0,0,0,0,0,0,0,1,0,0,0]
    elif x == 'November':
        return [0,0,0,0,0,0,0,0,1,0,0]
    elif x == 'October':
        return [0,0,0,0,0,0,0,0,0,1,0]
    elif x == 'September':
        return [0,0,0,0,0,0,0,0,0,0,1]
    else:
        return [0,0,0,0,0,0,0,0,0,0,0]



def User(data) :
    temp = data['temp']
    
    humidity = data['humidity']
    
    hour = data['hour']
        
    month = month_name(data['month'])
    
    day = weakday_name(data['day'])


    weather = preprocess_weather(data['weather'])
    
        
    final_data = [temp, humidity, hour] + weather + day + month    
    
    return final_data


# data = {'temp':20, 'humidity':0.34, 'hour':2, 'month':'April', 'day':'Monday', 'weather':'Clear'}
# Final_Data  = User(data)
# print((Final_Data))
# print()
# print(len(Final_Data))

# model = joblib.load('Models/model.h5')
# scaler = joblib.load('Models/scaler.h5')
# Final_Data = scaler.transform([Final_Data])

# print()
# print(Final_Data)
# predict = model.predict(Final_Data)[0]
# print(predict)
              