
def main():
    name=input("Enter you Name Sir!:  \n").title()
    message=f"Welcome to the board {name}\n Let's start the adventure!"
    print(message)
main()   

def destination():
    destination=input("Enter what you want to explore: \n").strip().lower()
    if destination =='mountain':
        print('Okay! Your want to explore the beauty of Mountain !')
    elif destination =='beach':   
        print('Okay! You want to releax on this trip! ')
    else:
        print('Invalid! Input')
destination()
def checkBudget():
    while True:
        try:
            budget=int(input('Budget for the trip'))
            return budget
        except ValueError:
            print("Invalid Input!, Enter again")
budget=checkBudget()

def luxury(budget):
        if budget >= 500:
           print('You gone have a Luxury trip')
        elif budget >= 200:
            print('You have to do decent trip')
        elif budget >= 0:
            print('You are going for a budget trip')
        else:
            print("Sorry! \n You don't have  budget for this trip" )
luxury(budget)
def numberOfDay():
    while True:
        try:
            days=int(input('No. of Days'))
            return days
        except ValueError:
            print("Invalid Input!, Enter again")
days=numberOfDay()

def totalCost1(budget,days):
    totalCost=budget*days
    return totalCost
    
totalCost=totalCost1(budget,days)
print(f'Your have the total buget = {totalCost} for this trip\n You are on the trip of =  {days} \n You gone to spend {budget} on each day')
