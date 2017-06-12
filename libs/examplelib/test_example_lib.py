from unittest import TestCase
from ExampleLibrary import ExampleLibrary

class TestExampleLibrary(TestCase):
    def setUp(self):
        self.lib = ExampleLibrary()

    def tearDown(self):
        self.lib = None

    def test_example(self):
        self.assertTrue(self.lib.library_keyword())