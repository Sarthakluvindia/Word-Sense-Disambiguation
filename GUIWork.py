import tkinter as tkinter
import os
import re

def btnclick():
    DisplayTextF = ent.get()
    word = DisplayTextF.split()

    hstfilename = "HindiStopWords.txt"
    hstfile = open(hstfilename, "r+", encoding="utf-8")
    HindiStopWords = hstfile.read()
    stopword = HindiStopWords.split()

    newString = []
    for x in word:
        if x not in stopword:
            newString.append(x)

    path = "C:/Users/ASUS/PycharmProjects/WSD/"
    dirs = os.listdir(path)
    reqWord=""
    # This would print all the files and directories
    for file in dirs:
        for w in newString:
            if w in file:
                reqWord = w
    if(reqWord==""):
        lbl25.config(text="The sentence is not ambiguous!")
    else:
        lbl25.config(text="The sentence is ambiguous because of : "+reqWord)
        wordpath = "C:/Users/ASUS/PycharmProjects/WSD/" + reqWord
        noswordpath = wordpath + "/No_of_Senses.txt"
        nosfile = open(noswordpath, "r+", encoding="utf-8")
        noSenses = nosfile.read()
        for i in range(int(noSenses)):
            meaningpath = wordpath + "/Senses00" + str(i + 1) + ".txt"
            meanfile = open(meaningpath, "r+", encoding="utf-16")
            meaning = meanfile.read()
            listbox.insert("end", meaning)
        for i in range(int(noSenses)):
            checkwordpath = wordpath + "/Meaning00" + str(i + 1) + ".txt"
            checkfile = open(checkwordpath, "r+", encoding="utf-16")
            checkwords = checkfile.read()
            checkstr = checkwords.split()
            for item in checkstr:
                if item in newString:
                    checkpath = checkwordpath
                else:
                    lbl4.config(text = "Sorry! Not able to predict the meaning.")
        digit = re.findall(r'\d+', checkpath)
        digitstr = ''.join(digit)
        finalpath = wordpath + "/Senses" + digitstr + ".txt"
        finalfile = open(finalpath, "r+", encoding="utf-16")
        result = finalfile.read()
        lbl4.config(text="The correct meaning would be: "+result)


# Instantiate a new GUI Window
window = tkinter.Tk()
window.title("Word Sense Disambiguation")
window.geometry("400x400")
window.configure(background = "#ffffff")

#Defines GUI Elements
lbl = tkinter.Label(window, text="Word Sense Disambiguation", fg="#383a39", bg="#ffffff", font=("Helvetica", 23))
lbl2 = tkinter.Label(window, text="Enter a sentence in Hindi")
ent = tkinter.Entry(window)
btn = tkinter.Button(window, text="Check Statement", command=btnclick)
lbl25 = tkinter.Label(window, text="")
lbl3 = tkinter.Label(window, text="The meanings of the word are:")
listbox = tkinter.Listbox(window)
hsb = tkinter.Scrollbar(window, orient="horizontal", command=listbox.xview)
listbox.configure(xscrollcommand=hsb.set)
lbl4 = tkinter.Label(window, text="The correct meaning would be:", wraplength = 400)

#Packs GUI Elements into window
lbl.pack()
lbl2.pack()
ent.pack()
btn.pack()
lbl25.pack()
lbl3.pack()
listbox.pack(side="top",fill="x")
hsb.pack(side="bottom",fill="x")
lbl4.pack()

window.mainloop()