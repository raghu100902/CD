def tokens(fname):
    num_token = 0
    number=1
    keywords = ['int', 'float', 'char', 'boolean', 'double', 'def', 'if', 'while', 'with']
    operators = ['=', '+', '-', '==', '*', '/', '%', '!=', '**']
    Special = [',', '(', ')', ';', ':', '[', ']', '&']
    print("Line No    lexeme   token")
    with open(fname,'r') as f:
        for line in f:
            w = line.split()
            key = 'N'
            num_token = num_token + len(w)
            for i in w:
                if (i in Special):
                    print(number,'    ', i, "    Special Character")
                    key = 'N'
                elif (i in keywords):
                    print(number,'    ',i, "    Keyword")
                    key = 'Y'
                elif (i.isdigit()):
                    print(number,'    ', i, "    Constant")
                    key = 'N'
                elif (i in operators):
                    print(number,'    ', i, "    Operator")
                    key = 'N'
                else:
                    if (key == 'Y'):
                        print(number,'    ', i, "    Identifier")
                        key = 'N'
                    else:
                        print(number,'    ', i,"    String")
            number=number+1
    print("Number of Tokens in text file: ", num_token)

if __name__ == '__main__':
    fname = input("Enter the file name: ")
    try:
        tokens(fname)
    except:
        print("File not found")
