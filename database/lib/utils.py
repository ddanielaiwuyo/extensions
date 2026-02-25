"""
Utils class
"""
class Utils:
    @staticmethod
    def get_quantity(max_choice) -> int:
        msg = " please provide the amount you want purchase"
        print(msg)
        while True:
            try:
                quantity = int(input(" enter: "))
                if quantity < 0 or quantity >= max_choice:
                    print(f" please provide choice between 1 and {max_choice}")
                    continue

                
                return quantity

            except ValueError:
                print(" please provide a valid number")

    @staticmethod
    def get_choice(max_choice) -> int:
        while True:
            try:
                choice = int(input( " enter: "))
                choice = choice - 1
                if choice < 0 or choice > max_choice - 1:
                    print(" provide choice between 1 and ", max_choice)
                    continue

                return choice
            except ValueError:
                print(" please provide a valid number")
