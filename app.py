
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
        description=response['weather'][0]['description']
        icon=response['weather'][0]['icon']

        if current_temperature:
            current_temperature_celsius = round(current_temperature - 273.15, 2)
            weather={
                'temp_cel':current_temperature_celsius,
                'city_name':city_name,
                'description':description,
                'icon':icon


            }
            return render_template("result.html",weather=weather )
           # return f'Current temperature of {city_name.title()} is {current_temperature_celsius} &#8451;'
        else:
            return f'Error getting temperature for {city_name.title()}'





"""@app.route('/city',methods=['POST','GET'])
def search_city():
    if request.method == 'POST':
        API_key = 'b20079dcfeb1f6d220aa1d3733d8692c'  # initialize your key here
        city = request.args.get('q')  # city name passed as argument

        # call API and convert response into Python dictionary
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}'
        response = requests.get(url).json()

        # error like unknown city name, inavalid api key
        if response.get('cod') != 200:
            message = response.get('message', '')
            return f'Error getting temperature for {city.title()}. Error message = {message}'

        # get current temperature and convert it into Celsius
        current_temperature = response.get('main', {}).get('temp')
        if current_temperature:
            current_temperature_celsius = round(current_temperature - 273.15, 2)
            return f'Current temperature of {city.title()} is {current_temperature_celsius} &#8451;'
        else:
            return f'Error getting temperature for {city.title()}'

"""




if __name__ == '__main__':
    app.run(debug=True)
