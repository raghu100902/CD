def counter(fname):
    num_words = 0
    num_lines = 0
    num_charc = 0
    with open(fname, 'r') as f:
        for line in f:
            num_lines += 1
            word = 'Y'
            for letter in line:
                if (letter != ' ' and word == 'Y'):
                    num_words += 1
                    word = 'N'
                elif (letter == ' '):
                    word = 'Y'
                for i in letter:
                    if(i !=" " and i !="\n"):
                        num_charc += 1
    print("Number of lines in text file: ", num_lines)
    print("Number of words in text file: ", num_words)
    print('Number of characters in text file: ', num_charc)

if __name__ == '__main__':
    fname = input("Enter the file name: ")
    try:
        counter(fname)
    except:
        print('File not found')
