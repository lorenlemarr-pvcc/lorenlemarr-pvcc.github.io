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
sales_tax = []
occ_tax= []
############## LISTS of data ############
cust = []
lname = []
fname = []
room = []
nights = []
# create output file
outfile = 'emerald-web-page.html'
# the only imortant variable
grand = 0
######################     define program functions     ######################
def main():
    read_in_emerald_file()  
    open_outfile()
    perform_calculations()
    display_results()

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
    f.write('<html> <head> <title> Emerald Beach Hotel and Resort</title>\n')
    f.write('<style> td{text-align: right} </style> </head>\n')
    f.write('<body style ="background-color: #985b45; background-image: url(beachsunset.jpg); color: #f8dd61; background-size: 100% auto;">\n')
    

def perform_calculations():
    global grand
    grand = 0
    for i in range(len(cust)):
        lname.append(cust[i][0])
        fname.append(cust[i][1])
        room.append(cust[i][2])
        nights.append(cust[i][3])
        if room[i] == "SR":
            subtotal = int(nights[i])*ROOM_COST[0]
        elif room[i] == "DR":
            subtotal = int(nights[i])*ROOM_COST[1]
        elif room[i] == "SU":
            subtotal = int(nights[i])*ROOM_COST[2]
        salestax = subtotal * TAX_RATE[0]
        occtax = subtotal*TAX_RATE[1]
        print(occtax)
        total = subtotal+salestax+occtax
        #print(total)
        sub_list.append(subtotal)
        sales_tax.append(salestax)
        occ_tax.append(occtax)
        total_list.append(total)
        grand += total
        print(grand)
def display_results():
    moneyf = '8,.2f'
    today = str(datetime.datetime.now())
    day_time = today[0:16]

    tr = '<tr><td>'
    endtd = '</td><td>'
    endtr = '</td></tr>\n'
    sp = " "

    f.write('\n<table border="3"   style ="background-color: #47161a;  font-family: arial; margin: auto;">\n')            
    f.write('<tr><th colspan = 8>\n')
    f.write('<h2>Emerald Beach Hotel and Resort</h2></th></tr>')
    f.write('<tr><th colspan= "8">Date/Time: ')
    f.write(day_time)
    f.write("</th><tr>")
    f.write(tr + "Last Name" + endtd + "First Name" + endtd + "Room TYPE" + endtd + "# Nights" + endtd + "Subtotal" + endtd + "Sales Tax" + endtd + "Occupancy Tax" + endtd + "Total" + endtr)
    for i in range(len(lname)):
        f.write(tr + lname[i] + endtd + fname[i] + endtd + room[i] + endtd +nights[i] + endtd + format(sub_list[i], moneyf) + endtd + format(sales_tax[i], moneyf) + endtd + format(occ_tax[i], moneyf) + endtd + format(total_list[i], moneyf) + endtr)

    f.write("<tr><td colspan=6> Grand Total:")
    f.write("<td colspan=2>"+ format(grand, moneyf) + endtr)
    f.write('</table>')
    f.write('</body>\n</html>')
    f.close()
    print("ok?")
######################      call on main program to execute ######################

main()



