import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

COLORS_R = [arcade.color.AZURE, arcade.color.SAE, arcade.color.AMERICAN_ROSE ]  # list des couleurs des rectangles

COLORS_C = [arcade.color.BLUE, arcade.color.FANDANGO_PINK,
arcade.color.FRENCH_ROSE, arcade.color.GOLDEN_POPPY]  # list des couleur des cerlces


class Cercle:

    def __init__(self, r, x, y, c):
        self.rayon = r
        self.centre_x = x
        self.centre_y = y
        self.color = c
        self.change_x = 3  # vitess du déplacement du centre_x
        self.change_y = 3  # vitess du déplacement du centre_y

    def update(self):  # appel la fonction à chaque frame
        # changement des centre x et y pour faire bouger le cercle
        self.centre_x += self.change_x 
        self.centre_y += self.change_y
        
        # si les cercles touches les bordures, il  rebondissent et vont 0.1 fois plus vite
        if self.centre_x < self.rayon or self.centre_x > SCREEN_WIDTH - self.rayon:
            self.change_x *= -1.1

        if self.centre_y < self.rayon or self.centre_y > SCREEN_HEIGHT - self.rayon:
            self.change_y *= -1.1

    def draw(self):  # fonction pour dessiner les cercles
        # arcade.draw_circle_filled(center_x, center_y, rayon, color)
        arcade.draw_circle_filled(self.centre_x, self.centre_y, self.rayon, self.color)

# même chose pour les rectangles
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
        self.angle = a  # l'angle du rectangle

    def update(self):
        self.center_x += self.changer_x
        self.center_y += self.changer_y
        self.angle += self.tilt_angle  # fait tourner le rectangle

        if self.center_x < self.longeur or self.center_x > SCREEN_WIDTH - self.longeur // 2:
            self.changer_x *= -1.1

        if self.center_y < self.hauteur or self.center_y > SCREEN_HEIGHT - self.hauteur // 2:
            self.changer_y *= -1.1

    def draw(self):
        # arcade.draw_rectangle_filled(center_x, center_y, width, height, color)
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.longeur, self.hauteur, self.color, self.angle)


class MyGame(arcade.Window):  # paramètres du jeux
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "cercles et rectangles")  
        self.liste_cercles = []  # création de la liste des cercles
        self.liste_rectangles = []  # création de la liste des rectangles

    def on_update(self, delta_time: float):
        for cercle in self.liste_cercles:
            cercle.update()  # appel la fonction

        for rectangle in self.liste_rectangles:
            rectangle.update()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):

            if button == arcade.MOUSE_BUTTON_LEFT:  # si le bouton de la souris gauche est appuié, crée un cercle
                rayon = random.randint(10, 30)
                centre_x = x
                centre_y = y
                couleur = random.choice(COLORS_C)
                cercle = Cercle(rayon, centre_x, centre_y, couleur)
                self.liste_cercles.append(cercle)

            if button == arcade.MOUSE_BUTTON_RIGHT:  # si le bouton de la souris droite est appuié, crée un rectangle
                hauteur = random.randint(15, 40)
                longeur = random.randint(15, 40)
                angle = random.randint(0, 360)
                center_x = x
                center_y = y
                color = random.choice(COLORS_R)
                rectangle = Rectangle(center_x, center_y, longeur, hauteur, color, angle)
                self.liste_rectangles.append(rectangle)

    def on_draw(self):
        arcade.start_render()  #  dessine le code

        for cercle in self.liste_cercles:
            cercle.draw()

        for rectangle in self.liste_rectangles:
            rectangle.draw()


def main():
    my_game = MyGame()
    arcade.run()


main()
