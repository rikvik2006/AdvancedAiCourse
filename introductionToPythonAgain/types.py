def area_rett(b: float, h: float) -> float:
    # Check if the input is a float
    if not isinstance(b, float) or not isinstance(h, float):
        raise TypeError("The input must be a float")

    return b * h


result = area_rett(2, 3)
print(result)
