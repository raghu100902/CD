with open("t.txt","r") as f:
    for line in f.readlines():
        l,r=line.split('=')
        if('+' in r):
            a,b=r.split('+')
            str="ADD"
        elif('-' in r):
            a,b=r.split('-')
            str="SUB"
        elif('*' in r):
            a,b=r.split('-')
            str="MUL"
        elif('/' in r):
            a,b=r.split('/')
            str="DIV"
        else:
            a=r
        
        print("LDA\t")
        print(a)
        if('+' in r or '-' in r or '*' in r or '/' in r):
            print(f"{str}\t")
            print(b)
        print("STA\t")
        print(l)
