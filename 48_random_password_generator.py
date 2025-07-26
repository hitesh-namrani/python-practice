import random
import string
length=int(input("Give length of password : "))
allchar=string.ascii_letters+string.punctuation+string.digits
password=''.join(random.choices(allchar,k=length))
print(password)