#Stone paper scissor game
import random
print("Welcome to Stone Paper Scissor game,"
      "You will play 5 times\nSo look who is going to win more times\n The computer or You ")
list=["Stone","Paper","Scissor"]

i=0
player_counter=0
cpu_counter=0
S="Stone"
P="Paper"
C="Scissor"
print("You Have To press->\nS-->for stone\nP-->for paper\nC-->for scissor ")
print("\nPress Enter to start---->")
game_start=input()
if game_start=="" \
               "":
    while(i<5):
        i=i+1
        print("Enter your choice")
        player_choice=input()
        cpu = random.choice(list)
        if player_choice=="S" or player_choice=="s" and cpu=="Scissor":
            player_counter=player_counter+1
            print(f"Player chose {S} \tcpu choose Scissor")
            print(f"Score Player-{player_counter}\t\t\tCPU-{cpu_counter}")
        elif player_choice=="S" or player_choice=="s" and cpu=="Paper":
            cpu_counter=cpu_counter+1
            print(f"Player chose {S} \tcpu choose Paper")
            print(f"Score Player-{player_counter}\t\t\tCPU-{cpu_counter}")
        elif player_choice=="P" or player_choice=="p" and cpu=="Stone":
            player_counter = player_counter + 1
            print(f"Player chose {P} \tcpu choose Stone")
            print(f"Score Player-{player_counter}\t\t\tCPU-{cpu_counter}")
        elif player_choice=="P" or player_choice=="p" and cpu=="Scissor":
            cpu_counter = cpu_counter + 1
            print(f"Player chose {P} \tcpu choose Scissor")
            print(f"Score Player-{player_counter}\t\t\tCPU-{cpu_counter}")
        elif player_choice=="C" or player_choice=="c"and cpu=="Paper":
            player_counter = player_counter + 1
            print(f"Player chose {C} \tcpu choose Paper")
            print(f"Score Player-{player_counter}\t\t\tCPU-{cpu_counter}")
        elif player_choice=="C" or player_choice=="c" and cpu=="Stone":
            cpu_counter = cpu_counter + 1
            print(f"Player chose {C} \tcpu choose Stone")
            print(f"Score Player-{player_counter}\t\t\tCPU-{cpu_counter}")
        elif player_choice=="S" or player_choice=="s" and cpu=="Stone":
            print(f"Player chose {S} \tcpu choose Stone")
            print("This round tied")
            i=i-1
            print(f"Score Player-{player_counter}\t\t\tCPU-{cpu_counter}")
        elif player_choice=="P" or player_choice=="p" and cpu=="Paper":
            print(f"Player chose {P} \tcpu choose Paper")
            print("This round tied")
            i=i-1
            print(f"Score Player-{player_counter}\t\t\tCPU-{cpu_counter}")
        elif player_choice=="C" or player_choice=="c" and cpu=="Scissor":
            print(f"Player chose {C} \tcpu choose Scissor")
            print("This round tied")
            i=i-1
            print(f"Score Player-{player_counter}\t\t\tCPU-{cpu_counter}")
        else:
            print("invalid input")
            i=i-1
        if i==5:
            print("Results are")
            if player_counter>cpu_counter:
                print(f"Hurray!!! You win\n Score: Player-{player_counter}\t\t\t CPU-{cpu_counter}\n Thanks for playing")
            if player_counter<cpu_counter:
                print(f"\nBad luck try Again You Lose!!!\nScore:Player-{player_counter}\t\t\tcpu-{cpu_counter}")
                print("Try again\n Press Y to play again\t\t\t N to quit")
                againinp=input()
                if againinp=="y" or againinp=="Y":
                    i=0
                    player_counter=0
                    cpu_counter=0
                else:
                    i=5
else:
    print("Press Enter to start")






