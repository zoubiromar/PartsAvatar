# Task: String Formatting
# Goal: Transform a raw SKU into a readable title.

def format_sku(sku_string):
    """
    Instructions: Convert 'engine-oil-10w30' to 'Engine Oil 10w30'.
    """
    # TODO: Implement logic
    text = sku_string.replace('-'," ").title()

    return (text)

print(format_sku("engine-oil-10w30"))

# Test: format_sku("brake-pads-ceramic") -> "Brake Pads Ceramic"
