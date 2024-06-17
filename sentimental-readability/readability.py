# TODO

from cs50 import get_string

text = get_string("text: ")

#words, letters and sentences
w = 1
l = 0
s = 0

for i in text:
    if i.isalpha():
        l += 1
    elif i == " ":
        w +=  1
    elif i == '.' or i == '!' or i == '?' :
        s+=1

index = 0.0588 * (l/w*100)- 0.296 * (s/w*100 )- 15.8

if index < 1:
    print("Before Grade 1")
elif index >= 16:
    print("Grade 16+")
else:
    print("Grade ",round(index))
