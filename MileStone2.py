from random import shuffle, randint, random
from _overlapped import NULL
global b2              #  THIS IS A BIT WRONG , KEYS APPEARING AGAIN EVEN AFTER POP   
global b1                          
#global D_total
#global P1_total
#global P2_total
P1_total=0
P2_total=0
b1=True
b2=True
print("Welcome to BlackJack! Get as close to 21 as you can without going over!\n"+
    "Dealer hits until she reaches 17. Aces count as 1 .\n"+
    "Card output goes a letter followed by a number of face notation\n")
l={"HA":1,"H2":2,"H3":3,"H4":4,"H5":5,"H6":6,"H7":7,"H8":8,"H9":9,"H10":10,"HJ":10,"HQ":10,"HK":10,
   "SA":1,"S2":2,"S3":3,"S4":4,"S5":5,"S6":6,"S7":7,"S8":8,"S9":9,"S10":10,"SJ":10,"SQ":10,"SK":10,
   "CA":1,"C2":2,"C3":3,"C4":4,"C5":5,"C6":6,"C7":7,"C8":8,"C9":9,"C10":10,"CJ":10,"CQ":10,"CK":10,
   "DA":1,"D2":2,"D3":3,"D4":4,"D5":5,"D6":6,"D7":7,"D8":8,"D9":9,"D10":10,"DJ":10,"DQ":10,"DK":10
   }    

def result():
    global D_total
    i=randint(0,len(l))
    D_total=D_total+l[keys[i]]
    print("Dealer total is - \n",D_total)
    if D_total > 21:
        print("Dealer is Busted !!\n")
    elif 21>D_total > P1_total and D_total < P2_total <22:
        print("Player 2 wins!! \n")
    elif D_total < P1_total <22 and 22>D_total > P2_total:
        print("Player 1 wins!! \n")
    elif D_total < P1_total<22 and P1_total<P2_total<22:
        print("Player 2 wins!!\n")
    else:
        print("Player 1 wins!!\n")
    l.pop(keys[i], None)
  #  print("WE ARE IN RESULT SECTION \n")

def Player_one_stand():
    b1=False
    if b1 and b2 == False:
        result()
    else:
        print("Total of player 1 is - \n",P1_total)
        print("Dealer hand total is -\n"+"{s}".format(s=D_total)+"\n with another card hidden upside down"+
        " Hit or Stand? Player two ? Press either h or s: ")
        ch=input()
        if ch=='h':
            Player_two_Hit()        
        else:
            Player_two_stand()
    
def Player_two_stand():
    b2=False
    if b1 and b2 == False:
        result()
    else:
        print("Total of player 2 is - \n",P2_total)
        print("Dealer hand total is -\n"+"{s}".format(s=D_total)+"\n with another card hidden upside down"+
        " Hit or Stand? Player one ? Press either h or s: ")
        ch=input()
        if ch=='h':
            Player_one_Hit()        
        else:
            Player_one_stand()
    
class Player_one(object):
    def __init__(self,card1,cardValue1,card2,cardValue2):
        self.card1=card1
        self.cardValue1=cardValue1
        self.card2=card2
        self.cardValue2=cardValue2
        global P1_total
        P1_total = P1_total+self.cardValue1+self.cardValue2
        print("player one cards are -\n"+"{c1} and {c2}".format(c1=self.card1, c2=self.card2))
        print("player one hand total - \n",P1_total)
       


class Player_two(object):
    def __init__(self,card1,cardValue1,card2,cardValue2):
        self.card1=card1
        self.cardValue1=cardValue1
        self.card2=card2
        self.cardValue2=cardValue2
        global P2_total
        P2_total = P2_total+self.cardValue1+self.cardValue2
        print("player two cards are -\n"+"{c1} and {c2}".format(c1=self.card1, c2=self.card2))
        print("player two hand total - \n",P2_total)


"""def Player_two(card1,cardValue1,card2,cardValue2):
    print("player two cards are -\n"+"{c1} and {c2}".format(c1=card1, c2=card2))
    print("player two hand total -\n"+"{sum}".format(sum=cardValue1+cardValue2))
    global P2_total
    P2_total= P2_total+cardValue1+cardValue2"""

def Player_two_Hit():
    i=randint(0,len(l))
    Player_two(keys[i], l[keys[i]], NULL, NULL) 
    if P2_total>21:
        print("The Player 2 is Busted!! \n")
        print("Dealer hand total is -\n"+"{s}".format(s=D_total)+"\n with another card hidden upside down"+
        " Hit or Stand? Player one ? Press either h or s: ")
        l.pop(keys[i], None)
        ch=input()
        if ch=='h':
            Player_one_Hit()        
        else:
            Player_one_stand()
    else:
        print("Dealer hand total is -\n"+"{s}".format(s=D_total)+"\n with another card hidden upside down"+
        " Hit or Stand? Player two ? Press either h or s: ")
        ch=input()
        if ch=='h':
            Player_two_Hit()        
        else:
            Player_two_stand()        
            
    
def Player_one_Hit():
    i=randint(0,len(l))
    Player_one(keys[i], l[keys[i]], NULL, NULL)
    if P1_total>21:
        print("The Player 1 is Busted!! \n")
        print("Dealer hand total is -\n"+"{s}".format(s=D_total)+"\n with another card hidden upside down"+
        " Hit or Stand? Player two ? Press either h or s: ")
        l.pop(keys[i], None)
        ch=input()
        if ch=='h':
            Player_two_Hit()        
        else:
            Player_two_stand()
    else:
        print("Dealer hand total is -\n"+"{s}".format(s=D_total)+"\n with another card hidden upside down"+
        " Hit or Stand? Player one ? Press either h or s: ")
        ch=input()
        if ch=='h':
            Player_one_Hit()        
        else:
            Player_one_stand()
            
    #print(len(l))
  
def Dealer(card1,cardValue1):
    print("Dealer one card is -\n"+"{c1}".format(c1=card1))
    print("Dealer hand total is -\n"+"{sum}".format(sum=cardValue1)+"\n with another card hidden upside down"+
        " Hit or Stand? Player one ? Press either h or s: ")
    global D_total
    D_total=cardValue1      
    l.pop(keys[i], None)
    ch=input()
    if ch=='h':
        Player_one_Hit() 
    else:
        Player_one_stand()


chips_1=int(input("Enter the number of chips player 1: \n"))
while True:
    if chips_1 >100:
        chips_1=int(input("enter a number less than 100 : \n"))
        continue
    else:
        break

chips_2=int(input("Enter the number of chips player 2: \n"))
while True:
    if chips_2 >100:
        chips_2=int(input("enter a number less than 100 : \n"))
        continue
    else:
        break
    
keys=list(l.keys())
#print(keys)
i=randint(0,len(l))
j=randint(0,len(l))
"""print(keys[i])
print(l[keys[i]])"""
Player_one(keys[i], l[keys[i]], keys[j], l[keys[j]])
l.pop(keys[i], None)
l.pop(keys[j], None)
#print(len(l))
i=randint(0,len(l))
j=randint(0,len(l))
Player_two(keys[i], l[keys[i]], keys[j], l[keys[j]])
l.pop(keys[i], None)
l.pop(keys[j], None)

i=randint(0,len(l))
Dealer(keys[i], l[keys[i]])

