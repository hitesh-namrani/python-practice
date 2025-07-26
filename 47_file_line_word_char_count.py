f=open("count.txt",'r')
lines=f.readlines()
char_count=0
word_count=0
for line in lines:
    word_count+=len(line.split())
    char_count+=len(line)
print(f"number of lines = {len(lines)}")
print(f"number of words = {word_count}")
print(f"number of characters = {char_count}")