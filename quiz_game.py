print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Ok, Let's play!")
score = 0

answer = input("What does CPU stand for? R: ")

if answer.lower() == "central processing unit":
    print("Correct!")
    score +=1

else: 
    print("Incorrect")

answer = input("What does GPU stand for? R: ")

if answer.lower() =="graphics processing unit":
    print("Correct!")
    score +=1

else:
    print("Incorrect!")

answer = input("What does RAM stand for? R: ")
if answer.lower() == "random acess memory":
    print("Correct")
    score += 1

else:
    print("Incorrect")

answer = input("What does PSU stand for? R: ")

if answer.lower() == "power supply":
    print("Correct!")
    score +=1

else:
    print("Incorrect!")

       
print("Your total score was " + str(score) + "     correct questions")
print("That is " + str(score / 4 * 100) + "%.")