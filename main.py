import pyxel


class App:
    def __init__(self):
        pyxel.init(160, 120, title="test")
        self.score = 0
        pyxel.playm(0, loop=True)
        pyxel.run(self.update, self.draw)

    def update(self):
        self.score += 1
    def draw(self):
        pyxel.text(4, 4, self.score, 7)


App()
