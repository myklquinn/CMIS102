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
CONFIRM_RESP = ["Y", "y", "Yes", "yes"]


# define console clearing function
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


# define function to display movie names and showtimes
def movie_list():
    i = 1
    for x in MOVIES_SHOWING:
        print(i, "-", x["name"])
        i += 1


def showtime_list(n):
    i = 1
    print("\n---Please select a showtime.---")
    print(MOVIES_SHOWING[n]["name"])
    print("0 - Go Back")
    for x in MOVIES_SHOWING[n]["showtimes"]:
        print(i, "-", x)
        i += 1


def calc_price(n, t):
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
    print("\n---", name, "@", time, "---")
    print("Adults: $" + str(price_adult))
    print("Child (12 and under): $" + str(price_child))
    print("Senior (65 and older): $" + str(price_senior))
    adult_tickets = is_number("How many adult tickets? ")
    child_tickets = is_number("How many child tickets? ")
    senior_tickets = is_number("How many senior tickets? ")
    adult_total = adult_tickets * price_adult
    child_total = child_tickets * price_child
    senior_total = senior_tickets * price_senior
    total_price = adult_total + child_total + senior_total
    print("\nYour total price is $" + str(total_price))
    complete_purchase = input("Do you want to complete your purchase? (y/n) ")
    if complete_purchase in CONFIRM_RESP:
        clear()
        print("\n---Receipt---")
        print("Movie: ", name)
        print("Adult Tickets: " + str(adult_tickets) + " @ " + str(price_adult) + "/ea - $" + str(adult_total))
        print("Child Tickets: " + str(child_tickets) + " @ " + str(price_child) + "/ea - $" + str(child_total))
        print("Senior Tickets: " + str(senior_tickets) + " @ " + str(price_senior) + "/ea - $" + str(senior_total))
        print("Total price: $" + str(total_price))
        print("Thank you for your purchase. Enjoy your movie.")
        new_purchase = input("----------\nWould you like to make another purchase? ")
        if new_purchase in CONFIRM_RESP:
            clear()
            user_interact()
        else:
            clear()
            print("\n\nThank you, goodbye.")
    else:
        print("\nWhat would you like to do?")
        print("1 - Start over.")
        print("2 - Reenter ticket selection.")
        user_choice = is_number("Next: ")
        if user_choice == 1:
            user_interact()
        else:
            calc_price(n, t)


def user_interact():
    print("Welcome to the Rio River Cinema 5")
    print("\n---Please select a movie to see the showtimes.---")
    movie_list()
    movie_picked = is_number("Which movie do you want to see? ")
    clear()
    showtime_list(movie_picked - 1)
    showtime_picked = is_number("Showtime: ")
    clear()
    if showtime_picked != 0:
        calc_price(movie_picked - 1, showtime_picked - 1)
    else:
        user_interact()


# print welcome message and start user interaction chain
clear()
user_interact()
