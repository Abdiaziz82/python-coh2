# # print("i'm learning loops in python")
# # print("i'm learning loops in python")
# # print("i'm learning loops in python")
# # print("i'm learning loops in python")
# # print("i'm learning loops in python")

# count = 10
# while count > 0:
#     print("i'm learning loops in python")
#     count -= 1

# i = 0
# while i <= 10:
#     print(i)
#     i+=1

# number = int(input("Enter any number "))
# multiply_by = 1

# while multiply_by <= 10:
#     product = number * multiply_by
#     print(f"{number} * {multiply_by} = {product}")
#     multiply_by += 1

# student_name = "sumeya"

# for char in student_name:
#     print(char)

# for i in range(5):
#     print("i'm learning loops in python")

# student_scores =[30,80,50,70,90,40]
# highest_score = 0 
# runner_up = 0 

# for score in student_scores:
#     if score > highest_score:
#         highest_score = score
#     elif score > runner_up:
#          runner_up = highest_score
         
# print(f"the highest score is; {highest_score}")
# print(f"the runerup score is; {runner_up}")

# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(i)


# word = ""
# while word != "exit":
#     word = input("type anything  ")
#     if word == "exit":
#         break
#     else: 
#         print(f"you have typed {word}")


prices = [200,300,400,600,700]
print(type(prices))
print(dir(prices))
prices.append(9000)
prices.insert(1,80)
prices.sort(reverse=True)

print(prices)


fruits = ("apple" ,"banana" ,"mango" )
print(dir(fruits))
print(fruits.index("apple"))
print (fruits.count("banana"))

prices_in_usd = [100,200,300,400,500]
# prices_in_Ksh =[]

# for price in prices_in_usd:
#     final_price = price * 129
#     prices_in_Ksh.append(final_price)

# print(prices_in_Ksh)



students = ["Kasim" ,"Abdi" ,"Hibo" ,"Ali"]
student_emails =[]

for student in students:
    if student != "Hibo":
        email = student + "@gau.ac.ke" 
        student_emails.append(email)

print(student_emails)


# #list comprehension
prices_list =[price * 129 for price in prices_in_usd]
print(prices_list)

students = ["Kasim" ,"Abdi" ,"Hibo" ,"Ali"]
student_emails =[student + "@gau.ac.ke" for student in students if student == "Kasim" ]
print(student_emails)