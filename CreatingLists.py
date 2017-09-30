dict = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0,'g':0, 'h':0,'i':0, 'j':0,'k':0, 'l':0,'m':0, 'n':0,'o':0,
        'p':0, 'q':0,'r':0, 's':0,'t':0, 'u':0,'v':0, 'w':0,'x':0, 'y':0,'z':0, 'A':0,'B':0, 'C':0,'D':0, 'E':0,
        'F':0, 'G':0,'H':0, 'I':0,'J':0, 'K':0,'L':0, 'M':0,'N':0, 'O':0,'P':0, 'Q':0,'R':0, 'S':0,'T':0, 'U':0,
        'V':0, 'W':0,'X':0, 'Y':0,'Z':0, '0':0,'1':0, '2':0,'3':0, '4':0,'5':0, '6':0,'7':0, '8':0,'9':0,
        '\n':0, ' ':0,'!':0, '"':0,'#':0, '$':0,'%':0, '&':0,'\'':0, '(':0,')':0, '*':0,'+':0, ',':0,'-':0, '.':0,
        '':0,'/':0, ':':0,';':0, '<':0,'=':0, '>':0,'?':0, '@':0,'[':0, '\\':0,']':0, '^':0,'_':0, '`':0, '~':0,'\t':0,
        '{':0,'|':0,'}':0} 

#'':0, '':0,'':0, '':0,'':0, '':0,'':0, '':0,'':0, '':0,'':0, '':0,'':0, '':0,'':0, '':0,

with open("Words.txt") as f:
  while True:
    c = f.read(1)
    dict[c] = dict[c] + 1
    #print(dict[c])
    
    if not c:
      print("End of file")
      break
    #print("Read a character:", c)

##for key,value in dict.items():
##    print(key, " ",value)

#find n times most frequent character
n = 5

letters = []
frequency = []

##i = 0
##for key,value in dict.items():
##    letters.append(key)
##    frequency.append(value)
    
#We are planning to find the n most frequent letters

for i in range(0,n):
    maxval = 0
    maxkey = ""
    for key,value in dict.items():
        if value > maxval:
            maxval = value
            maxkey = key
    letters.append(maxkey)
    frequency.append(maxval)
    #delete current max key and max value
    del dict[maxkey]

print("frequent letters:")
for j in letters:
    print(j)

print("frequent values:")
for k in frequency:
    print(k)
    
    
