from typing import List, Tuple


# answers
# 1 - n
# 2 - 1
# 3 - n^2
# 4 - n


def question1(first_list: List[int], second_list: List[int]) -> List[int]:
    # O(n) - using set intersection
    set_first_list = set(first_list)
    set_second_list = set(second_list)
    return list(set_first_list.intersection(set_second_list))


def question2(n: int) -> int:
    # O(1) - constant time complexity
    for _ in range(10):
        n **= 3
    return n


def question3(first_list: List[int], second_list: List[int]) -> List[int]:
    # O(n^2) - using list append and set membership test
    temp = first_list[:]
    for el_second_list in second_list:
        if el_second_list not in temp:
            temp.append(el_second_list)
    return temp


def question4(input_list: List[int]) -> int:
    # O(n) - using max function
    return max(input_list)