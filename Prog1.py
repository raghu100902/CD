def count(fname):
    num_line = 0
    num_words = 0
    num_char = 0
    with open(fname, 'r') as f:
        for line in f:
            num_line += 1
            w = line.split()
            num_words = num_words + len(w)
            for l in line:
                for i in l:
                    if (i != ' '):
                        num_char += 1
    print("Number of lines in text file: ", num_line)
    print("Number of words in text file: ", num_words)
    print('Number of characters in text file: ', num_char)

if __name__ == '__main__':
    fname = input("Enter the file name: ")
    try:
        count(fname)
    except:
        print('File not found')
