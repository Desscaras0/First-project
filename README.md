def add(n1, n2) :   
   return n1 + n2

def sub(n1, n2):
   return n1 - n2
def div(n1 , n2):
   return n1 / n2
def multi(n1, n2): 
   return n1 * n2


sel = int(input("Choose Operation:\n1. Add\n"))
if sel in (1,) :
  n1 = int(input("Enter a Number: "))
  n2 = int(input("Enter a Number: "))
 
  if sel == 1:
       print(n1 ,"+", n2 ,"=", add(n1, n2))
else:
 print("Invalid Input")
