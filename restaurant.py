class Restaurant():
    def __init__(self, restaurant_name: str, cuisine_type: str) -> None:
        """Creates a new restaurant object

        Args:
            restaurant_name (str): name of resturant
            cuisine_type (str): name of cuisine
        """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0 


    def describe_restaurant(self)-> None:
        """Prints a description of the restaurant
        """
        print(f"This type of resturant is {self.restaurant_name}, and the cuisine served here is {self.cuisine_type}")

    def open_restaurant(self)-> None:
        """Prints that the resturant is open
        """
        print(f"{self.restaurant_name} is open")

    def set_number_served(self, number: int)-> None:
        """Sets the number of serverd customers at the restaurant
        """
        if number > 0:
            self.number_served += number
        else:
            print("Number served must be positive.")

    def increment_number_served(self, number: int)-> None:
        """Adds on the amount served with given amount
        """
        if number > 0:
            self.number_served += number
        else:
            print("Increment must be positive.")