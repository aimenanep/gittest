from django.test import TestCase
from .models import Post



class PostTest(TestCase):

    def setUp(self):
        self.post=Post.objects.create(title="first title",slug="first-title",description="first description")
        print("Setup testing posts.....")


    def test_post_model(self):
        d=self.post
        print("testing post model .....")
        print(f"the post  {d.title} {d.slug} {d.description}" )


        self.assertTrue(isinstance(d,Post)) 

        print(self.assertEqual(d.title,"first tie"))    