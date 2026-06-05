#Vamos começar pelos inputs

#Inputs necessários
num_split = int(input("How many people are? "))

#Sub-divisões da conta
appetizers = int(input("Insert the total value of the appetizers: "))
main_courses = int(input("Insert the total value of the main courses: "))
drinks = int(input("Insert the total value of the drinks: "))
desserts = int(input("Insert the total value of the desserts: "))
tip = int(input("Insert the total value of the tip: "))

#Adição de gorjeta

total_tip = (appetizers + main_courses + drinks + desserts) * tip_percentage

#Divisão da conta
total_person = total_tip / num_split

print(total_person)
