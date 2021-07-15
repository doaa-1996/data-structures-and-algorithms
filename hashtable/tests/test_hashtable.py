from hashtable import __version__


def test_version():
    assert __version__ == '0.1.0'

import pytest
from contextlib import contextmanager

from hashtable.hashtable import HashTable

def test_hash_table():
  assert HashTable

def test_linked_list():
  assert HashTable._LinkedList

def test_node():
  assert HashTable._LinkedList._Node

@contextmanager
def does_not_raise():
  yield

@pytest.fixture()
def LL():
  return HashTable._LinkedList()

@pytest.fixture()
def populated_LL(LL):
  for i in range(20):
    LL.add(i , f'The Key is {i}')
  return LL

@pytest.fixture()
def populated_HT():
  ht = HashTable(10)
  for i in range(200):
    ht.add(f'The Key is {i}', i)
  return ht


def test_linked_list_add(LL):
  key, value = 6, 10
  LL.add(key, value)
  assert LL.head.key == key
  assert LL.head.value == value
  assert LL.head.next == None
  LL.add(key*2, value*3)
  assert isinstance(LL.head.next, HashTable._LinkedList._Node)
  assert LL.head.next.key == key*2
  assert LL.head.next.value == value*3

@pytest.mark.parametrize(
  "key,result",
    [
      (10, True),
      (5, True),
      (0, True),
      (19, True),
      (30, False),
      (-2, False),
    ],
)
def test_linked_list_contains(populated_LL, key, result):
  assert populated_LL.contains(key) == result


@pytest.mark.parametrize(
  "key,value,exception",
    [
      (10, 'The Key is 10', does_not_raise()),
      (5, 'The Key is 5', does_not_raise()),
      (0, 'The Key is 0', does_not_raise()),
      (19, 'The Key is 19', does_not_raise()),
      (30, None, pytest.raises(LookupError)),
      (-2, None, pytest.raises(LookupError)),
    ],
)
def test_linked_list_get(populated_LL, key, value, exception):
  with exception:
    assert populated_LL.get(key) == value


@pytest.mark.parametrize(
  "key, index, exception",
    [
      ('One', 310, does_not_raise()),
      ('Location', 723, does_not_raise()),
      ('Aiming for something higher', 811, does_not_raise()),
      ('Things that aren\'t letters 1 @ %', 744, does_not_raise()),
      (25, 115, does_not_raise()),
      (True ,None, pytest.raises(ValueError)),
      ([] ,None, pytest.raises(ValueError)),
    ],
)
def test_hash(key, index, exception):
  hash_table = HashTable()
  with exception:
    hashed = hash_table._hash(key)
    assert hashed == index


@pytest.mark.parametrize(
  "key, value, exception",
    [
      ('One', 310, does_not_raise()),
    ],
)
def test_hash_table_add(key, value, exception):
  ht = HashTable()
  with exception:
    ht.add(key, value)


@pytest.mark.parametrize(
  "key, result",
    [
      ('The Key is 1', True),
      ('The Key is 100', True),
      ('The Key is 299', False),
    ],
)
def test_contains(populated_HT, key, result):
  assert populated_HT.contains(key) == result

@pytest.mark.parametrize(
  "key,value,exception",
    [
      ('The Key is 10', 10, does_not_raise()),
      ('The Key is 150', 150, does_not_raise()),
      ('The Key is 0', 0, does_not_raise()),
      ('This string will fail', None, pytest.raises(LookupError)),
      ('As will this one', None, pytest.raises(LookupError)),
    ],
)
def test_hash_table_get(populated_HT, key, value, exception):
  with exception:
    assert populated_HT.get(key) == value