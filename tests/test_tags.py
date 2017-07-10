from django.test import TestCase
from django.template import Context, Template
from django.test.client import RequestFactory


class TestActiveLinkTags(TestCase):

    def setUp(self):
        self.client = RequestFactory()

    def test_active_link_no_request(self):
        template = Template("""
            {% load active_link_tags %}
            {% active_link 'simple' %}
        """)
        context = Context({'request': None})
        html = template.render(context)
        assert 'active' not in html

    def test_active_link_match_defaults(self):
        template = Template("""
            {% load active_link_tags %}
            {% active_link 'simple' %}
        """)
        context = Context({'request': self.client.get('/simple/')})
        html = template.render(context)
        assert 'active' in html

    def test_active_link_match_not_strict(self):
        template = Template("""
            {% load active_link_tags %}
            {% active_link 'simple' %}
        """)
        context = Context({'request': self.client.get('/simple/action/')})
        html = template.render(context)
        assert 'active' in html

    def test_active_link_no_match_not_strict(self):
        template = Template("""
            {% load active_link_tags %}
            {% active_link 'simple-action' %}
        """)
        context = Context({'request': self.client.get('/other/action/')})
        html = template.render(context)
        assert 'active' not in html

    def test_active_link_match_strict(self):
        template = Template("""
            {% load active_link_tags %}
            {% active_link 'simple-action' strict=True %}
        """)
        context = Context({'request': self.client.get('/simple/action/')})
        html = template.render(context)
        assert 'active' in html

    def test_active_link_no_match_strict(self):
        template = Template("""
            {% load active_link_tags %}
            {% active_link 'simple-action' strict=True %}
        """)
        context = Context({'request': self.client.get('/simple/')})
        html = template.render(context)
        assert 'active' not in html

    def test_active_link_custom_class(self):
        template = Template("""
            {% load active_link_tags %}
            {% active_link 'simple' 'my-active-class' %}
        """)
        context = Context({'request': self.client.get('/simple/')})
        html = template.render(context)
        assert 'my-active-class' in html
