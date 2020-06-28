# python3


def money_change(money):
    assert 0 <= money <= 10 ** 3
    remain = money
    count = 0
    while remain > 0:
        if remain >= 10:
            remain -= 10
            count += 1
        elif remain >= 5:
            remain -= 5
            count += 1
        elif remain >= 1:
            remain -= 1
            count += 1
    return count


if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
