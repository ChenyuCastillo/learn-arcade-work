import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def base():
    arcade.draw_lrtb_rectangle_filled(100, 700, 400, 50, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(100, 700, 400, 100, arcade.color.GRAY)


def disco():
    arcade.draw_circle_filled(320, 250, 140, arcade.color.BLACK)
    arcade.draw_circle_filled(320, 250, 100, arcade.color.WHITE)
    arcade.draw_circle_filled(320, 250, 99, arcade.color.BLACK)






def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.BABY_PINK)
    arcade.start_render()

    base()
    disco()

    arcade.finish_render()
    arcade.run()


main()
