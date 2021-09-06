import pyxel
import math

circleRadius = 10

def main():
    pyxel.init(256, 256, caption="First Game", scale=3)
    pyxel.run(update, draw)

def update():
    global circleRadius
    circleRadius = 10 + 10 *(math.sin(pyxel.frame_count))
    if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

def draw():
    pyxel.cls(5)
    pyxel.text(10, 8,"Wasshup", (pyxel.frame_count / 4) % 16)
    pyxel.circ(128,128, circleRadius, 8)
    pass


main()
