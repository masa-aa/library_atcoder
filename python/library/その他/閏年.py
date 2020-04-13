"""
y年が閏年か判定
閏年:True
"""

def uruu(y):
    if y % 400 == 0:
        return True
    elif y % 100 == 0:
        return False
    elif y % 4 == 0:
        return True
    return False