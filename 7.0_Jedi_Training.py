# 7.0 Jedi Training (20pts)  Name: Logan Knisley

'''
1. TEST PICTURE  (10pts)
------------------------
Recreate, exactly the Test Picture from the website. The arcade colors used in this picture in no particular order are:
BLACK, ALMOND, PHLOX, BLUSH, RED, BLUE, WISTERIA, AMBER, BRICK_RED and YELLOW.
The picture is 500px wide and 400px tall. Look up ARC in the documentation to do the PAC-MAN.
Upload your code and a screenshot of your picture.
'''

import arcade
from arcade import draw_rectangle_filled, draw_text

view_width, view_height = 500, 400
arcade.open_window(view_width, view_height, "Ch. 07")
arcade.set_background_color(arcade.color.ALMOND)

arcade.start_render()

for i in range(0, 500, 20):
    arcade.draw_line(0, i, view_width, i, arcade.color.BLACK, 1)
    arcade.draw_line(i, 0, i, view_height, arcade.color.BLACK, 1)
arcade.draw_rectangle_filled(50, 350, 60, 20, arcade.color.PHLOX, 0)
arcade.draw_rectangle_filled(200, 260, 40, 20, arcade.color.BLUSH, 315)
arcade.draw_ellipse_filled(100, 100, 120, 40, arcade.color.AMBER, 0, 64)
arcade.draw_circle_filled(view_width * 0.5, view_height * 0.5, 40, arcade.color.WISTERIA, 0, 64)
arcade.draw_line(80, 20, 120, 60, arcade.color.BLUE, 1)
arcade.draw_point(460, 10, arcade.color.RED, 5)
arcade.draw_text("I love you. I know.", 20, 160, arcade.color.BRICK_RED, 20, 0, "left", "arial", False, False, "left", "baseline", False,0)
arcade.draw_arc_filled(400, 320, 120, 120, arcade.color.YELLOW, 60, 360, 330, 64)
arcade.finish_render()
arcade.run()

'''
2. FLAG CREATION  (10pts)
---------------
Make your flag 260 pixels tall
Use the scaling image on the website to determine other dimensions
The hexadecimal colors for the official flag are red: #BF0A30 and blue: #002868
Title the window, "The Stars and Stripes"
You can use a draw_text command and used 20 pt. asterisks for the stars.
Can you use <20 lines of code?
CHALLENGE: Can you make the entire flag parametrically? This means if I change the hoist to 520px the flag will resize accordingly.
Upload your code and a screenshot of your flag.
'''

view_height = 260
view_width, prop_height = int(view_height * 1.9), 1/13 * view_height
arcade.open_window(view_width, view_height, "The Stars and Stripes")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()
for i in range(13):
    if i % 2 == 0:
        arcade.draw_line(0, i * prop_height + (prop_height * 0.5), view_width, i * prop_height + (prop_height * 0.5), (191, 10, 48), prop_height)
    else:
        continue
arcade.draw_rectangle_filled(0.38 * view_height, 10 * prop_height - (prop_height * 0.5), 0.76 * view_height, 7 * prop_height, (0, 40, 104), 0)
for i in range(9):
    if i % 2 == 0:
        for j in range(6):
            draw_text("*", 0.063 * view_height + (j * 0.126 * view_height), view_height - (0.108 * view_height) - (i * 0.054 * view_height), arcade.color.WHITE, 20 * (view_height/260), int(14 * view_width), "left", "arial", False, False, "center", "baseline", False, 0)
    else:
        for j in range(5):
            draw_text("*", 0.126 * view_height + (j * 0.126 * view_height), view_height - (0.108 * view_height) - (i * 0.054 * view_height), arcade.color.WHITE, 20 * (view_height/260), int(14 * view_width), "left", "arial", False, False, "center", "baseline", False, 0)
arcade.finish_render()
arcade.run()
