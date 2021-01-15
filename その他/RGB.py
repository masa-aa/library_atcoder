def RGB(*colors):
    """0 <= r,g,b <= 255 を受け取ってカラーコードを返す．"""
    rgb = "#"
    for c in colors:
        rgb += ("0" + hex(c)[2:])[-2:]
    return rgb
