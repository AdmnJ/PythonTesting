#!/usr/bin/env
import turtle
import tkinter

point1 = (-450, 0)
point2 = (456, 0)
point3 = (-450, 200)
point4 = (456, 200)
point5 = (-450, -200)
point6 = (456, -200)

vert1 = (0, -450)
vert2 = (0, 456)
vert3 = (200, -450)
vert4 = (200, 456)
vert5 = (-200, -450)
vert6 = (-200, 456)

turtle.penup()
turtle.goto(point1)
turtle.pendown()
turtle.goto(point2)
turtle.penup()
turtle.goto(point3)
turtle.pendown()
turtle.goto(point4)
turtle.penup()
turtle.goto(point5)
turtle.pendown()
turtle.goto(point6)
turtle.penup()

turtle.penup()
turtle.goto(vert1)
turtle.pendown()
turtle.goto(vert2)
turtle.penup()
turtle.goto(vert3)
turtle.pendown()
turtle.goto(vert4)
turtle.penup()
turtle.goto(vert5)
turtle.pendown()
turtle.goto(vert6)
turtle.penup()

tkinter.mainloop()