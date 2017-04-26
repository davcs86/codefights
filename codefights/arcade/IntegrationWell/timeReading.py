import re
def timedReading(maxLength, text):
    text = re.split("[^A-Za-z]+", text)
    return sum([1 for i in text if len(i)<=maxLength and len(i)>0])


text = "The Fox asked the stork, 'How is the soup?'"
length = 4


print timedReading(length, text)