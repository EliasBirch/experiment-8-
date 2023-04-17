degrees = 0 
difference = 0
goal = 0 

def on_button_pressed_a():
    global goal 
    if difference < 15:
        basic.show_string("Winner")
    else: 
        basic.show_string("Try Again")
        goal = randint(0, 360)
input.on_button_pressed(Button.A, on_button_pressed_a)

input.calibrate_compass()
img = images.create_image("""
    . # . # .
    . . . . .
    . . . . .
    # . . . #
    . # # # .
""")
img.show_image(0)
goal = randint(0, 360)

def on_forever():
    global degrees, difference
    degrees = input.compass_heading()
    difference = abs(goal - degrees)
    if difference > 180:
        difference = abs(360 - difference)
    pins.digital_write_pin(DigitalPin.P0, 1)
    basic.pause(difference * 5)
    pins.digital_write_pin(DigitalPin.P0, 0)
    basic.pause(difference * 5)
basic.forever(on_forever)





