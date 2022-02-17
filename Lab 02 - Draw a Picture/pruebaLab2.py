import arcade

arcade.open_window(800, 600, "Drawing Example")

arcade.set_background_color(arcade.color.BABY_BLUE)

arcade.start_render()

arcade.draw_circle_filled(725, 525, 50, arcade.color.ORANGE)

arcade.draw_lrtb_rectangle_filled(0, 800, 150, 0, arcade.color.BANGLADESH_GREEN)

arcade.draw_lrtb_rectangle_filled(200, 375, 350, 125, arcade.color.BLUE_GREEN)

arcade.finish_render()

arcade.run()