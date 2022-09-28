import random 

inputs = [] # todo: id
words = {}
outputs = {}
topics = []
pre_words = []
pro_words = []

questionings = []

def remove_specials(str):
    return str.replace("'",'').replace('!','')

while True:
    msg = input('You: ')
    if msg not in inputs:
        inputs.append(msg)

    for i in msg.split():
        i = remove_specials(i)
        
        if i not in words:
            words[i] = 0
        else:
            words[i] += 1

        if '?' in i:
            questionings.append(i)
            
    #print(inputs)
    #print(words)
    answer = []
    for i in words:
        if words[i]>0:
            answer.append(i)
    
    response = ''
    for i in range(len(answer)):
        response += random.choice(answer) + ' '
    
    print(f'AI: {response}')
