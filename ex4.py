cars = 100
# 一百輛汽車
space_in_a_car = 4.0
# 汽車內部的距離為4.0
drivers = 30
# 30個司機
passengers = 90
# 乘客為90人
cars_not_driven = cars - drivers
# 缺少司機的汽車車輛數目為 = 車輛 減去 司機的數目
cars_driven = drivers
# 汽車駕駛員 = 司機
carpool_capacity = cars_driven * space_in_a_car
# 合伙駕駛能力 = 汽車駕駛員 * 汽車內部的距離
average_passengers_per_car = passengers / cars_driven
# 每輛車平均乘客 = 乘客 / 汽車司機

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today")
print("We have", passengers, "to carpool today")
print("We need to put about", average_passengers_per_car, "in each car.")
