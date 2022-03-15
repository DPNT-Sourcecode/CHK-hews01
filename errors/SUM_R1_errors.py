class NotAnInteger(Exception):
    """Raised when a value is expected to be an integer and is not."""
    def __init__(self, variable):
        self.message = ""
        super().__init__(self.message)