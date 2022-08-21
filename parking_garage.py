from datetime import timedelta, datetime
from random import randint
from time import sleep

now = datetime.now()
time_in = now.strftime("%H:%M:%S")
# print("Current Time: ", time_in)

class ParkingGarage:
    def __init__(self):
        self.parking_spaces = [100]
        self.available_tickets = [100]
        self.current_ticket = {}
    
    def show_available_spaces(self):
        print(f"There are {self.parking_spaces[0]} parking spaces available")
    
    def check_if_paid(self):
        ticket_input = int(input("What is the number of your ticket?"))
        for x in self.current_ticket:
            if x == ticket_input:
                if self.current_ticket[x] == True:
                    print("paid")
                elif self.current_ticket[x] == False:
                    print("not paid")
                else:
                    print("This ticket number isn't here...")

    def leave_garage(self):
        pay = int(input("You are now leaving the garage. Please enter the number found on your ticket to confirm payment: "))
        if pay not in self.current_ticket.keys():
            print(f"Ticket #{pay} not in system. Please try again. Bozo." )
        elif self.current_ticket[pay] == True:
            print(f"You have paid your ticket at! It is now {time_now}, and you are leaving the garage. Thank You! Have a nice day! Or don't. I don't care.")
        else:
            print("You haven't paid for parking yet. Don't steal.")
            ParkingGarage.pay_for_parking(self)
        self.parking_spaces[0] += new_ticket
        self.available_tickets[0] += new_ticket

class GarageTransactions(ParkingGarage):
    def take_ticket(self):
        now = datetime.now()
        global time_now
        time_now = now.strftime("%H:%M:%S")
        print(f"You arrived at {time_now}.")
        if self.available_tickets[0] > 0:
            global new_ticket
            new_ticket = int(input("How many tickets would you like to purchase today? "))
            ticket_num = randint(1, 101)
            self.current_ticket[ticket_num] = False
            print(f"Here is your ticket! Enjoy your stay! #{ticket_num}")
            self.parking_spaces[0] -= new_ticket
            self.available_tickets[0] -= new_ticket

    def pay_for_parking(self):
        pay = int(input("Please enter the number found on your ticket: "))
        if pay not in self.current_ticket.keys():
            print(f"Ticket #{pay} not in system. Please try again. Bozo.")
        else:
            total_amount = randint(0, 300)
            pay_now = input(f"Your total amount is ${total_amount}. Would you like to pay this now? Y/N ")
            if pay_now.lower() in ("y", "yes"):
                self.current_ticket[pay] = True
                print("Your payment is confirmed. You have 15 minutes to exit the premises. Or else.")
            elif pay_now.lower() in ('n', 'no'):
                print("Good luck, you're stuck forever, mwahahaha!")
            else:
                print("Please pick a valid option.")          
        
my_garage = GarageTransactions()       

def run():
    while True:
        user_input = input("""
            Welcome to our Parking Garage! We have "state of the art" parking lots here and we're not afraid to overcharge!
            Are you here to: 
            1. Purchase a parking ticket
            2. Inquire about available parking spaces
            3. Check if your ticket is paid
            4. Pay for your ticket
            5. Leave the Parking Garage
            6. Quit/Exit
            """)
        if user_input == '6':
            print("I hope you paid for your parking while you were here, other wise we'll hunt you down")
            break
        elif user_input == '1':
            my_garage.take_ticket()
        elif user_input == '2':
            my_garage.show_available_spaces()
        elif user_input == '3':
            my_garage.check_if_paid()
        elif user_input == '4':
            my_garage.pay_for_parking()
        elif user_input == '5':
            my_garage.leave_garage()
        else:
            print("Please enter a valid number item 1-5 for the list of choices available")
run()