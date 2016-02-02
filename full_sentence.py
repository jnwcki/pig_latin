sentence = input("Write a sentence for pig latinizing >")
sentence = sentence.split(' ')
#print(sentence)
output = []
for word in sentence:

    if word[0].lower() in ["a","e","i","o","u"]:
        output.append(word[1] + word[2:] + 'say ')
    else:
        output.append(word[1:] + word[0] + 'ay ')
print(' '.join(output))