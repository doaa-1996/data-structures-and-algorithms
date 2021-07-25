from collections import Counter


def firstRepeatedWord(string):

    splittedstring = list(string.split(" "))

    repetition = Counter(splittedstring)

    for i in splittedstring:

        if(repetition[i] > 1):
            return i


s = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York.."
print(firstRepeatedWord(s))
