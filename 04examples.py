# 1
# 프로그래밍 언어 실습시 글꼴은
# 고정폭 글꼴을 사용할 것을 추천!
print("*   *       **      ****        ****    *   *       /////")
print("*   *      *  *     *   *       *   *   *   *      | o o |")
print("*****     *    *    ****        ****     * *      (|  ^  |)")
print("*   *     ******    *   *       *   *     *        | [_] |")
print("*   *     *    *    *    *      *    *    *         -----")

print("                  +---+")
print("                  |   |")
print("              +---+---+")
print("              |   |   |")
print("          +---+---+---+         /\_/\       -----")
print("          |   |   |   |        ( ' ' )    / Hello \\")
print("      +---+---+---+---+        (  -  )   <  Junior |")
print("      |   |   |   |   |         | | |     \\ Coder!/")
print("      +---+---+---+---+        (__|__)      -----")

# 3
#   : long, TimeLimit, numberOfWindows

# 4
x, y, z = 1, 2, 3
s0, v0, t, g = 4, 5, 6, 9.8
print(3 * x, 3 * x + y, (x + y) / 7)
print(s0 + v0*t + (1/2) * g * t**2)

# 6
x = 2.5
y = 1.5
m = 18
n = 4
print(x + n * y - (x + n) * 3)          # -11.0
print(m / n + m % n)                    # 6.5
print(5 * x - n / 5)                    # 11.7
print(1 - (1 - (1 - (1 - (1 - n)))))    # 4

# 7
print(3 + 4.5 * 2 + 27 / 8)

# 논리연산시 경우에 따라 단축식 평가가 적용되기도 함
print(True or False and 3 < 4 or not(5 == 7))
print(True or (3 < 5 and 6 >= 2))

# print(not True > ord('A'))                         # ord 함수 = character to int
print(not True > bool('A'))     # not (True > True)

print(7 % 4 + 3 - 2 / 6 * ord('Z'))
print(ord('D') + 1 + ord('M') % 2 / 3)
print(5.0 / 3 + 3 / 3)
print(53 % 21 < 45 / 18)
print((4 < 6) or True and False or False and (2 > 3))
print(7 - (3 + 8 * 6 + 3) - (2 + 5 * 2))

# 9
print(True and False and True or True)


# 10
# 파이썬의 if 단축식 : 참일때 값 if 조건식 else
# print('만나이', (age + 1) if isPassBirth else age)

# 13
print('7 x 1 = ', (7*1))
print('7 x 2 = ', (7*2))
print('7 x 3 = ', (7*3))
print('7 x 4 = ', (7*4))
print('7 x 5 = ', (7*5))
print('7 x 6 = ', (7*6))
print('7 x 7 = ', (7*7))
print('7 x 8 = ', (7*8))
print('7 x 9 = ', (7*9))

# % 서식
num1 = 7

print('단수 : %s' % num1)
print('7 x 1 = %d' % (7*1))
print('7 x 2 = %d' % (7*2))
print('7 x 3 = %d' % (7*3))
print('7 x 4 = %d' % (7*4))
print('7 x 5 = %d' % (7*5))
print('7 x 6 = %d' % (7*6))
print('7 x 7 = %d' % (7*7))
print('7 x 8 = %d' % (7*8))
print('7 x 9 = %d' % (7*9))

# .format
print('7 x 1 = {:d}'.format(7*1))
print('7 x 2 = {:d}'.format(7*2))
print('7 x 3 = {:d}'.format(7*3))
print('7 x 4 = {:d}'.format(7*4))
print('7 x 5 = {:d}'.format(7*5))
print('7 x 6 = {:d}'.format(7*6))
print('7 x 7 = {:d}'.format(7*7))
print('7 x 8 = {:d}'.format(7*8))
print('7 x 9 = {:d}'.format(7*9))

# f-string
print(f'7 x 1 = {7*1:2d}')
print(f'7 x 2 = {7*2:2d}')
print(f'7 x 3 = {7*3:2d}')
print(f'7 x 4 = {7*4:2d}')
print(f'7 x 5 = {7*5:2d}')
print(f'7 x 6 = {7*6:2d}')
print(f'7 x 7 = {7*7:2d}')
print(f'7 x 8 = {7*8:2d}')
print(f'7 x 9 = {7*9:2d}')
