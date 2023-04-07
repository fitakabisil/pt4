import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

COLORS_R = [arcade.color.AZURE, arcade.color.SAE, arcade.color.AMERICAN_ROSE ]

COLORS_C = [arcade.color.BLUE, arcade.color.FANDANGO_PINK,
arcade.color.FRENCH_ROSE, arcade.color.GOLDEN_POPPY]


class Cercle:

    def __init__(self, r, x, y, c):
        self.rayon = r
        self.centre_x = x
        self.centre_y = y
        self.color = c
        self.change_x = 3
        self.change_y = 3

    def update(self):
        self.centre_x += self.change_x
        self.centre_y += self.change_y

        if self.centre_x < self.rayon or self.centre_x > SCREEN_WIDTH - self.rayon:
            self.change_x *= -1.1

        if self.centre_y < self.rayon or self.centre_y > SCREEN_HEIGHT - self.rayon:
            self.change_y *= -1.1

    def draw(self):
        # arcade.draw_circle_filled(center_x, center_y, rayon, color)
        arcade.draw_circle_filled(self.centre_x, self.centre_y, self.rayon, self.color)


class Rectangle():

    def __init__(self, x, y, l, h, c, a):
        self.center_x = x
        self.center_y = y
        self.longeur = l
        self.hauteur = h
        self.color = c
        self.changer_x = 4
        self.changer_y = 4
        self.tilt_angle = 1
        self.angle = a

    def update(self):  # il y a un problème ici
        self.center_x += self.changer_x
        self.center_y += self.changer_y
        self.angle += self.tilt_angle

        if self.center_x < self.longeur or self.center_x > SCREEN_WIDTH - self.longeur // 2:
            self.changer_x *= -1.1

        if self.center_y < self.hauteur or self.center_y > SCREEN_HEIGHT - self.hauteur // 2:
            self.changer_y *= -1.1

    def draw(self):
        # arcade.draw_rectangle_filled(center_x, center_y, width, height, color)
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.longeur, self.hauteur, self.color, self.angle)


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")
        self.liste_cercles = []
        self.liste_rectangles = []

    def on_update(self, delta_time: float):
        for cercle in self.liste_cercles:
            cercle.update()

        for rectangle in self.liste_rectangles:
            rectangle.update()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):  # le code crash ici

            if button == arcade.MOUSE_BUTTON_LEFT:
                rayon = random.randint(10, 30)
                centre_x = x
                centre_y = y
                couleur = random.choice(COLORS_C)
                cercle = Cercle(rayon, centre_x, centre_y, couleur)
                self.liste_cercles.append(cercle)

            if button == arcade.MOUSE_BUTTON_RIGHT:
                hauteur = random.randint(15, 40)
                longeur = random.randint(15, 40)
                angle = random.randint(0, 360)
                center_x = x
                center_y = y
                color = random.choice(COLORS_R)
                rectangle = Rectangle(center_x, center_y, longeur, hauteur, color, angle)
                self.liste_rectangles.append(rectangle)

    def on_draw(self):
        arcade.start_render()

        for cercle in self.liste_cercles:
            cercle.draw()

        for rectangle in self.liste_rectangles:
            rectangle.draw()


def main():
    my_game = MyGame()
    arcade.run()


main()
