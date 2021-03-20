def clamp(v: int, low: int = None, high: int = None) -> int:
    """vの値を範囲[low, high]に収める."""
    if low != None:
        v = max(v, low)
    if high != None:
        v = min(v, high)
    return v
