import random
choices = ['rock','paper','scissors']

user_score = 0
computer_score = 0
round_number = 1

print("🎮 Welcome to Rock Paper Scissors game 🎮")

while True:
    print('Choices = rock | paper | scissors')
    user_choice = input("Enter your choice :").lower()
    if user_choice not in choices :
        print("❌Invalid choice! Try again")
        continue
    computer_choice = random.choice(choices)
    print("Computer choose:",computer_choice)
    if(user_choice == computer_choice):
        print("🙄  It's a tie")
    elif(user_choice=='rock'and computer_choice=='scissors') or (user_choice=='paper' and computer_choice =='rock') or (user_choice == 'scissors' and computer_choice=='paper'):
        print("🥳  You win this round")
        user_score += 1
    else:
        print("🥲  Computer win this round")
        computer_score += 1
    print("Score : Your score=",user_score,"|Computer score=",computer_score)
    play_again = input("Do you want to play again?(Yes/No): ").lower()
    if play_again !='yes':
        print('Total round played:',round_number)
        print("Game over!")
        break
        round_number += 1

print("Final Score:")
print("Your score :",user_score)
print("Computer score:",computer_score)
if (user_score==computer_score):
    print("🙄  It is a tie")
elif(user_score>computer_score):
    print("You win!  🥳")
else:
    print("You lost  😭")

