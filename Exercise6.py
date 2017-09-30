#MIGUEL DOMINGUEZ
#PHYTON AFTERNOON CLASS
#11/15/16

######PART1#######

#A   A definite loop is a loop that loops for a fixed amount of times since we knoe the number of iterations.

numbers = [4,5,7]

for count in numbers:
    print(count)
print("=============")
#B An indefinite loop is a loop that iterates or loops until a condition becomes true or false, or something breaks the loop and it is unknow until that occurs.

hot = True

while hot:
    temperature = input("Input 'yes' if it is hot. Input 'no' if cold")
    if temperature == "no":
        hot = False
print("=============")
#C We need BREAK to terminate the current loop and resume executetion at the next statement
#We need CONTROL to go back to the top of the loop while ignoring the rest of the statements
#We need PASS to execute a denoted statement. It is useful to denote where future statmeents and code will go.

#Break

temp = [1,2,3,4]
for counter in temp:
    if counter == 2:
        break
    print(counter)
print("=============")
#Countinue

height = [10,20,30,40,50]
for counter1 in height:
    if counter1 == 30:
        continue
    print(counter1)


print("=============")
#Passs

animals = ["dog", "bird", "fish"]
for counter2 in animals:
    if counter2 == "bird":
        pass
        print("PASS: I forgot my dog ate my cat")
    print("I have a ", counter2, " ")
print("=============")
#D Sentinel data is data that is dintinguishable from actual data such as characters or special numbers. We use then to stop or break loops
#or identify when a user has pressed enter or the user lets the program know when to terminate by inputing -1.

######PART2#######
    
str1 = "abcddeef"
str2 = "abcghg"


#A

for i in range(len(str1)):
    
    printer = True
    for j in range(len(str2)):
        if str1[i] == str2[j]:
            printer = False
            break;
            
    if printer == True:
        print(str1[i])
print("=============")
#B

for i in range(len(str2)):
    
    printer = True
    for j in range(len(str1)):
        if str2[i] == str1[j]:
            printer = False
            break;
            
    if printer == True:
        print(str2[i])

print("=============")
#C

for i in range(len(str1)):
    
    printer = True
    for j in range(len(str2)):
        if str1[i] == str2[j]:
            printer = False
            break;
            
    for x in range((i-1), -1, -1):
        if str1[x] == str1[i]:
            printer = False
            break;
    if printer == True:
        print(str1[i])

print("=============")  
#D        
    
for i in range(len(str2)):
    
    printer = True
    for j in range(len(str1)):
        if str2[i] == str1[j]:
            printer = False
            break;
            
    for x in range((i-1), -1, -1):
        if str2[x] == str2[i]:
            printer = False
            break;
    if printer == True:
        print(str2[i])


















