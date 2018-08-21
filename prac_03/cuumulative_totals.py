"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = [] #add to empty array
    number_of_months = int(input("How many months? ")) #refactor variable so it does not indicate as a list

    for month in range(1, number_of_months + 1): #for loop
        income = float(input("Enter income for month {}: ".format(month))) #change to string format()
        incomes.append(income) #add values to list

    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, number_of_months + 1): # start counter at 1
        income = incomes[month - 1]
        total += income #add each variable one after the other to be cumulative
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()

#retest; still works as it should
#how to refactor? cannot refactor using selected elements