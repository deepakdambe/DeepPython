
import pyttsx3
from pypdf import PdfReader

def getPageTxtFromPDF(pageNum):
    # creating a pdf reader object
    reader = PdfReader('D:\\Chrome_Downloads\\the_design_of_the_unix_operating_system.pdf')

    # printing number of pages in pdf file
    print(len(reader.pages))

    # creating a page object
    page = reader.pages[pageNum]

    # extracting text from page
    txt = page.extract_text()

    return txt


def getTxtFromTextFile():
    f = open("TxtFileToRead.txt", "r")
    txt = f.read()
    return txt


speaker = pyttsx3.init()
speaker.setProperty('rate', 122)

txt = getTxtFromTextFile()

speaker.say(txt)
speaker.runAndWait()
