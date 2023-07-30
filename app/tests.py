from django.test import TestCase
from app.models.panel import Panel



# Create your tests here.

class URLTests(TestCase):
    def test_testsurl(self):
        response = self.client.get('/tests/')
        self.assertEqual(response.status_code, 200)

    def test_organsurl(self):
        response = self.client.get('/organs/')
        self.assertEqual(response.status_code, 200)

    def test_panelsurl(self):
        response = self.client.get('/panels/')
        self.assertEqual(response.status_code, 200)

    def test_alternatenamesurl(self):
        response = self.client.get('/alternatenames/')
        self.assertEqual(response.status_code, 200)

    def test_panelsidreturns404(self):
        response = self.client.get('/panels/1')
        self.assertEqual(response.status_code, 404)
    
    def test_lipidpanelreturns200(self):
        panel = Panel(name='Lipid Panel')
        panel.save()
        response = self.client.get(f'/panels/{panel.id}')
        self.assertEqual(response.status_code, 200)
