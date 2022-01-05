from abs_adapter import AbsAdapter


class CustAdapter(AbsAdapter):
    @property
    def name(self):
        return self.adaptee.name

    @property
    def address(self):
        return self.adaptee.address
