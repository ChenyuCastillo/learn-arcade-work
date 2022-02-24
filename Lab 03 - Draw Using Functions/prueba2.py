import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.BABY_BLUE_EYES)
    arcade.start_render()

    arcade.finish_render()
    arcade.run()


main()
