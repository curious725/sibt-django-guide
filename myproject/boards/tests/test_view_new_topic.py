from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from ..models import Board, Topic, Post
from ..views import new_topic


class NewTopicTests(TestCase):
    def setUp(self):
        self.board = Board.objects.create(
            name='Django', description='Django board.'
        )
        self.user = User.objects.create_user(
            username='john',
            email='john@doe.com',
            password='123'
        )

    def test_new_topic_view_successful_status_code(self):
        url = reverse('boards:new_topic', kwargs={'pk': self.board.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_new_topic_view_not_found_status_code(self):
        url = reverse('boards:new_topic', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_new_topic_url_resolves_new_topic_view(self):
        view = resolve('/boards/1/new/')
        self.assertEqual(view.func, new_topic)

    def test_new_topic_contains_link_back_to_board_topics_view(self):
        new_topic_url = reverse('boards:new_topic', kwargs={
                                'pk': self.board.pk})
        board_topics_url = reverse(
            'boards:board_topics', kwargs={'pk': self.board.pk}
        )
        response = self.client.get(new_topic_url)
        self.assertContains(response, 'href="{0}"'.format(board_topics_url))

    def test_csrf(self):
        url = reverse('boards:new_topic', kwargs={'pk': self.board.pk})
        response = self.client.get(url)
        self.assertContains(
            response, 'csrfmiddlewaretoken'
        )

    def test_new_topic_valid_post_data(self):
        url = reverse('boards:new_topic', kwargs={'pk': self.board.pk})
        data = {
            'subject': 'Test title',
            'message': 'Lorem ipsum dolor sit amet'
        }
        response = self.client.post(url, data)
        self.assertTrue(Topic.objects.exists())
        self.assertTrue(Post.objects.exists())

    def test_new_topic_invalid_post_data(self):
        """
        Invalid post data should not redirect
        The expected behaviour is to show the form again with validation errors
        """
        url = reverse('boards:new_topic', kwargs={'pk': self.board.pk})
        response = self.client.post(url, {})
        self.assertEqual(response.status_code, 200)

    def test_new_topic_invalid_post_data_empty_fields(self):
        """
        Invalid post data should not redirect
        The expected behaviour is to show the form again with validation errors
        """
        url = reverse('boards:new_topic', kwargs={'pk': self.board.pk})
        data = {
            'subject': '',
            'message': ''
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Topic.objects.exists())
        self.assertFalse(Post.objects.exists())
