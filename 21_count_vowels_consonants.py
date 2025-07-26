string=input("Give string : ")
strlen=len(string)
vovels=0
consonants=0
for i in range(strlen):
    if(string[i] in 'aeiou'):
        vovels+=1
    elif(string[i] in 'bcdfghjklmnpqrstvwxyz'):
        consonants+=1
print(f"'{string}' has {vovels} vovels and {consonants} consonants.")