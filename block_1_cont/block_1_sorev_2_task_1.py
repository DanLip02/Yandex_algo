
"""
Вася пишет бота на основе LLM для знакомства с девушками. Бот будет посылать девушке мем, а в ответ девушка, по идее, должна смеяться. Для повышения качества работы бота необходимо организовать обучение с подкреплением. Для этого нужно оценить самую длинную последовательность из смеха над мемом.

Вася считает, что смех — это последовательность чередующихся букв "a" и "h". Так например, "ahahaha", "hah" и "a" являются смехом, а "abacaba" и "hh" — нет.

Необходимо выделить из строки-ответа девушки самую длинную подстроку, которая является смехом, и вывести ее длину.
"""

def longest_laugh(s):
    max_length = 0
    current_length = 0
    prev_char = ''

    for char in s:
        if char == 'a' or char == 'h':
            if current_length == 0 or (prev_char != char):
                current_length += 1
                if current_length > max_length:
                    max_length = current_length
            else:
                current_length = 1
            prev_char = char
        else:
            current_length = 0
            prev_char = ''

    return max_length

n, s = int(input()), input()
print(longest_laugh(s))