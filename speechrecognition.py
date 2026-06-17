from transformers import pipeline
import librosa#Librosa is not a model. It is a Python library used for audio and music analysis.

audio, sr = librosa.load(
    r"C:\Users\user\Downloads\Applied Ai\PYTHON-COMPLETE-TUTORIAL\jackhammer.wav",
    sr=16000
)

asr = pipeline(
    "automatic-speech-recognition",
    model="openai/whisper-base"
)

result = asr(audio)

print("Transcription:")
print(result["text"])