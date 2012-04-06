# coding=utf-8
from django.db import models
from django.forms import ModelForm

class brand(models.Model):
    name = models.CharField('Navn', max_length=25, unique=True)
    home_page = models.URLField('Hjemmeside', max_length=25, blank=True, null=True)
    email_address = models.EmailField('E-mail-adresse', blank=True, null=True)
    description = models.TextField('Beskrivelse', blank=True, null=True)
    only_vegan_products = models.BooleanField('Firmaet saelger udelukkende veganske produkter')
    verified = models.BooleanField('Sæt hak i dette felt for at godkende informationerne')
    last_updated = models.DateTimeField('Senest opdateret.', auto_now=True, editable=False)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']


class manufacturer(models.Model):
    name = models.CharField('Navn', max_length=25, unique=True)
    home_page = models.URLField('Hjemmeside', max_length=25, blank=True, null=True)
    email_address = models.EmailField('E-mail-adresse', blank=True, null=True)
    description = models.TextField('Beskrivelse', blank=True, null=True)
    only_vegan_products = models.BooleanField('Producenten fremstiller udelukkende veganske produkter.')
    verified = models.BooleanField('Sæt hak i dette felt for at godkende informationerne')
    last_updated = models.DateTimeField('Senest opdateret.', auto_now=True, editable=False)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']


class store(models.Model):
    name = models.CharField('Navn', max_length=25, unique=True)
    home_page = models.URLField('Hjemmeside', max_length=25, blank=True, null=True)
    email_address = models.EmailField('E-mail-adresse', blank=True, null=True)
    description = models.TextField('Beskrivelse', blank=True, null=True)
    only_vegan_products = models.BooleanField('Forretningen sælger udelukkende veganske produkter.')
    verified = models.BooleanField('Sæt hak i dette felt for at godkende informationerne?')
    last_updated = models.DateTimeField('Senest opdateret.', auto_now=True, editable=False)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']


class ingredient(models.Model):
    VEGAN_CHOICES = (
        ('V', 'Vegansk'),
        ('P', 'Potentielt vegansk'),
        ('I', 'Ikke vegansk'),
    )
    vegan = models.CharField('Vegansk', max_length=1, choices=VEGAN_CHOICES)
    name = models.CharField('Navn', max_length=35, unique=True)
    alias1 = models.CharField('Alias 1', max_length=35, blank=True, null=True)
    alias2 = models.CharField('Alias 2', max_length=35, blank=True, null=True)
    alias3 = models.CharField('Alias 3', max_length=35, blank=True, null=True)
    description = models.TextField('Beskrivelse', blank=True, null=True)
    verified = models.BooleanField('Sæt hak i dette felt for at godkende informationerne')
    last_updated = models.DateTimeField('Senest opdateret.', auto_now=True, editable=False)


    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']


class product(models.Model):
    VEGAN_CHOICES = (
        ('V', 'Vegansk'),
        ('P', 'Potentielt vegansk'),
        ('I', 'Ikke vegansk'),
    )
    vegan = models.CharField('Vegansk', max_length=1, choices=VEGAN_CHOICES)
    name = models.CharField('Navn', max_length=50)
    brands = models.ForeignKey(brand, verbose_name='Mærke')
    manufacturers = models.ForeignKey(manufacturer, verbose_name='Producent')
    stores = models.ManyToManyField(store, verbose_name='Hvilke forretninger kan produktet fås i?')
    ingredients = models.ManyToManyField(ingredient, verbose_name='Ingredienser')
#    picture = models.ImageField(upload_to='user_static')
    brand_manufacturer_contacted = models.TextField('Svar fra firmaet eller producenten bag ang. kilden til ingredienserne', blank=True, null=True)
    bio = models.BooleanField('Økologisk')
    fair_trade = models.BooleanField('Fair trade')
    gluten = models.NullBooleanField('Indeholder gluten')
    soy = models.NullBooleanField('Indeholder soja')
    nuts = models.NullBooleanField('Indeholder nødder')
    verified = models.BooleanField('Sæt hak i dette felt for at godkende informationerne')
    last_updated = models.DateTimeField('Senest opdateret.', auto_now=True, editable=False)


    def __unicode__(self):
        return self.name

    def csstags(self):
      cs = []
      if self.vegan == 'V':
        cs.append("vegan")
      elif self.vegan == 'P':
        cs.append("potvegan")
      elif self.vegan == 'I':
        cs.append("notvegan")
      if self.bio:
        cs.append("bio")
      if self.fair_trade:
        cs.append("fairtrade")

      return " ".join(cs)

    class Meta:
        ordering = ['name']
        unique_together = ("name", "brands")



# Forms:

class productForm(ModelForm):
    class Meta:
        model = product

class brandForm(ModelForm):
    class Meta:
        model = brand

class manufacturerForm(ModelForm):
    class Meta:
        model = manufacturer

class ingredientForm(ModelForm):
    class Meta:
        model = ingredient

class storeForm(ModelForm):
    class Meta:
        model = store
