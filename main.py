#variables
score = 0
marks = 4

# question 1
question1 = input('What is (2 x 3) + 5? ')



if question1 == '11' or question1.lower() == 'eleven':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')


# question 2

question2 = input('What is the Capital of Alberta? ')



if question2.lower() == 'edmonton':
    print('Correct!')
    score += 1
else: 
    print('Incorrect!')


# question 3

question3 = input('Who is the best coder? ')


if question3.lower() == 'elliot' or question3.lower() == 'you':
    print('Correct!')
    score += 1
else: 
    print('Incorrect!')


# question 4

question4 = input('Who is the President of the USA? ')


if question4.lower() == 'biden' or question4.lower() == 'mr. joe biden' or question4.lower() == 'joe biden':
    print(question4.lower())
    print('Correct!')
    score += 1
else:
    print('Incorrect!')


# process


percent = int((score/marks) * 100)

print('You got ', str(score),'/4 or ', str(int(percent)), '%!')

if percent > 75:
    print('Great Job!')
elif percent > 50:
    print("A litte studying wouldn't hurt. ")
elif percent > 25:
    print("I will expect better next time.")
elif percent >= 0:
    print("You need to study!")







