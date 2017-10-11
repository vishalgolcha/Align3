import sys 
import turtle_integrate as ti 


sys.stdout.write("Welcome to Align3\n 2.Show game Grid .\n\
 0.Play with minimax \n 1.Play with alpha beta minimax . \n 3. Analyze .\n 4.Exit")

print "\n"
chosen = sys.stdin.readline()
while int(chosen)!=4 :
	if int(chosen)==1:
		ti.play_game(1)
	# print "\n"
	# ti.oc = ti.oc+1;
	chosen = sys.stdin.readline()
	