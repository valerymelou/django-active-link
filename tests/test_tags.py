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
