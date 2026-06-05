#Vamos começar pelos inputs

#Inputs necessários
num_split = int(input("How many people are? "))

#Sub-divisões da conta
appetizers = int(input("Insert the total value of the appetizers: "))
main_courses = int(input("Insert the total value of the main courses: "))
drinks = int(input("Insert the total value of the drinks: "))
desserts = int(input("Insert the total value of the desserts: "))
tip = int(input("Insert the total value of the tip: "))
total_bill = appetizers + main_courses + drinks + desserts
print(f"Total of the bill: ${total_bill}")

#Adição de gorjeta
tip_percentage = tip / 100
total_tip = total_bill * tip_percentage
print(f"Total tip: ${total_tip}")

#Divisão da conta
total_person = total_tip / num_split
print(f"Total per person: ${total_person}")