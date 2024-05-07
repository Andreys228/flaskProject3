from flask import Flask, render_template, request
import requests

app = Flask(__name__)
def makelink():
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

def get_weather(city, api_key):
    response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}')
    weather_data = response.json()


    return weather_data
get_weather("Moscow", "9108dea7ba0db115b547dc98d6e84f25")
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        weather = get_weather(city)
        return render_template('index.html', weather=weather, city=city)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    print(get_weather("Moscow", "9108dea7ba0db115b547dc98d6e84f25"))