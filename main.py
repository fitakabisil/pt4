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

        if self.centre_x < self.rayon:
            pass
        if self.centre_x > SCREEN_WIDTH - self.rayon:
            pass
        if self.centre_y < self.rayon:
            pass
        if self.centre_y > SCREEN_HEIGHT - self.rayon:
            pass
        if self.centre_x < self.rayon:
            self.centre_x *= -1

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
        self.angle = a

    def update(self):
        pass

    def draw(self):
        # arcade.draw_rectangle_filled(center_x, center_y, width, height, color)
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.longeur, self.hauteur, self.color, self.angle)


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")
        self.liste_cercles = []
        self.liste_rectangles = []

    def setup(self):
        # remplir la liste avec 20 objets de type Cercle
        for cercle in range(20):
            rayon = random.randint(10, 30)
            centre_x = random.randint(10 + rayon, SCREEN_WIDTH - rayon)
            centre_y = random.randint(10 + rayon, SCREEN_HEIGHT - rayon)
            couleur = random.choice(COLORS_C)
            cercle = Cercle(rayon, centre_x, centre_y, couleur)
            self.liste_cercles.append(cercle)

        for rectangle in range(20):
            hauteur = random.randint(10, 30)
            longeur = random.randint(10, 30)
            angle = random.randint(0, 360)
            center_x = random.randint(0 + longeur, SCREEN_WIDTH - longeur)
            center_y = random.randint(0 + hauteur, SCREEN_HEIGHT - hauteur)
            color = random.choice(COLORS_R)
            rectangle = Rectangle(center_x, center_y, longeur, hauteur, color, angle)
            self.liste_rectangles.append(rectangle)

    def on_update(self, delta_time: float):
        Cercle.update(self)

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        pass

    def on_draw(self):
        arcade.start_render()

        for cercle in self.liste_cercles:
            cercle.draw()

        for rectangle in self.liste_rectangles:
            rectangle.draw()


def main():
    my_game = MyGame()
    my_game.setup()

    arcade.run()


main()
