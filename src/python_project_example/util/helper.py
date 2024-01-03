

class StringHelper:
    
    @staticmethod
    def has_spaces(data: str) -> bool:
        if " " in data:
            return True
        else:
            return False
    
    def to_lower(data: str) -> str:
        return data.lower()