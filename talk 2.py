words=[]
def copy(words,newWord):
    print(newWord)
    words.append(newWord)
def find(words,newWord):
    n=1
    while n<=len(words):
        if words[n-1]==newWord:
            return n
        else:
            n=n+1
    return -1
while True:
    newWord=input()
    if find(words,newWord)==-1 or find(words,newWord)==len(words):
        copy(words,newWord)
    else:
        print(words[find(words,newWord)])
        words.append(words[find(words,newWord)])
        words.remove(words[find(words,newWord)])
