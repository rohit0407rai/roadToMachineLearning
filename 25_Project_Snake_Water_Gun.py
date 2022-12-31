import random
def game(comp,you):
    if(comp==you):
        return None
    elif (comp=='s'):
        if(you=='w'):
            return False
        elif(you=='G'):
            return True
    elif (comp=='w'):
        if(you=='s'):
            return True
        elif(you=='G'):
            return False
    elif (comp=='G'):
        if(you=='s'):
            return False
        elif(you=='w'):
            return True

print("Player 1 Turn : Snake(s) Water(w) or Gun(G)?")
randNo=random.randint(1,3)

if randNo==1:
    comp="s"
elif randNo==2:
    comp="w"
elif randNo==3:
    comp="G"
b=input("Player 2 Turn: Snake(s) Water(w) or Gun(G)?")
c=game(comp,b)
if(c==False):
    print("YOU LOST")
elif(c==True):
    print("You Won")
elif(c==None):
    print("Tie")


