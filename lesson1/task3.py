from urllib.request import urlopen

randnumbers = {}


def genRandomFromRange(minimum, maximum):
    randurl = "https://www.random.org/integers/?num=1&min=" + str(minimum) + "&max=" + str(maximum) + "&col=5&base=10&format=plain&rnd=new"
    num = int(urlopen(randurl).read().strip())
    return num


for i in range(10):
    n = genRandomFromRange(100, 200)
    key = 'elem_' + str(i)
    randnumbers[key] = n


print(randnumbers)
