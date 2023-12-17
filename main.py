import pyxel

class App:
    def __init__(self,screen=False):
        self.screen = screen
        # 初期化
        pyxel.init(240, 192, caption="sinkyu seisaku",
        palette=[0x000000,
                 0xdcdcdc, 
                 0x4b4b4b, 
                 0x171717, 
                 0x1e2430,
                 0x414855, 
                 0x49505f, 
                 0x676487, 
                 0xb4b2e0, 
                 0xeb00f5, 
                 0xc1f0f9,
                 0x00faff, 
                 0xffecee, 
                 0xccc7e4,
                 0xf49b39,#空き
                 0xffffff],
                fps=60,
                fullscreen=screen,
                quit_key=pyxel.KEY_F4
                 )
        self.count = 0
        pyxel.mouse(True) 
        # 実行
        pyxel.run(self.update, self.draw)

    def update(self):

        self.count += 1

    def draw(self):

            pyxel.cls(0)
            pyxel.text(self.count,1,"a",1)
            


if __name__ == '__main__':
    App()   