from django.contrib import admin

from .models import ContactMessage, Service, TeamMember, Testimonial


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('business_name', 'contact_name', 'email', 'monthly_investment', 'created_at')
    list_filter = ('created_at', 'is_operational', 'monthly_investment')
    search_fields = ('business_name', 'contact_name', 'email', 'services_interested')
    readonly_fields = ('created_at',)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'summary', 'order')
    list_editable = ('order',)


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'order')
    list_editable = ('order',)


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('author', 'company', 'order')
    list_editable = ('order',)
