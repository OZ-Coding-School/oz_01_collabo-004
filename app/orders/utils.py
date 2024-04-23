from config import constants


def cal_option_price(data) -> int:  # type: ignore
    big_size_price = int(data.get("pet_size_big", 0)) * constants.BIG_SIZE_PET_PRICE
    medium_size_price = int(data.get("pet_size_medium", 0)) * constants.MEDIUM_SIZE_PET_PRICE
    small_size_price = int(data.get("pet_size_small", 0)) * constants.SMALL_SIZE_PET_PRICE
    person_price = int(data.get("people", 0)) * constants.PEOPLE_PRICE
    option_price = big_size_price + medium_size_price + small_size_price + person_price
    return option_price
