from django.db import models

from common.models import CommonModel
from common.utils import get_random_id
from products.models import Product
from users.models import User


def upload_to_review_image(instance, filename: str) -> str:  # type: ignore
    # 파일명은 랜덤한 8자리의 문자열과 업로드한 파일이름을 조합해서 만듦(유일성 보장)
    # 상품별로 리뷰 이미지를 분류
    return f"reviews/{instance.product.name}/images/{get_random_id()} + {filename}"


class ProductReview(CommonModel):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=500)
    image_url = models.ImageField(null=True, upload_to=upload_to_review_image, default=None)
    status = models.BooleanField(default=True)
    view_count = models.IntegerField(default=0)

    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
