from mock_customers import MOCKCUSTOMERS
from mock_vendors import MOCKVENDORS
"""Classification: Structural"""

CUSTOMERS = MOCKVENDORS


def main():
    for customer in MOCKCUSTOMERS:
        print('customer -> Name: %s; Address: %s' %
              (customer.name, customer.address))
    for vendor in MOCKVENDORS:
        print('vendor -> Name: %s; Address: %s' %
              (vendor.name, vendor.address))


if __name__ == '__main__':
    main()
