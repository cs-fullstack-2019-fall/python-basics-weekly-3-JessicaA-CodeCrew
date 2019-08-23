
# Give the user the following options. Once the option that is selected is completed keep asking them until they hit 4 to quit:
#
# Hello, please choose one of following options:
# 1) Check balance
# 2) Add money to account
# 3) Withdraw money from account
# 4) Quit
# What will you like to do?

user_selection = -1

while user_selection !=4:
    print ('\nHello, please make a selection:  \n'
            f'1) Check balance\n'
           f'2) Add money to account\n'
           f'3) Withdraw money from account\n'
           f'4) Quit\n'
           )
    # Get the User Selection
    user_selection = int(input('What will you like to do? :  '))

    # Check the users selection

    if user_selection == 1:
        balance = 500
        print (f'Your balance is $ {balance} dollars.')

    # Once this selection is chosen, ask the user how much money they want to deposit. Update their account, then print the updated balance.
    # Example: How much would you like to deposit?
    # Example: Your account now holds $205 dollars

    elif user_selection == 2:
        user_selection2 = int(input(f'How much would you like to deposit: '))
        balance = 500
        newBalance = (balance + user_selection2)
        print (f'Your account now holds ${newBalance} dollars.')
    # Once this selection is chosen, ask the user how much money they want to withdraw. If they don't have enough money in the account, print "Insufficient funds". Otherwise, update their account, then print the updated balance.

    elif user_selection == 3:
        user_input3 = int(input(f'How much would you like to withdraw: '))
        if user_input3 > user_selection2:
            print("Insufficient Funds")

