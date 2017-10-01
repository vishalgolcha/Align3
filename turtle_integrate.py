import turtle 
import time
import align3 as game
# -----------------------
play = game.grid_create()
# ------------------------
def init_turtles (raph,donney,mikey,leo):
# 	TNMT FTW
	raph.shape("turtle")
	raph.color("blue")
	
	# mikey  = turtle.Turtle()
	mikey.shape("turtle")
	mikey.color("red")
	
	# leo    = turtle.Turtle()
	leo.shape("turtle")
	leo.color("green")

	# donney = turtle.Turtle()
	donney.shape("turtle")
	donney.color("yellow")

disp = turtle.Screen()
disp.setup (width=700, height=700)

raph   = turtle.Turtle() 
mikey  = turtle.Turtle()
leo    = turtle.Turtle()
donney = turtle.Turtle()
sensei = turtle.Turtle()

init_turtles(raph,donney,mikey,leo)
leo.speed(10)
squares=[]
square_limits=[]
def construct_square(turt):
	turt.fd(70) ;turt.lt(90)
	turt.fd(70) ;turt.lt(90)
	turt.fd(70) ;turt.lt(90)
	turt.fd(70)

def board_init():
	for j in range(4):
		for i in range(4):
			leo.pu()
			xxx=20+ (i*70) ; yyy= 20+ (j*70)
			leo.setx(xxx); leo.sety(yyy)
			leo.setheading(0)
			leo.begin_poly()
			leo.pd()
			construct_square(leo)
			leo.end_poly()
			p=leo.get_poly()
			# print p
			squares.append(p)
			square_limits.append([[xxx,xxx+70],[yyy,yyy+70]])

id_to_grid=[]
grid_to_id={}

for i in range(4):
    for j in range(4):
        id_to_grid.append([i,j])

for i in range(16):
    grid_to_id[tuple(id_to_grid[i])]=i


def draw_baseline():
	mikey.pensize(4)
	mikey.pu()
	mikey.fd(20)
	mikey.pd()
	mikey.fd(280)
	mikey.pu()
	mikey.goto(200,-250)
	mikey.pd()
	mikey.fd(30);mikey.lt(90)
	mikey.fd(30);mikey.lt(90)
	mikey.fd(30);mikey.lt(90)
	mikey.fd(30)

def fill_square(i, turt):
	turt.begin_fill()
	for tx,ty in i :
		# print tx,ty	
		turt.pu()
		turt.goto(tx,ty)

	turt.end_fill()

def board_wipe():
	for i in squares : 
		raph.begin_fill()
		for tx,ty in i:
			# for tx,ty in j:
			raph.pu()
			raph.goto(tx,ty)
		raph.end_fill()		

def printxy(x,y):
	print (x,y)

break_flag=0

def rect_chek(x,y):
	flag=1
	for j,i in enumerate(square_limits) : 
		# print i
		# print "-------------"
		if x>= i[0][0] and x<=i[0][1] and y<=i[1][1] and y>=i[1][0]:
			return j
		# raph.end_fill()	

def gotoandprint(x, y):
    if x<0:
    	break_flag =1
    leo.pu()
    gotoresult = leo.goto(x, y)
    # print squares
    marker = rect_chek(x,y)
    print marker
    fill_square(squares[marker],leo)
    fx,fy=id_to_grid[marker]
    play.perma_set(fx,fy,2)

    play.recurse(game.x,game.y,1,1,1)
    ai_marker = grid_to_id[(play.idx,play.idy)]
    fill_square(squares[ai_marker],raph)

# terminal check needed
    play.sett(play.idx,play.idy,1)
    if play.terminate(play.idx,play.idy)== True:
    	# print "1 won"
    	sensei.pu()
    	sensei.goto(-300,300)
    	sensei.pd()
    	sensei.write("computer wins", font=("Arial",30, "normal"))
    	time.sleep(10)
    	turtle.bye() #check 

    play.perma_set(play.idx,play.idy,1)
    print (play.idx,play.idy)
    
    # donney.pu()
    # donney.goto(x+50,y+60)
    print(leo.xcor(), leo.ycor())

    # leo.pd()
    return gotoresult

play.perma_set(0,2,1)
board_init()
draw_baseline()

fill_square(squares[2],raph)


disp.onscreenclick(gotoandprint)

turtle.getscreen()._root.mainloop()

# print z
print "move"
time.sleep(10)
quit()

