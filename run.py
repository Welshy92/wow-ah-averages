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
        titansteel_str = input("Enter the price of a Titansteel Bar:\n")

        if validate_data(titansteel_str):
            update_new_prices(titansteel_str)
            break

    return titansteel_str


def get_deviate_data():
    """
    Get price figure input for a Savory Deviate Delight from the user.
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be a whole number.
    The loop will repeatedly request data, until it is valid.
    """
    while True:
        deviate_str = input("Enter the price of a Savory Deviate Delight\n")

        if validate_data(deviate_str):
            update_new_prices(deviate_str)
            break

    return deviate_str


def get_pygmy_data():
    """
    Get price figure input for a Pygmy Oil from the user.
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be a whole number.
    The loop will repeatedly request data, until it is valid.
    """
    while True:
        pygmy_str = input("Enter the price of a Pygmy Oil\n")

        if validate_data(pygmy_str):
            update_new_prices(pygmy_str)
            break

    return pygmy_str


def get_orb_data():
    """
    Get price figure input for a Frozen Orb from the user.
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be a whole number.
    The loop will repeatedly request data, until it is valid.
    """
    while True:
        orb_str = input("Enter the price of a Frozen Orb\n")

        if validate_data(orb_str):
            update_new_prices(orb_str)
            break

    return orb_str


def get_lotus_data():
    """
    Get price figure input for a Frost Lotus from the user.
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be a whole number.
    The loop will repeatedly request data, until it is valid.
    """
    while True:
        lotus_str = input("Enter the price of a Frost Lotus\n")

        if validate_data(lotus_str):
            update_new_prices(lotus_str)
            break

    return lotus_str


def get_illusion_data():
    """
    Get price figure input for a Illusion Dust from the user.
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be a whole number.
    The loop will repeatedly request data, until it is valid.
    """
    while True:
        illusion_str = input("Enter the price of a Illusion Dust\n")

        if validate_data(illusion_str):
            update_new_prices(illusion_str)
            break

    return illusion_str


def get_eternal_data():
    """
    Get price figure input for a Eternal Fire from the user.
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be a whole number.
    The loop will repeatedly request data, until it is valid.
    """
    while True:
        eternal_str = input("Enter the price of a Eternal Fire\n")

        if validate_data(eternal_str):
            update_new_prices(eternal_str)
            break

    return eternal_str


def get_frostweave_data():
    """
    Get price figure input for a Frostweave Cloth from the user.
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be a whole number.
    The loop will repeatedly request data, until it is valid.
    """
    while True:
        frostweave_str = input("Enter the price of a Frostweave Cloth\n")

        if validate_data(frostweave_str):
            update_new_prices(frostweave_str)
            break

    return frostweave_str


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


new_price_list = []


def update_new_prices(value):
    """
    Adds verified data to a list to be later appended to a new row.
    """
    new_price_list.append(int(value))
    print("Price confirmed!")


def append_new_prices(list):
    """
    Add all the new data to a new row within the price worksheet.
    """
    SHEET.worksheet("price").append_row(list)
    print("uploading new data.")
    print(list)
    print("New prices added to datasheet.")


def last_five_prices():
    """
    Collects columns of data from price worksheet, collecting
    the last 5 entries for each item and returns the data
    as a list of lists.
    """
    prices = SHEET.worksheet("price")

    columns = []
    for ind in range(1, 9):
        column = prices.col_values(ind)
        columns.append(column[-5:])

    calculate_new_averages(columns)


def calculate_new_averages(data):
    """
    Calculate the average price for each item type over the last
    5 sets on inputs, then append them to the average worksheet.
    """
    print("Calculating new average prices...\n")
    new_average_data = []

    for column in data:
        int_column = [int(num) for num in column]
        average = sum(int_column) / len(int_column)
        new_average_data.append(round(average))

    print("New averages calculated!")
    SHEET.worksheet("average").append_row(new_average_data)
    display_new_averages(new_average_data)


def display_new_averages(data):
    """
    This will display all the new price averages with the
    item name attached to it.
    """
    print("The new price averages are as follows.")
    print("Titansteel Bar:", data[0])
    print("Savory Deviate Delight:", data[1])
    print("Pygmy Oil:", data[2])
    print("Frozen Orb:", data[3])
    print("Frost Lotus:", data[4])
    print("Illusion Dust:", data[5])
    print("Eternal Fire:", data[6])
    print("Frostweave Cloth:", data[7], "\n")


def outro():
    print("###############################################")
    print("Thank you for your input. See you again soon!")
    print("Program created by Jacob Welsh.")


def main():
    """
    This will run all the required program functions
    """
    introduction()
    get_titansteel_data()
    get_deviate_data()
    get_pygmy_data()
    get_orb_data()
    get_lotus_data()
    get_illusion_data()
    get_eternal_data()
    get_frostweave_data()
    append_new_prices(new_price_list)
    last_five_prices()
    outro()


main()
