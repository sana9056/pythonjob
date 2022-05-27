def get_percent(amount, months):
    if months not in [6, 12, 24]:
        return False

    rates = (
        {'begin_sum': 1000, 'end_sum': 10000, 6: 5, 12: 6, 24: 5},
        {'begin_sum': 10000, 'end_sum': 100000, 6: 6, 12: 7, 24: 6.5},
        {'begin_sum': 100000, 'end_sum': 1000000, 6: 7, 12: 8, 24: 7.5},
    )

    for rate in rates:
        if rate['begin_sum'] <= amount < rate['end_sum']:
            return rate[months]

    return False


def chargable_deposit(amount, months, charge=0):
    percent = get_percent(amount, months)
    if not percent:
        print('Нет подходящего тарифа')

    total = amount
    for month in range(months):
        profit = total * percent / 100 / 12
        total += profit
        if month != 0 and month != months - 1:
            total += charge + charge * percent / 100 / 12

    print(round(total, 2))


chargable_deposit(50000, 12, 500)
