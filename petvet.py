# Name: your-name-here
# Prog Purpose: This program finds the cost of pet vaccines & medications for dogs and cats
#
# NOTE: Pet medications prescribed by licensed veterinarians are not subject to sales tax in Virginia
#
# PET CARE MEDS Pricing
# -----------------------------------
# Canine Vaccines:
#   1. Bordatella $30.00
#   2. DAPP $35.00
#   3. Influenza $48.00
#   4. Leptospirosis $21.00
#   5. Lyme Disease $41.00
#   6. Rabies $25.00
#   7. Full Vaccine Package (includes all vaccines): 15% discount
#
# Canine Heartworm Preventative Chews (price per chew; one chew per month)
#   Small dogs, Up to 25 lbs: $9.99
#   Medium-sized dogs, 26 to 50 lbs: $11.99
#   Large dogs: 51 to 100 lbs: $13.99

import datetime

# Define global variables
# Define dog prices
PR_BORD = 30
PR_DAPP = 35
PR_FLU = 48
PR_LEP = 21
PR_LYME = 41
PR_RAB = 25

PR_ALL = 0

PR_CHEWS_SMALL = 9.99
PR_CHEWS_MED = 11.99
PR_CHEWS_LARGE = 13.99

# Define global variables

# Define program functions
def main():
    more = True
    while more:
        get_user_data()
        
        if pet_type.upper() == "D":
            get_dog_data()
            perform_dog_calculations()
            display_dog_results()
        else:       
            get_cat_data()
            perform_cat_calculations()
            display_cat_results()
            
        askAgain = input("\nWould you like to process another pet (Y/N)?: ")
        if askAgain.upper() == "N":
            more = False
            print("Thank you for trusting PET CARE MEDS with your pet vaccines and medications.")

def get_user_data():
    global pet_name, pet_type, pet_weight
    pet_name = input("Pet name: ")
    pet_type = input("Is this pet a dog (D) or cat (C)?: ")
    pet_weight = input("Weight of your pet (in pounds): ")

# DOG functions
def get_dog_data():
    global pet_vax_type, num_chews
    print("\n** Dog Vaccines:")
    print("\t1. Bordatella")
    print("\t2. DAPP")
    print("\t3. Influenza")
    print("\t4. Leptospirosis")
    print("\t5. Lyme Disease")
    print("\t6. Rabies")
    print("\t7. Full Vaccine Package (includes all vaccines)")
    print("\t8. NONE")
    pet_vax = int(input("\n* Enter the vaccine number: "))

    print("\nMonthly heartworm prevention medication is recommended for all dogs.")
    heart_yesno = input("Would you like to order monthly heartworm medication for " + pet_name + " (Y/N)?: ")
    if heart_yesno.upper() == "Y":
        num_chews = input("How many heartworm chews would you like to order?: ")

def perform_dog_calculations():
    PR_ALL = PR_BORD + PR_DAPP + PR_FLU + PR_LEP + PR_LYME + PR_RAB

    if pet_vax_type == 1:
        vax_cost = PR_BORD
        vax_name = "Bordatella"

    elif pet_vax_type == 2:
        vax_cost = PR_DAPP
        vax_name = "DAPP"

    elif pet_vax_type == 3:
        vax_cost = PR_FLU
        vax_name = "Influenza"

    elif pet_vax_type == 4:
        vax_cost = PR_LEP
        vax_name = "Leptospirosis"

    elif pet_vax_type == 5:
        vax_cost = PR_LYME
        vax_name = "Lyme Diseas"

    elif pet_vax_type == 6:
        vax_cost = PR_RAB
        vax_name = "Rabies"

    elif pet_vax_type == 7:
        vax_cost = PR_ALL
        vax_name = "Full Vaccine Package (includes all vaccines)"

    elif pet_vax_type == 8:
        vax_cost = 0
        vax_name = "NONE"


def display_dog_results():
    print("DISPLAY DOGS")

# CAT functions
def get_cat_data():
    print("CAT DATA")

def perform_cat_calculations():
    print("CAT CALCS")

def display_cat_results():
    print("DISPLAY CATS")

# Call the main program to execute
main()
