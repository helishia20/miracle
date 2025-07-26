import requests
import tkinter as tk


def get_weather():
    city = entry.get()
    api_key = "cfd013ff6fa3ead40edf7e8a8127907a"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()
    try:
        if 'main' in data:
            label_Result.config(text=f"CURRENTLY WEATHER IN {city}:\{data['main']['temp']} °C")   
    except ValueError:
        label_Result.config(text=f"the responses for {city} have problems:{data}")


app = tk.Tk()
app.title("current weather")
label = tk.Label(app, text="which city?")
label.pack(padx=10, pady=5)
entry = tk.Entry(app, width=30)
entry.pack(padx=10, pady=5)
button = tk.Button(app, text="get current weather", command=get_weather)
button.pack(padx=10, pady=10)
label_Result = tk.Label(app, text="weather: ")
label_Result.pack(padx=10, pady=40)


app.mainloop()
