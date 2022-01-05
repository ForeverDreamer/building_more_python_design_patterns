from empty import Empty
from not_empty import NotEmpty
from check_out import AtCheckOut
from paid_for import PaidFor


class ShoppingCart:

    def __init__(self):
        self._empty = Empty(self)
        self._not_empty = NotEmpty(self)
        self._check_out = AtCheckOut(self)
        self._paid_for = PaidFor(self)

        self._size = 0
        self._state = self._empty

    @property
    def empty(self):
        return self._empty

    @property
    def not_empty(self):
        return self._not_empty

    @property
    def check_out(self):
        return self._check_out

    @property
    def paid_for(self):
        return self._paid_for

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, s):
        self._size = s

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, s):
        self._state = s

    def add_item(self):
        self._state.add_item()

    def remove_item(self):
        self._state.remove_item()

    def checkout(self):
        self._state.checkout()

    def pay(self):
        self._state.pay()

    def empty_cart(self):
        self._state.empty_cart()
