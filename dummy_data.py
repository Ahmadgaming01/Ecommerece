import os , django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()
from faker import Faker
import random
from products.models import Product,Brand



def seed_brand (n):
    fake = Faker()
    images = ['1.jpeg','2.jpeg','3.jpeg','4.jpeg','5.jpeg','6.jpeg','7.jpeg','8.jpeg','9.jpeg','10.jpeg','11.jpeg','12.jpeg','13.jpeg','14.jpeg','15.jpeg','16.jpeg']
    for x in range (n):
        Brand.objects.create(
            name = fake.name(),
            image = f'brand/{images[random.randint(0,15)]}'
        )
    print (f'{n} brands was created successfuly')

def seed_products(n):
    fake = Faker()
    images = ['1.jpeg','2.jpeg','3.jpeg','4.jpeg','5.jpeg','6.jpeg','7.jpeg','8.jpeg','9.jpeg','10.jpeg','11.jpeg','12.jpeg','13.jpeg','14.jpeg','15.jpeg','16.jpeg']
    flag_types = [
        "New",
        "Sale",
        "Feature"
    ]
    for x in range (n):
        Product.objects.create(
            name = fake.name(),
            description = fake.text(max_nb_chars = 30000),
            sku = random.randint(100,1000000),
            price = round(random.uniform(20.99,99.99),2),
            subtitle = fake.text(max_nb_chars = 30000),
            image = f'brand/{images[random.randint(0,15)]}',
            brand = Brand.objects.get(id=random.randint(0,99)),
            flag = flag_types[random.randint(0,2)],

            


        )
    print (f'{n} Products was created successfuly')
seed_products(1000)
#seed_brand(100)

