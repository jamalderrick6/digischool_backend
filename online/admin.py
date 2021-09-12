from django.contrib import admin
from .models import Course, Level, Price, YearRange, Feature


class CourseAdmin(admin.ModelAdmin):
    fields = ['name', 'headline', 'level', 'icon', 'description', 'rating']


class LevelAdmin(admin.ModelAdmin):
    fields = ['name', ]


class PriceAdmin(admin.ModelAdmin):
    fields = ['name', 'age_range', 'amount', 'features']


class YearRangeAdmin(admin.ModelAdmin):
    fields = ['smallest_age',  'highest_age', 'range']


class FeatureAdmin(admin.ModelAdmin):
    fields = ['name', ]


admin.site.register(Course, CourseAdmin)
admin.site.register(Level, LevelAdmin)
admin.site.register(Price, PriceAdmin)
admin.site.register(YearRange, YearRangeAdmin)
admin.site.register(Feature, FeatureAdmin)
