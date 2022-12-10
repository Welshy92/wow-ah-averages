import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('wow-averages')


def introduction():
    """
    This prints an introductory statement and gives a brief explaination
    of how the data should be entered by the user into the terminal.
    """
    print("Welcome to the WoW AH average price analyser.\n")
    print("You will go through 8 popular items to sell, one by one.")
    print("You will need to know the current lowest price of each item on the AH.")
    print("When asked, please enter your price in Silver. Remember 1 Gold = 100 Silver.")
    print("If the price has Copper in it, please round it to the nearest Silver.\n")


def get_titansteel_data():
    """
    Get price figure input for a Titansteel Bar from the user.
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be a whole number.
    The loop will repeatedly request data, until it is valid.
    """
    while True:
        data_str = input("Enter the price of a Titansteel Bar:\n")

        if validate_data(data_str):
            print("Data is valid!")
            break

    return data_str


def validate_data(value):
    """
    Inside the try, converts the string value into an integer.
    Raises ValueError if the string cannot be converted into int.
    """
    try:
        [int(value)]
    except ValueError as e:
        print(f"Invalid data: '{value}'. Data must be a whole number. Try again.\n")
        return False

    return True


def main():
    """
    This will run all the required program functions
    """
    introduction()
    get_titansteel_data()


main()
