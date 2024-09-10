# lots_in_gram = 13.3
# pounds_in_talent = 20
# lots_per_pound = 32
#
# talents = float(input("Enter talents: "))
# pounds = float(input("Enter pounds: "))
# lots = float(input("Enter lots: "))
# total_lots = (talents * pounds_in_talent * lots_per_pound ) + (pounds * lots_per_pound ) + lots
# total_grams = total_lots * lots_in_gram
#
#
# kilograms = int(total_grams // 1000)
# grams = total_grams % 1000
# print(f"The weight in modern units: {kilograms} kilograms and {grams:.2f} grams.")
size_zander = int(input("Enter the size of zender in cm : "))
if size_zander >= 42 :
    print("fish released successfully")
else:
    print("fish released unsuccessfully")
    print(f"The fish is {size_zander:.2f} centimeters below the size limit")