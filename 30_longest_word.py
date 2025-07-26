sentence=input("Give sentence : ")
words=sentence.split()
longest_word=0
for i in range(len(words)):
    if len(words[i])>len(words[longest_word]):
        longest_word=i
print("longest word is",words[longest_word])