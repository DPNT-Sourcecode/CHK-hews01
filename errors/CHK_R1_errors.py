class NotAString(Exception):
    """Raised when a value representing a basket of SKU is not a string."""
    def __init__(self, variable):
        self.message = "{} is not a string.".format(variable)
        super().__init__(self.message)


class NotInPriceTable(Exception):
    """Raised when an SKU is not in the price table."""
    def __init__(self, variable):
        self.message = "{} is not an SKU in the price table.".format(variable)
        super().__init__(self.message)
