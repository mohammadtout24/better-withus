from django.core.management.base import BaseCommand

from pages.models import Service


class Command(BaseCommand):
    help = "Seed the database with starter service listings for Better WithUs."

    def handle(self, *args, **options):
        services = [
            ('📊', 'Strategy Consulting',
             'Market analysis, competitive positioning, and long-range planning that holds up under pressure-testing.'),
            ('⚙️', 'Operations & Process',
             'Workflow audits, org design, and process automation that removes friction without adding bureaucracy.'),
            ('📈', 'Growth & Marketing',
             'Go-to-market strategy, channel testing, and demand generation built to compound.'),
            ('💰', 'Financial Advisory',
             'Budgeting, fundraising prep, and unit economics that give leadership real visibility.'),
            ('👥', 'Organizational Design',
             "Team structure, hiring plans, and leadership coaching for the stage you're actually at."),
            ('🔄', 'Change Management',
             'Rollout plans and communication frameworks that get real buy-in, not just sign-off.'),
        ]
        for order, (icon, title, summary) in enumerate(services):
            Service.objects.update_or_create(
                title=title, defaults={'icon': icon, 'summary': summary, 'order': order},
            )

        self.stdout.write(self.style.SUCCESS('Seeded services.'))
