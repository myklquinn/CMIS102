# import dependencies
import os

# define constants
TICKET_PRICE = 15
MATINEE_END = 1800
DISCOUNT_MATINEE = -6
DISCOUNT_YOUTH = -3
DISCOUNT_SENIOR = -4
SURCHARGE_3D = 3
MOVIES_SHOWING = [
    {"name": "Another Scary Movie [PG-13]", "showtimes": [1000, 1300, 1530, 1800, 2100], "3D": False},
    {"name": "Flowers (3D) [G]", "showtimes": [1100, 1445, 1810, 2200], "3D": True},
    {"name": "My Favorite Superhero (3D) [PG-13]", "showtimes": [1030, 1240, 1455, 1905, 2115], "3D": True},
    {"name": "Saving Sally [R]", "showtimes": [1200, 1500, 1930], "3D": False},
    {"name": "Windows and Mirrors [PG]", "showtimes": [1030, 1420, 1810, 2200], "3D": False},
]
RESP_CONFIRM = ["Y", "y", "Yes", "yes"]
RESP_CANCEL = ["N", "n", "No", "no"]


# define function to clear text from console window 
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# define function to error check if value entered is a number
def is_number(message):
    while True:
        customerInput = input(message)
        try:
            customerInput = eval(customerInput)
            return customerInput
            break
        except:
            print("Please enter a numerical value ")
            pass


# define function to display movie names and determine if input is valid
def movie_list():
    i = 1
    for x in MOVIES_SHOWING:
        print(i, "-", x["name"])
        i += 1
    while True:
        movie_picked = is_number("Which movie do you want to see? ")
        if movie_picked <= len(MOVIES_SHOWING) and movie_picked > 0:
            return movie_picked
            break
        else:
            print("You have made and invalid selection. Please try again.")
            pass


# define function to display movie showtimes and determine if input is valid
def showtime_list(n):
    i = 1
    print("\n---Please select a showtime.---")
    print(MOVIES_SHOWING[n]["name"])
    print("0 - Go Back")
    showtimes = MOVIES_SHOWING[n]["showtimes"]
    for x in showtimes:
        print(i, "-", x)
        i += 1
    while True:
        showtime_picked = is_number("Showtime: ")
        if showtime_picked <= len(showtimes):
            return showtime_picked
            break
        else:
            print("You have made and invalid selection. Please try again.")
            pass


# define function to collect number of tickets desired, calculate total, and confirm purchase
def complete_purchase(n, t):
    # get parameters and set ticket pricesfor selected movie and showtime
    movie = MOVIES_SHOWING[n]
    name = movie["name"]
    time = movie["showtimes"][t]
    movie_is3d = movie["3D"]
    price_adult = TICKET_PRICE
    if time < MATINEE_END:
        price_adult += DISCOUNT_MATINEE
    if movie_is3d:
        price_adult += SURCHARGE_3D
    price_child = price_adult + DISCOUNT_YOUTH
    price_senior = price_adult + DISCOUNT_SENIOR

    # collect inputs for number of desired tickets
    print("\n---", name, "@", time, "---")
    print("Adults: $" + str(price_adult))
    print("Child (12 and under): $" + str(price_child))
    print("Senior (65 and older): $" + str(price_senior))
    adult_tickets = is_number("How many adult tickets? ")
    child_tickets = is_number("How many child tickets? ")
    senior_tickets = is_number("How many senior tickets? ")

    # calculate total for customer purchase
    adult_total = adult_tickets * price_adult
    child_total = child_tickets * price_child
    senior_total = senior_tickets * price_senior
    total_price = adult_total + child_total + senior_total
    print("\nYour total price is $" + str(total_price))

    # confirm purchase and print receipt or redirect customer if they do not want to complete their purchase
    while True:
        customer_complete = input("Do you want to complete your purchase? (y/n) ")
        if customer_complete in RESP_CONFIRM:
            clear()
            print("\n---Receipt---")
            print("Movie: ", name)
            if adult_tickets > 0:
                print("Adult Tickets: " + str(adult_tickets) + " @ " + str(price_adult) + "/ea - $" + str(adult_total))
            if child_tickets > 0:
                print("Child Tickets: " + str(child_tickets) + " @ " + str(price_child) + "/ea - $" + str(child_total))
            if senior_tickets > 0:
                print("Senior Tickets: " + str(senior_tickets) + " @ " + str(price_senior) + "/ea - $" + str(
                    senior_total))
            print("Total price: $" + str(total_price))
            print("Thank you for your purchase. Enjoy your movie.")

            new_purchase()
            break
        elif customer_complete in RESP_CANCEL:
            while True:
                print("\nWhat would you like to do?")
                print("1 - Start over.")
                print("2 - Reenter ticket selection.")
                user_choice = is_number("Next: ")
                if user_choice == 1:
                    clear()
                    user_interact()
                    break
                elif user_choice == 2:
                    clear()
                    complete_purchase(n, t)
                    break
                else:
                    print("You have made and invalid selection. Please try again.")
                    pass
            break
        else:
            print("You have made and invalid selection. Please try again.")
            pass


# define function to present customer with the option to purchase more tickets
def new_purchase():
    while True:
        new_purchase = input("----------\nWould you like to make another purchase? (y/n) ")
        if new_purchase in RESP_CONFIRM:
            clear()
            user_interact()
            break
        elif new_purchase in RESP_CANCEL:
            clear()
            print("\n\nThank you, goodbye.")
            break
        else:
            print("You have made and invalid selection. Please try again.")
            pass


# set order of user interactions and collect inputs
def user_interact():
    print("Welcome to the Rio River Cinema 5")
    print("\n---Please select a movie to see the showtimes.---")
    movie_picked = movie_list()
    clear()
    showtime_picked = showtime_list(movie_picked - 1)
    clear()
    if showtime_picked != 0:
        complete_purchase(movie_picked - 1, showtime_picked - 1)
    else:
        user_interact()


# print welcome message and start user interaction chain
clear()
user_interact()
