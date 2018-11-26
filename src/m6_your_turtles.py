"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Kirsten Rockey.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()

titus = rg.SimpleTurtle('turtle')
titus.pen = rg.Pen('red', 6)
titus.speed = 20

titus.draw_circle(5)

titus.pen_up()
titus.right(90)
titus.forward(100)
titus.left(90)
titus.pen_down()
titus.draw_circle(100)

counter = 10
for k in range(2):
    titus.pen_up()
    titus.right(90)
    titus.forward(20)
    titus.left(90)
    titus.pen_down()
    titus.draw_circle(100 + counter*2)
    counter = counter + 10

jace = rg.SimpleTurtle()
jace.pen = rg.Pen('midnight blue', 6)
jace.speed = 20

jace.pen_up()
jace.left(90)
jace.forward(120)
jace.pen_down()
jace.right(90)

# jace.right(60)
# jace.forward(200)
# jace.right(120)
# jace.forward(200)
# jace.right(120)
# jace.forward(200)
# jace.pen_up()
# jace.right(60)

counter = 0
for k in range(3):
    jace.right(60)
    jace.forward(200+counter)
    jace.right(120)
    jace.forward(200+counter)
    jace.right(120)
    jace.forward(200+counter)
    jace.left(30)
    jace.pen_up()
    jace.forward(40)
    jace.right(90)
    jace.pen_down()
    counter = counter+70


window.close_on_mouse_click()

