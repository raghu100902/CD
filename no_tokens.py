def tokens(fname):
    num_token = 0
    keywords = ['int', 'float', 'char', 'boolean', 'double', 'def', 'if', 'while', 'with']
    operators = ['=', '+', '-', '==', '*', '/', '%', '!=', '**']
    Special = [',', '(', ')', ';', ':', '[', ']', '&']
    with open(fname,'r') as f:
        for line in f:
            w = line.split()
            key = 'N'
            num_token = num_token + len(w)
            for i in w:
                if (i in Special):
                    print(i, ": Special Character")
                    key = 'N'
                elif (i in keywords):
                    print(i, ": Keyword")
                    key = 'Y'
                elif (i.isdigit()):
                    print(i, ": Constant")
                    key = 'N'
                elif (i in operators):
                    print(i, ": Operator")
                    key = 'N'
                else:
                    if (key == 'Y'):
                        print(i, ": Identifier")
                        key = 'N'
                    else:
                        print(i,": String")
    print("Number of Tokens in text file: ", num_token)

if __name__ == '__main__':
    fname = input("Enter the file name: ")
    try:
        tokens(fname)
    except:
        print("File not found")
