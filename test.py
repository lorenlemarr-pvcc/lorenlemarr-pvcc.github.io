cust = []
name = []
room = []
number = []

def main():
    read_in_emerald_file()
    perform_calculations()
    
def read_in_emerald_file():
    cust_data = open("emerald.csv","r")
    cust_in = cust_data.readlines()
    cust_data.close()

  #split the data into fields
    for i in cust_in:
        cust.append(i.split(","))
def perform_calculations():
    for i in range(len(cust)):
            amt_owed = float(cust[i][2])*1.10
            total += amt_owed
            print(cust[i][1] + "   \t" + cust[i][0]+"\t"+format(amt_owed.fcurrency))
