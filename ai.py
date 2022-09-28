import random 

inputs = [] # todo: id
words = []
outputs = []
topics = []
pre_words = []
pro_words = []

while True:
    msg = input('You: ')
    inputs.append(msg)
    for i in msg.split():
        if i not in words:
            words.append(i)
            
    print(inputs)
    print(words)
