class NotAnInteger(Exception):
    """Raised when a value is expected to be an integer but is not."""
    def __init__(self, variable):
        self.message = "{} is not an integer.".format(variable)
        super().__init__(self.message)


class OutOfRange(Exception):
    """Raised when a value is outside a permitted range."""
    def __init__(self, variable, lower_limit, upper_limit):
        self.message = "{} is not between {} and {}.".format(variable, lower_limit, upper_limit)
        super().__init__(self.message)
