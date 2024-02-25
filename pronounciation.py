from gtts import gTTS
import os

def generate_pronunciation_audio(word):
    # Generate pronunciation text using Google Text-to-Speech (gTTS)
    tts = gTTS(text=word, lang='en', slow=False)
    
    # Save the pronunciation audio as a temporary file
    audio_file = "pronunciation.mp3"
    tts.save(audio_file)
    
    return audio_file

def main():
    word = input("Enter a word to generate its pronunciation: ")
    audio_file = generate_pronunciation_audio(word)
    
    # Play the generated audio
    os.system("start " + audio_file)  # for Windows
    # For Linux/Mac, you can use:
    # os.system("mpg321 " + audio_file)
    
    # Optionally, you can delete the temporary audio file after playing
    # os.remove(audio_file)

if __name__ == "__main__":
    main()
