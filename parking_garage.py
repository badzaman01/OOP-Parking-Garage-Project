from datetime import timedelta, datetime
from random import randint
from time import sleep

now = datetime.now()
time_in = now.strftime("%H:%M:%S")
# print("Current Time: ", time_in)

class ParkingGarage:
    def __init__(self, parking_spaces, available_tickets):
        self.parking_spaces = parking_spaces
        self.available_tickets = available_tickets
        self.current_ticket = {}
    
    def take_ticket(self):
        now = datetime.now()
        time_in = now.strftime("%H:%M:%S")
        print(f"You arrived at {time_in}.")
        if self.available_tickets > 0:
            global new_ticket
            new_ticket = int(input("How many tickets would you like to purchase today? "))
            ticket_num = randint(1, 101)
            self.current_ticket[ticket_num] = False
            print(f"Here is your ticket! Enjoy your stay! #{ticket_num}")
            self.available_tickets -= new_ticket
            self.parking_spaces -= new_ticket

    def show_available_spaces(self):
        print(f"There are {self.parking_spaces} parking spaces available")


    def pay_for_parking(self):
        pay = int(input("Please enter the number found on your ticket: "))
        if pay not in self.current_ticket.keys():
            print(f"Ticket #{pay} not in system. Please try again. Bozo." )
        else:
            total_amount = randint(5, 10)
            pay_now = input(f"Your total amount is ${total_amount}. Would you like to pay this now? Y/N ")
            if pay_now.lower() in ("y", "yes"):
                self.current_ticket[pay] = True
                print("Your payment is confirmed.")
            elif pay_now.lower() in ('n', 'no'):
                print("Good luck, you're stuck forever, mwahahaha!")
            else:
                print("Please pick a valid option.")
                
    def leave_garage(self):
        pay = int(input("You are now leaving the garage. Please enter the number found on your ticket to confirm payment: "))
        if pay not in self.current_ticket.keys():
            print(f"Ticket #{pay} not in system. Please try again. Bozo." )
        elif self.current_ticket[pay] == True:
            print("You have paid your ticket! Thank You! Have a nice day! Or don't. I don't care.")
        else:
            print("You haven't paid for parking yet. Don't steal.")
            ParkingGarage.pay_for_parking(self)
        self.available_tickets += new_ticket 
        self.parking_spaces += new_ticket
        
my_garage = ParkingGarage(100,100)       

def run():
    while True:
        user_input = input("""
            Welcome to our Parking Garage! We have "state of the art" parking lots here and we're not afraid to overcharge!
            Are you here to: 
            1. Purchase a parking ticket
            2. Inquire about available parking lots
            3. Pay for your ticket
            4. Leave the Parking Garage
            5. Quit/Exit
            """)
        if user_input == '5':
            print("I hope you paid for your parking while you were here, other wise we'll hunt you down")
            break
        elif user_input == '1':
            my_garage.take_ticket()
        elif user_input == '2':
            my_garage.show_available_spaces()
        elif user_input == '3':
            my_garage.pay_for_parking()
        elif user_input == '4':
            my_garage.leave_garage()
        else:
            print("Please enter a valid number item 1-5 for the list of choices available")
run()