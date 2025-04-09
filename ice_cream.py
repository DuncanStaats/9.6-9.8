from restaurant import Restaurant
from user import User


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name: str, cuisine_type: str, flavors) -> None:
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self) -> None:
        print(f"{self.restaurant_name} offers the following {self.cuisine_type} flavors:")
        for flavor in self.flavors:
            print(f"{flavor}")

class Privileges():

    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self) -> None:
        print("Privileges:")
        for privilege in self.privileges:
            print(f"{privilege}")

class Admin(User):
    def __init__(self, first_name: str, last_name: str, age: int, sex: str, height: int, privileges):
        super().__init__(first_name, last_name, age, sex, height)
        self.privileges = Privileges(privileges)

def main():

    ice_cream_stand = IceCreamStand("Suuupppper Scoops", "Ice Cream", ["Vanilla", "Chocolate", "Strawberry"])
    ice_cream_stand.display_flavors()
    print()
    admin1 = Admin("Bird", "Larry", 35, "Male", 66, ["can add post", "can delete post", "can ban user"])
    admin1.privileges.show_privileges()
    print()
    admin2 = Admin("Jordan", "Micheal", 40, "Male", 70, ["can add post", "can delete post", "can ban user"])
    admin2.privileges.show_privileges()


if __name__ == "__main__":
    main()

