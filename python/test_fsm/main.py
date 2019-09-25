import keyboard
import time
import os
import atexit
from transitions import Machine, State

machine = Machine(states=["no_light", "near_light_enabled", "far_light_enabled"], initial="no_light")
machine.add_transition('next_state', 'no_light', 'near_light_enabled')
machine.add_transition('next_state', 'near_light_enabled', 'far_light_enabled')
machine.add_transition('next_state', 'far_light_enabled', 'no_light')

# disabling echoing of user input and enable it when program finished
atexit.register(lambda: os.system("stty echo"))
os.system("stty -echo")

print("Press SPACE to change state")

keyboard.on_release_key(' ', lambda _: machine.next_state())
while True:
    print(machine.state)
    time.sleep(1)
