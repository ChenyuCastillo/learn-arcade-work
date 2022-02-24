import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def ventanas():
    arcade.draw_lrtb_rectangle_filled(225, 275, 335, 285, arcade.color.PURPLE_MOUNTAIN_MAJESTY)
    arcade.draw_lrtb_rectangle_filled(230, 270, 330, 290, arcade.color.BABY_BLUE_EYES)

    arcade.draw_lrtb_rectangle_filled(325, 375, 335, 285, arcade.color.PURPLE_MOUNTAIN_MAJESTY)
    arcade.draw_lrtb_rectangle_filled(330, 370, 330, 290, arcade.color.BABY_BLUE_EYES)

    arcade.draw_lrtb_rectangle_filled(225, 275, 255, 205, arcade.color.PURPLE_MOUNTAIN_MAJESTY)
    arcade.draw_lrtb_rectangle_filled(230, 270, 250, 210, arcade.color.BABY_BLUE_EYES)

    arcade.draw_lrtb_rectangle_filled(325, 375, 255, 205, arcade.color.PURPLE_MOUNTAIN_MAJESTY)
    arcade.draw_lrtb_rectangle_filled(330, 370, 250, 210, arcade.color.BABY_BLUE_EYES)

def puerta():
    arcade.draw_lrtb_rectangle_filled(275, 325, 200, 125, arcade.color.BRONZE)
    arcade.draw_circle_filled(320, 160, 2, arcade.color.BROWN)




def casa():
    arcade.draw_lrtb_rectangle_filled(200, 400, 380, 125, arcade.color.BLUE_GREEN)

    ventanas()
    puerta()

def suelo():
    arcade.draw_lrtb_rectangle_filled(0, 800, 150, 0, arcade.color.BANGLADESH_GREEN)
    arcade.draw_lrtb_rectangle_filled(250, 350, 125, 0, arcade.color.GRAY)


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.BABY_BLUE_EYES)
    arcade.start_render()

    suelo()
    casa()

    arcade.finish_render()
    arcade.run()

main()