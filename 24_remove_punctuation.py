string=input("Give string : ")
removed_punc=''
for i in range(len(string)):
    if (string[i] in ',.;'):
        continue
    else:
        removed_punc+=string[i]
string=removed_punc
print("New string is :",string)