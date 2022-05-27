def compare_parts(string):
    try:
        number = float(string)
        if int(number) == number:
            print('целое')
            return None
        else:
            print('дробное')
            left, right = string.split('.')
            return left == right
    except ValueError:
        print('Не число')


print(compare_parts(input('Введите число: ')))
