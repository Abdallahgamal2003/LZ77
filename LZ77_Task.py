from Tags import Tag
tags=[]
sample="XYXXXYYXYXYXYXYXYXYYXZ"
string =""


def compress(sample):
    tags=[]
    look = ""
    temp = ""
    n = 0
    #i =0
    #j=0
    for letter in sample:
        temp += letter
        Location = len(look) - look.rfind(temp)
        if look.rfind(temp) > -1:
            n = Location
        else:
            tags.append(Tag(n, len(temp) - 1, letter))
            n=0
            look += temp
            temp = ""
    return tags



def decompress(tags):
    string=""
    for tag in tags:
        if tag.length==0:
            string+=tag.Next_Char

        elif tag.length>=1:
            i = len(string) - tag.previous
            for x in range(tag.length):
                string+=string[i]
                i+=1
            if tag.Next_Char != "null":
             string += tag.Next_Char
    return string



def fully_compressed (sample):
    temp ="null"
    flag = False
    diff =0
    tags =[]
    i=0
    j=0
    loock=""
    droped=""
    tags=compress(sample)
    string = ""
    string=decompress(tags)
    if len(string) < len(sample):
        diff = len(sample) -len(string)
        j= diff
        if diff ==1:
            droped = sample[len(sample) - 1]
            for x in range(len(sample) - 2):
                loock += sample[i]
                i += 1
            if loock.rfind(droped) == -1:
                tags.append(Tag(0, 0, droped))
            else:
                tags.append(Tag(len(loock) - loock.rfind(droped), 1, "null"))
        elif diff >1:
            for x in range(len(sample) - (diff+1)):
                loock += sample[i]
                i += 1
            for x in range(diff):
                droped+=sample[len(loock)+j-1]
                j-=1
            while flag==False:
                if loock.rfind(droped)>-1:
                    tags.append(Tag(len(loock) - loock.rfind(droped)+1,len(droped),temp))
                    flag=True
                else:
                    temp.pop()
                    temp = droped.pop()


    return tags



tags=fully_compressed(sample)
for tag in tags:
    tag.screen()
string = decompress(tags)
print (string)

