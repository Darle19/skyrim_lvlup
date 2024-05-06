from pynput.mouse import Controller as MouseController, Button as MouseButton
from pynput.keyboard import Controller as KeyboardController
import time
import threading
import keyboard as kb  # Renamed to avoid conflict with pynput

# Initialize controllers
mouse = MouseController()
keyboard = KeyboardController()

# Flag to control the execution
stop_flag = False


def check_for_stop_key():
    global stop_flag
    while True:
        if kb.is_pressed('\''):
            stop_flag = True
            break
        time.sleep(0.1)  # Small delay to prevent high CPU usage


def press_buttons():
    global stop_flag

    while not stop_flag:

        mouse.press(MouseButton.left)
        mouse.press(MouseButton.right)
        time.sleep(2)
        mouse.release(MouseButton.left)
        mouse.release(MouseButton.right)
        time.sleep(1)


# Start the thread to check for the stop key
stop_thread = threading.Thread(target=check_for_stop_key)
stop_thread.start()

print("Press '\\' to start. Press '\\' again to stop.")
kb.wait('\\')  # Wait for the first '\\' press to start

# Start the main function
press_buttons()

# Wait for the stop thread to finish
stop_thread.join()
print("Script stopped.")
