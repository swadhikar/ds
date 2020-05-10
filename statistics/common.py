from decimal import Decimal


def round_off(float_num, decimals):
    decimal_num = Decimal(float_num)
    rounded_num = round(decimal_num, decimals)
    return float(rounded_num)
