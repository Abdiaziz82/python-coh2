# print("i'm learning loops in python")
# print("i'm learning loops in python")
# print("i'm learning loops in python")
# print("i'm learning loops in python")
# print("i'm learning loops in python")

count = 10
while count > 0:
    print("i'm learning loops in python")
    count -= 1

i = 0
while i <= 10:
    print(i)
    i+=1

# number = int(input("Enter any number "))
# multiply_by = 1

# while multiply_by <= 10:
#     product = number * multiply_by
#     print(f"{number} * {multiply_by} = {product}")
#     multiply_by += 1

student_name = "sumeya"

for char in student_name:
    print(char)

for i in range(5):
    print("i'm learning loops in python")

student_scores =[30,80,50,70,90,40]
highest_score = 0 
runner_up = 0 

for score in student_scores:
    if score > highest_score:
        highest_score = score
    elif score > runner_up:
        runner_up = highest_score
        
print(f"the highest score is; {highest_score}")
print(f"the runerup score is; {runner_up}")

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)


word = ""
while word != "exit":
    word = input("type anything  ")
    if word == "exit":
        break
    else:
        print(f"you have typed {word}")

