# Tests

This directory contains the test suite for AI Live Genie.

## Test Files

- `test_memory_system.py` - Tests for memory management (23 tests)
- `test_api.py` - Tests for REST API endpoints (35 tests)

## Running Tests

### Run All Tests

```bash
# From project root
python -m pytest tests/ -v

# Or run individually
python tests/test_memory_system.py -v
python tests/test_api.py -v
```

### Run with Coverage

```bash
pip install pytest-cov
python -m pytest tests/ --cov=src/ai_live_genie --cov-report=html
```

## Test Coverage

Current test coverage: **100%** of core functionality

### Memory System Tests (23 tests)

#### ConversationalMemory
- ✅ Adding messages
- ✅ Retrieving history
- ✅ History limits
- ✅ Clearing memory

#### LongTermMemory
- ✅ Storing/retrieving facts
- ✅ Storing/retrieving preferences
- ✅ Storing/retrieving entities
- ✅ Persistence across instances
- ✅ Searching memory

#### GoalsManager
- ✅ Adding goals
- ✅ Updating progress
- ✅ Adding milestones
- ✅ Completing goals

#### StreamingPlatformData
- ✅ Getting platform data
- ✅ Calculating earnings
- ✅ Comparing platforms
- ✅ Subscriber calculations
- ✅ Conversion rates
- ✅ Monetization requirements
- ✅ Custom platforms

### API Tests (35 tests)

#### Authentication
- ✅ Valid key in header
- ✅ Valid key in query parameter
- ✅ Invalid key handling
- ✅ Missing key handling

#### Endpoints
- ✅ Health check
- ✅ Conversation management (5 endpoints)
- ✅ Memory management (6 endpoints)
- ✅ Goals management (5 endpoints)
- ✅ Streaming data (7 endpoints)
- ✅ Full context retrieval
- ✅ Error handling

## Adding New Tests

When adding new features, follow these guidelines:

1. **Test Structure**
   ```python
   class TestNewFeature(unittest.TestCase):
       def setUp(self):
           # Initialize test fixtures
           pass
       
       def test_specific_behavior(self):
           """Test description."""
           # Test implementation
           self.assertEqual(actual, expected)
   ```

2. **Test Naming**
   - Use descriptive names: `test_feature_behavior`
   - Add docstrings explaining what is being tested

3. **Test Coverage**
   - Test normal cases
   - Test edge cases
   - Test error conditions
   - Test boundary values

4. **Cleanup**
   - Clean up test data in `tearDown()` or `tearDownClass()`
   - Use temporary directories for file operations

## Continuous Integration

Tests run automatically on:
- Every push to main branch
- Every pull request
- Multiple OS: Ubuntu, macOS, Windows
- Multiple Python versions: 3.7, 3.8, 3.9, 3.10, 3.11

See `.github/workflows/ci.yml` for CI configuration.

## Test Data

Test files use temporary data:
- `test_*_memory.json` files are created and cleaned up
- `test_*_goals.json` files are created and cleaned up
- Data directory is cleared between test runs

## Debugging Tests

Run specific test:
```bash
python tests/test_memory_system.py TestConversationalMemory.test_add_message
```

Run with verbose output:
```bash
python -m pytest tests/ -vv
```

Run with debugging:
```bash
python -m pytest tests/ --pdb
```

## Contributing Tests

When contributing:
1. Add tests for new features
2. Ensure all tests pass
3. Maintain or improve coverage
4. Follow existing test patterns
5. Document complex test scenarios
