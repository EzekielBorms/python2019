import turtle 

yeet = turtle.Turtle()

turtle.tracer(3)

yeet.pencolor("blue")

def square(t,length):
	for side in range(0,4):
		t.forward(length)
		t.right(90)
		
def firstturtle():
	hi = turtle.Screen()
	hi.setup(1080, 700)
	hi.clear()
	hi.bgcolor("black")
	tut = turtle.Turtle()
	tut.penup()
	x = -100
	y = 0
	count = 0
	tut.color("red")
	while (count < 10):
		tut.goto(x,y)
		tut.pendown()
		square(tut,50)
		count = count + 1
		x = x - 10
		y = y + 10
		if (count < 9):
			tut.color("purple")
		print(x,y,count)
		if (count < 8):
			tut.color("blue")
		print(x,y,count)
		if (count < 7):
			tut.color("green")
		print(x,y,count)
		if (count < 5):
			tut.color("yellow")
		print(x,y,count)
		if (count < 3):
			tut.color("orange")
		print(x,y,count)
	hi.exitonclick()
	
for i in range(45):
	yeet.penup()
	yeet.pensize(10)
	yeet.goto(300,0)
	yeet.pendown()
	
	yeet.width(10)
	yeet.forward(200)
	yeet.left(100)
	yeet.forward(160)
	yeet.right(80)
	yeet.forward(30)
	yeet.right(70)

yeet.pencolor("red")

for i in range(45):
	yeet.penup()
	yeet.pensize(10)
	yeet.goto(-300,0)
	yeet.pendown()
	
	yeet.width(10)
	yeet.forward(200)
	yeet.left(100)
	yeet.forward(160)
	yeet.right(80)
	yeet.forward(30)
	yeet.right(70)	

yeet.pencolor("#f1cd9b")
for i in range(1):
	yeet.penup()
	yeet.goto(-400,-400)
	yeet.pendown()
	
	yeet.left(180)
	yeet.forward(50)
	yeet.right(25)
	yeet.forward(50)
	yeet.left(25)
	yeet.forward(550)
	yeet.left(25)
	yeet.forward(50)
	yeet.right(25)
	yeet.forward(50)
	
for i in range(1):
	yeet.penup()
	yeet.goto(-10,0)
	yeet.pendown()
	
	yeet.right(45)
	yeet.forward(50)
	yeet.right(25)
	yeet.forward(50)
	yeet.right(15)
	yeet.forward(50)
	yeet.right(2)
	yeet.forward(50)
	yeet.right(93)
	yeet.forward(100)
	yeet.right(102)
	yeet.forward(185)
	yeet.left(102)	
	
yeet.pencolor("black")
yeet.begin_fill()

if yeet.begin_fill():
	yeet.fillcolor("black")
else:
	yeet.pensize(2)

for i in range(1):
	yeet.penup()
	yeet.goto(-450,325)
	yeet.pendown()
	
	yeet.right(180)
	yeet.forward(350)
	yeet.left(90)
	yeet.forward(150)
	yeet.right(90)
	yeet.forward(200)
	yeet.right(90)
	yeet.forward(150)
	yeet.left(90)
	yeet.forward(350)
	yeet.right(90)
	yeet.forward(50)
	yeet.right(90)
	yeet.forward(950)
	yeet.right(90)
	yeet.forward(50)
	yeet.right(90)
	yeet.forward(50)

yeet.end_fill()

turtle.update()

def main():
	firstturtle()
	
if __name__ =='__main__':
	main()

turtle.done()
