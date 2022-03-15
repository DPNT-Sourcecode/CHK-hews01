class NotAString(Exception):
    """Raised when a value is expected to be a string but is not."""
    def __init__(self, variable):
        self.message = "{} is not a string.".format(variable)
        super().__init__(self.message)

