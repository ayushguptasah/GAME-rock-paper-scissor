import random
print("Winning Rules of the Rock Paper Scissor Game as Follows: \n"
								+"Rock vs Paper->Paper wins \n"
								+ "Rock vs Scissor->Rock wins \n"
								+"Paper vs Scissor->Scissor wins \n")

while True:
	print("Enter Choice \n 1. Rock \n 2. Paper \n 3. Scissor \n")
	choice = int(input("User turn: "))
	while choice > 3 or choice < 1:
		choice = int(input("Enter valid Input: "))
		
	if choice == 1:
		choice_name = 'Rock'
	elif choice == 2:
		choice_name = 'Paper'
	else:
		choice_name = 'Scissor'
		
	print("User Choice is: " + choice_name)
	print("\nNow its Computer turn: ")

	comp_choice = random.randint(1, 3)
	
	while comp_choice == choice:
		comp_choice = random.randint(1, 3)

	if comp_choice == 1:
		comp_choice_name = 'Rock'
	elif comp_choice == 2:
		comp_choice_name = 'Paper'
	else:
		comp_choice_name = 'Scissor'
		
	print("Computer Choice is: " + comp_choice_name)

	print(choice_name + " v/s " + comp_choice_name)

	if((choice == 1 and comp_choice == 2) or
	(choice == 2 and comp_choice ==1 )):
		print("<= Paper Wins =>\n ", end = "")
		result = "Paper"
		
	elif((choice == 1 and comp_choice == 3) or
		(choice == 3 and comp_choice == 1)):
		print("<= Rock Wins =>\n", end = "")
		result = "Rock"
	else:
		print("<= Scissor Wins =>\n", end = "")
		result = "Scissor"

	if result == choice_name:
		print("<== USER WIN ==>")
	else:
		print("<== COMPUTER WIN ==>")
		
	print("\nDo you want to play again? (Y/N)")
	ans = input()

	if ans == 'n' or ans == 'N':
		break

print("\nThanks for playing")
