🌤️ Weather App (Flask + OpenWeather API)
--
A simple Flask web application that fetches real-time weather data for any city using the OpenWeather API.
It displays temperature (Kelvin & Celsius), humidity, pressure, country code, and coordinates.

🚀 Features

Search weather by city name

Displays:

Temperature (Kelvin + Celsius)

Humidity

Pressure

Country code

Longitude & Latitude

Uses OpenWeather API

.env support for API key

Error-handled and secure

Built with Python + Flask
--
📂 Project Structure
.
├── weather.py          # Main Flask app
├── templates/
│   └── index.html      # HTML template (you create)
└── README.md

--
2️⃣ Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
--
3️⃣ Install dependencies
pip install flask python-dotenv
--
4️⃣ Add your OpenWeather API key

Create a .env file in the project root:

api=YOUR_OPENWEATHER_API_KEY


or:

OPENWEATHER_API_KEY=YOUR_OPENWEATHER_API_KEY
--
▶️ Run the Application
python weather.py


Then open your browser and go to:

http://127.0.0.1:5000/
--
📝 Environment Variables
Variable	Description
api or OPENWEATHER_API_KEY	Your OpenWeather API key

The app will throw an error if the key is missing.
---
⚙️ How It Works

The app listens on /

If the user submits a city name, it queries the OpenWeather API

Default city: Patna

Responses are parsed and converted (Kelvin → Celsius)

Data is passed to the HTML template for display

Weather fetching logic is implemented in weather.py using urllib.request and JSON parsing 

weather

--
🔐 Error Handling

The app gracefully handles:

Missing API key

Invalid city name

API unreachable

Malformed API response

Missing fields in the JSON


