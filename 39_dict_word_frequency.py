text=input("Give the text : ")
words=text.split()
word_count={}
for word in words:
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word]=1
print(f"the dictionary with word counts is {word_count}")