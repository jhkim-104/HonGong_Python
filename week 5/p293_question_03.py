# page 293, 문제 3
# 다음 중 구문 오류 발생이 예상되면'구문 오류'에, 예외 발생이 예상되면 '예외'에 체크 표시를 한 후, 
# 예상되는 에러명도 적어 보세요.

output = 10 + "개"      # 1)
int("안녕하세요")       # 2)
cursor.close)           # 3)
[1, 2, 3, 4., 5][10]    # 4)

# 1) : 예외 -> (TypeError)
# Traceback (most recent call last):
#   File "p293_question_03.py", line 4, in <module>
#     output = 10 + "개"      # 1)
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

# 2) : 예외 -> (TypeError)
# Traceback (most recent call last):
#   File "p293_question_03.py", line 5, in <module>
#     int("안녕하세요")       # 2)
# ValueError: invalid literal for int() with base 10: '안녕하세요'

# 3) : 구문 오류 -> (SyntaxError)
#   File "p293_question_03.py", line 6
#     cursor.close)           # 3)
#                 ^
# SyntaxError: unmatched ')'

# 4) : 예외 -> (IndexError)
# Traceback (most recent call last):
#   File "p293_question_03.py", line 7, in <module>
#     [1, 2, 3, 4., 5][10]    # 4)
# IndexError: list index out of range
