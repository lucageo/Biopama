from geonode.base.models import (ProtectedArea)


class ProtectedAreaAdmin(MediaTranslationAdmin):
    model = ProtectedArea
    list_display_links = ('identifier',)
    list_display = ('identifier', 'description', 'gn_description', 'is_choice')
    if settings.MODIFY_TOPICCATEGORY is False:
        exclude = ('identifier', 'description',)

admin.site.register(ProtectedArea, ProtectedAreaAdmin)
