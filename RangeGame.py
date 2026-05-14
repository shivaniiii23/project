""" Gussing Number"""
import random
print("welcome to number Gussing Game")
print("You can choose level:")
choice = input("entr the Choice (Easy/medium/difficult):").lower()
match choice:
    case "easy": 
        chance = 15
    case "medium":
        chance = 10
    case "difficult":
        chance = 5    
         
low = int(input("Enter the low Number: "))
High = int(input("Enter the Higher Number: "))
print(f"You have {chance} chances to guess the number between{low}and{High}")
num = random.randint(low,High)
count = 0
score = 100
while chance>count:
    count+=1
    guess = int(input("Enter your guess:"))
    score-=5
    if guess == num:
        print(f"correct the Number is {num}.you Guessed it in {count} attempt")
        break
    elif guess>num:
        print("Too High! Try a lower Number.")
    elif guess<num:
        print("Too Low! Try a higher Number")
    else:    
        while True:
            again = input("Do you want to play again? (yes/no): ").lower()
            if again != "yes":
                print("Thanks for playing! Goodbye")
                break   
    if count==chance//2:   
        print(f" Hint: The number is between {num-3} and {num+3}")                
if num!=guess:    
    print(f"Sorry! The number was {num}. Better luck next time.")
    
print(f"Your final score is {score}")
