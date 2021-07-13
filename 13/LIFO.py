"""
Проверяет корректность скобочной последовательности
из круглых и квадратных скобок() []

>>> is_braces_sequence_correct("(([()]))[]")
True
>>> is_braces_sequence_correct("([)]")
False
>>> is_braces_sequence_correct("(")
False
>>> is_braces_sequence_correct("]")
False
"""

import A_stack


s = "(([()]))[]"
def is_braces_sequence_correct(s:str):
	for brace in s:
		if brace not in "()[]":
			continue
		if brace in "([":
			A_stack.push(brace)
		else:
			assert brace in ")]", "Ожидалось закрывающая скобка: " + str(brace)
			if A_stack.is_empty():
				return False
			left = A_stack.pop()
			assert left in "([", "Ожидалось открывающая скобка: " + str(brace)
			if left == "(":
				right = ")"
			elif left == "[":
				right = "]"
			if right != brace:
				return False
	return A_stack.is_empty()


if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)


1
(
_stack = ['(']

2
(
_stack = ['((']

3
[
_stack = ['(([']

4
(
_stack = ['(([(']




5
)

left = (
right = ")"
_stack = ['(([']





6
]
left = [
right = "]"
_stack = ['((']



7
)

left = (
right = ")"
_stack = ['(']

8
)
left = (
right = ")"
_stack = ['']

9
[
_stack = ['[']

10
]
left = [
right = "]"
_stack = ['']

True


 1 2 3 4 5 6 7 8 9 10
"( ( [ ( ) ] ) ) [ ]"



2____________________________________________

 1 2 3 4
"( [ ) ]"


1
(
_stack = ['(']

2
[
_stack = ['([']

3
)
left = [
right = "]"
false
_stack = ['(']


4
]
left = (
right = ")"
_stack = ['']


