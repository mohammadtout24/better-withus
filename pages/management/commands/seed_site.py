from django.core.management.base import BaseCommand

from pages.models import Service


class Command(BaseCommand):
    help = "Seed the database with starter service listings for Better WithUs."

    def handle(self, *args, **options):
        services = [
            (
                'brand-identity',
                'Brand Identity',
                'A clear identity for your business.',
                ['Visual identity', 'Brand guidelines', 'Consistent brand direction'],
            ),
            (
                'content-creation',
                'Content Creation',
                'Content that brings your brand to life.',
                ['Social media content', 'Creative concepts', 'Brand storytelling'],
            ),
            (
                'websites',
                'Websites',
                'A digital home built around your business.',
                ['Website design', 'Website development', 'Clear user experiences'],
            ),
            (
                'business-consulting',
                'Business Consulting',
                'Fresh thinking for your next move.',
                ['Understand your challenges', 'Explore practical solutions', 'Define clear next steps'],
            ),
        ]
        for order, (icon_slug, title, summary, bullets) in enumerate(services):
            Service.objects.update_or_create(
                title=title,
                defaults={
                    'summary': summary,
                    'bullets': '\n'.join(bullets),
                    'icon_slug': icon_slug,
                    'order': order,
                },
            )

        self.stdout.write(self.style.SUCCESS('Seeded services.'))
