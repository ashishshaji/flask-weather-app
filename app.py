
from flask import Flask,request, render_template
import requests
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")



@app.route('/city',methods=['POST','GET'])
def search_city():
    if request.method == 'POST':
        city_name = request.form.get('city')
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=b20079dcfeb1f6d220aa1d3733d8692c'
        response = requests.get(url).json()
        current_temperature = response.get('main', {}).get('temp')
        description = response['weather'][0]['description']
        icon = response['weather'][0]['icon']

        if current_temperature:
            current_temperature_celsius = round(current_temperature - 273.15, 2)
            weather={
                'temp_cel':current_temperature_celsius,
                'city_name':city_name,
                'description': description,
                'icon': icon

            }
            return render_template("result.html",weather=weather )
           # return f'Current temperature of {city_name.title()} is {current_temperature_celsius} &#8451;'
        else:
            return f'Error getting temperature for {city_name.title()}'









if __name__ == '__main__':
    app.run(debug=True)
