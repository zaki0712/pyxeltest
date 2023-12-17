import pyxel

class App:
    def __init__(self):
        # 初期化
        pyxel.init(240, 192)
        self.count = 0
        # 実行
        pyxel.run(self.update, self.draw)

    def update(self):

        self.count += 1

    def draw(self):

            pyxel.cls(0)
            pyxel.text(self.count,1,"a",1)
            
App()   