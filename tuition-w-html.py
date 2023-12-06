#Name: Loren Lemarr
#Name: Christina Creegan
#Prog Purpose: This program computes PVCC college tuition & fees based on the number of credits
#   PVCC Fee Rates are from: https://www.pvcc.edu/tuition-and-fees
#   Price for adults: $156.61
#   price for children: $336.21
#   Service fee rate: $23.50
#   Sales tax rate: $1.75
#                   $2.90

import datetime

######################     define global variables      ######################
# define tax rate and prices
RATE_TUITION_IN = 156.61
RATE_TUITION_OUT = 336.21
RATE_CAPITAL_FEE = 23.50
RATE_INSTITUTION_FEE = 1.75
RATE_ACTIVITY_FEE = 2.90

# define global variables
inout = 1 #1 = instate,  2 = out of state
numcredits = 0
scholarshipamt = 0
capital_amt = 0

# create output file
outfile = 'tuition.html'


######################     define program functions     ######################
def main():

    open_outfile()
    more = True

    while more:
        get_user_data()
        perform_calculations()
        display_results()

        askAgain = input("\nWould you like to calculate tuition and fees for another student (Y or N)?: ")
        if askAgain.upper() == "N" or askAgain == "n":
            more = False
            print('\n** Open this file in a browser window to see your results: ' + outfile)
            f.write('</body></html>')
            f.close()
            
def open_outfile():
    global f
    f = open(outfile, 'w')
    f.write('<html> <head> <title> PVCC Tuition Costs </title>\n')
    f.write('<style> td{text-align: right} </style> </head>\n')
    f.write('<body style ="background-color: #985b45; background-image: url(wp-tuition.png); color: #f8dd61;">\n')
    
def get_user_data():
    global inout, numcredits, scholarshipamt
    inout = int(input("Enter a 1 for IN-STATE; enter a 2 for OUT-OF-STATE: "))
    numcredits = int(input("Number of credits registered for: "))
    scholarshipamt = float(input("Scholarship amount received: "))

def perform_calculations():
    global tuition_amount, capital_amt,  institution_fee, student_fee, total, balance
    if inout == 1:
        tuition_amount = RATE_TUITION_IN * numcredits
    else:
        tuition_amount = RATE_TUITION_OUT * numcredits
        capital_amt = RATE_CAPITAL_FEE * numcredits

    institution_fee = RATE_INSTITUTION_FEE * numcredits
    student_fee = RATE_ACTIVITY_FEE * numcredits
    total = tuition_amount + capital_amt + institution_fee + student_fee
    balance = total - scholarshipamt
def display_results():
    moneyf = '8,.2f'
    today = str(datetime.datetime.now())
    day_time = today[0:16]

    tr = '<tr><td>'
    endtd = '</td><td>'
    endtr = '</td></tr>\n'
    sp = " "

    f.write('\n<table border="3"   style ="background-color: #47161a;  font-family: arial; margin: auto;">\n')            
    f.write('<tr><td colspan = 3>\n')
    f.write('<h2>PVCC</h2></td></tr>')
    f.write('<tr><td colspan = 3>\n')
    f.write('*** Costs for enrollment ***\n')

    f.write(tr + 'Tuition amount' + endtd + format(tuition_amount, moneyf) + endtr)
    f.write(tr + 'Capital fee' + endtd + format(capital_amt, moneyf) + endtr)
    f.write(tr + 'Institution fee' + endtd + format(institution_fee, moneyf) + endtr)
    f.write(tr + 'Activity fee' + endtd + format(student_fee, moneyf) + endtr)
    f.write(tr + 'Total' + endtd + format(total, moneyf) + endtr)
    f.write(tr + 'Scholarship amount' + endtd + format(scholarshipamt, moneyf) + endtr)
    f.write(tr + 'Balance' + endtd + format(balance, moneyf) + endtr)

    f.write('<tr><td colspan= "3">Date/Time: ')
    f.write(day_time)
    f.write(endtr)
    f.write('</table>')    
######################      call on main program to execute ######################

main()



