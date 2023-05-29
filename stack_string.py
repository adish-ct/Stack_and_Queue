# reverse a string using stack

# def reverse(string):
#     stack = []
#     for letter in string:
#         stack.append(letter)
#
#     reverse_string = ''
#     while stack:
#         reverse_string += stack.pop()
#     return reverse_string
#
#
# print(reverse('amal'))

def reverse(string):
    stack = []
    for i in string:
        stack.append(i)
    print(stack)
    reverse_string = ''
    while stack:
        reverse_string += stack.pop()
    print(stack)
    return reverse_string


rev = reverse("adish")
print(rev)