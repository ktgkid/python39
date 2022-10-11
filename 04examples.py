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