import factory
from drfecommerce.product.models import Category, Brand, Product


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.sequence(lambda n: "Category_%d" % n)


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand

    name = "test_brand"


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = "test_product"
    description = "test description"
    is_digital = True
    brand = factory.SubFactory(BrandFactory)
    category = factory.SubFactory(CategoryFactory)
    