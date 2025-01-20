import unittest
from music_store import MusicStore
from exception import InvalidPriceError, InvalidEmailError

class TestMusicStore(unittest.TestCase):

    def setUp(self):
        self.store = MusicStore()

    def test_add_album(self):
        self.store.add_album("Test Album", "Test Artist", 2023, 19.99)
        self.assertEqual(len(self.store.albums), 1)
        self.assertEqual(self.store.albums[0].title, "Test Album")

    def test_update_album(self):
        self.store.add_album("Test Album", "Test Artist", 2023, 19.99)
        self.store.update_album("Test Album", new_title="Updated Album", new_year=2024, new_price=24.99)
        self.assertEqual(self.store.albums[0].title, "Updated Album")
        self.assertEqual(self.store.albums[0].year, 2024)
        self.assertEqual(self.store.albums[0].price, 24.99)

    def test_delete_album(self):
        self.store.add_album("Test Album", "Test Artist", 2023, 19.99)
        self.store.delete_album("Test Album")
        self.assertEqual(len(self.store.albums), 0)

    def test_add_artist(self):
        self.store.add_artist("Test Artist", "Test Genre")
        self.assertEqual(len(self.store.artists), 1)
        self.assertEqual(self.store.artists[0].name, "Test Artist")

    def test_update_artist(self):
        self.store.add_artist("Test Artist", "Test Genre")
        self.store.update_artist("Test Artist", new_name="Updated Artist", new_genre="Updated Genre")
        self.assertEqual(self.store.artists[0].name, "Updated Artist")
        self.assertEqual(self.store.artists[0].genre, "Updated Genre")

    def test_delete_artist(self):
        self.store.add_artist("Test Artist", "Test Genre")
        self.store.delete_artist("Test Artist")
        self.assertEqual(len(self.store.artists), 0)

    def test_add_customer(self):
        self.store.add_customer("Test Customer", "test@example.com")
        self.assertEqual(len(self.store.customers), 1)
        self.assertEqual(self.store.customers[0].name, "Test Customer")

    def test_update_customer(self):
        self.store.add_customer("Test Customer", "test@example.com")
        self.store.update_customer("Test Customer", new_name="Updated Customer", new_email="updated@example.com")
        self.assertEqual(self.store.customers[0].name, "Updated Customer")
        self.assertEqual(self.store.customers[0].email, "updated@example.com")

    def test_delete_customer(self):
        self.store.add_customer("Test Customer", "test@example.com")
        self.store.delete_customer("Test Customer")
        self.assertEqual(len(self.store.customers), 0)

    def test_invalid_price(self):
        with self.assertRaises(InvalidPriceError):
            self.store.add_album("Test Album", "Test Artist", 2023, -10)

    def test_invalid_email(self):
        with self.assertRaises(InvalidEmailError):
            self.store.add_customer("Test Customer", "invalid-email")

if __name__ == '__main__':
    unittest.main()
