from django.contrib import admin
from KASIR.models import Kategori, Produk, Penjualan, ItemPenjualan

# Register your models here.
admin.site.register(Kategori)
admin.site.register(Produk)
admin.site.register(Penjualan)
admin.site.register(ItemPenjualan)
# admin.site.register(Employees)
