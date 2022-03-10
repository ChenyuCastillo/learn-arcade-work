import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

    def on_draw(self):
        # color de fondo de nuestra ventana
        arcade.set_background_color(arcade.color.BABY_BLUE)

        arcade.start_render()

        # creación del sol
        arcade.draw_circle_filled(725, 525, 50, arcade.color.ORANGE)

        # creación del suelo donde se apoya la casa
        arcade.draw_lrtb_rectangle_filled(0, 800, 150, 0, arcade.color.BANGLADESH_GREEN)

        # creación de la estructura de la casa(parte rectangular)
        arcade.draw_lrtb_rectangle_filled(200, 400, 380, 125, arcade.color.BLUE_GREEN)

        # creación de la ventanas(primer cuadrado--> exterior, segundo cuadrado-->interior)
        arcade.draw_lrtb_rectangle_filled(225, 275, 335, 285, arcade.color.PURPLE_MOUNTAIN_MAJESTY)
        arcade.draw_lrtb_rectangle_filled(230, 270, 330, 290, arcade.color.BABY_BLUE_EYES)

        arcade.draw_lrtb_rectangle_filled(325, 375, 335, 285, arcade.color.PURPLE_MOUNTAIN_MAJESTY)
        arcade.draw_lrtb_rectangle_filled(330, 370, 330, 290, arcade.color.BABY_BLUE_EYES)

        arcade.draw_lrtb_rectangle_filled(225, 275, 255, 205, arcade.color.PURPLE_MOUNTAIN_MAJESTY)
        arcade.draw_lrtb_rectangle_filled(230, 270, 250, 210, arcade.color.BABY_BLUE_EYES)

        arcade.draw_lrtb_rectangle_filled(325, 375, 255, 205, arcade.color.PURPLE_MOUNTAIN_MAJESTY)
        arcade.draw_lrtb_rectangle_filled(330, 370, 250, 210, arcade.color.BABY_BLUE_EYES)

        # creación de la puerta
        arcade.draw_lrtb_rectangle_filled(275, 325, 200, 125, arcade.color.BRONZE)

        # pomio de la puerta
        arcade.draw_circle_filled(320, 160, 2, arcade.color.BROWN)

        # tejado de la casa
        arcade.draw_triangle_filled(200, 380, 400, 380, 300, 450, arcade.color.WHITE)

        # camino que sale de la casa

        arcade.draw_lrtb_rectangle_filled(250, 350, 125, 0, arcade.color.GRAY)

        #arcade.start_render()


def main():
    window = MyGame()
    arcade.run()


main()