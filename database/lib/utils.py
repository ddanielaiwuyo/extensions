"""
Utils class
"""
class Utils:
    @staticmethod
    def get_quantity(max_choice) -> int:
        print( "  Please provide the quantity")
        while True:
            try:
                quantity = int(input(" enter: "))
                if quantity < 0 or quantity >= max_choice:
                    print(f"  Please provide choice between 1 and {max_choice}")
                    continue
                
                return quantity

            except ValueError:
                print("  Please provide a valid number")

    @staticmethod
    def get_choice(max_choice) -> int:
        while True:
            try:
                choice = int(input( "  enter: "))
                choice = choice - 1
                if choice < 0 or choice > max_choice - 1:
                    print("  Provide choice between 1 and ", max_choice)
                    continue

                return choice
            except ValueError:
                print("  Please provide a valid number")
