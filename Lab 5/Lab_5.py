import sys
import os
import string

def index_text_file(txt_filename, resultant_file = "index.txt",delimiter_chars=",.;:!?"):
    
    text_file = open(txt_filename, "r")                             #Open file in read mode
    dict_of_words = {}                                              #Dictionary to store words           
    line = 0                                                        #Store Line number    

    for lin in text_file:
        line += 1
        words = lin.split()                                              # Split the line by whitespace.
        clean_words = [ word.strip(delimiter_chars) for word in words ]  #Removing extra chracters 
        for word in clean_words:
            if dict_of_words.has_key(word):
                dict_of_words[word].append(line)
            else:
                dict_of_words[word] = [ line ]
    word_keys = dict_of_words.keys()
    length = len(word_keys)
    length = str(length)
    print ( length + " unique words found." + "   in "+ txt_filename)
    word_keys = dict_of_words.keys()
    word_keys.sort()                                                                 

    idx_fil = open(resultant_file, "a")                                  # Create the index file.
    for word in word_keys:
        line_nums = dict_of_words[word]
        idx_fil.write(word + " " +" Path : " + txt_filename + "( Line number: ")
        for line in line_nums:
            idx_fil.write("  " + str(line) + " ) ")
        idx_fil.write("\n")

    text_file.close()                                                    #Closing both files
    idx_fil.close()

#C:\\
#../
print ("Welcome to my file indexer \n\n")

while (True):
    print ("(1) Create text file index \n\n")
    print ("(2) Search keyword in index \n\n")
    choice = raw_input("Enter choice number : ")

    if (choice == "1"):
        print("Creating index file ... Please wait ..\n\n")  
        for root, dirs, files in os.walk("C://Users//"):                #To search current Directory replace "C:\\" with "../"
            for file in files:
                if file.endswith(".txt"):
                    file = os.path.join(root, file)
                    index_text_file(file)
        print("DONE\n\n")        

    if (choice == "2"):
        keyword = raw_input("Enter Keyword : ")
        with open("index.txt") as openfile:
            for line in openfile:
                for part in line.split():
                    if keyword in part:
                        print ("\nFOUND: " + part + "\nPATH: "+ line)
                   