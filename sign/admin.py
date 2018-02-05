from django.contrib import admin
from django.utils.html import format_html

from sign.models import Signature


class SignatureAdmin(admin.ModelAdmin):
    model = Signature

    def admin_image(self, obj):
        return format_html("<img src='{}'/>", obj.signature)

    admin_image.short_description = "Signature"
    admin_image.admin_order_field = 'last_name'

    list_display = [admin_image, ]


admin.site.register(Signature, SignatureAdmin)
