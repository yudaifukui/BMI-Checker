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


