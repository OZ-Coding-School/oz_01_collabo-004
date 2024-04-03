from django.db import models
from common.models import CommonModel
from products.models import Product
from users.models import User


class Category(CommonModel):
    name = models.CharField(max_length=20)
    product = models.ManyToManyField(Product)

<<<<<<< Updated upstream
class UserConnector(CommonModel):
=======
class CategoryUserConnector(CommonModel):
>>>>>>> Stashed changes
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)