
def product_schema(product) -> dict:
    return {"plu": str(product["plu"]),
            "name": product["name"],
            "price": product["price"]}