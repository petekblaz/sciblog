from django import template
import sciblog.settings as scisettings

register = template.Library()

"""
    Returns data from Google Analytics defined in settings.py

    To load in the template:
    {% load analytics %}
    ...
    <!-- Global site tag (gtag.js) - Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id={% ga_tracking_id %}"></script>
    <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());

    gtag('config', '{% ga_tracking_id %}');
    </script>
"""

@register.simple_tag
def ga_tracking_id():
    return scisettings.GA_TRACKING_ID
