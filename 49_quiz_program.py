questions={"What is the capital of India":"new delhi",
           "What is 10+8":"18",
           "What is the capital of Goa":"panaji",
           "Delhi is in which country":"india"}
score=0
for question,correct_ans in questions.items():
    print(question)
    ans=input("Give your answer : ").strip().lower()
    if ans==correct_ans:
        print("Correct answer !")
        score+=1
    else:
        print("Wrong answer")
print(f"Your total score is {score}")