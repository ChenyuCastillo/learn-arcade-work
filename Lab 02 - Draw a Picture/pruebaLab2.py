import arcade

arcade.open_window(800, 600, "Drawing Example")

arcade.set_background_color(arcade.color.BABY_BLUE)

arcade.start_render()

arcade.draw_circle_filled(725, 525, 50, arcade.color.ORANGE)

arcade.draw_lrtb_rectangle_filled(0, 800, 150, 0, arcade.color.BANGLADESH_GREEN)

arcade.draw_lrtb_rectangle_filled(200, 400, 380, 125, arcade.color.BLUE_GREEN)

arcade.draw_lrtb_rectangle_filled(225, 275, 335, 285, arcade.color.PURPLE_MOUNTAIN_MAJESTY)
arcade.draw_lrtb_rectangle_filled(230, 270, 330, 290, arcade.color.BABY_BLUE_EYES)

arcade.draw_lrtb_rectangle_filled(325, 375, 335, 285, arcade.color.PURPLE_MOUNTAIN_MAJESTY)
arcade.draw_lrtb_rectangle_filled(330, 370, 330, 290, arcade.color.BABY_BLUE_EYES)

arcade.draw_lrtb_rectangle_filled(225, 275, 235, 185, arcade.color.PURPLE_MOUNTAIN_MAJESTY)
arcade.draw_lrtb_rectangle_filled(230, 270, 230, 190, arcade.color.BABY_BLUE_EYES)

arcade.draw_lrtb_rectangle_filled(325, 375, 235, 185, arcade.color.PURPLE_MOUNTAIN_MAJESTY)
arcade.draw_lrtb_rectangle_filled(330, 370, 230, 190, arcade.color.BABY_BLUE_EYES)

arcade.finish_render()

arcade.run()