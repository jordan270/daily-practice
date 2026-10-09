class RomanNumerals:
    @staticmethod
    def to_roman(val : int) -> str:
        pairs = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
        (1, 'I')
    ]
        result = []
        for (value, symbol) in pairs:
            while val >= value:
                result.append(symbol)
                val -= value
        return ''.join(result)

    @staticmethod
    def from_roman(roman : str) -> int:
        pairs = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
            (1, 'I')
        ]

        total = 0
        for (value, symbol) in pairs:
            while roman.startswith(symbol):
                total += value
                roman = roman[len(symbol):]
        return total
    
