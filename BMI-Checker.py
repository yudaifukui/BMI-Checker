def bmi(height, weight):
	bmi = weight / (height * height)
	bmi = round(bmi, 1)
	return bmi

height = round(float(input("身長を入力(m ) >> ")), 2)
weight = round(float(input("体重を入力(kg) >> ")), 1)

bmi = bmi(height, weight)

print("\n<<判定結果>>")
print("----------------------------")
print("・あなたのBMI",bmi)
print("・判定")
print("・標準体重")
print("----------------------------")


result = ""
if bmi < 18.5:
    result = "やせ型"
if (18.5 <= bmi) and (bmi < 25):
    result = "標準体重"
if (25 <= bmi) and (bmi < 30):
    result = "肥満（軽）"
if bmi >= 30:
    result = "肥満（重）"

print("判定：", result)
