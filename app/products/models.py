from django.db import models

from common.models import CommonModel
from common.utils import get_random_id


def upload_to_thumbnail(instance: models.Model, filename: str) -> str:
    # 파일명은 랜덤한 8자리의 문자열과 업로드한 파일이름을 조합해서 만듦(유일성 보장)
    return f"products/thumbnails/{get_random_id()} + {filename}"


def upload_to_description(instance: models.Model, filename: str) -> str:
    # 파일명은 랜덤한 8자리의 문자열과 업로드한 파일이름을 조합해서 만듦(유일성 보장)
    return f"products/descriptions/{get_random_id()} + {filename}"


class Product(CommonModel):
    name = models.CharField(max_length=100)
    product_img = models.ImageField(null=True, upload_to=upload_to_thumbnail, default=None)
    description_img = models.ImageField(null=True, upload_to=upload_to_description, default=None)
    description_text = models.TextField(default=None)
    price = models.IntegerField(default=0)
    travel_period = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)
    view_count = models.IntegerField(default=0)
    status = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name
