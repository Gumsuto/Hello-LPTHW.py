types_of_people = 10
# 類型的人們 = 10
x = f"There are {types_of_people} types of people."
# x = 格式化後的他們有{types_of_people}種不同類型的人
binary = "binary"
# 二進制 = binary
do_not = "don't"
# d0_not = don't
y = f"Those who know {binary} and those who {do_not}."
# y = 格式化 那誰知道 {binary} 和那一些人 {do_not}

print(x)
# 顯示(X)
print(y)
# 顯示(Y)

print(f"I said: {x}")
# 顯示 格式化 我說 {x}
print(f"I also said: '{y}'")
# 顯示 格式化 我又說 {y}

hilarious = False
# 是不是很快樂 = 否
joke_evaluation = "Isn't that joke so funny?! {}"
# 笑話評估? = 我說的笑話真好笑,不是嗎?

print(joke_evaluation.format(hilarious))
# 顯示 Isn't that joke so funny?!False

w = "This is the left side of..."
# w = 這昆...的左邊
e = "a string with a right side."
# e = 有右側的弦

print(w + e)
# 顯示 This is the left side of... a string with a right side
