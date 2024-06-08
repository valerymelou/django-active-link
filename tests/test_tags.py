from django.template.loader import render_to_string
from django.test import Client, TestCase, override_settings
from django.urls import reverse


class TestActiveLink(TestCase):
    def setUp(self):
        self.client = Client()

    def reverse_helper(self, reverse_url_string, kwargs=None):
        if kwargs:
            reverse_url = reverse(reverse_url_string, kwargs=kwargs)
        else:
            reverse_url = reverse(reverse_url_string)
        response = self.client.get(reverse_url)
        content = response.content.decode()
        return content

    def test_no_request(self):
        html = render_to_string("simple.html")
        self.assertNotIn('<div class="active">', html)

    def test_no_request_inactive_class(self):
        html = render_to_string("simple.html")
        self.assertInHTML('<div class="not-active">', html)

    def test_match_defaults(self):
        content = self.reverse_helper("simple")
        self.assertInHTML('<div class="active">', content)

    def test_match_strict(self):
        content = self.reverse_helper("simple-action")
        self.assertInHTML('<div class="active">', content)

    def test_no_match_strict(self):
        content = self.reverse_helper("simple-strict-no-match")
        self.assertNotIn('<div class="active">', content)

    def test_custom_class(self):
        content = self.reverse_helper("simple-custom-class")
        self.assertInHTML('<div class="my-active-class">', content)

    @override_settings(ACTIVE_LINK_CSS_CLASS="my-active-class")
    def test_settings_css_active_class(self):
        content = self.reverse_helper("simple")
        self.assertInHTML('<div class="my-active-class">', content)

    @override_settings(ACTIVE_LINK_CSS_INACTIVE_CLASS="my-not-active-class")
    def test_settings_css_not_active_class(self):
        content = self.reverse_helper("simple-strict-no-match")
        self.assertInHTML('<div class="my-not-active-class">', content)

    @override_settings(ACTIVE_LINK_STRICT=True)
    def test_settings_strict(self):
        content = self.reverse_helper("simple-settings-strict")
        self.assertNotIn('<div class="active">', content)

    def test_match_url_with_kwargs(self):
        content = self.reverse_helper("detailed-action", {"pk": 12})
        self.assertInHTML('<div class="active">', content)

    def test_match_url_with_kwargs_with_multiple(self):
        content = self.reverse_helper("detailed-action-multiple", {"pk": 12})
        self.assertInHTML('<div class="active">', content)

    def test_match_url_with_kwargs_with_multiple_not_active(self):
        content = self.reverse_helper("detailed-action-not-active", {"pk": 12})
        self.assertInHTML('<div class="not-active">', content)
