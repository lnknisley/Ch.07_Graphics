import arcade
import random

from pymunk.examples.constraints import screen

view_width, view_height = int(1.5 * 640), int(1.5 * 480)
arcade.open_window(view_width, view_height, "Corn")
arcade.set_background_color(arcade.color.CORN)
pos_x, pos_y = view_width * 0.5, view_height * 0.5

arcade.start_render()
picture = arcade.load_texture("LoganKnisley.png", 0, 0, 778, 1038, False, False, False, True, None, None, 0)
arcade.draw_texture_rectangle(view_width / 2, view_height / 2, view_width, view_height, picture, 0, 255)

arcade.finish_render()

arcade.run()