control.onEvent(EventBusSource.MICROBIT_ID_BUTTON_AB, EventBusValue.MICROBIT_EVT_ANY, function () {
    pins.servoSetPulse(AnalogPin.P0, 1500)
})
function dim_by (factor: number) {
    for (let ind_x = 0; ind_x <= 4; ind_x++) {
        for (let ind_y = 0; ind_y <= 4; ind_y++) {
            led.plotBrightness(ind_x, ind_y, led.pointBrightness(ind_x, ind_y) / factor)
        }
    }
}
control.onEvent(EventBusSource.MICROBIT_ID_BUTTON_B, EventBusValue.MICROBIT_EVT_ANY, function () {
    acc_scale = clip(acc_scale / 1.5, 0.001, 100000)
})
control.onEvent(EventBusSource.MICROBIT_ID_ACCELEROMETER, EventBusValue.MICROBIT_ACCELEROMETER_EVT_DATA_UPDATE, function () {
    circle_y += clip(input.acceleration(Dimension.Y) / acc_scale, -1, 1)
    circle_y = clip(circle_y, 0, 4)
    circle_x += clip(input.acceleration(Dimension.X) / acc_scale, -1, 1)
    circle_x = clip(circle_x, 0, 4)
})
function clip (num: number, min: number, max: number) {
    return Math.min(max, Math.max(min, num))
}
control.onEvent(EventBusSource.MICROBIT_ID_BUTTON_A, EventBusValue.MICROBIT_EVT_ANY, function () {
    acc_scale = clip(acc_scale * 1.5, 0.001, 100000)
})
let acc_scale = 0
let circle_y = 0
let circle_x = 0
let epsilon = 0.01
let delta_y = 0
let delta_x = 0
circle_x = 0
circle_y = 0
acc_scale = 1
input.setAccelerometerRange(AcceleratorRange.OneG)
basic.forever(function () {
    dim_by(1.7)
    led.plotBrightness(circle_x, circle_y, 255)
})
