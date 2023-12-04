#Name: Loren Lemarr
#Prog Purpose: This program computes the cost of hotel guests then creates an html file where the data is displayed
#   Price for single room per night: $195.00
#   price for double room per night: $250
#   price for suite per night: $350
#   Sales tax rate: 6.5%
#   Occupancy tax rate: 11.25%

import datetime

######################     define global variables      ######################
######## TUPLES of constants ###########
#            SR    DR   SU
#indexes      0     1    2
ROOM_COST = (195, 250, 350)
#           sales occupancy  
#indexes      0      1
TAX_RATE = (.065, .1125)
###### NEW LISTS for calculated amounts ##########
sub_list = []
total_list = []
grand_list = []
sales_tax = []
occ_tax= []
############## LISTS of data ############
name = []
room = []
number = []
# create output file
outfile = 'hotelsalesrep.html'


######################     define program functions     ######################
def main():
    read_in_emerald_file()
    open_outfile()
    perform_calculations()

def read_in_emerald_file():
    cust_data = open("emerald.csv","r")
    cust_in = cust_data.readlines()
    cust_data.close()

  #split the data into fields
    for i in cust_in:
        cust.append(i.split(","))

def open_outfile():
    global f
    f = open(outfile, 'w')
    f.write('<html> <head> <title> Emerald Beach Hotels room Costs </title>\n')
    f.write('<style> td{text-align: right} </style> </head>\n')
    f.write('<body style ="background-color: #985b45; background-image: url(wp-tuition.png); color: #f8dd61;">\n')
    

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



