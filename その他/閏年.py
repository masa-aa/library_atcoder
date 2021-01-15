def is_leap(year):
    """year年が閏年か判定, 閏年:True"""
    return year % 4 == 0 and year % 100 or year % 400 == 0
