# 3/21/2025
# Program 5 - Coffee shop menu calculator
# Tax rate: 6%
# ---------------------------------------------------------------------
# Variable           Type            Porpose
# ---------------------------------------------------------------------
#choose              str             gets input from user to start/end loop and choose other options from the menu
#total               float           saves the calculation done using calc_total function
#subtotal            str then float  gets input from user then saves base price
#sales_tax           float           saves the sale tax that is calculated using calc_tax function
#cost                float           saves the addition of subtotal and sales tax and return it to main function for display
#tax                 float           saves the calculation of sales_tax*6% then return it to calc_total




#defining main function
def main():
    choose="go"
    #adding a loop with X to end
    while choose != "X":
        #display output
        print("---------------------------------------------------------------------")
        print("*                       The Coffee Connection                       *")
        print("---------------------------------------------------------------------")
        print("\nC: Calculate price for coffee drink being ordered")
        print("D: Display coffee menu price information")
        print("X: Exit application")
        #ask for input from user then make a decision on what function to use based on user choice
        choose=input("\nEnter your menu selection: ")
        if choose == "C" or choose == "c":
            total = calc_total() #calls for calc_total function and saves it in total variable
            print("Total price: $",total,sep="") #printing output for user with the price of the item
            print("")
            print (input("Press Enter to return to menu.")) #asking for input to return to menu loop
        elif choose == "D" or choose== "d":
            display_menu()
        elif choose=="X":
            print("")
        else:
            print("Error: wrong input")
            print(input("Press Enter to return to menu."))#asks user for input to get back to menu loop
#defining display menu function then printing output to user
def display_menu():
    print("---------------------------------------------------------------------")
    print("*                  The Coffee Connection Menu                       *")
    print("---------------------------------------------------------------------")
    print("")
    print("All prices before tax.")
    print("")
    print("Black Coffee: $1.59 ")
    print("Cappuccino: $3.79")
    print("Latte: $2.99 ")
    print("Mocha Latte: $3.59 ")
    print("Shot of Espresso: $1.99 ")
    print("")
    print (input("Press Enter to return to menu.")) #asks user for input to get back to menu loop
def calc_total():
    subtotal=input("Enter the drink you would like to order: ((B)lack Coffee, (C)appuccino, (L)atte, (M)ocha Latte, (S)hot of Espresso: ")
    #comparing user input to get the right price
    if subtotal == "B" or subtotal =="b":
        subtotal=float("1.59") #changing variable to a float for caluclations
        sale_tax=calc_tax(subtotal) #calling calc_tax function for calculations and saving result in sales_tax variable
        cost=format(subtotal+sale_tax, '0.2f')
        return cost #returning the variable
    elif subtotal == "C" or subtotal =="c":
        subtotal=float("3.79") #changing variable to a float for caluclations
        sale_tax=calc_tax(subtotal) #calling calc_tax function for calculations and saving result in sales_tax variable
        cost=format(subtotal+sale_tax, '0.2f')
        return cost #returning the variable
    elif subtotal == "L" or subtotal =="l":
        subtotal=float("2.99") #changing variable to a float for caluclations
        sale_tax=calc_tax(subtotal) #calling calc_tax function for calculations and saving result in sales_tax variable
        cost=format(subtotal+sale_tax, '0.2f')
        return cost #returning the variable
    elif subtotal== "M" or subtotal =="m":
        subtotal=float("3.59") #changing variable to a float for caluclations
        sale_tax=calc_tax(subtotal) #calling calc_tax function for calculations and saving result in sales_tax variable
        cost=format(subtotal+sale_tax, '0.2f')
        return cost #returning the variable
    elif subtotal == "S" or subtotal =="s":
        subtotal=float("1.99") #changing variable to a float for caluclations
        sale_tax=calc_tax(subtotal) #calling calc_tax function for calculations and saving result in sales_tax variable
        cost=format(subtotal+sale_tax, '0.2f')
        return cost #returning the variable
    else:
        print("Error: wrong input")
        print(input("Press Enter to return to menu."))#asks user for input to get back to menu loop
#definigng calc_tax function and doing calculations    
def calc_tax(sales_tax):
        tax=(sales_tax*6/100) 
        return tax #returning the variable

main()

#output
##>>> 
##======== RESTART: C:\Users\taniz\OneDrive\Desktop\programs\program 5.py ========
##---------------------------------------------------------------------
##*                       The Coffee Connection                       *
##---------------------------------------------------------------------
##
##C: Calculate price for coffee drink being ordered
##D: Display coffee menu price information
##X: Exit application
##
##Enter your menu selection: d
##---------------------------------------------------------------------
##*                  The Coffee Connection Menu                       *
##---------------------------------------------------------------------
##
##All prices before tax.
##
##Black Coffee: $1.59 
##Cappuccino: $3.79
##Latte: $2.99 
##Mocha Latte: $3.59 
##Shot of Espresso: $1.99 
##
##Press Enter to return to menu.
##
##---------------------------------------------------------------------
##*                       The Coffee Connection                       *
##---------------------------------------------------------------------
##
##C: Calculate price for coffee drink being ordered
##D: Display coffee menu price information
##X: Exit application
##
##Enter your menu selection: c
##Enter the drink you would like to order: ((B)lack Coffee, (C)appuccino, (L)atte, (M)ocha Latte, (S)hot of Espresso: l
##Total price: $3.17
##
##Press Enter to return to menu.
##
##---------------------------------------------------------------------
##*                       The Coffee Connection                       *
##---------------------------------------------------------------------
##
##C: Calculate price for coffee drink being ordered
##D: Display coffee menu price information
##X: Exit application
##
##Enter your menu selection: X
##
##>>> 
