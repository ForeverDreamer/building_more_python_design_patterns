from datetime import date
from person import Person
from family import Family
"""复合（合成）模式"""
"""Classification: Structural"""


def main():
    hitchhikers = Family([
        Person('Trillian', date(1970, 3, 14)),
        Person('Arthur', date(1965, 7, 4)),
        Person('Ford', date(1995, 2, 2)),
        Person('Zaphod', date(1997, 5, 1)),
        Person('Douglas', date(1999, 4, 2))
    ])

    singles = Family([
        Person('Marvin', date(1991, 1, 1)),
        Person('Slarti', date(1993, 9, 9))
    ])

    loner = Person('Dirk', date(1990, 6, 6))

    family1 = Family([hitchhikers])
    family2 = Family([singles, loner])
    family3 = Family([family1, family2])

    for f in family1, family2, family3:
        oldest = f.get_oldest()
        max_age = (date.today() - oldest.birthdate).days / 365.2425
        print('Oldest person: {}; Age: {:6.2f}'.format(oldest.name, max_age))


if __name__ == '__main__':
    main()
