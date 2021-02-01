def split_name_from_full_name(full_name) -> dict:
    """
    Retrieves given, middle, family name from full_name.
    :param str full_name:
    """
    name = {}
    full_name = full_name.split()
    name["given_name"] = full_name[0]
    if len(full_name) >= 2:
        name["family_name"] = full_name[-1]
    if len(full_name) >= 3:
        name["middle_name"] = " ".join(full_name[1:-1])

    return name
