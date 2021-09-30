from app import app
from refactor import convert
from unittest import TestCase


class ConvertTestCase(TestCase):
    def test_convert(self):
        self.assertEqual(convert('USD', 'USD', 1), 'US$1.0')


class ForexConverterTestCase(TestCase):
    def test_index(self):
        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1>Forex Converter</h1>', html)

    def test_form(self):
        with app.test_client() as client:
            res = client.post(
                '/result', data={'convertFrom': 'USD', 'convertTo': 'USD', 'amount': 1})
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<p>The result is US$1.0</p>', html)

    def test_redirect(self):
        with app.test_client() as client:
            res = client.post(
                '/result', data={'convertFrom': 'test', 'convertTo': 'redirect', 'amount': 1})

            self.assertEqual(res.status_code, 302)
            self.assertEqual(res.location, 'http://localhost/')

    def test_redirect_followed(self):
        with app.test_client() as client:
            res = client.post(
                '/result', data={'convertFrom': 'test', 'convertTo': 'redirect', 'amount': 1}, follow_redirects=True)
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn(
                '<p>Not a valid conversion: TEST =&gt; REDIRECT.</p>', html)
