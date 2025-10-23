# Contributing to AI Live Genie

Thank you for your interest in contributing to AI Live Genie! This document provides guidelines for contributing to the project.

## Code of Conduct

- Be respectful and inclusive
- Welcome newcomers and help them learn
- Focus on constructive feedback
- Respect differing viewpoints and experiences

## How to Contribute

### Reporting Bugs

If you find a bug, please open an issue with:
- A clear, descriptive title
- Steps to reproduce the issue
- Expected vs actual behavior
- Your environment (OS, Python version, etc.)
- Any relevant error messages or logs

### Suggesting Features

We welcome feature suggestions! Please:
- Check existing issues to avoid duplicates
- Describe the feature and its use case
- Explain why it would be valuable
- Consider implementation details if possible

### Pull Requests

1. **Fork the repository** and create your branch from `main`
2. **Make your changes** following our coding standards
3. **Add tests** for new functionality
4. **Update documentation** if needed
5. **Run tests** to ensure everything works
6. **Submit a pull request** with a clear description

### Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/aI-lIVE-genie.git
cd aI-lIVE-genie

# Install in development mode
pip install -e ".[dev]"

# Run tests
python -m pytest tests/

# Run linting
black src/ tests/
pylint src/
```

## Coding Standards

### Python Style

- Follow [PEP 8](https://pep8.org/) guidelines
- Use meaningful variable and function names
- Add docstrings to all public functions and classes
- Use type hints where appropriate
- Keep functions focused and small
- Maximum line length: 100 characters

### Documentation

- Update README.md for user-facing changes
- Update API_DOCUMENTATION.md for API changes
- Add inline comments for complex logic
- Include examples in docstrings

### Testing

- Write unit tests for new features
- Maintain test coverage above 80%
- Test edge cases and error conditions
- Use descriptive test names

### Commit Messages

Use clear, descriptive commit messages:

```
Add earnings calculator CLI command

- Implement calculate_earnings function
- Add command-line argument parsing
- Include formatting for output display
```

## Project Structure

```
aI-lIVE-genie/
├── src/
│   └── ai_live_genie/     # Main package
│       ├── __init__.py
│       ├── memory_manager.py
│       ├── streaming_data.py
│       ├── api_server.py
│       └── cli.py
├── tests/                  # Test files
├── examples/              # Example scripts
├── docs/                  # Documentation
└── data/                  # Data storage (gitignored)
```

## Adding New Platforms

To add a new streaming platform:

1. Add platform data to `streaming_data.py`
2. Include payout rates and requirements
3. Add conversion rate data if available
4. Update tests
5. Update documentation

## Release Process

1. Update version in `pyproject.toml` and `src/ai_live_genie/__init__.py`
2. Update CHANGELOG.md
3. Run full test suite
4. Create a GitHub release with tag
5. Build and publish to PyPI (maintainers only)

## Questions?

Feel free to open an issue for questions or join discussions in existing issues.

## Recognition

All contributors will be recognized in our README.md. Thank you for helping make AI Live Genie better!
