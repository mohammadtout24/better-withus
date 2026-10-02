from django import forms

OPERATIONAL_CHOICES = [
    ('Yes', 'Yes'),
    ('No', 'No'),
]

SOCIAL_MEDIA_STATUS_CHOICES = [
    ("I don't have any social media accounts yet", "I don't have any social media accounts yet"),
    ("I have social media accounts but I have not launched yet", "I have social media accounts but I have not launched yet"),
]

SERVICE_CHOICES = [
    ('Brand Identity', 'Brand Identity'),
    ('Content Creation', 'Content Creation'),
    ('Websites', 'Websites'),
    ('Business Consulting', 'Business Consulting'),
    ('All of the above', 'All of the above'),
]

INVESTMENT_CHOICES = [
    ('', 'Select ...'),
    ('Under $5,000 / month', 'Under $5,000 / month'),
    ('$5,000 – $15,000 / month', '$5,000 – $15,000 / month'),
    ('$15,000 – $50,000 / month', '$15,000 – $50,000 / month'),
    ('$50,000+ / month', '$50,000+ / month'),
]

REFERRAL_CHOICES = [
    ('Referral', 'Referral'),
    ('LinkedIn', 'LinkedIn'),
    ('Google Search', 'Google Search'),
    ('Instagram', 'Instagram'),
    ('Other', 'Other'),
]


class InquiryForm(forms.Form):
    business_name = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    contact_name = forms.CharField(
        max_length=120,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
    )
    phone = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'tel'}),
    )

    is_operational = forms.ChoiceField(
        label='Is your business currently operational',
        choices=OPERATIONAL_CHOICES,
        widget=forms.RadioSelect,
    )

    social_media_status = forms.ChoiceField(
        label='Your social media accounts status',
        choices=SOCIAL_MEDIA_STATUS_CHOICES,
        widget=forms.RadioSelect,
        required=False,
    )
    social_media_links = forms.CharField(
        label='Enter your social media links (Instagram, Facebook, TikTok)',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        required=False,
    )

    services_interested = forms.MultipleChoiceField(
        label='Services you are interested in',
        choices=SERVICE_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    monthly_investment = forms.ChoiceField(
        label='Expected monthly investment, including our retainer',
        choices=INVESTMENT_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        required=False,
    )

    referral_source = forms.MultipleChoiceField(
        label='How did you hear about us',
        choices=REFERRAL_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
