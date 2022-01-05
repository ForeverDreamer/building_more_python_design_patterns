from bus import Bus
from airplane import Airplane
"""模板方法模式(Template Method Pattern)"""
"""Classification: Behavioral"""


def main():
    travel('New York', Bus)
    travel('Amsterdam', Airplane)


def travel(destination, transport):
    print(('Taking the {} to {} ' + '=====>').format(
        transport.__name__,
        destination
    ))

    means = transport(destination)
    means.take_trip()


if __name__ == '__main__':
    main()
