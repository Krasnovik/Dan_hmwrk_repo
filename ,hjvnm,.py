import turtle
from turtle import*
m=100
speed(100)
color("black","red")
begin_fill()
for i in range(0,4):
    forward((4*5**0.5)*m)
    right(150)
    forward((4*5**0.5)*m)
    right(300)
    print(turtle.pos())
end_fill()
c=getcanvas()
count=0
for x in range((-120)*m,120*m,m):
    for y in range((-120) * m, 120 * m, m):
        h=c.find_overlapping(x,y,x,y)
        if len(h)==1 and h[0]==5:
            count+=1
print(count)




