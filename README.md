# asgmt-3-programming-design-2025
Assignment 3: Programming Design 2025.

## 01. Define a function `first_n_fizz_buzz()` which returns the first `n` FizzBuzz numbers as a `list`.

Source: <https://en.wikipedia.org/wiki/Fizz_buzz>

```python
def first_n_fizz_buzz(n: int) -> list:
    """
    >>> first_n_fizz_buzz(4)
    [1, 2, 'Fizz', 4]
    >>> first_n_fizz_buzz(6)
    [1, 2, 'Fizz', 4, 'Buzz', 'Fizz']
    >>> first_n_fizz_buzz(15)
    [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'Fizz Buzz']
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 02. Define a function `collect_divisors()` which returns all positive divisors of a given `int`.

Source: <https://en.wikipedia.org/wiki/Divisor>

```python
def collect_divisors(x: int) -> list:
    """
    >>> collect_divisors(1)
    [1]
    >>> collect_divisors(2)
    [1, 2]
    >>> collect_divisors(3)
    [1, 3]
    >>> collect_divisors(4)
    [1, 2, 4]
    >>> collect_divisors(5)
    [1, 5]
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 03. Define a function `find_common_divisors()` which returns the common divisors given 2 integers as a `set`.

Source: <https://en.wikipedia.org/wiki/Divisor>


```python
def find_common_divisors(x: int, y: int) -> set:
    """
    >>> find_common_divisors(3, 5)
    {1}
    >>> find_common_divisors(2, 7)
    {1}
    >>> find_common_divisors(4, 8)
    {1, 2, 4}
    >>> find_common_divisors(18, 24)
    {1, 2, 3, 6}
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 04. Define a function `is_prime()` which returns whether `x` is a prime number or not. You may extend the previous `collect_divisors()` function to solve this problem.

Source: <https://en.wikipedia.org/wiki/Prime_number>

```python
def is_prime(x: int) -> bool:
    """
    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(4)
    False
    >>> is_prime(5)
    True
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 05. Define a function `filter_primes_within_range()` which returns prime numbers within given `a` and `b` where $a < b$. Include `a` or `b` in function output if they are prime numbers.

Source: <https://en.wikipedia.org/wiki/Prime_number>

```python
def filter_primes_within_range(a: int, b: int) -> list:
    """
    >>> filter_primes_within_range(1, 5)
    [2, 3, 5]
    >>> filter_primes_within_range(6, 10)
    [7]
    >>> filter_primes_within_range(11, 15)
    [11, 13]
    >>> filter_primes_within_range(16, 20)
    [17, 19]
    >>> filter_primes_within_range(21, 25)
    [23]
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 06. Define a function `reverse_vowels()` converts the vowels in a word from upper-cased to lower-cased, and from lower-cased to upper-cased.

```python
def reverse_vowels(x: str) -> str:
    """
    >>> reverse_vowels('Luke Skywalker')
    'LUkE SkywAlkEr'
    >>> reverse_vowels('Darth Vadar')
    'DArth VAdAr'
    >>> reverse_vowels('The Avengers')
    'ThE avEngErs'
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 07. Define a function `find_unique_vowels()` which returns the unique vowels as a `set` found in a given `str`.

```python
def find_unique_vowels(x: str) -> set:
    """
    >>> find_unique_vowels("Python")
    {'o'}
    >>> find_unique_vowels("Anaconda")
    {'a', 'o'}
    >>> find_unique_vowels("Programming Design")
    {'a', 'e', 'i', 'o'}
    >>> find_unique_vowels("National Taiwan University")
    {'a', 'e', 'i', 'o', 'u'}
    >>> find_unique_vowels("Giannis Antetokounmpo")
    {'a', 'e', 'i', 'o', 'u'}
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 08. Define a function `count_number_of_each_vowel()` which counts the number of occurrence for each vowel as a `dict` found in a given `str`.

```python
def count_number_of_each_vowel(x: str) -> dict:
    """
    >>> count_number_of_each_vowel("Python")
    {'o': 1}
    >>> count_number_of_each_vowel("Anaconda")
    {'a': 3, 'o': 1}
    >>> count_number_of_each_vowel("Programming Design")
    {'o': 1, 'a': 1, 'i': 2, 'e': 1}
    >>> count_number_of_each_vowel("National Taiwan University")
    {'a': 4, 'i': 4, 'o': 1, 'u': 1, 'e': 1}
    >>> count_number_of_each_vowel("Giannis Antetokounmpo")
    {'i': 2, 'a': 2, 'e': 1, 'o': 3, 'u': 1}
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 09. Define a function `is_palindrome()` which reverses the input text and tells us whether it is a palindrome or not.

Source: <https://en.wikipedia.org/wiki/Palindrome>

```python
def is_palindrome(x: str) -> tuple:
    """
    >>> is_palindrome('eye')
    ('eye', True)
    >>> is_palindrome('dye')
    ('eyd', False)
    >>> is_palindrome('refer')
    ('refer', True)
    >>> is_palindrome('ravel')
    ('levar', False)
    """
    ## BEGIN SOLUTION
    
    ### END SOLUTION
```

## 10. Define a function named `reverse_keys_values_from_dict()` which reverses a given dictionary's key-value pairs.

```python
def reverse_keys_values_from_dict(x: dict) -> dict:
    """
    >>> reverse_keys_values_from_dict({'twn': 'Taiwan'})
    {'Taiwan': 'twn'}
    >>> reverse_keys_values_from_dict({'twn': 'Taiwan', 'jpn': 'Japan'})
    {'Taiwan': 'twn', 'Japan': 'jpn'}
    >>> reverse_keys_values_from_dict({'twn': 'Taiwan', 'jpn': 'Japan', 'ltu': "Lithuania"})
    {'Taiwan': 'twn', 'Japan': 'jpn', 'Lithuania': 'ltu'}
    >>> reverse_keys_values_from_dict({'twn': 'Taiwan', 'jpn': 'Japan', 'ltu': "Lithuania", 'svn': 'Slovenia'})
    {'Taiwan': 'twn', 'Japan': 'jpn', 'Lithuania': 'ltu', 'Slovenia': 'svn'}
    """
    ### BEGIN SOLUTION

    ### END SOLUTION
```