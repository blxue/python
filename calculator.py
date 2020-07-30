def Convert(string): 
    li = list(string.split(" ")) 
    return li 

print('Enter the number')

string = input()

op = ['+', '-', '*', '/', '=']

strc = Convert(string)
stro = []
strn = []

for x in range (0, len(strc)):
    if strc[x] in op:
        stro.append(strc[x])
    else :
        strn.append(int (strc[x]))

#print(stro , "\n") 
#print(strn , "\n")

while ( len(stro) > 0) :
    if '*' in stro:
        i=stro.index('*')
        res = int (strn[i]) * int(strn[i+1])
        del strn[i+1]
        strn[i] = res
        del stro [i]
    
    if '/' in stro:
        i=stro.index('/')
        res = int (strn[i]) / int(strn[i+1])
        del strn[i+1]
        strn[i] = res
        del stro [i]
    
    if '+' in stro:
        i=stro.index('+')
        res = int (strn[i]) + int(strn[i+1])
        del strn[i+1]
        strn[i] = res
        del stro [i]
    
    if '-' in stro:
        i=stro.index('-')
        res = int (strn[i]) - int(strn[i+1])
        del strn[i+1]
        strn[i] = res
        del stro [i]
res = strn[0]   
print(res)
