from django.contrib import admin
from texonomy.models import Post,Category,Genre
from mptt.admin import MPTTModelAdmin

"""
admin.site.register(Post)
admin.site.register(Category) 
"""

from mptt.admin import DraggableMPTTAdmin
#admin.site.register(Genre,MPTTModelAdmin)
admin.site.register(Post)
admin.site.register(Category, MPTTModelAdmin )

admin.site.register(
    Genre,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
        # ...more fields if you feel like it...
    ),
    list_display_links=(
        'indented_title',
    ),
)