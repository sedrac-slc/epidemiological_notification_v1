
def get_firstname(full_name):
    if not full_name: return ""
    parts = full_name.split()
    return parts[0] if parts else full_name


def get_lastname(full_name):
    if not full_name: return ""
    parts = full_name.split()
    return parts[-1] if parts else full_name