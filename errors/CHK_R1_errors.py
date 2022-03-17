class NotAnInteger(Exception):
    """Raised when a value is expected to be an integer but is not."""
    def __init__(self, variable):
        self.message = "{} is not an integer.".format(variable)
        super().__init__(self.message)

