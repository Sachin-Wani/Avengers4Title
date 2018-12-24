import re
def getWords(text):
    return re.compile('[A-Za-z]+').findall(text)

def lst2set(data: list)->set:
    return set(data)

with open("AVENGERS1.srt","r") as A1:
    AV1=A1.readlines()
    AVE1="".join(AV1)
    AVEN1=getWords(AVE1)
    AVENG1 = [word.lower() for word in AVEN1]
    AVENGE1=lst2set(AVENG1)


with open("AVENGERS2.srt","r") as A2:
    AV2=A2.readlines()
    AVE2="".join(AV2)
    AVEN2=getWords(AVE2)
    AVENG2 = [word.lower() for word in AVEN2]
    AVENGE2=lst2set(AVENG2)

with open("AVENGERS3.srt","r") as A3:
    AV3=A3.readlines()
    AVE3="".join(AV3)
    AVEN3=getWords(AVE3)
    AVENG3 = [word.lower() for word in AVEN2]
    AVENGE3=lst2set(AVENG3)

with open("words_alpha.txt","r") as ENG:
    ALPHA=ENG.read().split("\n")
    ALPHAQ=lst2set(ALPHA)

common = (AVENGE2.intersection(AVENGE3)).difference(ALPHAQ)


bigcommon = [word for word in common if len(word)>6]

print(bigcommon)

