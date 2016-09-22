#encoding = utf-8

f = open('abc.txt',wt,encoding="utf-8")
f.write("Imagine non-english language here")
f.close()

text = open("abc.txt", encoding="utf-8").read()