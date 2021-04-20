p=input("enter your name: ")
import turtle
import random 
import time
import MySQLdb as mys
con=mys.connect(host="localhost",user='root',passwd='235489',database='snakes')
if con.is_connected:
    print("Connection established with database successfully")
    print("Starting Game")
mycursor=con.cursor()




d=0.03

body=[]
sc = 0 
hsc = 0

#Screen
w=turtle.Screen()
w.bgcolor('Orange')
w.setup(width=900,height=600)
w.tracer(0)
w.title("Snake")

#snake head
h=turtle.Turtle()
h.color("Black")
h.shape("square")
h.penup()
h.goto(0,0)
h.speed(0)
h.direction='stop'

#Snake food
food=turtle.Turtle()
food.color("Blue")
food.shape("circle")
food.penup()
food.goto(100,0)
food.speed(0)

#pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("White")
pen.penup()
pen.hideturtle()
pen.goto(-430,260)
pen.write("Score= 0  High Score= 0",align="left",font=("arial",20))




def up():
    if h.direction!='down':
        h.direction="up"
def down():
    if h.direction!='up':
        h.direction="down"
def left():
    if h.direction!='right':
        h.direction="left"
def right():
    if h.direction!='left':
        h.direction="right"


def move():
    if h.direction == "up":

        h.sety(h.ycor()+10)
    if h.direction == "down":

        h.sety(h.ycor()-10)
    if h.direction == "left":

        h.setx(h.xcor()-10)
    if h.direction == "right":

        h.setx(h.xcor()+10)
    
w.listen()
w.onkeypress(up,"Up")
w.onkeypress(down,"Down")
w.onkeypress(left,"Left")
w.onkeypress(right,"Right")

while True:
    w.update()
    if h.distance(food)<10:
        #moving food to a random position
        food.goto(random.randint(-410,410),random.randint(-250,250))

        sc+=5
        if 1>0:
            t_hsc=mycursor.execute("SELECT MAX(score) FROM score")
            res=mycursor.fetchall()
            for i in res:
                hsc=i[0]
        pen.clear()
        pen.write("Your Score= {}  Previous High Score= {}".format(sc,hsc),align="left",font=("arial",20))
       
                  
        body_p=turtle.Turtle()
        body_p.shape("circle")
        body_p.color("Silver")
        body_p.penup()
        body.append(body_p)
       
     
    
    for i in range(len(body)-1,0,-1):
        x=body[i-1].xcor()
        y=body[i-1].ycor()
        body[i].goto(x,y)
       
    #move body 0 to head
    if len(body) > 0:
        
        body[0].goto(h.xcor(),h.ycor())
    
    #Border Collision
    if h.xcor()<-440 or h.xcor()>440 or h.ycor()<-290 or h.ycor()>290:
        sql =("INSERT INTO score (NAME,score) VALUES ('{}',{})".format(p,sc))

        mycursor.execute(sql)

        con.commit()
        time.sleep(1)
        h.goto(0,0)
        h.direction='stop'
    
        sc=0
        pen.clear()
        pen.write("Score= {} Previous High Score= {}".format(sc,hsc),align="left",font=("arial",20))
        
        for i in body:
            i.goto(1000,1000) 
        body.clear()
        
   
    move()

    #Body Collision
    for i in body:
        if h.distance(body_p)<10:
            sql =("INSERT INTO score (NAME,score) VALUES ('{}',{})".format(p,sc))
            mycursor.execute(sql)

            con.commit()
            time.sleep(1)
            h.goto(0,0)
            h.direction='stop'
            sc=0
            pen.clear()
            pen.write("Score= {}  High Score= {}".format(sc,hsc),align="left",font=("arial",20))

            for i in body:
                i.goto(1000,1000) 
            body.clear()
          

    time.sleep(d)


w.mainloop()

