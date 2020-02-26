from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont # Font
from reportlab.pdfbase import pdfmetrics # Font
from reportlab.lib.styles import ParagraphStyle


def wrap_text(text, maximal_length):
    letter_counter = 0
    result = []
    curr_sentence = ""

    for i in text.split(" "): # i is every word split by space in text

        if curr_sentence != "":
            curr_sentence += " " # Add spaces between words

        word_letters_counter = 0
        for j in i: # For each letter in word i
            word_letters_counter += 1


            curr_sentence += j # Add letter to sentence on current row
            letter_counter += 1 # Letter counter for line break

            if letter_counter >= maximal_length and len(i) >= 6 and (word_letters_counter >= 4 and (len(i) - word_letters_counter) >= 3) and j not in [".", "-", ","]: # If words have reached the end of row and word is longer than 6 letters
                curr_sentence += "-" # Add hyphen for unfinished word
                result.append(str(curr_sentence)) # Add the whole sentence to the result
                curr_sentence = "" # Reset current sentence
                letter_counter = 0 # Reset letter count


        if letter_counter >= maximal_length: # If we reached end of row
            result.append(str(curr_sentence)) # Add the whole sentence to the result
            curr_sentence = "" # Reset current sentence
            letter_counter = 0 # Reset letter count

    if result[-1] != curr_sentence:
        result.append(str(curr_sentence))
    return result

# Init PDF
pdf = canvas.Canvas('first.pdf')

#Register fonts
pdfmetrics.registerFont(
    TTFont('Ubuntu_B', 'Ubuntu-Bold.ttf'),
)
pdfmetrics.registerFont(
    TTFont('Ubuntu_R', 'Ubuntu-Regular.ttf')
)


# Write title
pdf.setTitle("Kulový blesk")

# DO NOT TOUCH, IT WORKS!!!
from reportlab.lib.units import cm
from reportlab.platypus import Frame, Image
from reportlab.lib import utils

def get_image(path, width=1*cm):
    img = utils.ImageReader(path)
    iw, ih = img.getSize()
    aspect = ih / float(iw)
    return Image(path, width=width, height=(width * aspect))
frame = Frame(1*cm, 1*cm, 19*cm, 10*cm)
story = []
story.append(get_image('kulovy_blesk.png', width=8*cm))
frame.addFromList(story, pdf)
pdf.drawImage('kulovy_blesk.png', 30, 380, width=200, preserveAspectRatio=True)
# END OF DO NOT TOUCH

# Title
pdf.setFont('Ubuntu_B', 32)
pdf.setFillColorRGB(0.85098039215,0.11764705882,0.21176470588)
pdf.drawCentredString(350, 780, "Kulový blesk")

# Author
pdf.setFont('Ubuntu_B', 15)
pdf.setFillColorRGB(0.3294117647,0.3294117647,0.3294117647)
pdf.drawCentredString(295, 755, "Liou Cch'sin")

# Most important info

# Names
pdf.setFont('Ubuntu_B', 15)
pdf.setFillColorRGB(0.85098039215,0.11764705882,0.21176470588)
pdf.drawString(253, 710, "Hlavní téma:")
pdf.setFillColorRGB(0.85098039215,0.11764705882,0.21176470588)
pdf.drawString(253, 675, "Časoprostor:")
pdf.setFillColorRGB(0.85098039215,0.11764705882,0.21176470588)
pdf.drawString(253, 640, "Žánr:")
pdf.setFillColorRGB(0.85098039215,0.11764705882,0.21176470588)
pdf.drawString(253, 605, "Datum dočtení:")
pdf.setFillColorRGB(0.85098039215,0.11764705882,0.21176470588)
pdf.drawString(253, 570, "Literární druh:")
pdf.setFillColorRGB(0.85098039215,0.11764705882,0.21176470588)
pdf.drawString(253, 535, "Hlavní postavy:")
# Values
pdf.setFillColorRGB(0.3294117647,0.3294117647,0.3294117647)
pdf.drawString(385, 710, "Nové fyzikální objevy")
pdf.setFillColorRGB(0.3294117647,0.3294117647,0.3294117647)
pdf.drawString(385, 675, "21. století, Čína")
pdf.setFillColorRGB(0.3294117647,0.3294117647,0.3294117647)
pdf.drawString(385, 640, "Sci-fi")
pdf.setFillColorRGB(0.3294117647,0.3294117647,0.3294117647)
pdf.drawString(385, 605, "14. 2. 2020")
pdf.setFillColorRGB(0.3294117647,0.3294117647,0.3294117647)
pdf.drawString(385, 570, "Epika")
pdf.setFillColorRGB(0.3294117647,0.3294117647,0.3294117647)
pdf.drawString(385, 535, "Čchen, Lin Jun, Ting I")

# Long string
pdf.setFont('Ubuntu_R', 15)
text = pdf.beginText(40, 680)
fillText = 'Když se Řehoř Samsa jednou ráno probudil z nepokojných snů, shledal, že se v posteli proměnil v jakýsi nestvůrný hmyz. Ležel na hřbetě tvrdém jak pancíř, a když trochu nadzvedl hlavu, uviděl své vyklenuté, hnědé břicho rozdělené obloukovitými výztuhami, na jehož vrcholu se sotva ještě držela přikrývka a tak tak že úplně nesklouzla dolů. Jeho četné, vzhledem k ostatnímu objemu žalostně tenké nohy se mu bezmocně komíhaly před očima. Co se to se mnou stalo? pomyslel si. Nebyl to sen. Jeho pokoj, správný, jen trochu příliš malý lidský pokoj, spočíval klidně mezi čtyřmi dobře známými stěnami, Nad stolem, na němž byla rozložena vybalená kolekce vzorků soukenného zboží - Samsa byl obchodní cestující -, visel obrázek, který si nedávno vystřihl z jednoho ilustrovaného časopisu a zasadil do pěkného pozlaceného rámu. Představoval dámu, opatřenou kožešinovou čapkou a kožešinovým boa, jak vzpřímeně sedí a nastavuje divákovi těžký kožešinový rukávník, v němž se jí ztrácí celé předloktí. Řehořův pohled se pak obrátil k oknu a pošmourné počasí - bylo slyšet, jak kapky deště dopadají na okenní plech - ho naplnilo melancholií. '

res = wrap_text(fillText, 60)

for line in res:
    text.textLine(line)

# pdf.drawText(text)


pdf.save()
