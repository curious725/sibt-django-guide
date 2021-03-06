from django.urls import reverse, resolve
from django.test import TestCase

from ..models import Board
from ..views import board_topics


class BoardTopicTests(TestCase):
    def setUp(self):
        self.board = Board.objects.create(
            name='Django', description='Django board.')

    def test_board_topics_view_success_status_code(self):
        url = reverse('boards:board_topics', kwargs={'pk': self.board.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_board_topics_view_not_found_status_code(self):
        url = reverse('boards:board_topics', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_board_topics_url_resolves_board_topics_view(self):
        view = resolve('/boards/1/')
        self.assertEquals(view.func, board_topics)

    def test_board_topics_page_contains_link_back_to_homepage(self):
        homepage_url = reverse('home')
        url = reverse('boards:board_topics', kwargs={'pk': self.board.pk})
        response = self.client.get(url)
        self.assertContains(
            response, 'href="{0}"'.format(homepage_url)
        )

    def test_board_topics_page_contains_link_to_new_topic(self):
        new_topic_url = reverse('boards:new_topic', kwargs={
                                'pk': self.board.pk})
        url = reverse('boards:board_topics', kwargs={'pk': self.board.pk})
        response = self.client.get(url)
        self.assertContains(
            response, 'href="{0}"'.format(new_topic_url)
        )
