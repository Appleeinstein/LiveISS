import json
import turtle
import urllib.request
import time
import webbrowser
import geocoder

window = turtle.Screen()
window.setup(1500, 550)  
window.setworldcoordinates(-180, -90, 180, 90)
window.title("ISS Tracker")

boot_turtle = turtle.Turtle()
boot_turtle.hideturtle()
boot_turtle.penup()
boot_turtle.goto(0, 0)
window.bgcolor("black") 

boot_turtle.speed(0)
boot_turtle.pencolor("white")
boot_turtle.width(2)
for i in range(36):  
    boot_turtle.circle(100)
    boot_turtle.left(10)  
    window.update()
    time.sleep(0.05) 
boot_turtle.penup()
boot_turtle.goto(0, 0)
boot_turtle.write("Loading...", font=("Arial", 24, "bold"))
window.update()

try:
    url = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())

    location = result["iss_position"]
    lat = float(location['latitude'])
    lon = float(location['longitude'])

    url = "http://api.open-notify.org/astros.json"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    astronauts = result["people"]

except Exception as e:
    print(f"Error: {e}")

time.sleep(1)

boot_turtle.clear()
window.bgcolor("white")  

window.bgpic("Map.gif")

window.register_shape("ISS GIF2.gif")

iss = turtle.Turtle()
iss.shape("ISS GIF2.gif")
iss.setheading(45)
iss.penup()

iss.goto(lon, lat)

text_turtle = turtle.Turtle()
text_turtle.hideturtle()
text_turtle.penup()

sidebar_turtle = turtle.Turtle()
sidebar_turtle.hideturtle()
sidebar_turtle.penup()
sidebar_turtle.goto(150, 80)  


text_turtle.clear()
text_turtle.goto(-180, 80) 
text_turtle.write(f"ISS Location: Lat {lat:.2f}, Lon {lon:.2f}", font=("Arial", 12, "bold"))

sidebar_turtle.clear()
sidebar_turtle.goto(150, 80)  
sidebar_turtle.pencolor("lime green") 
sidebar_turtle.write("Astronauts on Board:", font=("Arial", 12, "bold"))
sidebar_turtle.pencolor("black") 
y_pos = 60 
for astronaut in astronauts:
    sidebar_turtle.goto(150, y_pos) 
    sidebar_turtle.write(f"• {astronaut['name']}", font=("Arial", 11)) 
    y_pos -= 10  
def update_iss_location():
    try:
        url = "http://api.open-notify.org/iss-now.json"
        response = urllib.request.urlopen(url)
        result = json.loads(response.read())

        location = result["iss_position"]
        lat = float(location['latitude'])
        lon = float(location['longitude'])
        iss.goto(lon, lat)

        text_turtle.clear()
        text_turtle.goto(-180, 80)  # Moved the text slightly to the left
        text_turtle.write(f"ISS Location: Lat {lat:.2f}, Lon {lon:.2f}", font=("Arial", 12, "bold"))

        url = "http://api.open-notify.org/astros.json"
        response = urllib.request.urlopen(url)
        result = json.loads(response.read())
        astronauts = result["people"]

        sidebar_turtle.clear()
        sidebar_turtle.goto(150, 80) 
        sidebar_turtle.pencolor("lime green")  
        sidebar_turtle.write("Astronauts on Board:", font=("Arial", 12, "bold"))
        sidebar_turtle.pencolor("black")  
        y_pos = 60  
        for astronaut in astronauts:
            sidebar_turtle.goto(150, y_pos) 
            sidebar_turtle.write(f"• {astronaut['name']}", font=("Arial", 11))  
            y_pos -= 10  

    except Exception as e:
        print(f"Error: {e}")

    window.ontimer(update_iss_location, 5000)

update_iss_location()
turtle.done()
