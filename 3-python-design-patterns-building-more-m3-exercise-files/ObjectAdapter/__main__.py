from mock_customers import MOCKCUSTOMERS
from mock_vendors import MOCKVENDORS
"""Classification: Structural"""


def main():
    for adapter in (MOCKCUSTOMERS + MOCKVENDORS):
        print('adapter -> Name: %s; Address: %s' %
              (adapter.name, adapter.address))


if __name__ == '__main__':
    main()
