from django.db import models


class ContactMessage(models.Model):
    business_name = models.CharField(max_length=150)
    contact_name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)

    is_operational = models.CharField(max_length=10, blank=True)
    social_media_status = models.CharField(max_length=40, blank=True)
    social_media_links = models.TextField(blank=True)

    services_interested = models.CharField(max_length=255, blank=True)
    monthly_investment = models.CharField(max_length=40, blank=True)
    referral_source = models.CharField(max_length=255, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.business_name} — {self.contact_name}"


class Service(models.Model):
    ICON_CHOICES = [
        ('brand-identity', 'Brand Identity'),
        ('content-creation', 'Content Creation'),
        ('websites', 'Websites'),
        ('business-consulting', 'Business Consulting'),
    ]

    title = models.CharField(max_length=100)
    summary = models.CharField(
        max_length=255,
        help_text="Short tagline shown under the title, e.g. 'A clear identity for your business.'",
    )
    bullets = models.TextField(
        blank=True,
        help_text="One bullet point per line.",
    )
    icon_slug = models.CharField(
        max_length=30, choices=ICON_CHOICES, blank=True,
        help_text="Which icon graphic to show for this service.",
    )
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'title']

    def __str__(self):
        return self.title

    @property
    def bullet_list(self):
        return [line.strip() for line in self.bullets.splitlines() if line.strip()]

    @property
    def icon_path(self):
        slug = self.icon_slug or 'business-consulting'
        return f'pages/img/icons/{slug}.svg'


class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='team/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=100)
    company = models.CharField(max_length=100, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.author} — {self.company}"
