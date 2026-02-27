SALES_TAX = 0.06


def getSalesTax(subtotal):
    return round(subtotal * SALES_TAX, 2)

def totalAfterTax(subtotal):
    taxAmount = getSalesTax(subtotal)
    return round(subtotal + taxAmount ,2)