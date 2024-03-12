from vocabulary import morse_language
from pydub import AudioSegment
from pydub.playback import play


def convert(text: str):
    output: list = []
    for word in text:
        for letter in word:
            new_letter = morse_language[letter]
            output.append(new_letter)

    return output


def reproduce(output):
    dot = AudioSegment.from_wav("sounds/dot.wav")
    dash = AudioSegment.from_wav("sounds/dash1.wav")
    for word in output:
        for simbol in word:
            if simbol == ".":
                play(dot)
            elif simbol == "-":
                play(dash)


text: str = input("Type here your text: ").lower()
output = convert(text=text)
print("".join(output))
reproduce(output=output)
