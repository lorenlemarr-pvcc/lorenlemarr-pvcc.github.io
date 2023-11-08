#Name: Loren Lemarr
#Name: Wyatt Pennington
#Prog Purpose: This program finds the tax for owning a car in Charlottesville based on car value
#   Personal property tax rate per year: $4.20 per $100 vehicle value (4.20%)
#   Tax relief rate: 33%

import datetime

######################     define global variables      ######################
# define tax rate and prices

PPTR = .042
TRR = .33

# define global variables
car_value = 0
annual_amount = 0
semi_amount = 0
ref_amount = 0
total = 0

######################     define program functions     ######################
def main():
    
    more_food = True

    while more_food:
        get_user_data()
        perform_calculations()
        display_results()
        askAgain = input("\nWould you like to order again (Y or N)?: ")
        if askAgain.upper() == "N" or askAgain == "n":
            more_food = False
            print("Thank you for your order. Enjoy your food")

def get_user_data():
    global car_value, relief_yesno, total
    car_value = int(input("\nWhat is the assessed value of the vehicle?: "))
    relief_yesno = input("Is your vehicle eligible for tax relief (Y/N)?: ")
   
def perform_calculations():
    global sales_tax, total, annual_amount, ref_amount
  
    annual_amount = car_value*PPTR
    semi_amount = annual_amount/2
    if relief_yesno.upper() == "Y" or relief_yesno == "y":
        ref_amount = semi_amount*TRR    
    total = semi_amount - ref_amount

def display_results():
    moneyf = '8,.2f'
    print('--------------------------------')
    print('**** City of Charlottesville, Virginia *****')
    print('**PERSONAL PROPERTY TAX**')
    print('--------------------------------')
    print('Assessed value of vehicle         \t$'+format(car_value, moneyf))
    print('Full annual amount owed           \t$'+format(annual_amount, moneyf))
    print('Relief amount                     \t$'+format(ref_amount, moneyf))
    print('Total                             \t$'+format(total, moneyf))
    print('--------------------------------')
    print(str(datetime.datetime.now()))
    
######################      call on main program to execute ######################

main()




