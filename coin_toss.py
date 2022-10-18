import random

toss_array = []
attempts_number = 10


def coin_toss():
    toss_result = random.randint(0, 1)
    return toss_result


def multiple_toss(attempts):
    _toss_array = [0, 0]
    for x in range(attempts):
        value = coin_toss()
        if value == 0:
            _toss_array[0] = _toss_array[0] + 1
        elif value == 1:
            _toss_array[1] = _toss_array[1] + 1
        else:
            print("ERROR")
            break
    return _toss_array


if __name__ == '__main__':
    toss_array = multiple_toss(attempts_number)
    print(toss_array[0], "HEADS", "AND", toss_array[1], "REVERSE")
    print("Ratio: ", round(toss_array[0] / attempts_number, 2), ' : ', round(toss_array[1] / attempts_number, 2))
