#IF STATEMENTS : IF ELIF STATEMENTS  : IF.....ELIF.....ELSE
# Testing stuff that runs particular parts of your code
# if a certain condition is True. 
# Uses boolean tests True or False

#Syntax

isLearning = True;

if isLearning:
    print("Stephen is learning! 😋")
else:
    print("Stephen is becoming lazy 😁")
    

# IF_ELSE CONDITIONAL STATEMENTS 

"""
A house costs $1m. If a buyer has good credit, they need to put down 10%
Otherwise, they need to put down 20%. Print the down payment. 
"""

buyerGoodCredit = False
housePrice = 1000000
rate = 0

#One Line tenary operator
## rate = 0.1 if buyerGoodCredit else 0.2

if buyerGoodCredit:
    rate = 0.1
else:
    rate = 0.2

downpayment = (1000000 * rate)

print(f'''For the user: 
      Downpayment for the house with price ${housePrice} 
      is {downpayment}''')

