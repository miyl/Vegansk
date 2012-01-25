# coding=utf-8
from django.db import models


class brand(models.Model):
    name = models.CharField('Navn', max_length=25, unique=True)
    home_page = models.URLField('Hjemmeside', max_length=25, blank=True)
    email_address = models.EmailField('E-mail-adresse', blank=True)
    description = models.TextField('Beskrivelse', blank=True)
    only_vegan_products = models.BooleanField('Firmaet saelger udelukkende veganske produkter', blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']


class manufacturer(models.Model):
    name = models.CharField('Navn', max_length=25, unique=True)
    home_page = models.URLField('Hjemmeside', max_length=25, blank=True)
    email_address = models.EmailField('E-mail-adresse', blank=True)
    description = models.TextField('Beskrivelse', blank=True)
    only_vegan_products = models.BooleanField('Producenten fremstiller udelukkende veganske produkter.', blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']


class store(models.Model):
    name = models.CharField('Navn', max_length=25, unique=True)
    home_page = models.URLField('Hjemmeside', max_length=25, blank=True)
    email_address = models.EmailField('E-mail-adresse', blank=True)
    description = models.TextField('Beskrivelse', blank=True)
    only_vegan_products = models.BooleanField('Forretningen sælger udelukkende veganske produkter.', blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']


class ingredient(models.Model):
    VEGAN_CHOICES = (
        ('Vegansk', 'Vegansk'),
        ('Potentielt vegansk', 'Potentielt vegansk'),
        ('Ikke vegansk', 'Ikke vegansk'),
    )
    vegan = models.CharField('Vegansk', max_length=35, choices=VEGAN_CHOICES)
    name = models.CharField('Navn', max_length=35, unique=True)
    description = models.TextField('Beskrivelse', blank=True)


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
    brand_manufacturer_contacted = models.TextField('Svar fra firmaet eller producenten bag ang. kilden til ingredienserne', blank=True)
    gluten = models.NullBooleanField('Indeholder gluten')
    soy = models.NullBooleanField('Indeholder soja')
    nuts = models.NullBooleanField('Indeholder nødder')
    bio = models.BooleanField('Økologisk')
    fair_trade = models.BooleanField('Fair trade')
    last_updated = models.DateTimeField('Senest opdateret.', auto_now=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']

