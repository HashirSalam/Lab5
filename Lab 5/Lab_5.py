import sys
import os
import string


def index_text_file(txt_filename, idx_filename = "index.txt",delimiter_chars=",.;:!?"):
    
    txt_fil = open(txt_filename, "r")
    word_occurrences = {}
    line_num = 0

    for lin in txt_fil:
        line_num += 1
        print("line_num", line_num)
        # Split the line into words delimited by whitespace.
        words = lin.split()
        print("words", words)
        # Remove unwanted delimiter characters adjoining words.
        words2 = [ word.strip(delimiter_chars) for word in words ]
        print("words2", words2)
        # Find and save the occurrences of each word in the line.
        for word in words2:
            if word_occurrences.has_key(word):
                word_occurrences[word].append(line_num)
            else:
                word_occurrences[word] = [ line_num ]

    print("Processed {} lines".format(line_num))

    if line_num < 1:
        print "No lines found in text file, no index file created."
        txt_fil.close()
        sys.exit(0)

    # Display results.
    word_keys = word_occurrences.keys()
    print "{} unique words found.".format(len(word_keys))
    #print("DEBUG: Word_occurrences", word_occurrences)
    word_keys = word_occurrences.keys()
    #print("DEBUG: word_keys", word_keys)

    # Sort the words in the word_keys list.
    word_keys.sort()
    #print("DEBUG: after sort, word_keys", word_keys)

    # Create the index file.
    idx_fil = open(idx_filename, "a")

    # Write the words and their line numbers to the index file.
    # Since we read the text file sequentially, there is no need 
    # to sort the line numbers associated with each word; they are 
    # already in sorted order.
    for word in word_keys:
        line_nums = word_occurrences[word]
        idx_fil.write(word + " " +" Path : " + txt_filename + "( Line number: ")
        for line_num in line_nums:
            idx_fil.write("  " + str(line_num) + " ) ")
        idx_fil.write("\n")

    txt_fil.close()
    idx_fil.close()





#C:\\
#for root, dirs, files in os.walk("../"):
#    for file in files:
#        if file.endswith(".txt"):
#            file = os.path.join(root, file)
#            #print(os.path.join(root, file))
#            index_text_file(file)    


with open("index.txt") as openfile:
    for line in openfile:
        for part in line.split():
            if "Hashir" in part:
                print part , line