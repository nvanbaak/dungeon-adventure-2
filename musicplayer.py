import simpleaudio as sa
# from pydub import AudioSegment
# from pydub.playback import play

class MusicPlayer:
    """
    class for managing music and audio cues
    """
    def __init__(self, bg='audio/cyberpunk.wav') -> None:
        self.bg_track = sa.WaveObject.from_wave_file(bg)
        self.background_music = self.bg_track.play()

    def toggle_music(self):
        """
        Stops music if playing;
        plays music if stopped
        """
        if self.background_music.is_playing(): self.stop_music()
        else: self.start_music()

    def stop_music(self):
        """
        stops background music playback
        """
        self.background_music.stop()

    def start_music(self):
        """
        resumes background music playback
        """
        self.background_music = self.bg_track.play()
