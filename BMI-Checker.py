height = input("身長を入力(m ) >> ")
weight = input("体重を入力(kg) >> ")

print("\n判定結果")
print(あなたのBMI)
print(判定)
print(標準体重)


result = ""
if bmi < 18.5:
    result = "やせ型"
if (18.5 <= bmi) and (bmi < 25):
    result = "標準体重"
if (25 <= bmi) and (bmi < 30):
    result = "肥満（軽）"
if bmi >= 30:
    result = "肥満（重）"
