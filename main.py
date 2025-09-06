def on_microbit_id_button_ab_evt():
    pins.servo_set_pulse(AnalogPin.P0, 1500)
control.on_event(EventBusSource.MICROBIT_ID_BUTTON_AB,
    EventBusValue.MICROBIT_EVT_ANY,
    on_microbit_id_button_ab_evt)

def dim_by(factor: number):
    for ind_x in range(5):
        for ind_y in range(5):
            led.plot_brightness(ind_x, ind_y, led.point_brightness(ind_x, ind_y) / factor)

def on_microbit_id_button_b_evt():
    global acc_scale
    acc_scale = clip(acc_scale / 1.5, 0.001, 100000)
control.on_event(EventBusSource.MICROBIT_ID_BUTTON_B,
    EventBusValue.MICROBIT_EVT_ANY,
    on_microbit_id_button_b_evt)

def on_microbit_id_accelerometer_evt_data_update():
    global circle_y, circle_x
    circle_y += clip(input.acceleration(Dimension.Y) / acc_scale, -1, 1)
    circle_y = clip(circle_y, 0, 4)
    circle_x += clip(input.acceleration(Dimension.X) / acc_scale, -1, 1)
    circle_x = clip(circle_x, 0, 4)
control.on_event(EventBusSource.MICROBIT_ID_ACCELEROMETER,
    EventBusValue.MICROBIT_ACCELEROMETER_EVT_DATA_UPDATE,
    on_microbit_id_accelerometer_evt_data_update)

def clip(num: number, min2: number, max2: number):
    return min(max2, max(min2, num))

def on_microbit_id_button_a_evt():
    global acc_scale
    acc_scale = clip(acc_scale * 1.5, 0.001, 100000)
control.on_event(EventBusSource.MICROBIT_ID_BUTTON_A,
    EventBusValue.MICROBIT_EVT_ANY,
    on_microbit_id_button_a_evt)

acc_scale = 0
circle_y = 0
circle_x = 0
epsilon = 0.01
delta_y = 0
delta_x = 0
circle_x = 0
circle_y = 0
acc_scale = 1
input.set_accelerometer_range(AcceleratorRange.ONE_G)

def on_forever():
    dim_by(1.7)
    led.plot_brightness(circle_x, circle_y, 255)
basic.forever(on_forever)
