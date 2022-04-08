from django.db import models

class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"
    name = models.CharField(max_length=300)

    def makeJson(self):
        return{
            'id': self.id,
            'name': self.name
        }

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=300)
    price = models.FloatField(default=0)
    description = models.TextField(default='')
    count = models.IntegerField()
    isActive = models.BooleanField()
    cat_id = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    # link = models.CharField(max_length=600, default='')
    # imgLink = models.CharField(max_length=600, default = '')
    # rate = models.IntegerField(default=0)
    # likes = models.IntegerField(default=0)
    # catId = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def makeJson(self):
        return{
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'count': self.count,
            'isActive': self.isActive,
            'cat_id' : self.cat_id.id
        }

        # return{
        #     'id': self.id,
        #     'name': self.name,
        #     'price': self.price,
        #     'desc': self.desc,
        #     'count': self.count,
        #     'isActive': self.isActive,
        #     'link': self.link,
        #     'imgLink':self.imgLink,
        #     'rate' : self.rate,
        #     'likes' : self.likes,
        #     'catId' : self.catId
        # }


