"""
Extended person

Program prints the information of the class Person. Class represents an
electric wallet and object has a type Person. Object has a name, money and
address. Money can be added and removed from the wallet and the address can be
changed.

Writer of the program: EILeh

"""


class Person:
    """
    This class models a person with a simple electronic wallet.
    """

    def __init__(self, name, initial_money, move):
        """
        A person object is initialized with the name and
        the initial amount of money in the wallet.

        :param name: str, the name of the person whose
            spending the object is following.
        :param initial_money: float, how much money will
            there be in the wallet at the point of creation.
        """

        self.__name = name
        self.__money = initial_money
        self.__move = move

    def printout(self):
        """
        When a person's data is needed to be printed on
        screen this method will handle it. Also good
        for debugging and testing purposes.
        """

        print("—" * 25)
        print("Name:   ", self.__name)
        print("Wealth: ", self.__money)
        print("Address:", self.__move)

    def add_money(self, amount):
        """
        It is possible to add money in the electronic wallet.

        :param amount: float, the amount of money added.

        :return: True if operation successfull, False otherwise.
        """

        if amount < 0.0:
            return False
        else:
            self.__money += amount
            return True

    def make_payment(self, price):
        """
        When making a payment, money needs to be
        deducted from the person's wallet.

        :param price: float, the price of the purchase
            i.e. how much money to deduct from the wallet.
        """

        if price < 0.0:
            print("The price can't be negative.")
        elif price > self.__money:
            print("You can't afford that.")
        else:
            self.__money -= price

    def move(self, location):
        """
        When person moves to a new appartment and changes their
        address, the address can be changed as well.
        :param location: str, person's location
        :return: False if address is not given correclty
        """
        try:
            self.__move = location
        except ValueError:
            return False

def main():
    # Let's create an object of type Person, name it denzil,
    # and use to spy on Prof. Dexter's spending.
    denzil = Person("Denzil Dexter", 100.00, "320 Memorial Dr.")

    # State of Denzil
    denzil.printout()

    # Denzil moves out of a dormitory to a place of his own.
    denzil.move("20 Chestnut St.")

    # Where's Denzil after the move.
    denzil.printout()


if __name__ == "__main__":
    main()