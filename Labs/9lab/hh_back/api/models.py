from django.db import models

class Company(models.Model):
    class Meta:
        verbose_name_plural = "Companies"

    name = models.CharField(max_length=300)
    description = models.TextField(default='')
    city = models.CharField(max_length=300)
    address = models.TextField(default='')


    def makeJson(self):
        return{
            'id' : self.id,
            'name' : self.name,
            'description' : self.description,
            'city' : self.city,
            'address' : self.address
        }

class Vacancy(models.Model):
    class Meta:
        verbose_name_plural = "Vacancies"

    name = models.CharField(max_length=300)
    description = models.TextField(default='')
    salary = models.FloatField(default=0)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)



    def makeJson(self):
        return{
            'id' : self.id,
            'name' : self.name, 
            'description' : self.description,
            'salary' : self.salary,
            'company' : self.company.id
        }