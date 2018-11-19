formatter = "{} {} {} {}"# 給formatter賦值

print(formatter.format(1,2,3,4))
# 顯示 已經被程序格式化的(1,2,3,4)
print(formatter.format("one", "two", "three", "four"))
#顯示 被格式化的参數 (one ,two ,therr four)
print(formatter.format(True, False, False, True))
#顯示 被程序格式化的格式参數(True,False,False,True)
#不需要用引號是因為Trye和False是python話言中的重要参數,用來判斷是否正確,如果加上引號,就會変成字符串
print(formatter.format(formatter, formatter, formatter, formatter))
# 顯示 (formatter字符串{} {} {} {})
print(formatter.format(
  "Try your",
  "Own text here",
  "Maybe a poem",
  "Or a song about fear"
  ))
# 顯示 被格式化後的字符串Try your Own text here Maybe a poem Or a song about fear

# 1.取第1行定義的formatter字符串.
# 2.調用它的format,這相當于告訴它執行一个叫format的命令行命令
# 3.給format傳遞4个参數,這些参數和formatter変量中的{}匹配,相當于1將参數傳遞給了format這个命令
