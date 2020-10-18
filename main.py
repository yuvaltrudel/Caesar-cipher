import eel


@eel.expose
def encrypted(text, key):
    cipher = ""
    for char in text:
        if char == ' ':
            cipher = cipher + char;
        elif char.isupper():
            cipher = cipher + chr((ord(char) + key - 65) % 26 + 65)
        else:
            cipher = cipher + chr((ord(char) + key - 97) % 26 + 97)
    return cipher


@eel.expose
def decrypted(text, key):
    cipher = ""
    for char in text:
        if char == ' ':
            cipher = cipher + char;
        elif char.isupper():
            cipher = cipher + chr((ord(char) - key - 65) % 26 + 65)
        else:
            cipher = cipher + chr((ord(char) - key - 97) % 26 + 97)
    return cipher


eel.init('web')
eel.start('index.html', size=(1300, 570), port=0)  # python will select free ephemeral ports.
