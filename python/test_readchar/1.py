import readchar

for i in range(10):
    key = readchar.readkey()
    if key == readchar.key.UP:
        print("UP")
    if key == readchar.key.DOWN:
        print("DOWN")
    if key == readchar.key.LEFT:
        print("LEFT")
    if key == readchar.key.RIGHT:
        print("RIGHT")

