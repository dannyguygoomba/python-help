from elevenlabs.client import ElevenLabs
from elevenlabs import play, stream, save
import time
import os
os.environ['PATH'] += os.pathsep + 'C:\Program Files\mpv'


client = ElevenLabs(
  api_key="" # Defaults to ELEVEN_API_KEY
)

class ElevenLabsManager:

    def __init__(self):
        # CALLING voices() IS NECESSARY TO INSTANTIATE 11LABS FOR SOME FUCKING REASON
        all_voices = client.voices.get_all()
        print(f"\nAll ElevenLabs voices: \n{all_voices}\n")

    # Convert text to speech, then save it to file. Returns the file path
    def text_to_audio(self, input_text, voice="GamerGirl", save_as_wave=True, subdirectory=""):
        audio_saved = client.generate(
          text=input_text,
          voice=voice,
          model="eleven_monolingual_v1"
        )
        if save_as_wave:
          file_name = f"___Msg{str(hash(input_text))}.wav"
        else:
          file_name = f"___Msg{str(hash(input_text))}.mp3"
        tts_file = os.path.join(os.path.abspath(os.curdir), subdirectory, file_name)
        save(audio_saved,tts_file)
        return tts_file

    # Convert text to speech, then play it out loud
    def text_to_audio_played(self, input_text, voice="Gamergirl"):
        audio = client.generate(
          text=input_text,
          voice=voice,
          model="eleven_monolingual_v1"
        )
        play(audio)

    # Convert text to speech, then stream it out loud (don't need to wait for full speech to finish)
    def text_to_audio_streamed(self, input_text, voice="Gamergirl"):
        audio_stream = client.generate(
          text=input_text,
          voice=voice,
          model="eleven_monolingual_v1",
          stream=True
        )
        stream(audio_stream)


if __name__ == '__main__':
    elevenlabs_manager = ElevenLabsManager()

    # elevenlabs_manager.text_to_audio_streamed("This is my streamed test audio, I'm so much cooler than played", "gamergirl2")
    elevenlabs_manager.text_to_audio_streamed("This is my streamed test audio, I'm so much cooler than played", "21m00Tcm4TlvDq8ikWAM")
    time.sleep(2)
    # elevenlabs_manager.text_to_audio_played("This is my played test audio, helo hello", "gamergirl2")
    elevenlabs_manager.text_to_audio_played("This is my played test audio, helo hello", "21m00Tcm4TlvDq8ikWAM")
    time.sleep(2)
    # file_path = elevenlabs_manager.text_to_audio("This is my saved test audio, please make me beautiful", "gamergirl2")
    file_path = elevenlabs_manager.text_to_audio("This is my saved test audio, please make me beautiful", "21m00Tcm4TlvDq8ikWAM")
    print("Finished with all tests")

    time.sleep(30)