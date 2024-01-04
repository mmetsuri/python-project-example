"""
Helper tools for string manipulation.
"""

class StringHelper:
    """
    A class for inspecting and checking strings.
    """

    @staticmethod
    def has_spaces(data: str) -> bool:
        """Check if the string contains spaces."""
        if " " in data:
            return True

        return False

    @staticmethod
    def to_lower(data: str) -> str:
        """Convert all characters in a string to lowercase."""
        
        return data.lower()