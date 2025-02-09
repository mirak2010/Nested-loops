string=input("Please enter a word: ")
char=input("Please enter a character that you want to find: ")
i=0
count=0
while(i< len(string)):
    if(string[i]==char):
        count=count+1 
    i=i+1

print("The amount of characters provided is  ", count)