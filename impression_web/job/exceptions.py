"""
Exceptions relating to Job creation and acess
"""


class JobCreationError(Exception):
    """on failure to create a new impression_web"""
    pass


class JobNotFoundError(Exception):
    """Invalid impression_web id"""
    pass


class JobAccessError(Exception):
    """No access to impression_web"""
    pass
