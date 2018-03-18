from django.test import TestCase
from django.urls import resolve
from graph.views import index, graph_display, all_path, path_length, less_times, equal_times, less_distance,shortest_path

# Create your tests here.

# urls - > views test
class PageTest(TestCase):
    def test_rool_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, index)
    
    def test_graphDisplay_resolves_to_graph_display_view(self):
        found = resolve('/graph/graphDisplay/')
        self.assertEqual(found.func, graph_display)

    def test_pathLength_resolves_to_path_length_view(self):
        found = resolve('/graph/pathLength/')
        self.assertEqual(found.func, path_length)

    def test_shortestPath_resolves_to_shortest_path_view(self):
        found = resolve('/graph/shortestPath/')
        self.assertEqual(found.func, shortest_path)

    def test_allPath_resolves_to_all_path_view(self):
        found = resolve('/graph/allPath/')
        self.assertEqual(found.func, all_path)

    def test_lessTimes_resolves_to_less_times_view(self):
        found = resolve('/graph/lessTimes/')
        self.assertEqual(found.func, less_times)

    def test_equalTimes_resolves_to_equal_times_view(self):
        found = resolve('/graph/equalTimes/')
        self.assertEqual(found.func, equal_times)

    def test_lessDistance_resolves_to_less_Distance_view(self):
        found = resolve('/graph/lessDistance/')
        self.assertEqual(found.func, less_distance)


