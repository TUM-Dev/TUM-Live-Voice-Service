import subprocess


class SubtitleGenerator:
    """Generate Subtitles with a given model.
    """

    def __init__(self, model_path):
        """Initialize SubtitleGenerator with a given model.

        Args:
            model_path (str): The path to a language model provided by vosk.
                Visit https://alphacephei.com/vosk/models for a list of available models.
        """
        self.__model_path = model_path

    def generate(self, input_path: str) -> None:
        """Generate SRT content for input parameter 'input_path'.

        Note:
            Waiting for next vosk-api release to remove subprocess call
            and implement SRT creation in python.

        Args:
             input_path (str): The path of the video file for which subtitles should be generated.
        """
        _ = subprocess.call(['vosk-transcriber',
                             '--model', self.__model_path,
                             '-i', input_path,
                             '-t', 'srt', '-o', 'test.srt'])
