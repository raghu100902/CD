global s
print("enter the input string below") 
s = list(input())
global i 
i = 0 
def match(a):
    global s 
    global i 
    if(i>=len(s)):
        return False
    elif(s[i]==a):
        i+=1
        return True 
    else:
        return False 
def F():
    if(match("(")):
        if(E()):
            if(match(")")):
                return True 
            else:
                return False 
        else:
            return False 
    elif(match("i")):
        return True 
    else:
        return False 
def Tx():
    if(match("*")):
        if(F()):
            if(Tx()):
                return True 
        else:
            return False 
    else:
        return True 
def T():
    if(F()):
        if(Tx()):
            return True 
        else:
            return False 
    else:
        return False 
    
def Ex():
    if(match("+")):
        if(T()):
            if(Ex()):
                return True 
        else:
            return False 
    else:
        return True 
def E():
    if(T()):
        if(Ex()):
            return True 
        else:
            return False 
    else:
        return False 

if(E()):
    if(i == len(s)):
        print("accepted")
    else:
        print("not accepted")
else:
    print("not accepeted")