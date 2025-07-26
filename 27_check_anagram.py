word1=input("Give 1st word : ")
word2=input("Give 2nd word : ")
if sorted(word1.lower())==sorted(word2.lower()):
    print(f"{word1} and {word2} are anagrams")
else:
    print(f"{word1} and {word2} are not anagrams")