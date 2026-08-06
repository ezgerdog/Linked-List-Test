# Linked List Test

A Python implementation of a linked list data structure with manual and randomized tests.

The project demonstrates how a linked list can be created from scratch using `Node` and `LinkedList` classes. It supports adding and removing elements from both ends of the list and verifies the implementation using Python assertions.

## Features

- Add elements to the back of the list
- Add elements to the front of the list
- Remove elements from the back
- Remove elements from the front
- Read the first element
- Read the last element
- Track the current list size
- Run manual unit-style tests
- Run randomized stress tests
- Compare linked list behavior with a standard Python list

## Data Structure

### Node

Each node stores:

- A data value
- A reference to the next node
- A reference to the previous node

```python
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        self.prev = None
```

### LinkedList

The `LinkedList` class stores:

- `_head`: First node in the list
- `_tail`: Last node in the list
- `_size`: Current number of elements

## Supported Operations

### `pushBack(value)`

Adds a new value to the end of the list.

```python
linked_list.pushBack(10)
```

### `pushFront(value)`

Adds a new value to the beginning of the list.

```python
linked_list.pushFront(5)
```

### `popBack()`

Removes the final element from the list.

```python
linked_list.popBack()
```

### `popFront()`

Removes the first element from the list.

```python
linked_list.popFront()
```

### `front()`

Returns the value stored at the beginning of the list.

```python
first_value = linked_list.front()
```

### `back()`

Returns the value stored at the end of the list.

```python
last_value = linked_list.back()
```

### `size()`

Returns the current number of elements.

```python
current_size = linked_list.size()
```

## Testing

The project includes several test functions.

### Push Back Test

```python
testPushBack()
```

Checks whether elements are correctly added to the end of the list.

### Push Front Test

```python
testPushFront()
```

Checks whether elements are correctly added to the beginning of the list.

### Pop Back Test

```python
testPopBack()
```

Checks whether elements are correctly removed from the end of the list.

### Pop Front Test

```python
testPopFront()
```

Checks whether elements are correctly removed from the beginning of the list.

### Randomized Test

```python
randomTest()
```

The randomized test compares the custom linked list with a standard Python list.

It performs multiple sequences of random operations:

```text
200 push operations
100 pop operations
100 push operations
200 pop operations
```

After each operation, the test verifies:

- The first elements are equal
- The last elements are equal
- The sizes are equal

Python `assert` statements are used to detect incorrect behavior.

## Example Usage

```python
linked_list = LinkedList()

linked_list.pushBack(10)
linked_list.pushBack(20)
linked_list.pushFront(5)

print(linked_list.front())
print(linked_list.back())
print(linked_list.size())

linked_list.popFront()
linked_list.popBack()
```

Expected output:

```text
5
20
3
```

## Successful Test Output

When all tests complete without assertion errors, the program prints:

```text
Everything should be fine if you see this
```

## Project Structure

```text
Linked-List-Test/
├── LinkedList Test.py
├── .gitattributes
└── README.md
```

For a cleaner file name, rename:

```text
LinkedList Test.py
```

to:

```text
linked_list_test.py
```

## Running the Project

Clone the repository:

```bash
git clone https://github.com/ezgerdog/Linked-List-Test.git
```

Open the project directory:

```bash
cd Linked-List-Test
```

Run the Python file:

```bash
python linked_list_test.py
```

No external libraries are required.

## Technologies and Concepts

- Python
- Data Structures
- Linked Lists
- Nodes
- Object-Oriented Programming
- Randomized Testing
- Assertions
- Algorithm Testing

## Time Complexity

| Operation | Current Complexity |
|---|---:|
| `pushFront()` | O(1) |
| `pushBack()` | O(1) |
| `popFront()` | O(1) |
| `popBack()` | O(n) |
| `front()` | O(1) |
| `back()` | O(1) |
| `size()` | O(1) |

Although each node contains a `prev` attribute, the current implementation does not update or use it. Therefore, `popBack()` traverses the list from the head and takes O(n) time.

## Current Limitations

- Removing from an empty list is not handled
- Reading the front or back of an empty list causes an error
- The `prev` references are declared but never updated
- `popBack()` requires traversal from the head
- The class does not support iteration
- The class does not include a string representation
- The tests use plain assertions instead of a testing framework
- Method names do not follow standard Python naming conventions

## Possible Improvements

- Implement the list as a complete doubly linked list
- Update the `prev` reference during insertion and removal
- Make `popBack()` operate in O(1) time
- Add empty-list checks
- Raise clear exceptions for invalid operations
- Rename methods using snake_case
- Add an iterator with `__iter__`
- Add `__len__` support
- Add a `__str__` method
- Add insertion and deletion by index
- Add search functionality
- Move tests into a separate file
- Use Python's `unittest` or `pytest`
- Add automated testing with GitHub Actions

## Author

Developed by **Ezgi Erdoğan**

GitHub: [ezgerdog](https://github.com/ezgerdog)
