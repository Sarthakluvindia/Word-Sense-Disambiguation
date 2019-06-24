import nltk

filename = "कुंभ\ContextSenses003.txt"
file = open(filename, "r+", encoding="utf-16")
DisplayTextF = file.read()

word = DisplayTextF.split()
print(word)

hstfilename = "HindiStopWords.txt"
hstfile = open(hstfilename,"r+",encoding="utf-8")
HindiStopWords = hstfile.read()

stopword = HindiStopWords.split()
print(stopword)

newString=[]

for x in word:
    if x not in stopword:
        newString.append(x)
print(newString)


def CountFrequency(my_list):
    # Creating an empty dictionary
    freq = {}
    for item in my_list:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1

    for key, value in freq.items():

        if value>5:
            print(key,value)


CountFrequency(newString)