from flask import Flask,render_template,request,abort

import json

import urllib.request
import urllib.parse
import urllib.error
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
def tocelcius(temp):
    try:
        return str(round(float(temp) - 273.15, 2))
    except Exception:
        return "N/A"

@app.route('/',methods=['POST','GET'])
def weather():

    api_key = os.getenv('api') or os.getenv('OPENWEATHER_API_KEY')
    if not api_key:
        return abort(500, "OpenWeather API key not configured (set 'api' or 'OPENWEATHER_API_KEY' in .env)")

    if request.method == 'POST':
        city = request.form.get('city', '').strip()
    else:
        # default city
        city = 'patna'

    if not city:
        return abort(400, "City name required")

 
    qcity = urllib.parse.quote(city)

    # source contain json data from api
    try:
        url = f'http://api.openweathermap.org/data/2.5/weather?q={qcity}&appid={api_key}'
        resp = urllib.request.urlopen(url, timeout=10)
        source = resp.read()
    except urllib.error.HTTPError as e:
       
        return abort(e.code, f"Weather API error: {e.reason}")
    except Exception:
        return abort(502, "Failed to reach weather API")

    # converting json data to dictionary
    try:
        list_of_data = json.loads(source)
    except Exception:
        return abort(502, "Invalid response from weather API")
    try:
        coord = list_of_data['coord']
        sys = list_of_data['sys']
        main = list_of_data['main']
    except KeyError:
        return abort(502, "Unexpected API response structure")

    # data for variable list_of_data
    data = {
        "country_code": str(sys.get('country', '')),
        "coordinate": f"{coord.get('lon', '')} {coord.get('lat', '')}",
        "temp": f"{main.get('temp', '')}k",
        "temp_cel": tocelcius(main.get('temp', 0)) + 'C' if main.get('temp') is not None else "N/A",
        "pressure": str(main.get('pressure', '')),
        "humidity": str(main.get('humidity', '')),
        "cityname": str(city),
    }
    # use template in templates/index.html
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)