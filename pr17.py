# Write a program in python to implement Railway Reservation System using file handling technique.System should perform below operations.
#a. Reserve a ticket for a passenger.
#b. List information all reservations done for today’s trains.
#(Note: Use of object oriented paradigm is compulsory.)


import datetime

class TrainReservationSystem:
    def __init__(self, trains_file='trains.txt', reservations_file='reservations.txt'):
        self.trains_file = trains_file
        self.reservations_file = reservations_file

    def reserve_ticket(self, train_no, passenger_name):
        with open(self.reservations_file, 'a') as file:
            file.write(f"{train_no},{passenger_name},{datetime.datetime.now()}\n")

    def list_reservations_for_today(self):
        today = datetime.date.today()
        with open(self.reservations_file, 'r') as file:
            for line in file:
                train_no, passenger_name, reservation_date = line.strip().split(',')
                reservation_date = datetime.datetime.strptime(reservation_date, '%Y-%m-%d %H:%M:%S.%f').date()
                if reservation_date == today:
                    print(f"Train Number: {train_no}, Passenger Name: {passenger_name}, Reservation Date: {reservation_date}")

# Create an instance of TrainReservationSystem
reservation_system = TrainReservationSystem()

# Reserve a ticket
train_no = input("Enter Train Number: ")
passenger_name = input("Enter Passenger Name: ")
reservation_system.reserve_ticket(train_no, passenger_name)
print("Ticket reserved successfully.")

# List information about all reservations done for today's trains
print("Reservations for Today's Trains:")
reservation_system.list_reservations_for_today()
