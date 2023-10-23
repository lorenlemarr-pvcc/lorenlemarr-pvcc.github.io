#Name: Loren Lemarr
#Name: Finn Zschaebitz
#Prog Purpose: This program finds the cost of movie tickets
#   Price for adults: $19.95
#   price for children: $11.95
#   Service fee rate: 10%
#   Sales tax rate: 6.2%

import datetime

######################     define global variables      ######################
# define tax rate and prices
SALES_TAX_RATE = .062
SERVICE_FEE_RATE = .1
PR_ADULT = 19.95
PR_CHILD = 11.95

# define global variables
num_adult = 0
num_child = 0
cost_adult = 0
cost_child = 0
subtotal = 0
service_fee = 0
sales_tax = 0
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
    global num_adult, num_child
    num_adult = int(input("Number of adultss:"))
    num_child = int(input("Number of children:"))

def perform_calculations():
    global cost_adult ,cost_child, subtotal, sales_tax, total, service_fee
    cost_adult = num_adult*PR_ADULT
    cost_child = num_child*PR_CHILD
    subtotal = cost_adult+cost_child
    service_fee = subtotal*SERVICE_FEE_RATE
    sales_tax = subtotal*SALES_TAX_RATE
    total = subtotal + sales_tax + service_fee

def display_results():
    moneyf = '8,.2f'
    print('------------------------------')
    print('**** BRANCH BARBECUE BUFFET *****')
    print('Your neighborhood movie house')
    print('------------------------------')
    print('Adults       $'+format(cost_adult, moneyf))
    print('Child        $'+format(cost_child, moneyf))
    print('Subtotal     $'+format(subtotal, moneyf))
    print('Service fee   $'+format(service_fee, moneyf))
    print('Sales Tax    $'+format(sales_tax, moneyf))
    print('Total        $'+format(total, moneyf))
    print('------------------------------')
    print(str(datetime.datetime.now()))
    
######################      call on main program to execute ######################

main()


