import simpleaudio
from pydub import AudioSegment
from pydub.playback import play

class MusicPlayer:
    """
    class for managing music and audio cues
    """
    def __init__(self, bg='audio/cyberpunk.wav') -> None:
        self.background_music = AudioSegment.from_wav(bg)
        self.volume_offset = 4
        self.background_music.play()
        self.playing = True

    def toggle_music(self):
        """
        Stops music if playing;
        plays music if stopped
        """
        if self.playing: self.stop_music()
        else: self.start_music()

    def stop_music(self):
        """
        stops background music playback
        """
        self.background_music.stop()
        self.playing = False

    def start_music(self):
        """
        resumes background music playback
        """
        self.background_music.play()
        self.playing = True