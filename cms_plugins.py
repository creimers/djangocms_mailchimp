# -*- coding: utf-8 -*-

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from django.conf import settings


class MailchimpPlugin(CMSPluginBase):
    render_template = 'djangocms_mailchimp/mailchimp.html'

    def render(self, context, instance, placeholder):

        MAILCHIMP_API_KEY = getattr(settings, "MAILCHIMP_API_KEY", None)
        MAILCHIMP_ID = getattr(settings, "MAILCHIMP_ID", None)
        MAILCHIMP_PRE = getattr(settings, "MAILCHIMP_PRE", None)

        context.update({
            'instance': instance,
            'api_key': MAILCHIMP_API_KEY,
            'id': MAILCHIMP_ID,
            'pre': MAILCHIMP_PRE
        })

        return context

plugin_pool.register_plugin(MailchimpPlugin)
