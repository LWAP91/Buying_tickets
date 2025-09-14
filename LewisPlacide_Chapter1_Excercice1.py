
    
# Defining the function that handles buying tickets
def buying_tickets(tickets_left):
    
# Asking each buyer for tickets needed and return how many were purchased
    tickets_needed = int(input("Could you tell me how  many tickets do you want to buy ? "))
    
# Etablishing the rules for selling tickets using conditional statements
    if tickets_needed > 4:
        print("You cannot buy more than 4 tickets.")
        return 0
    elif tickets_needed > tickets_left:
        print(" unfortunately, only", tickets_left, " ticket(s)remain(s).")
        return 0
    else:
        print("Great! Thank you for your purchase")
        return tickets_needed

# Defining the main function 
def main():

# Calling tickets_left the quantity ticket left to sell after each purchase
    tickets_left = 10

# Initializing a variable accumulator to keep track of the number of buyers
    Purchaser = 0

# Applying a loop to stop selling when the tickets_left reaches 0

    while tickets_left > 0:

# Calling tickets_bought the number of tickets purchased by the current buyer
        tickets_bought = buying_tickets(tickets_left)
        
# Using an if statement to check whether the purchase is successful
        if tickets_bought > 0:

# Updating the number of ticket left and the buyers count after each purchase
            tickets_left -= tickets_bought
            buyers += 1

# Displaying the remaining tickets after each purchase
            print("The remaining tickets are:",tickets_left)
            
# Notifying when tickets have run out using an conditional statement
            if tickets_left == 0:
                print(" All tickets are sold out. No more tickets can be pursached.")

# Displaying the total of buyers after all tickets run out
    print("Total buyers:", buyers)
    
# Run the program
main()


