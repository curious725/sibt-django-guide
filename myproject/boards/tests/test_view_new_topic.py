from django.test import TestCase
from django.urls import reverse, resolve
from ..models import Board
from ..views import new_topic


class NewTopicTests(TestCase):
    def setUp(self):
        self.board = Board.objects.create(
            name='Django', description='Django board.'
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
