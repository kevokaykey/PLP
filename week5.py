# Assignment 1: Design Your Own Class! 🏗️

class smartPhone:
    def __init__(self, brand, model, color, storage, price):
        self.brand = brand
        self.model = model
        self.color = color
        self.storage = storage
        self.price = price

    def get_info(self):
        return f"Brand: {self.brand}, Model: {self.model}, Color: {self.color}, Storage: {self.storage}"    

    def get_discounted_price(self, discount_percentage):
        discount_amount = self.price * (discount_percentage / 100)
        return self.price - discount_amount
    
class AndroidPhone(smartPhone):
    def __init__(self, brand, model, color, storage, price, android_version):
        super().__init__(brand, model, color, storage, price)
        self.android_version = android_version

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Android Version: {self.android_version}"
    
class iPhone(smartPhone):
    def __init__(self, brand, model, color, storage, price, ios_version):
        super().__init__(brand, model, color, storage, price)
        self.ios_version = ios_version

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, iOS Version: {self.ios_version}"
    
def main():
    android_phone = AndroidPhone("Samsung", "Galaxy S21", "Phantom Gray", "128GB", 799, "11")
    iphone = iPhone("Apple", "iPhone 13", "Midnight", "128GB", 799, "15")

    print(android_phone.get_info())
    print(f"Discounted Price: ${android_phone.get_discounted_price(10):.2f}\n")

    print(iphone.get_info())
    print(f"Discounted Price: ${iphone.get_discounted_price(10):.2f}")

if __name__ == "__main__":
    main()


# Activity 2: Polymorphism Challenge! 🎭. Create a program that includes animals or vehicles with the same action (like move()). However, make each class define move() differently (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).

class animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

class dog(animal):
    def speak(self):
        print(f"{self.name} barks")

class cat(animal):
    def speak(self):
        print(f"{self.name} meows.")

class cow(animal):
    def speak(self):
        print(f"{self.name} moos.")

dog1 = dog("Buddy")
dog1.speak()
cat1 = cat("Whiskers")
cat1.speak()
cow1 = cow("Bessie")
cow1.speak()