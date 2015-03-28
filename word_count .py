##################################################
#Jake Stocker                                    #
#                                                #
#07/18/2014                                      #
#                                                #
#This program reads the programmer designated    #
#file (in this case gettysburg.txt) sorts the    #
#words in the file by frequency and then         #
#alphabetically.  It then prints the sorted      #
#tuple.                                          #
##################################################










#This function used a special dictionary type named collections.
#It uses function Counter() to set dictionary (wordcount) to count
#all words by line it calls line.lower() to ensure all letters are
#counted as lower clase and split() to split the words on the line.



def read_and_count():
    from collections import Counter
    wordcount = Counter()
    with open('gettysburg.txt') as fin:
       for line in fin:
           wordcount.update(line.lower().split())
           return wordcount

#This function sorts the list passed in alphabetically using
#the built in python function sorted().  First it takes the counter passed
#into the function and stores it in tuple sortedList sorted by
#the method most_common().  It then sorts sortedList by frequency of the word.
#Next it calls sorted() on sortedList and alphabetizes the sorted Tuple.

    
def sort(d):
    
    from collections import Counter
    sortedList=Counter(d.most_common())
    sortedList=sorted(sortedList)
    sortedList=sorted(sortedList,key=lambda tup:tup[1],reverse=True)
    
    return sortedList

#Prints the tuple

def print_tuple(d):
    for (word,count) in d:
        print word, count


#Calls read_and_count() to read defined text file.
#Calls sort() to sort by frequency and alphabetically.
#Calls print_tuple() to print all values.
def main():
    wordcount=read_and_count()
    wordcount=sort(wordcount)
    print_tuple(wordcount)



main()

    

