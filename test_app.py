import unittest
from app import app

class TestApp(unittest.TestCase):

    def test_header(self):
        """Test that the header is present."""

        header = str(app.layout.children[0].children)
        self.assertEqual(header, "H1('Sales Data Visualizer')")

    def test_visualizer(self):
        """Test that the line chart visualizer is present."""

        visualizer = app.layout.children[2].id
        self.assertEqual(visualizer, 'line-chart-container')

    def test_region_picker(self):
        """Test that the region picker is present."""

        region_picker = app.layout.children[1].id
        self.assertEqual(region_picker, 'region-tabs')
