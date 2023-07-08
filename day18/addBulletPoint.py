import pyperclip

text = pyperclip.paste().split("\n")

for index, each in enumerate(text):
    text[index] = "* "+each.strip()

new_text = "\n".join(text)
pyperclip.copy(new_text)
