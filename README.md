# live-weather-tracker
minimal Python CLI weather app using WeatherAPI to track global data. It captures dynamic city inputs to display live conditions, humidity, wind, and air quality in Celsius. Features an integrated Windows PowerShell RoboSpeaker that reads reports aloud. Clean, comment-free backend code optimized for PyCharm with a small footprint.
# CLI Weather Application with RoboSpeaker

A lightweight, minimal Command Line Interface (CLI) weather application built in Python. This app utilizes WeatherAPI to fetch real-time, global weather metrics directly inside your terminal and reads the data out loud using an integrated Windows PowerShell text-to-speech engine.

## Features
* **Live Global Weather:** Fetches instant, accurate meteorological data for any city worldwide.
* **Metric Units:** All temperatures are automatically tracked and displayed in Celsius.
* **Granular Filters:** Choose to see specific details (Temperature, Humidity, Wind Speed) or an all-inclusive report.
* **Integrated RoboSpeaker:** Uses native Windows PowerShell speech synthesis (`System.Speech`) to announce weather summaries audibly without requiring external heavy libraries.
* **Zero Comments:** Clean, production-ready, comment-free structural code optimized for immediate deployment in PyCharm.

## Setup & Requirements
1. Clone or download this repository.
2. Open the project folder inside **PyCharm**.
3. Install the required `requests` library via the PyCharm Terminal:
   ```bash
   pip install requests
