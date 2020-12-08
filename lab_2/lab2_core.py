from graphics import *
from lab2_utils import draw_figure


def main_core(rotate, rotate_and_move, text):
    # -------------- Input data -----------------
    xw = 600
    yw = 600
    dx = 50
    dy = 50
    startX = 20
    startY = 550
    x1 = startX
    y1 = startY
    x2 = startX + 15
    y2 = startY - 25
    x3 = startX + 75
    y3 = startY - 25
    x4 = startX + 60
    y4 = startY

    p1 = [x1, y1]
    p2 = [x2, y2]
    p3 = [x3, y3]
    p4 = [x4, y4]

    TetaG = 45
    TetaR = (3 / 14 * TetaG) / 180

    # -------------- Create window -----------------
    win = GraphWin("Graphics. " + text, xw, yw)
    win.setBackground('white')

    draw_figure(win, 'black', p1, p2, p3, p4)

    stop = xw / dx * 1.5
    stop = float(stop)
    ii = int(stop)

    # -------------- Rotate -----------------
    for i in range(10):
        time.sleep(0.2)

        DTetaR = (3 / 14 * (1 * 0.65)) / 180
        TetaR = TetaR + DTetaR

        p1, p2, p3, p4 = rotate(p1, p2, p3, p4, **{'dx': dx, 'dy': dy, 'TetaR': TetaR})
        draw_figure(win, 'green', p1, p2, p3, p4)

    # -------------- Rotate + Move -----------------
    for i in range(10):
        time.sleep(0.2)

        DTetaR = (3 / 14 * ((xw / dx) * 0.65)) / 180
        TetaR = TetaR + DTetaR

        p1, p2, p3, p4 = rotate_and_move(p1, p2, p3, p4, **{'dx': dx, 'dy': dy, 'TetaR': TetaR})
        draw_figure(win, 'brown', p1, p2, p3, p4)
        draw_figure(win, 'brown', p1, p2, p3, p4)

    win.getMouse()
    win.close()