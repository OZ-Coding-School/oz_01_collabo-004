from rest_framework.request import Request

from config import constants


def check_pet_count(data) -> bool:  # type: ignore
    pet_count = int(data.get("pet", 0))
    size_big = int(data.get("pet_size_big", 0))
    size_medium = int(data.get("pet_size_medium", 0))
    size_small = int(data.get("pet_size_small", 0))

    # 선택된 사이즈의 합계를 계산
    sum_selected_size = size_big + size_medium + size_small

    return pet_count == sum_selected_size


def cal_option_price(data) -> int:  # type: ignore
    big_size_price = int(data.get("pet_size_big", 0)) * constants.BIG_SIZE_PET_PRICE
    medium_size_price = int(data.get("pet_size_medium", 0)) * constants.MEDIUM_SIZE_PET_PRICE
    small_size_price = int(data.get("pet_size_small", 0)) * constants.SMALL_SIZE_PET_PRICE
    person_price = int(data.get("people", 0)) * constants.PEOPLE_PRICE
    sum = big_size_price + medium_size_price + small_size_price + person_price
    return sum
