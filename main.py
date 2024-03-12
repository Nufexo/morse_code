from vocabulary import morse_language


def convert(text: str):
    output = []
    for word in text:
        for letter in word:
            new_letter = morse_language[letter]
            output.append(new_letter)

    return output


text: str = input("Type here your text: ").lower()
output = convert(text=text)
print("".join(output))
