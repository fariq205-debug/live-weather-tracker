import os
import requests


def speak(text):
    clean_text = text.replace('"', '').replace("'", "")
    command = f'PowerShell -Command "Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{clean_text}\')"'
    os.system(command)


def get_weather(city_name, aspect):
    api_key = "860e3f2c929145d99b9105724260207"
    base_url = "https://api.weatherapi.com/v1/current.json"

    params = {
        "key": api_key,
        "q": city_name,
        "aqi": "yes"
    }

    try:
        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            data = response.json()

            city = data["location"]["name"]
            country = data["location"]["country"]
            weather_desc = data["current"]["condition"]["text"]

            print("\n" + "=" * 35)
            print(f" Weather Report: {city}, {country} ")
            print("=" * 35)
            print(f"Condition:    {weather_desc}")

            speech_text = f"The weather in {city} is currently {weather_desc}."

            aspect = aspect.lower()
            if aspect in ["temperature", "temp", "1"]:
                temp = data['current']['temp_c']
                print(f"Temperature:  {temp}°C")
                print(f"Feels Like:   {data['current']['feelslike_c']}°C")
                speech_text += f" The temperature is {temp} degrees Celsius."

            elif aspect in ["humidity", "humid", "2"]:
                humidity = data['current']['humidity']
                print(f"Humidity:     {humidity}%")
                speech_text += f" The humidity level is {humidity} percent."

            elif aspect in ["wind", "wind speed", "3"]:
                wind = data['current']['wind_kph']
                print(f"Wind Speed:   {wind} kph")
                speech_text += f" The wind speed is {wind} kilometers per hour."

            elif aspect in ["all", "4"]:
                temp = data['current']['temp_c']
                humidity = data['current']['humidity']
                wind = data['current']['wind_kph']

                print(f"Temperature:  {temp}°C")
                print(f"Feels Like:   {data['current']['feelslike_c']}°C")
                print(f"Humidity:     {humidity}%")
                print(f"Wind Speed:   {wind} kph")
                print(f"Air Quality (PM2.5): {data['current']['air_quality']['pm2_5']:.2f}")

                speech_text += f" The temperature is {temp} degrees Celsius, humidity is {humidity} percent, and wind speed is {wind} kilometers per hour."
            else:
                print(f"\n[Note] '{aspect}' not recognized. Showing basic condition only.")

            print("=" * 35 + "\n")
            speak(speech_text)

        elif response.status_code == 400:
            print(f"\n[Error] Location error or invalid key matching API query.\n")
        elif response.status_code == 401:
            print(f"\n[Error] Key provided is invalid.\n")
        else:
            print(f"\n[Error] Failed to get data. Status Code: {response.status_code}\n")

    except requests.exceptions.ConnectionError:
        print("\n[Network Error] Could not connect to the internet.\n")


def main():
    print("--- CLI Weather Application with RoboSpeaker ---")
    while True:
        city = input("Enter city name (or type 'exit' to quit): ").strip()
        if city.lower() == 'exit':
            print("Goodbye!")
            speak("Goodbye")
            break
        if city == "":
            print("Please enter a valid city name.")
            continue

        print("\nWhat weather details do you want to see?")
        print("1. Temperature\n2. Humidity\n3. Wind Speed\n4. All (with Air Quality)")
        aspect = input("Enter selection (Name or Number): ").strip()

        if aspect == "":
            print("Please enter a valid detail option.")
            continue

        get_weather(city, aspect)


if __name__ == "__main__":
    main()