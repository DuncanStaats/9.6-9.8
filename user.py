class User():
    def __init__(self,first_name: str, last_name: str, age: int, sex: str, height: int, login_attempts:int = 0)-> None:
        """creates a new user object

        Args:
            first_name (str): first name of person
            last_name (str): last name of person
            age (int): age of person
            sex (str): birth sex of person
            height (int): height in inches of person
            login_attempts (int): login attemps of person, default 0
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.height = height
        self.login_attempts = login_attempts

    def describe_user(self)-> None:
        """Prints a description of the person
        """
        print(f"Your name is, {self.first_name} {self.last_name} and you are {self.age} years old and are a {self.sex}. Your height is {self.height} in inches.")

    def greet_user(self)-> None:
        """Prints a greating
        """
        print(f"Hello there {self.first_name} {self.last_name}. I hope you have been well and continue to be well.")

    def increment_login_attempts(self)-> None:
        """Adds 1 to the total amount of login attemps
        """
        self.login_attempts += 1

    def reset_login_attempts(self)-> None:
        """Resets the login attemps to zero
        """
        self.login_attempts = 0