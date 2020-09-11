"""
app.py

============================================================
A Simple Gui Weather Application using Open Weather Map API

This application uses an open API to tell a user the weather
"""

import tkinter as tk
import requests

height = 700
width = 700


def get_weather(city):
    """
    Requests the weather forecast from any city using the Open Weather Map Api

        :param city: user input for the city
        :param type: str
    """
    weather_key = '43f3a0e27f380e22a6533486e2a5e691'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'metric'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = format_response(weather)


def format_response(weather):
    """
    Using Python String Formatting to display the results in the application

        :param weather: json object from API request
        :param type: str

        :return: str
    """
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']

        final_str = 'City: %s \nConditions: %s \nTemperature (°C): %s' % (name, desc, temp)
    except:
        final_str = 'Error! Retry!'
    return final_str


""" 
Application structuring for tkinter, using frames to display the output and entry boxes for user input

"""

if __name__ == "__main__":
    root = tk.Tk()

    # Canvas, place sub elements on the canvas, buttons, frames, entries
    canvas = tk.Canvas(root, height=height, width=width, bg='grey')
    canvas.pack()

    # adding background image. file must be .png
    background_image = tk.PhotoImage(file='/Users/hakeem/PycharmProjects/Weather/media/background.png')
    background_label = tk.Label(root, image=background_image)
    background_label.place(relwidth=1, relheight=1)

    # Adding a frame to place elements
    frame = tk.Frame(root, bg='black', bd=5)
    frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

    # Place an entry box
    entry = tk.Entry(frame, bg='white', font=40)
    entry.place(relwidth=0.65, relheight=1)

    # adding a button to the frame
    button = tk.Button(frame, text="Get Weather", fg='black', bg='black', font='40',
                       command=lambda: get_weather(entry.get()))

    button.place(relx=0.7, relwidth=0.3, relheight=1)

    lowerFrame = tk.Frame(root, bg='black', bd=10)
    lowerFrame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

    # Place a label ina  frame title text etc
    label = tk.Label(lowerFrame, font=('Helvetica', 20))
    label.place(relwidth=1, relheight=1)

    root.mainloop()
