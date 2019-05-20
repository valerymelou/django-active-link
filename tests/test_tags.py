from django.test import TestCase, override_settings
from django.template import Context, Template
from django.test.client import RequestFactory


class TestActiveLink(TestCase):

    def setUp(self):
        self.client = RequestFactory()

    def test_no_request(self):
        template = Template("""
            {% load active_link_tags %}
            {% active_link 'simple' %}
        """)
        context = Context({'request': None})
        html = template.render(context)
        assert 'active' not in html

    def test_match_defaults(self):
        template = Template("""
            {% load active_link_tags %}
            {% active_link 'simple' %}
        """)
        context = Context({'request': self.client.get('/simple/')})
        html = template.render(context)
        assert 'active' in html

    def test_match_defaults_with_multiple_view_name(self):
        template = Template("""
            {% load active_link_tags %}
            {% active_link 'simple || multiple' %}
        """)
        context0 = Context({'request': self.client.get('/simple/')})
        context1 = Context({'request': self.client.get('/multiple/')})
        html0 = template.render(context0)
        html1 = template.render(context1)
        assert 'active' in html0
        assert 'active' in html1

    def test_match_not_strict(self):
        template = Template("""
            {% load active_link_tags %}
            {% active_link 'simple' %}
        """)
        context = Context({'request': self.client.get('/simple/action/')})
        html = template.render(context)
        assert 'active' in html

    def test_no_match_not_strict(self):
        template = Template("""
            {% load active_link_tags %}
            {% active_link 'simple-action' %}
        """)
        context = Context({'request': self.client.get('/other/action/')})
        html = template.render(context)
        assert 'active' not in html

    def test_no_match_not_strict_with_multiple_view_name(self):
        template = Template("""
            {% load active_link_tags %}
            {% active_link 'simple-action || multiple-action' %}
        """)
        context = Context({'request': self.client.get('/other/action/')})
        html = template.render(context)
        assert 'active' not in html

    def test_match_strict(self):
        template = Template("""
            {% load active_link_tags %}
            {% active_link 'simple-action' strict=True %}
        """)
        context = Context({'request': self.client.get('/simple/action/')})
        html = template.render(context)
        assert 'active' in html

    def test_no_match_strict(self):
        template = Template("""
            {% load active_link_tags %}
            {% active_link 'simple-action' strict=True %}
        """)
        context = Context({'request': self.client.get('/simple/')})
        html = template.render(context)
        assert 'active' not in html

    def test_custom_class(self):
        template = Template("""
            {% load active_link_tags %}
            {% active_link 'simple' 'my-active-class' %}
        """)
        context = Context({'request': self.client.get('/simple/')})
        html = template.render(context)
        assert 'my-active-class' in html

    @override_settings(ACTIVE_LINK_CSS_CLASS='my-active-class')
    def test_settings_css_class(self):
        template = Template("""
            {% load active_link_tags %}
            {% active_link 'simple' %}
        """)
        context = Context({'request': self.client.get('/simple/')})
        html = template.render(context)
        assert 'my-active-class' in html

    @override_settings(ACTIVE_LINK_STRICT=True)
    def test_settings_strict(self):
        template = Template("""
            {% load active_link_tags %}
            {% active_link 'simple-action' %}
        """)
        context = Context({'request': self.client.get('/simple/')})
        html = template.render(context)
        assert 'active' not in html

    def test_match_url_with_kwargs(self):
        template = Template("""
            {% load active_link_tags %}
            {% active_link 'detailed-action' pk=12 %}
        """)
        context = Context({'request': self.client.get('/detailed/action/12/')})
        html = template.render(context)
        assert 'active' in html

    def test_match_url_with_kwargs_with_multiple(self):
        template = Template("""
            {% load active_link_tags %}
            {% active_link 'simple || detailed-action' pk=12 %}
        """)
        context = Context({'request': self.client.get('/detailed/action/12/')})
        html = template.render(context)
        assert 'active' in html
