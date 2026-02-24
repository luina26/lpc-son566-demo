# lpc_son566_demo.py

class LPCSon566:
    def __init__(self):
        self.recording = False

    def start_recording(self):
        self.recording = True
        print("Recording started...")

    def stop_recording(self):
        self.recording = False
        print("Recording stopped.")

    def playback(self):
        if self.recording:
            print("Can't play back while recording.")
        else:
            print("Playing back the recorded audio...")


def main():
    lpc_son566 = LPCSon566()

    while True:
        command = input("Enter command (start/stop/play/exit): ").strip().lower()
        if command == "start":
            lpc_son566.start_recording()
        elif command == "stop":
            lpc_son566.stop_recording()
        elif command == "play":
            lpc_son566.playback()
        elif command == "exit":
            print("Exiting the demo.")
            break
        else:
            print("Unknown command. Please enter 'start', 'stop', 'play', or 'exit'.")


if __name__ == "__main__":
    main()