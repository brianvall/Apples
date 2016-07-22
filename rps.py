from random import choice
print "Hi my name is Brian tha Rap Gawd. Let's play rock, paper, scisors!"
def rock_paper_scissors (User_Choice,user_score, CPU_score):
	CPU_Choice =choice ("rps")
	print "Your move is " + User_Choice + ", I play " + CPU_Choice
	if User_Choice == CPU_Choice:
		print "Tie!"
		return (user_score, CPU_score)
	elif (User_Choice == "p" and CPU_Choice == "r") or (User_Choice == "s" and CPU_Choice == "p") or (User_Choice == "r" and CPU_Choice == "s"): 
		print "YOU WIN!"
		return (user_score +1, CPU_score)
	else: 
		print "YOU LOSE!"
		return (user_score, CPU_score + 1)
x = 0
y = 0 
User_Choice = raw_input ("Make your move (r,p,s or q for quit) >>") 
while User_Choice != "q": 
	x, y = rock_paper_scissors (User_Choice,x, y)
	print str(x) + ":" + str(y)
	User_Choice = raw_input ("Make your move (r,p,s or q for quit) >>") 

