"""
Try-except block are utilized to capture invalid user entries such as strings; if-then statements are used to catch
negative numbers
"""
ERR_MSG = 'Please enter a valid amount for the meal purchase ❌'

class RestaurantMealPurchase:
    def __init__(self):
        self.__food_charge = None
        self.__tip_percentage = None
        self.__tax_percentage = None
        self.__tip_amount = None
        self.__tax_amount = None
        self.__user_charge()
        self.set_tip_tax()

    def set_tip_tax(self, tip = .18, tax = .07):
        self.__tip_percentage = tip
        self.__tax_percentage = tax
        self.__tip_amount = self.__food_charge * self.__tip_percentage
        self.__tax_amount = self.__food_charge * self.__tax_percentage

    def __user_charge(self):
        while True:
            try:
                self.__food_charge = float(input('Please enter the purchase amount: '))
                if self.__food_charge < 0:
                    print(ERR_MSG)
                else:
                    break
            except (ValueError, OverflowError):
                print(ERR_MSG)

    def get_amounts(self):
        return self.__food_charge, self.__tip_amount, self.__tax_amount

