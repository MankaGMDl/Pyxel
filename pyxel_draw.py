import pyxel
import os

# Taille de la fenêtre et de la grille
SCREEN_WIDTH = 128
SCREEN_HEIGHT = 128
PIXEL_SIZE = 4  # taille de chaque "pixel" dessiné

SAVE_FILE = "drawing.png"

class PyxelDraw:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="Pyxel Draw 🎨")
        pyxel.mouse(True)
        self.color = 7  # blanc par défaut
        self.drawing = {}

        pyxel.run(self.update, self.draw)

    def update(self):
        # Changer de couleur avec les touches 0-15
        for i in range(16):
            if pyxel.btnp(getattr(pyxel, f"KEY_{i}")):
                self.color = i

        # Effacer tout (touche C)
        if pyxel.btnp(pyxel.KEY_C):
            self.drawing.clear()

        # Sauvegarder (touche S)
        if pyxel.btnp(pyxel.KEY_S):
            pyxel.image(0).save(SAVE_FILE)
            print(f"Image sauvegardée sous {SAVE_FILE}")

        # Dessiner avec le clic gauche
        if pyxel.btn(pyxel.MOUSE_LEFT_BUTTON):
            x = pyxel.mouse_x // PIXEL_SIZE
            y = pyxel.mouse_y // PIXEL_SIZE
            self.drawing[(x, y)] = self.color

        # Effacer avec clic droit
        if pyxel.btn(pyxel.MOUSE_RIGHT_BUTTON):
            x = pyxel.mouse_x // PIXEL_SIZE
            y = pyxel.mouse_y // PIXEL_SIZE
            if (x, y) in self.drawing:
                del self.drawing[(x, y)]

    def draw(self):
        pyxel.cls(0)
        for (x, y), color in self.drawing.items():
            pyxel.rect(x * PIXEL_SIZE, y * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE, color)

        # Afficher infos à l’écran
        pyxel.text(2, 2, f"Couleur: {self.color}", 7)
        pyxel.text(2, 10, "C: Effacer | S: Sauver", 6)
        pyxel.text(2, 18, "0-15: changer couleur", 6)
        pyxel.text(2, 26, "Click G: dessiner | D: effacer", 13)


if __name__ == "__main__":
    PyxelDraw()
