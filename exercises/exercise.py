# class Tanvir:
#     def __init__(self, name, age, height, money, weight, address, university, tuition_fees):
#         self.name = name
#         self.age = age
#         self.height = height
#         self.money = money
#         self.weight = weight
#         self.address = address
#         self.university = university
#         self.tuition_fees = tuition_fees
#
#     def status(self):
#         print(f"name: {self.name}, age: {self.age}, height: {self.height}, balance: {self.money}, weight: {self.weight}, address: {self.address}")
#
#     def accelarate(self):
#         if self.money <= 0:
#             self.money += 100
#         return
#
#     def money_check(self):
#         if self.money > 10000000:
#             print(f"{self.name} peisa hu to kya kuch nehi huta, sahi khel gya behenchod")
#         elif self.money < 100000:
#             print(f"{self.name} koye bat nehi seh lenge thora sa")
#         return
#
#     def check_height(self):
#         if self.height > 6:
#             print(f"{self.name} chutiya motherchod, behenke lowre")
#         return
#
#     def university_check(self):
#         if self.university == "Metropolia UAS" and self.tuition_fees == 11000:
#             print(f"oww {self.name} your'e IT student here nice, then you love coding right? ")
#
#     def fitness_check(self):
#         if self.weight > 80:
#             print(f"{self.name} abhi fitness par dhyan de behenchod, thoda kam kha")
#         elif self.weight < 60:
#             print(f"{self.name} kya itna patla hai? Khana kha bhai!")
#             return
#
#     def age_check(self):
#         if self.age < 25:
#             print(f"{self.name} abhi jawan hai, aur kuch kar sakta hai")
#         elif self.age > 30:
#             print(f"{self.name} abhi settle hone ka time hai")
#         return
#     def financial_plan(self):
#         if self.money > 10000000:
#             print(f"{self.name} tu millionaire hai, abhi business kar behenchod")
#         elif self.money < 100000:
#             print(f"{self.name} paisa kama le thoda, savings kar")
#             return
#
# tanvir = Tanvir("tanvir", 20, 5.11, 0, 76, "kilonrinne 10F 127", "Metropolia UAS", 11000)
# ahmed = Tanvir("ahmed", 24, 6.5, 99999999999999999, 72, "kilonrinne 10D 100", "Metropolia UAS", 11000)
# ayush = Tanvir("ayush", 28, 5.5, 99999, 68, "ki 10D 100", "Metropolia UAS", 11000)
# rohit = Tanvir("rohit", 30, 5.9, 500000, 85, "India", "IIT Delhi", 20000)
# sharma = Tanvir("sharma", 35, 6.0, 20000, 95, "Mumbai", "IIM Bangalore", 15000)
#
# def check_all():
#     for person in [tanvir, ahmed, ayush, rohit, sharma]:
#         person.accelarate()
#         person.status()
#         person.money_check()
#         person.university_check()
#         person.check_height()
#         person.fitness_check()
#         person.age_check()
#         person.financial_plan()
#
# def extended_check():
#     tanvir.accelarate()
#     tanvir.status()
#     tanvir.money_check()
#     tanvir.university_check()
#     tanvir.check_height()
#     tanvir.fitness_check()
#     ahmed.accelarate()
#     ahmed.status()
#     ahmed.money_check()
#     ahmed.university_check()
#     ahmed.check_height()
#     ayush.accelarate()
#     ayush.status()
#     ayush.money_check()
#     ayush.university_check()
#     ayush.check_height()
#     rohit.accelarate()
#     rohit.status()
#     rohit.money_check()
#     rohit.university_check()
#     rohit.check_height()
#     sharma.accelarate()
#     sharma.status()
#     sharma.money_check()
#     sharma.university_check()
#     sharma.check_height()
#
# def main():
#     while True:
#         ask = input("Ha ha you're here to know information about my students nice nice then say the secret code now!: ").lower()
#         secret_code = "bsdk"
#         if ask == secret_code:
#             extended_check()
#         elif ask.isdigit():
#             print("Kya motherchud pi kar aya ha kya thik se bol nehi to ma chud dunga")
#         else:
#             print("pakar behenchod, MOTHERCHUD. MA CHUD DE ISKE")
#
# main()
import requests
















