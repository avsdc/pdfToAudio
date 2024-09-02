
import pyttsx3
import PyPDF2
import io
import requests
from pypdf import PdfReader
from flask import Flask


app = Flask(__name__)
app.config['SECRET_KEY'] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"

#speaker = pyttsx3.init()
#speaker.say('')
#speaker.runAndWait()
speaker = pyttsx3.init()
speaker.setProperty("rate", 180)


#Part 1
#Reading a page from a page(text based, fiction)
book = open('OliverTwist.pdf', 'rb')
reader = PyPDF2.PdfReader(book)
page = reader.pages[0]

text = page.extract_text()

speaker = pyttsx3.init()
speaker.say(text)
speaker.runAndWait()

#Part2
#Reading a page from a page(text-based, fiction) with open
with open('OliverTwist.pdf', 'rb') as book:
    reader = PyPDF2.PdfReader(book)
    page = reader.pages[0]

    text = page.extract_text()

speaker = pyttsx3.init()
speaker.say(text)
speaker.runAndWait()


#Part3
#Reading a page from a page(text based, non-fiction)
book = open('SOPHE_2023.pdf', 'rb')
reader = PyPDF2.PdfReader(book)
page = reader.pages[2]

text = page.extract_text()

speaker.save_to_file(text, "myaudio.mp3")
speaker.say(text)
speaker.runAndWait()


#Part4
#Reading all pages from the articel(text, image amd non-fiction)
full_text = " "

book = open('SOPHE_2023.pdf', 'rb')
reader = PyPDF2.PdfReader(book)
pages = len(reader.pages)

for num in range(pages):
    page = reader.pages[num]
    text = page.extract_text()
    full_text += text


#speaker.save_to_file(text, "myaudio.mp3")
speaker.say(full_text)
speaker.runAndWait()

#Part5
# Download content and read text and translate math
url = "https://arxiv.org/pdf/2101.05907.pdf"
r = requests.get(url)
f = io.BytesIO(r.content)

# Extract text
reader = PdfReader(f)
print(reader.pages[0].extract_text())


if __name__ == '__main__':
    app.run(debug=True)