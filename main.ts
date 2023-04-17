let degrees = 0
let difference = 0
let goal = 0
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    if (difference < 15) {
        basic.showString("Winner")
    } else {
        basic.showString("Try Again")
        goal = randint(0, 360)
    }
    
})
input.calibrateCompass()
let img = images.createImage(`
    . # . # .
    . . . . .
    . . . . .
    # . . . #
    . # # # .
`)
img.showImage(0)
goal = randint(0, 360)
basic.forever(function on_forever() {
    
    degrees = input.compassHeading()
    difference = Math.abs(goal - degrees)
    if (difference > 180) {
        difference = Math.abs(360 - difference)
    }
    
    pins.digitalWritePin(DigitalPin.P0, 1)
    basic.pause(difference * 5)
    pins.digitalWritePin(DigitalPin.P0, 0)
    basic.pause(difference * 5)
})
