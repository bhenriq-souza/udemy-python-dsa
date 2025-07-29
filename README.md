# Python Data Structures and Algorithms (DSA)

This repository compiles the Python code and tests I've created while learning Data Structures and Algorithms. The focus is on clarity, maintainability, and effective demonstration of concepts.

## Project Structure

```bash
.
├── README.md
├── common
│   └── node.py          # Common Node class used in multiple structures
├── linked_list
│   └── linked_list.py   # Implementation of Linked List
├── linked_list_main.py  # Example script demonstrating Linked List usage
├── pyproject.toml       # Project configuration file
├── tests
│   └── test_linked_list.py # Unit tests for Linked List
├── udemy-python-dsa.tree  # Project directory tree
└── uv.lock              # Lock file for UV dependency manager
```

## Dependencies

This project uses [UV](https://github.com/astral-sh/uv) for dependency management.

- **Install dependencies:**

```bash
uv install
```

## Running the Code

Execute scripts using the following command pattern:

```bash
uv run <SCRIPT_NAME>.py
```

### Example

To run the Linked List example:

```bash
uv run linked_list_main.py
```

## Running Tests

Tests are written using Python's built-in `unittest` framework and coverage is measured with `coverage.py`.

- **Run Tests:**

```bash
uv run python -m coverage run --omit "tests/*" -m unittest discover -s tests
```

- **Check Coverage:**

```bash
uv run python -m coverage report -m -i
```

## Coverage Report

After running the tests and checking coverage, you will receive a detailed coverage report showing the percentage of code tested, helping ensure reliability and completeness.

## Contributing

As this is a learning and portfolio-focused project, external contributions aren't being accepted. However, feedback and suggestions are welcome!

## License

This project is licensed under the MIT License.

## References

- [Algorithms for Competitive Programming](https://cp-algorithms.com/)

