from vocabulary import morse_language


def convert(text: str):
    output = []
    for word in range(len(text)):
        for letter in word:
            new_letter = morse_language[letter]
            output[word].append(new_letter)

    return output


text: str = input("Type here your text: ").lower()
print(convert(text=text))
