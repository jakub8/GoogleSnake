import keyboard
from pyautogui import press, typewrite, dragTo
import time
from ctypes import windll

#I hope this works

dc = windll.user32.GetDC(0)
#610, 324 with step of 40 is top left corner of snake game regular size board
#618, 326 with step of 66 small board

def getpixel(x, y):
    pcolor = windll.gdi32.GetPixel(dc, x, y)
    red = pcolor & 0xFF
    green = (pcolor & 0xFF00) >> 8
    blue = (pcolor & 0xFF0000) >> 16
    return red, green, blue



def playsnake(startx, starty, step):
    isclear = False
    case = 11
    buffer = 0
    while True:
        if case == 11:
            while True:
                r, g, b = getpixel(startx + (step * 3) + buffer, starty + 33)
                # behind rgb(205, 91, 106)
                # rgb(191, 102, 137) mid
                # rgb(177, 113, 168) ahead
                # turnip rgb(73, 197, 39)
                # r2, g2, b2 = getpixel(startx + step + buffer, starty + 51)
                # r, g, b = getpixel(100, 500)
                # print(f"{startx + step - 15} {int(starty + (step / 2))}")
                # print(f"{r} {g} {b}")
                # if((r1 > 220 and g1 > 220 and b1 > 220) or (r2 > 220 and g2 > 220 and b2 > 220)):
                if isclear and 205 > r > 177 and 113 > g > 91 and 168 > b > 91:
                    press('s')
                    isclear = False
                    case = 1
                    break
                elif not isclear and ((158 < r < 174 and 205 < g < 219 and 69 < b < 85) or
                                      (70 < r < 76 and 194 < g < 200 and 36 < b < 42) or
                                      (r > 230 and g > 20 and b > 220)):
                # elif (r == 170 and g == 215 and b == 81) or (r == 162 and g == 209 and b == 73):
                    # light green rgb(170, 215, 81)
                    # dark green rgb(162, 209, 73)
                    isclear = True
        elif case <= 9:
            # print("hello")
            instruction = 'dw'
            # beginx = 0
            # beginy = 0
            diff = 0

            if case % 2 == 0:
                # print("hi")

                instruction = 'ds'
                beginx = startx + (step * case) - 33
                # beginx2 = startx + (step * case) - 51
                beginy = starty + (step * 4) + buffer
            else:
                instruction = 'dw'
                beginx = startx + (step * case) - 33
                # beginx2 = startx + (step * case) - 15
                beginy = starty + (step * 6) - buffer

            # print(f"case: {case}")
            # print(f"{beginx} {beginy}")
            while True:
                # r, g, b = getpixel(beginx, beginy)

                r, g, b = getpixel(beginx, beginy)
                if isclear and 205 > r > 177 and 113 > g > 91 and 168 > b > 91:
                    typewrite(instruction)
                    case += 1
                    isclear = False
                    break

                elif not isclear and ((158 < r < 174 and 205 < g < 219 and 69 < b < 85) or
                                      (70 < r < 76 and 194 < g < 200 and 36 < b < 42) or
                                      (r > 230 and g > 20 and b > 220)):
                    isclear = True
        else:
            while True:
                r, g, b = getpixel(startx + (step * 9) + 33, starty + (step * 3) + buffer)
                # r2, g2, b2 = getpixel(startx + (step * 9) + 51, starty + step + buffer)
                # r, g, b = getpixel(100, 500)
                # print(f"{startx + step - 15} {int(starty + (step / 2))}")
                # print(f"{r} {g} {b}")
                if isclear and 205 > r > 177 and 113 > g > 91 and 168 > b > 91:
                    press('a')
                    isclear = False
                    case += 1
                    break
                elif not isclear and ((158 < r < 174 and 205 < g < 219 and 69 < b < 85) or
                                      (70 < r < 76 and 194 < g < 200 and 36 < b < 42) or
                                      (r > 230 and g > 20 and b > 220)):
                    isclear = True




time.sleep(3)
playsnake(618, 326, 66)
# dragTo(618 + (66 * 2) - 33, 326 + (66 * 3))


# dragTo(910 - 66, 620)
# r, g, b = getpixel(910 - 66 - 10, 620)
# print(f"rgb({r}, {g}, {b})")
#light green rgb(170, 215, 81)
#dark green rgb(162, 209, 73)
# turnip rgb(73, 197, 39)
# behind rgb(205, 91, 106)
# rgb(191, 102, 137) mid
# rgb(177, 113, 168) ahead


# x = 618 + (66 * 6)
# y = 326 + (66 * 4)
#
# r1, g1, b1 = getpixel(x, y + 15)
# r2, g2, b2 = getpixel(x, y + 51)
# dragTo(x, y + 15)
# while True:
#     r1, g1, b1 = getpixel(x + 10, y + 15)
#     r2, g2, b2 = getpixel(x + 10, y + 51)
#     if (r1 > 220 and g1 > 220 and b1 > 220) or (r2 > 220 and g2 > 220 and b2 > 220):
#         press('w')











# playsnake(0, 540, 100)

# red, green, blue = getpixel(3, 540)
# for i in range(0, 10):
#     time.sleep(0.5)
#     dragTo(619 + (i * 66), 326)
# dragTo(612, 320)
# dragTo(618, 326)
# dragTo(610, 324)
# x = 618
# y = 326
# s = 66
# while True:
#     time.sleep(0.1)
#     first = x + s
#     second = int(y + (s / 2))
#     red, green, blue = getpixel(first, second)
#     print(f"{red} {green} {blue}")

#
# flag = 0
# counter = 0
# sleepTime = 0.2
#
# while True:
#     if keyboard.is_pressed('m'):
#         if flag == 0:
#             typewrite('s')
#             time.sleep(sleepTime)
#             counter = 0
#             flag = 1
#         elif flag == 1:
#             typewrite('dw')
#             time.sleep(sleepTime)
#             counter += 1
#             flag = 2
#             if counter == 9:
#                 flag = 4
#         elif flag == 2:
#             typewrite('ds')
#             time.sleep(sleepTime)
#             counter += 1
#             flag = 1
#         elif flag == 4:
#             typewrite('a')
#             time.sleep(sleepTime)
#             flag = 0
#
#
# # diagTime = 1.325
#
# # time.sleep(5)
# # press('w')
# # time.sleep(0.75)
# # press('a')
# # time.sleep(0.35)
#
# # while True:
# #     press('s')
# #     time.sleep(diagTime)
# #     typewrite('dw')
# #     time.sleep(diagTime)
# #     typewrite('ds')
# #     time.sleep(diagTime)
# #     typewrite('dw')
# #     time.sleep(diagTime)
# #     typewrite('ds')
# #     time.sleep(diagTime)
# #     typewrite('dw')
# #     time.sleep(diagTime)
# #     typewrite('ds')
