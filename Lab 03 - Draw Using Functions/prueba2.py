import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def base():
    arcade.draw_lrtb_rectangle_filled(100, 700, 500, 50, arcade.color.WHITE)

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.BABY_PINK)
    arcade.start_render()

    base()

    arcade.finish_render()
    arcade.run()


main()
