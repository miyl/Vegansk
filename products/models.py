# coding=utf-8
from django.db import models as m
from django.forms import ModelForm
from django.contrib.auth.models import User
# For user creation and their passwords:
from django.forms import CharField, Form, PasswordInput


class Brand(m.Model):
    name = m.CharField('Navn', max_length=25, unique=True)
    home_page = m.URLField('Hjemmeside', max_length=25, blank=True, null=True)
    email_address = m.EmailField('E-mail-adresse', blank=True, null=True)
    description = m.TextField('Beskrivelse', blank=True, null=True)
    only_vegan_products = m.BooleanField('Firmaet saelger udelukkende veganske produkter')

    created = m.DateTimeField('Oprettet.', auto_now_add=True, editable=False)
    last_updated = m.DateTimeField('Senest opdateret.', auto_now=True, editable=False)
    added_by = m.ForeignKey(User, verbose_name='Tilføjet af', default=1, editable=False)
    verified = m.BooleanField('Sæt hak i dette felt for at godkende informationerne')

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = "mærke"
        verbose_name_plural = "mærker"


class Manufacturer(m.Model):
    name = m.CharField('Navn', max_length=25, unique=True)
    home_page = m.URLField('Hjemmeside', max_length=25, blank=True, null=True)
    email_address = m.EmailField('E-mail-adresse', blank=True, null=True)
    description = m.TextField('Beskrivelse', blank=True, null=True)
    only_vegan_products = m.BooleanField('Fabrikanten fremstiller udelukkende veganske produkter.')

    created = m.DateTimeField('Oprettet.', auto_now_add=True, editable=False)
    last_updated = m.DateTimeField('Senest opdateret.', auto_now=True, editable=False)
    added_by = m.ForeignKey(User, verbose_name='Tilføjet af', default=1, editable=False)
    verified = m.BooleanField('Sæt hak i dette felt for at godkende informationerne')

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = "fabrikant"
        verbose_name_plural = "fabrikanter"


class Store(m.Model): 
    name = m.CharField('Navn', max_length=25, unique=True)
    home_page = m.URLField('Hjemmeside', max_length=25, blank=True, null=True)
    email_address = m.EmailField('E-mail-adresse', blank=True, null=True)
    description = m.TextField('Beskrivelse', blank=True, null=True)
    only_vegan_products = m.BooleanField('Forretningen sælger udelukkende veganske produkter.')
    created = m.DateTimeField('Oprettet.', auto_now_add=True, editable=False)
    last_updated = m.DateTimeField('Senest opdateret.', auto_now=True, editable=False)
    added_by = m.ForeignKey(User, verbose_name='Tilføjet af', default=1, editable=False)
    verified = m.BooleanField('Sæt hak i dette felt for at godkende informationerne?')

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = "forretning"
        verbose_name_plural = "forretninger"


class Ingredient(m.Model):
    VEGAN_CHOICES = (
        ('V', 'Vegansk'),
        ('P', 'Potentielt vegansk'),
        ('N', 'Ikke vegansk'),
    )
    vegan = m.CharField('Vegansk', max_length=1, choices=VEGAN_CHOICES)
    name = m.CharField('Navn', max_length=35, unique=True)
    alias1 = m.CharField('Alias 1', max_length=35, blank=True, null=True)
    alias2 = m.CharField('Alias 2', max_length=35, blank=True, null=True)
    alias3 = m.CharField('Alias 3', max_length=35, blank=True, null=True)
    description = m.TextField('Beskrivelse', blank=True, null=True)

    created = m.DateTimeField('Oprettet.', auto_now_add=True, editable=False)
    last_updated = m.DateTimeField('Senest opdateret.', auto_now=True, editable=False)
    added_by = m.ForeignKey(User, verbose_name='Tilføjet af', default=1, editable=False)
    verified = m.BooleanField('Sæt hak i dette felt for at godkende informationerne')


    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = "ingrediens"
        verbose_name_plural = "ingredienser"


class Product(m.Model):
    VEGAN_CHOICES = (
        ('V', 'Vegansk'),
        ('P', 'Potentielt vegansk'),
        ('N', 'Ikke vegansk'),
    )
    vegan = m.CharField('Vegansk', max_length=1, choices=VEGAN_CHOICES)
    name = m.CharField('Navn', max_length=50)
    brands = m.ForeignKey(Brand, verbose_name='Mærke')
    manufacturers = m.ForeignKey(Manufacturer, verbose_name='Producent')
    stores = m.ManyToManyField(Store, verbose_name='Hvilke forretninger kan produktet fås i?')
    ingredients = m.ManyToManyField(Ingredient, verbose_name='Ingredienser')
    picture = m.ImageField(upload_to='product_images', verbose_name='billede', blank=True, null=True)
    brand_manufacturer_contacted = m.TextField('Svar fra firmaet eller producenten bag ang. kilden til ingredienserne', blank=True, null=True)
    bio = m.BooleanField('Økologisk')
    fair_trade = m.BooleanField('Fair trade')
    gluten = m.NullBooleanField('Indeholder gluten')
    soy = m.NullBooleanField('Indeholder soja')
    nuts = m.NullBooleanField('Indeholder nødder')
    featured = m.NullBooleanField('Hilighted')

    created = m.DateTimeField('Oprettet.', auto_now_add=True, editable=False)
    last_updated = m.DateTimeField('Senest opdateret.', auto_now=True, editable=False)
    added_by = m.ForeignKey(User, verbose_name='Tilføjet af', default=1, editable=False)
    verified = m.BooleanField('Sæt hak i dette felt for at godkende informationerne')


    def __unicode__(self):
        return self.name

    def csstags(self):
      cs = []
      if self.vegan == 'V':
        cs.append("vegan")
      elif self.vegan == 'P':
        cs.append("potvegan")
      elif self.vegan == 'N':
        cs.append("notvegan")
      if self.bio:
        cs.append("bio")
      if self.fair_trade:
        cs.append("fairtrade")

      return " ".join(cs)

    class Meta:
        ordering = ['name']
        unique_together = ("name", "brands")
        verbose_name = "produkt"
        verbose_name_plural = "produkter"






# Forms:

class productForm(ModelForm):
    class Meta:
        model = Product

class brandForm(ModelForm):
    class Meta:
        model = Brand

class manufacturerForm(ModelForm):
    class Meta:
        model = Manufacturer

class ingredientForm(ModelForm):
    class Meta:
        model = Ingredient

class storeForm(ModelForm):
    class Meta:
        model = Store
