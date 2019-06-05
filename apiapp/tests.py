from django.test import TestCase
from . models import Posts
from django.urls import reverse
class PostsTest(TestCase):
    def createUser(self, fname="Faisal", sname="Semuko", sex="male", amount="100"):
        return Posts.objects.create(
            fname=fname,
            sname=sname,
            sex=sex,
            amount=amount
         )
    #testing the model
    def test_Posts_creation(self):
        created = self.createUser()
        self.assertTrue(isinstance(created, Posts))
        self.assertEqual(created.__str__(), created.fname)
        self.assertEqual(created.sname, 'Semuko')
    #testing the home view

    def test_view_home(self):
        created = self.createUser()
        url = reverse('list-all')
        resp=self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertIn(created.fname, 'Faisal')

    def test_update_post(self):
        post = Posts.objects.create(id=5, fname='Namayanja', sname='Masitula', sex='female', amount='9000000')

        response = self.client.post(
            reverse('update-entry',kwargs={'id':post.id}), 
            {'fname': 'Namayanja', 'sname': 'Masitula', 'sex':'female', 'amount':9000000})
        self.assertEqual(response.status_code, 302)
        post.refresh_from_db()
        self.assertEqual(post.fname, 'Namayanja')
