from django.test import TestCase


class HomePageTest(TestCase):

    def test_index_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_index_page_contains_correct_html(self):
        response = self.client.get('/')
        self.assertContains(response, '<p>Welocme<p>')

    def test_view_uses_correct_template(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_index_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/')
        self.assertNotContains(response, 'Hi there! I should not be on the page.')


class ReservationsPageTest(TestCase):

    def test_reservations_view_url_and_status(self):
        response = self.client.get('/reservations/')
        self.assertEquals(response.status_code, 200)

    def test_reservations_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/reservations/')
        self.assertNotContains(response, 'Hi there! I should not be on the page.')

    def test_reservations_view_headers(self):
        response = self.client.get('/reservations/')
        hearders = {'Content-Type': 'application/json',
                    'Vary': 'Accept, Cookie',
                    'Allow': 'GET, HEAD, OPTIONS',
                    'X-Frame-Options': 'DENY', 'Content-Length': '2',
                    'X-Content-Type-Options': 'nosniff',
                    'Referrer-Policy': 'same-origin',
                    'Cross-Origin-Opener-Policy': 'same-origin'}
        self.assertEquals(response.headers, hearders)
