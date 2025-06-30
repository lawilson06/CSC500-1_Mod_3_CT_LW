"""
Lawrence Wilson
CSC500-1 Module 3 Critical Thinking Assignment
June 29, 2025
"""

from time_clock import TimeClock
from restaurant_meal_purchase import RestaurantMealPurchase

# Restaurant meal purchase and 24-hour time clock objects are created and their methods are executed

new_meal_purchase_obj = RestaurantMealPurchase()
meal_amount, tip_amount, tax_amount = new_meal_purchase_obj.get_amounts()
print(f"Meal Amount: ${meal_amount:.2f}, Tip Amount: ${tip_amount:.2f}, Tax Amount: ${tax_amount:.2f}, Total Amount: $"
      f"{meal_amount + tip_amount + tax_amount:.2f}")

new_time_obj = TimeClock()
current_time, alarm_hours, alarm_out_time = new_time_obj.get_alarm_output()
print(f"Current Time: {current_time}, Alarm Hours: {alarm_hours}, Time Alarm Goes Off: "
      f"{alarm_out_time[0]} ({alarm_out_time[1]})")
