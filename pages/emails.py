import logging

import requests
from django.conf import settings

logger = logging.getLogger(__name__)

RESEND_API_URL = 'https://api.resend.com/emails'


def send_inquiry_email(contact_message):
    """Send a notification email via Resend's HTTP API.

    Uses the HTTP API rather than SMTP so this also works on hosts (e.g.
    PythonAnywhere's free tier) that block raw SMTP but allow HTTPS to
    whitelisted domains.
    """
    if not settings.RESEND_API_KEY:
        logger.info("RESEND_API_KEY not set; skipping inquiry email.")
        return

    body = (
        f"Business: {contact_message.business_name}\n"
        f"Contact: {contact_message.contact_name} <{contact_message.email}>\n"
        f"Phone: {contact_message.phone or 'n/a'}\n\n"
        f"Operational: {contact_message.is_operational}\n"
        f"Social media status: {contact_message.social_media_status or 'n/a'}\n"
        f"Social media links: {contact_message.social_media_links or 'n/a'}\n\n"
        f"Services interested: {contact_message.services_interested or 'n/a'}\n"
        f"Monthly investment: {contact_message.monthly_investment or 'n/a'}\n"
        f"Heard about us via: {contact_message.referral_source or 'n/a'}\n"
    )

    try:
        response = requests.post(
            RESEND_API_URL,
            headers={'Authorization': f'Bearer {settings.RESEND_API_KEY}'},
            json={
                'from': settings.DEFAULT_FROM_EMAIL,
                'to': [settings.CONTACT_EMAIL],
                'subject': f"New inquiry: {contact_message.business_name}",
                'text': body,
            },
            timeout=10,
        )
        if not response.ok:
            logger.warning(
                "Resend API returned %s: %s", response.status_code, response.text
            )
    except requests.RequestException:
        logger.exception("Failed to send inquiry email via Resend.")
