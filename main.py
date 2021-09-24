def Countwords():
    filename= input("Enter the name of the file: ")
    numberofwords=0
    file=open(filename,'r')
    for line in file:
        words= line.split()
        numberofwords=numberofwords+len(words)
    print("Number Of Words In The File")
    print(numberofwords)

Countwords()