from django.test import TestCase
from app.models.panel import Panel
from app.models.test import AlternateName, Test
from app.models.organ import Organ


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

    def test_altnamereturns200(self):
        alt = AlternateName(name='AST')
        alt.save()
        response = self.client.get(f'/alternatenames/{alt.id}')
        self.assertEqual(response.status_code, 200)

    def test_tests200(self):
        labtest = Test(name='Aspartate Aminotransferase')
        labtest.save()
        response = self.client.get(f'/tests/{labtest.id}')
        self.assertEqual(response.status_code, 200)

    def test_organ200(self):
        organ = Organ(name='Liver')
        organ.save()
        response = self.client.get(f'/organs/{organ.id}')
        self.assertEqual(response.status_code, 200)

    def test_panel_invalid_id_returns_404(self):
        invalid_panel_id = 99999
        response = self.client.get(f'/panels/{invalid_panel_id}')
        self.assertEqual(response.status_code, 404)

    def test_alternate_name_invalid_id_returns_404(self):
        invalid_alt_id = 99999
        response = self.client.get(f'/alternatenames/{invalid_alt_id}')
        self.assertEqual(response.status_code, 404)

    def test_test_invalid_id_returns_404(self):
        invalid_test_id = 99999
        response = self.client.get(f'/tests/{invalid_test_id}')
        self.assertEqual(response.status_code, 404)

    def test_organ_invalid_id_returns_404(self):
        invalid_organ_id = 99999
        response = self.client.get(f'/organs/{invalid_organ_id}')
        self.assertEqual(response.status_code, 404)

    def test_panel_non_integer_id_returns_400(self):
        non_int_panel_id = 'abc'
        response = self.client.get(f'/panels/{non_int_panel_id}')
        self.assertEqual(response.status_code, 400)

    def test_test_non_integer_id_returns_400(self):
        non_int_test_id = 'xyz'
        response = self.client.get(f'/tests/{non_int_test_id}')
        self.assertEqual(response.status_code, 400)

    def test_organ_non_integer_id_returns_400(self):
        non_int_organ_id = '123abc'
        response = self.client.get(f'/organs/{non_int_organ_id}')
        self.assertEqual(response.status_code, 400)

    def test_invalidnamereturns404(self):
        lab = "vitamin x"
        response = self.client.get(f'/tests/{lab}')
        self.assertEqual(response.status_code, 400)
