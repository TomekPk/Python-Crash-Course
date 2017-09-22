'''
7-10. Dream Vacation: Write a program that polls users about their dream
vacation. Write a prompt similar to If you could visit one place in the world,
where would you go? Include a block of code that prints the results of the poll.
'''

question = "If you could visit one place in the world, where would you go?"
question +="\nPlease enter answer: "

answer_list = []
while True:
    answer = input(question)
    print("Your answer is: " + answer)
    answer_list.append(answer)
    repeat = input("\nWould You like to make another poll? (yes/no): ")
    if repeat.lower() == "no":
        break
    elif repeat.lower() == "yes":
        continue

print("\nPoll end. You can see Your answers below: ")
for i in answer_list:
    print("\t" + i)








