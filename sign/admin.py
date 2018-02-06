from django.contrib import admin
from django.utils.html import format_html

from sign.models import Signature


def admin_image(obj):
    return format_html("<img src='{}'/>", obj.signature)


class SignatureAdmin(admin.ModelAdmin):
    model = Signature

    admin_image.short_description = "Signature"
    admin_image.admin_order_field = 'last_name'

    list_display = ["first_name", "last_name", admin_image, ]


admin.site.register(Signature, SignatureAdmin)
