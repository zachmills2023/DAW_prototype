import pyaudio
import numpy as np

def init_pyaudio():
    """Initialize PyAudio and return the instance."""
    return pyaudio.PyAudio()

def open_stream(p, format, channels, rate, frames_per_buffer):
    """Open an audio stream with the given parameters."""
    return p.open(format=format,
                  channels=channels,
                  rate=rate,
                  input=True,
                  frames_per_buffer=frames_per_buffer)

def read_stream(stream, frames_per_buffer):
    """Read data from the audio stream and convert it to a NumPy array."""
    data = stream.read(frames_per_buffer, exception_on_overflow=False)
    audio_data = np.frombuffer(data, dtype=np.int16)
    return audio_data

def process_audio_data(audio_data):
    """Process the audio data (e.g., pitch detection)."""
    # Placeholder for processing logic
    print(audio_data)

def close_stream(stream):
    """Stop and close the audio stream."""
    stream.stop_stream()
    stream.close()

def terminate_pyaudio(p):
    """Terminate the PyAudio session."""
    p.terminate()

def main():
    # Initialize PyAudio
    p = init_pyaudio()

    # Define audio stream parameters
    FORMAT = pyaudio.paInt16     # Audio format (16-bit PCM)
    CHANNELS = 1                 # Number of audio channels
    RATE = 44100                 # Sampling rate (44.1 kHz)
    FRAMES_PER_BUFFER = 1024     # Number of frames per buffer

    control = 0
    while control == 0:
        usr_input = int(input("Would you like to:\
            1.) Start an audio stream\
            2.) Read pitch from sample\n>"))

        if usr_input == 1:
            # Open audio stream
            stream = open_stream(p, FORMAT, CHANNELS, RATE, FRAMES_PER_BUFFER)
            control = 1
        elif usr_input == 2:
            print("Feature coming soon")
            control = 1
        else:
            print("Sorry you need to enter either 1 or 2 for your options.")
            control = 0

    print("Recording...")

    try:
        while True:
            # Read and process audio data
            audio_data = read_stream(stream, FRAMES_PER_BUFFER)
            process_audio_data(audio_data)
    except KeyboardInterrupt:
        print("Recording stopped")
    finally:
        # Clean up the resources
        close_stream(stream)
        terminate_pyaudio(p)

if __name__ == "__main__":
    main()
