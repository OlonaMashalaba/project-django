def calculate_total(price, tax_rate):
    """
    Calculate the total price after applying tax.

    Parameters:
    ----------
    price : float
        The initial price before tax.

    tax_rate : float
        The tax rate as a decimal (e.g., 0.2 for 20%).

    Returns:
    -------
    float
        The total price after applying tax, calculated as `price * (1 + tax_rate)`.

    Raises:
    ------
    TypeError
        If `price` or `tax_rate` is not a numeric type.
    """
    
    # Check if inputs are of numeric types
    if not isinstance(price, (int, float)) or not isinstance(tax_rate, (int, float)):
        raise TypeError("Both price and tax_rate must be numbers")
    
    return price * (1 + tax_rate)
