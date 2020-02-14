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
pdfmetrics.registerFont(
    TTFont('Anonymous_R', 'AnonymousPro-Regular.ttf')
)


# Write title
pdf.setFont('Ubuntu_B', 36)
pdf.setTitle("Test")

# Heading
pdf.drawCentredString(295, 780, "Heading")

# Subheading
pdf.setFont('Ubuntu_R', 15)
pdf.drawCentredString(295, 750, "Subtitles are long")

# Draw line
pdf.line(30, 710, 550, 710)

# Long string
pdf.setFont('Ubuntu_R', 15)
text = pdf.beginText(40, 680)
fillText = 'Když se Řehoř Samsa jednou ráno probudil z nepokojných snů, shledal, že se v posteli proměnil v jakýsi nestvůrný hmyz. Ležel na hřbetě tvrdém jak pancíř, a když trochu nadzvedl hlavu, uviděl své vyklenuté, hnědé břicho rozdělené obloukovitými výztuhami, na jehož vrcholu se sotva ještě držela přikrývka a tak tak že úplně nesklouzla dolů. Jeho četné, vzhledem k ostatnímu objemu žalostně tenké nohy se mu bezmocně komíhaly před očima. Co se to se mnou stalo? pomyslel si. Nebyl to sen. Jeho pokoj, správný, jen trochu příliš malý lidský pokoj, spočíval klidně mezi čtyřmi dobře známými stěnami, Nad stolem, na němž byla rozložena vybalená kolekce vzorků soukenného zboží - Samsa byl obchodní cestující -, visel obrázek, který si nedávno vystřihl z jednoho ilustrovaného časopisu a zasadil do pěkného pozlaceného rámu. Představoval dámu, opatřenou kožešinovou čapkou a kožešinovým boa, jak vzpřímeně sedí a nastavuje divákovi těžký kožešinový rukávník, v němž se jí ztrácí celé předloktí. Řehořův pohled se pak obrátil k oknu a pošmourné počasí - bylo slyšet, jak kapky deště dopadají na okenní plech - ho naplnilo melancholií. '

res = wrap_text(fillText, 60)

for line in res:
    text.textLine(line)

pdf.drawText(text)


pdf.save()
