from turtle import *
import time
#cor do fundo
bgcolor('black')
right(90)
#espassamento da letra N
pos = [(-40, 0 ), (40, 0)]

for x , y in pos:
    up()
    goto(x,y)
    down()
    fillcolor('red')
    begin_fill()
    for i in range(2):
        forward(200)
        left(90)
        forward(48)
        left(90)
    end_fill()
up()
goto(-40,0)
down()
begin_fill()
left(22)
for i in range(2):
        forward(217)
        left(68)
        forward(48)
        left(112)
end_fill()
time.sleep(10)