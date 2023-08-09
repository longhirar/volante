import vgamepad as vg
from tkinter import *
import serial

#config
sensitivity = 100

#end-config

arduino = serial.Serial(input("Arduino Serial Port: "), 115200 , timeout=1)

gamepad = vg.VX360Gamepad()

callback_id=0
def gamepadCallback(client, target, large_motor, small_motor, led_number, user_data):
    global callback_id
    callback_id+=1
    print(f":[GamepadCallback {callback_id}]")
    print(f"[{callback_id}] client: {client}\n[{callback_id}] target: {target}\n[{callback_id}] large_motor: {large_motor}\n[{callback_id}] small_motor: {small_motor}\n[{callback_id}] led_number: {led_number}\n[{callback_id}] user_data: {user_data}")
    pass

gamepad.register_notification(callback_function=gamepadCallback)

buttons = {
    "A": vg.XUSB_BUTTON.XUSB_GAMEPAD_A,
    "B": vg.XUSB_BUTTON.XUSB_GAMEPAD_B,
    "X": vg.XUSB_BUTTON.XUSB_GAMEPAD_X,
    "Y": vg.XUSB_BUTTON.XUSB_GAMEPAD_Y
}

def getValues():
    global sensitivity
    recv = arduino.readline().decode()
    if recv[0] == "c": # Command
        cmd = recv[1:]
        if cmd == "S+":
            sensitivity+=10
        elif cmd == "S-":
            sensitivity-=10
        print(f"[ArduinoCommand {cmd}]")
    elif recv[0] == "d": # buttonDown
        print(f"[ButtonDown {recv[1:].strip()}]")
        try:
            buttonid = buttons.get(recv[1:].strip())
            gamepad.press_button(buttonid)
        except IndexError:
            pass
    elif recv[0] == "u": # buttonUp
        print(f"[ButtonUp {recv[1:].strip()}]")
        try:
            buttonid = buttons.get(recv[1:].strip())
            gamepad.release_button(buttonid)
        except IndexError:
            pass
    else:
        steer = 0
        try:
            steer = int(recv)
        except ValueError:
            print(f"[ValueError] Invalid String: {recv.strip()}") 
        #gamepad.left_joystick_float(steer/sensitivity, 0)
        gamepad.right_joystick_float(steer/sensitivity, 0)

def updateGamepad():
    gamepad.update()

running = True
while running:
    try:
        getValues()
        updateGamepad()

    except KeyboardInterrupt:
        print(f"![KeyboardInterrupt]")
        running = False
    except serial.SerialException:
        print(f"![SerialException]")
        running = False
    except Exception as e:
        print(f":[{type(e)}]")

