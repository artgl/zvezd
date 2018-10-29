from flask import Flask
from flask import render_template
import time
from ev3dev2.button import Button
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
app = Flask(__name__)

tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)


@app.route("/up")
def up():
    tank_drive.on_for_rotations(SpeedPercent(75), SpeedPercent(75), 10)
    print("UP")
    return "UP"
@app.route("/down")
def down():
    tank_drive.on_for_rotations(-SpeedPercent(75), -SpeedPercent(75), 10)
    print("DOWN")
    return "DOWN"
@app.route("/left")
def left():
    tank_drive.on_for_rotations(-SpeedPercent(75), SpeedPercent(75), 10)
    print("LEFT")
    return "LEFT"
@app.route("/right")
def right():
    tank_drive.on_for_rotations(SpeedPercent(75), -SpeedPercent(75), 10)
    print("RIGHT")
    return "RIGHT"

@app.route("/center")
def center():

    print("CENTER")
    return "CENTER"

@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(port=8888)