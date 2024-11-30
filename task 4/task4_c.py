def sort(userinput):
    words = userinput.split()  
    n = len(words)

    for i in range(n):
        for j in range(0, n-i-1):
          
            if ord(words[j][0]) > ord(words[j+1][0]):
                
                words[j], words[j+1] = words[j+1], words[j]

    return ' '.join(words)

userinput = input("ENter the value: ")
print(sort(userinput))
