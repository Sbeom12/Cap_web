from django.shortcuts import render
from tensorflow.keras.models import load_model
# from sklearn.preprocessing import StandardScaler
import numpy as np
import h5py

def index(request):
    # if POST
    if request.method == "POST":
        form = request.POST
        
        # 전류, 전압 받아서
        current = abs(float(form["current"]))
        voltage = abs(float(form["voltage"]))
        x = [[current, voltage]]
        
        # model 불러오기
        with h5py.File('cnn_3_layer.h5', 'r', libver='latest', swmr=True) as f:
            model = load_model(f, compile=False)
        #model = load_model('cnn_3_layer.h5', encoding='utf-8')
        
        # 결과 출력
        result = model.predict(x)
        result = round(result[0][0]*100, 2)
        if result <= 0:
            result = 0
        elif result >= 100:
            result = 100

        # 내보내기
        return render(request, "web/input.html", {"result":result})
    # if GET
    else:
        return render(request, "web/input.html")
        