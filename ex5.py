name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches 英寸
inches_equal_centimecer = 2.54 # 英寸轉換成厘米的系數值
height_cm = round(height * inches_equal_centimecer)
weight = 180 # lbs 磅
pounds_equal_kilogram = 0.4536 # 磅轉換成千克的系數值
weight_kg = round(weight * pounds_equal_kilogram)
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print(f"Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

print(f"He's {height_cm} centimecer tall.")
print(f"He's {weight_kg} kilogram heavy.")
print(f"He's got {eyes} eyes and {hair} hair")
print(f"his teeth are usually {teeth} depending on the coffee")
#this line is tricky, try to get it ecactly right
total = age + height_cm + weight_kg
print(f"If I add {age}, {height_cm}, and {weight_kg} i get {total}.")
