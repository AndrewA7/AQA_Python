class Human:
    def __init__(self, name: str, surname: str, age: int, phone: int, address: str):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone = phone
        self.address = address

    def get_info(self):
        return self.__dict__

    def call(self, phone_number):
        return f"{self.phone} вызывает абонента {phone_number}"


svarog = Human("Svarog", "Borysovych", 32, 380991234567, "Hoverla mount. 35")
perun = Human("Perun", "Vasyliovych", 40, 380991234545, "Petros mount. 14")
dashboh = Human("Dashboh", "Oleksandrovych", 28, 380998765432, "Dragobrat sq. 25")
