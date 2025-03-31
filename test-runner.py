import unittest
import importlib

class TestAssignmentThree(unittest.TestCase):
    def test_01_first_n_fizz_buzz(self):
        self.assertEqual(asgmt.first_n_fizz_buzz(1), [1])
        self.assertEqual(asgmt.first_n_fizz_buzz(2), [1, 2])
        self.assertEqual(asgmt.first_n_fizz_buzz(3), [1, 2, 'Fizz'])
        self.assertEqual(asgmt.first_n_fizz_buzz(4), [1, 2, 'Fizz', 4])
        self.assertEqual(asgmt.first_n_fizz_buzz(6), [1, 2, 'Fizz', 4, 'Buzz', 'Fizz'])
        self.assertEqual(asgmt.first_n_fizz_buzz(15), [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'Fizz Buzz'])
    def test_02_collect_divisors(self):
        self.assertEqual(asgmt.collect_divisors(1), [1])
        self.assertEqual(asgmt.collect_divisors(2), [1, 2])
        self.assertEqual(asgmt.collect_divisors(3), [1, 3])
        self.assertEqual(asgmt.collect_divisors(4), [1, 2, 4])
        self.assertEqual(asgmt.collect_divisors(5), [1, 5])
        self.assertEqual(asgmt.collect_divisors(6), [1, 2, 3, 6])
        self.assertEqual(asgmt.collect_divisors(7), [1, 7])
    def test_03_find_common_divisors(self):
        self.assertEqual(asgmt.find_common_divisors(3, 7), {1})
        self.assertEqual(asgmt.find_common_divisors(3, 5), {1})
        self.assertEqual(asgmt.find_common_divisors(2, 7), {1})
        self.assertEqual(asgmt.find_common_divisors(2, 4), {1, 2})
        self.assertEqual(asgmt.find_common_divisors(4, 8), {1, 2, 4})
        self.assertEqual(asgmt.find_common_divisors(18, 24), {1, 2, 3, 6})
    def test_04_is_prime(self):
        self.assertFalse(asgmt.is_prime(1))
        self.assertTrue(asgmt.is_prime(2))
        self.assertTrue(asgmt.is_prime(3))
        self.assertFalse(asgmt.is_prime(4))
        self.assertTrue(asgmt.is_prime(5))
        self.assertFalse(asgmt.is_prime(6))
        self.assertTrue(asgmt.is_prime(7))
    def test_05_filter_primes_within_range(self):
        self.assertEqual(asgmt.filter_primes_within_range(1, 5), [2, 3, 5])
        self.assertEqual(asgmt.filter_primes_within_range(6, 10), [7])
        self.assertEqual(asgmt.filter_primes_within_range(11, 15), [11, 13])
        self.assertEqual(asgmt.filter_primes_within_range(16, 20), [17, 19])
        self.assertEqual(asgmt.filter_primes_within_range(21, 25), [23])
        self.assertEqual(asgmt.filter_primes_within_range(26, 30), [29])
        self.assertEqual(asgmt.filter_primes_within_range(31, 35), [31])
    def test_06_reverse_vowels(self):
        self.assertEqual(asgmt.reverse_vowels('Luke Skywalker'), 'LUkE SkywAlkEr')
        self.assertEqual(asgmt.reverse_vowels('Darth Vadar'), 'DArth VAdAr')
        self.assertEqual(asgmt.reverse_vowels('The Avengers'), 'ThE avEngErs')
        self.assertEqual(asgmt.reverse_vowels('Python'), 'PythOn')
        self.assertEqual(asgmt.reverse_vowels('Anaconda'), 'anAcOndA')
        self.assertEqual(asgmt.reverse_vowels('aaa'), 'AAA')
        self.assertEqual(asgmt.reverse_vowels('AAA'), 'aaa')
        self.assertEqual(asgmt.reverse_vowels('bbb'), 'bbb')
    def test_07_find_unique_vowels(self):
        self.assertEqual(asgmt.find_unique_vowels("Java"), {'a'})
        self.assertEqual(asgmt.find_unique_vowels("Ruby"), {'u'})
        self.assertEqual(asgmt.find_unique_vowels("Python"), {'o'})
        self.assertEqual(asgmt.find_unique_vowels("Anaconda"), {'a', 'o'})
        self.assertEqual(asgmt.find_unique_vowels("Programming Design"), {'a', 'e', 'i', 'o'})
        self.assertEqual(asgmt.find_unique_vowels("National Taiwan University"), {'a', 'e', 'i', 'o', 'u'})
        self.assertEqual(asgmt.find_unique_vowels("Giannis Antetokounmpo"), {'a', 'e', 'i', 'o', 'u'})
    def test_08_count_number_of_each_vowel(self):
        self.assertEqual(asgmt.count_number_of_each_vowel("Java"), {'a': 2})
        self.assertEqual(asgmt.count_number_of_each_vowel("Ruby"), {'u': 1})
        self.assertEqual(asgmt.count_number_of_each_vowel("Python"), {'o': 1})
        self.assertEqual(asgmt.count_number_of_each_vowel("Anaconda"), {'a': 3, 'o': 1})
        self.assertEqual(asgmt.count_number_of_each_vowel("Programming Design"), {'o': 1, 'a': 1, 'i': 2, 'e': 1})
        self.assertEqual(asgmt.count_number_of_each_vowel("National Taiwan University"), {'a': 4, 'i': 4, 'o': 1, 'u': 1, 'e': 1})
        self.assertEqual(asgmt.count_number_of_each_vowel("Giannis Antetokounmpo"), {'i': 2, 'a': 2, 'e': 1, 'o': 3, 'u': 1})
    def test_09_is_palindrome(self):
        self.assertEqual(asgmt.is_palindrome('eye'), ('eye', True))
        self.assertEqual(asgmt.is_palindrome('dye'), ('eyd', False))
        self.assertEqual(asgmt.is_palindrome('refer'), ('refer', True))
        self.assertEqual(asgmt.is_palindrome('ravel'), ('levar', False))
        self.assertEqual(asgmt.is_palindrome('anna'), ('anna', True))
        self.assertEqual(asgmt.is_palindrome('kayak'), ('kayak', True))
        self.assertEqual(asgmt.is_palindrome('wow'), ('wow', True))
    def test_10_reverse_keys_values_from_dict(self):
        self.assertEqual(asgmt.reverse_keys_values_from_dict({'twn': 'Taiwan'}), {'Taiwan': 'twn'})
        self.assertEqual(asgmt.reverse_keys_values_from_dict({'twn': 'Taiwan', 'jpn': 'Japan'}), {'Taiwan': 'twn', 'Japan': 'jpn'})
        self.assertEqual(asgmt.reverse_keys_values_from_dict({'twn': 'Taiwan', 'jpn': 'Japan', 'ltu': "Lithuania"}), {'Taiwan': 'twn', 'Japan': 'jpn', 'Lithuania': 'ltu'})
        self.assertEqual(asgmt.reverse_keys_values_from_dict({'twn': 'Taiwan', 'jpn': 'Japan', 'ltu': "Lithuania", 'svn': 'Slovenia'}), {'Taiwan': 'twn', 'Japan': 'jpn', 'Lithuania': 'ltu', 'Slovenia': 'svn'})

asgmt = importlib.import_module("asgmt")
suite = unittest.TestLoader().loadTestsFromTestCase(TestAssignmentThree)
runner = unittest.TextTestRunner(verbosity=2)
test_results = runner.run(suite)
number_of_failures = len(test_results.failures)
number_of_errors = len(test_results.errors)
number_of_test_runs = test_results.testsRun
number_of_successes = number_of_test_runs - (number_of_failures + number_of_errors)
print("You've got {} successes among {} questions.".format(number_of_successes, number_of_test_runs))