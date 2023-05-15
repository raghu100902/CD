#symbol table
def symboltable(expr):
    operators=['+','-','/','%','','//','*','=']
    keywords=['int','char','float','return','include','bool']
    for i in fname:
        if(i in operators):
            print(i,id(i),'operator')
        elif(i in keywords):
            print(i,id(i),'keyword')
        elif(i.isdigit()):
            print(i,id(i),'constant')
        else:
            print(i,id(i),'identifier')
if _name=='main_':
    expr=input('enter an experssion:')
    symboltable(expr)



