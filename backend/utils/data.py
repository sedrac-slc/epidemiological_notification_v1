
def get_item_by_name(items, item):
    for itemness in items:
        if itemness.name == item.name:
            return itemness
    return item

def get_item_by_username(items, item):
    for itemness in items:
        if itemness.username == item.username:
            return itemness
    return item