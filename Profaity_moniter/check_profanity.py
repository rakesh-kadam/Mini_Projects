import urllib

def read_txt():
    quotes = open("/home/rakesh/Desktop/Projects/Read_file/movie_quotes")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=s"+text_to_check)
    output  = connection.read()
    #print(output)
    connection.close()
    if "true" in output:
        print("Profanity Alert!!!")
    elif "false" in output:
        print("This document has no curse words")
    else:
        print("Could not sca the document properly")


read_txt()