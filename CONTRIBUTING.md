# Contributing to AI Live Genie

Thank you for your interest in contributing to AI Live Genie! This document provides guidelines and information for contributors.

## Ways to Contribute

- 🐛 **Report bugs** - Help us identify and fix issues
- 💡 **Suggest features** - Share your ideas for improvements
- 📝 **Improve documentation** - Help make our docs clearer
- 🎨 **Add platform support** - Extend to new streaming platforms
- 🔧 **Fix issues** - Submit pull requests for bug fixes
- ✨ **Add features** - Implement new functionality

## Getting Started

### 1. Fork and Clone

```bash
# Fork the repository on GitHub, then clone your fork
git clone https://github.com/YOUR_USERNAME/aI-lIVE-genie.git
cd aI-lIVE-genie
```

### 2. Set Up Development Environment

```bash
# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install development dependencies (if any)
pip install -e .
```

### 3. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

## Development Guidelines

### Code Style

- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Keep functions focused and single-purpose

### Docstring Format

```python
def example_function(param1: str, param2: int) -> bool:
    """
    Brief description of what the function does.
    
    Args:
        param1: Description of param1
        param2: Description of param2
    
    Returns:
        Description of return value
    
    Raises:
        ValueError: When validation fails
    """
    pass
```

### Type Hints

Always use type hints:

```python
from typing import List, Dict, Optional

def process_data(
    data: List[Dict[str, Any]],
    threshold: Optional[float] = None
) -> Dict[str, Any]:
    pass
```

## Adding a New Platform

To add support for a new streaming platform:

### 1. Update Platform List

Edit `ai_live_genie/platforms/platform_manager.py`:

```python
SUPPORTED_PLATFORMS = [
    "twitch",
    "youtube",
    # ... existing platforms
    "new_platform",  # Add your platform
]
```

### 2. Add System Prompt

Edit `ai_live_genie/models/groq_model.py`:

```python
platform_prompts = {
    # ... existing prompts
    "new_platform": (
        "You are an expert AI assistant for [Platform] streamers. You understand "
        "[platform-specific features and culture]. You provide advice on "
        "[key platform capabilities]."
    ),
}
```

### 3. Add Platform Info

Edit `ai_live_genie/platforms/platform_manager.py`:

```python
platform_info = {
    # ... existing info
    "new_platform": {
        "name": "Platform Name",
        "description": "Description of the platform",
        "monetization": "Monetization methods",
        "features": "Key features"
    },
}
```

### 4. Add Training Templates

Edit `ai_live_genie/config.py`:

```python
TRAINING_TEMPLATES = {
    # ... existing templates
    "new_platform": {
        "system_instructions": [
            "Platform-specific instruction 1",
            "Platform-specific instruction 2",
        ],
        "example_queries": [
            "Example question 1",
            "Example question 2",
        ]
    }
}
```

### 5. Update Documentation

Add platform guide to `docs/PLATFORM_GUIDE.md`:

```markdown
## New Platform

### Key Features
- Feature 1
- Feature 2

### Growth Strategy
1. Strategy point 1
2. Strategy point 2

### Model Usage
\`\`\`python
model = GroqModel(platform="new_platform")
advice = model.get_streaming_advice("Your question")
\`\`\`
```

## Testing

### Run Tests

```bash
python test_package.py
```

### Add Tests

When adding new features, include tests:

```python
def test_new_feature():
    """Test description."""
    # Test implementation
    assert expected == actual
```

## Submitting Changes

### 1. Commit Your Changes

```bash
git add .
git commit -m "Brief description of changes"
```

Commit message format:
- Use present tense ("Add feature" not "Added feature")
- Use imperative mood ("Move cursor to..." not "Moves cursor to...")
- Keep first line under 50 characters
- Add detailed description if needed

Examples:
```
Add support for Mixer platform
Fix chat bot memory leak
Update documentation for CLI usage
Improve error handling in GroqModel
```

### 2. Push to Your Fork

```bash
git push origin feature/your-feature-name
```

### 3. Create Pull Request

- Go to the original repository on GitHub
- Click "New Pull Request"
- Select your fork and branch
- Fill out the PR template
- Submit the pull request

### Pull Request Guidelines

- Provide a clear description of the changes
- Reference any related issues
- Include screenshots for UI changes
- Ensure all tests pass
- Update documentation if needed

## Code Review Process

1. Maintainers will review your PR
2. They may request changes or clarifications
3. Make requested changes in your branch
4. Once approved, your PR will be merged

## Feature Requests

To request a new feature:

1. Check if it already exists in [Issues](https://github.com/MIHAchoppa/aI-lIVE-genie/issues)
2. If not, create a new issue with:
   - Clear description of the feature
   - Use cases and benefits
   - Any relevant examples or mockups

## Bug Reports

To report a bug:

1. Check if it's already reported in [Issues](https://github.com/MIHAchoppa/aI-lIVE-genie/issues)
2. If not, create a new issue with:
   - Clear description of the bug
   - Steps to reproduce
   - Expected behavior
   - Actual behavior
   - Environment details (OS, Python version, etc.)
   - Error messages or logs

### Bug Report Template

```markdown
**Description**
Clear description of the bug

**To Reproduce**
1. Step 1
2. Step 2
3. See error

**Expected Behavior**
What should happen

**Actual Behavior**
What actually happens

**Environment**
- OS: [e.g., Windows 10, macOS 12, Ubuntu 20.04]
- Python Version: [e.g., 3.9.7]
- Package Version: [e.g., 0.1.0]

**Additional Context**
Any other relevant information
```

## Documentation

### Updating Documentation

- Keep docs clear and concise
- Include code examples
- Update API reference for any API changes
- Check for typos and grammar

### Documentation Structure

```
docs/
├── GETTING_STARTED.md  # Getting started guide
├── API_REFERENCE.md    # Complete API documentation
├── PLATFORM_GUIDE.md   # Platform-specific guides
└── TRAINING_BOT_GUIDE.md  # Training bot usage
```

## Community Guidelines

### Be Respectful

- Be kind and courteous
- Respect different viewpoints
- Accept constructive criticism gracefully
- Focus on what's best for the project

### Be Collaborative

- Help others when you can
- Share knowledge and insights
- Give credit where it's due
- Celebrate contributions

### Be Professional

- Keep discussions on-topic
- Use clear and professional language
- Provide constructive feedback
- Follow the code of conduct

## Questions?

If you have questions:

1. Check the [documentation](docs/)
2. Search [existing issues](https://github.com/MIHAchoppa/aI-lIVE-genie/issues)
3. Create a new issue with your question
4. Tag it with "question" label

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to AI Live Genie! 🎮✨
