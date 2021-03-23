import json
from product import Product

def load_offers():
    """
    Load all the discounts into the memory. Generate qualification map
    to be able to query the products more efficient (by using hash maps
    instead of having to loop through every single promotion each time)
    Each discount should contain (otherwise it will be discarded):
    qualification_item_ids - List of products, to which the promotion
                             is applied to
    qualifying_no - how many products does somebody has to buy, in order
                    to get the discount
    discount_size - how big is the discount

    :return: Tuple, consisting of two dictionaries, one for discounts,
             one for fast access to the discounts.
    """
    with open('offers.json', encoding="utf-8") as json_file:
        qualif_map = {}
        loaded_discounts = json.load(json_file)
        valid_values = {'qualification_item_ids', 'qualifying_no', 'discount_size'}
        values_to_discard = []
        for discount in loaded_discounts:
            if valid_values.issubset(loaded_discounts[discount].keys()):
                for qualif_id in loaded_discounts[discount]['qualification_item_ids']:
                    if not qualif_id in qualif_map:
                        qualif_map[qualif_id] = []
                    qualif_map[qualif_id].append(discount)
            else:
                values_to_discard.append(discount)
        for value in values_to_discard:
            print(f"Invalid configuration for offer: {value}")
            loaded_discounts.pop(value)
        return loaded_discounts, qualif_map


def get_product_catalogue():
    """
    Load all the products into the memory. Every product has to follow
    a convention, otherwise, it is discarded.

    :return: dictionary of products
    """
    with open('product_list.json', encoding="utf-8") as json_file:
        product_catalogue = {}
        product_catalogue_json = json.load(json_file)
        for name in product_catalogue_json:
            try:
                prod = product_catalogue_json[name]
                product_catalogue[name] = Product(name=name,
                                                  price=prod["price"],
                                                  id=prod["id"])
            except ValueError as ve:
                print(f"Failed to load product: {ve}")
            except KeyError as ke:
                print(f"Failed to load value: {ke} from {name} entity")
        return product_catalogue