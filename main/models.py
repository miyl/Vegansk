# coding=utf-8
from django.db import models as m
from django.forms import ModelForm

class brand(m.Model):
    name = m.CharField('Navn', max_length=25, unique=True)
    home_page = m.URLField('Hjemmeside', max_length=25, blank=True, null=True)
    email_address = m.EmailField('E-mail-adresse', blank=True, null=True)
    description = m.TextField('Beskrivelse', blank=True, null=True)
    only_vegan_products = m.BooleanField('Firmaet saelger udelukkende veganske produkter')
    verified = m.BooleanField('Sæt hak i dette felt for at godkende informationerne')
    last_updated = m.DateTimeField('Senest opdateret.', auto_now=True, editable=False)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']


class manufacturer(m.Model):
    name = m.CharField('Navn', max_length=25, unique=True)
    home_page = m.URLField('Hjemmeside', max_length=25, blank=True, null=True)
    email_address = m.EmailField('E-mail-adresse', blank=True, null=True)
    description = m.TextField('Beskrivelse', blank=True, null=True)
    only_vegan_products = m.BooleanField('Producenten fremstiller udelukkende veganske produkter.')
    verified = m.BooleanField('Sæt hak i dette felt for at godkende informationerne')
    last_updated = m.DateTimeField('Senest opdateret.', auto_now=True, editable=False)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']


class store(m.Model):
    name = m.CharField('Navn', max_length=25, unique=True)
    home_page = m.URLField('Hjemmeside', max_length=25, blank=True, null=True)
    email_address = m.EmailField('E-mail-adresse', blank=True, null=True)
    description = m.TextField('Beskrivelse', blank=True, null=True)
    only_vegan_products = m.BooleanField('Forretningen sælger udelukkende veganske produkter.')
    verified = m.BooleanField('Sæt hak i dette felt for at godkende informationerne?')
    last_updated = m.DateTimeField('Senest opdateret.', auto_now=True, editable=False)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']


class ingredient(m.Model):
    VEGAN_CHOICES = (
        ('V', 'Vegansk'),
        ('P', 'Potentielt vegansk'),
        ('I', 'Ikke vegansk'),
    )
    vegan = m.CharField('Vegansk', max_length=1, choices=VEGAN_CHOICES)
    name = m.CharField('Navn', max_length=35, unique=True)
    alias1 = m.CharField('Alias 1', max_length=35, blank=True, null=True)
    alias2 = m.CharField('Alias 2', max_length=35, blank=True, null=True)
    alias3 = m.CharField('Alias 3', max_length=35, blank=True, null=True)
    description = m.TextField('Beskrivelse', blank=True, null=True)
    verified = m.BooleanField('Sæt hak i dette felt for at godkende informationerne')
    last_updated = m.DateTimeField('Senest opdateret.', auto_now=True, editable=False)


    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']


class product(m.Model):
    VEGAN_CHOICES = (
        ('V', 'Vegansk'),
        ('P', 'Potentielt vegansk'),
        ('I', 'Ikke vegansk'),
    )
    vegan = m.CharField('Vegansk', max_length=1, choices=VEGAN_CHOICES)
    name = m.CharField('Navn', max_length=50)
    brands = m.ForeignKey(brand, verbose_name='Mærke')
    manufacturers = m.ForeignKey(manufacturer, verbose_name='Producent')
    stores = m.ManyToManyField(store, verbose_name='Hvilke forretninger kan produktet fås i?')
    ingredients = m.ManyToManyField(ingredient, verbose_name='Ingredienser')
#    picture = m.ImageField(upload_to='user_static')
    brand_manufacturer_contacted = m.TextField('Svar fra firmaet eller producenten bag ang. kilden til ingredienserne', blank=True, null=True)
    bio = m.BooleanField('Økologisk')
    fair_trade = m.BooleanField('Fair trade')
    gluten = m.NullBooleanField('Indeholder gluten')
    soy = m.NullBooleanField('Indeholder soja')
    nuts = m.NullBooleanField('Indeholder nødder')
    verified = m.BooleanField('Sæt hak i dette felt for at godkende informationerne')
    last_updated = m.DateTimeField('Senest opdateret.', auto_now=True, editable=False)


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
