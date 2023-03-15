print("Welcome to the VBR's Master Mind Quiz")

playing = input("Continue? (type y: to continue or any other key to terminate)")

if playing.lower()!='y':
    quit()

else :
    print("Okay! Let's play! \n")

i=0

answer=input("Q1. What is the national animal of India? ")
if answer.lower()=='tiger':
    print("Correct answer\n")
    i+=1
else :
    print("Wrong answer\n")

answer=input("Q2. What is the national fruit of India? ")
if answer.lower()=='mango':
    print("Correct answer\n")
    i+=1
else :
    print("Wrong answer\n")

answer=input("Q3. What does RCB(IPL team) stand for? ")
if answer.lower()=='royal challengers bangalore':
    print("Correct answer\n")
    i+=1
else :
    print("Wrong answer\n")

answer=input("Q4. What is the national bird of India? ")
if answer.lower()=='peacock':
    print("Correct answer\n")
    i+=1
else :
    print("Wrong answer\n")


print("you scored " +str(i)+" out of 4")
print("That means you scored " +str((i/4)*100)+ "%")