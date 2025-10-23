# Project Structure

## Directory Layout

```
aI-lIVE-genie/
│
├── .github/                    # GitHub configuration
│   └── workflows/
│       └── ci.yml             # CI/CD pipeline
│
├── docs/                       # Documentation
│   ├── API_DOCUMENTATION.md   # Complete REST API reference
│   ├── IMPLEMENTATION.md      # Technical implementation details
│   ├── QUICKSTART.md         # 5-minute quick start guide
│   └── PROJECT_STRUCTURE.md  # This file
│
├── examples/                   # Example code
│   ├── example_usage.py      # Python usage examples
│   └── example_website.html  # Web integration example
│
├── src/                        # Source code
│   └── ai_live_genie/         # Main package
│       ├── __init__.py        # Package exports
│       ├── api_server.py      # Flask REST API server
│       ├── cli.py             # Command-line interface
│       ├── memory_manager.py  # Memory management system
│       └── streaming_data.py  # Streaming platform data
│
├── tests/                      # Test suite
│   ├── README.md              # Testing documentation
│   ├── test_api.py            # API endpoint tests (35 tests)
│   └── test_memory_system.py  # Memory system tests (23 tests)
│
├── .gitignore                  # Git ignore rules
├── CHANGELOG.md                # Version history
├── CONTRIBUTING.md             # Contribution guidelines
├── LICENSE                     # MIT License
├── Makefile                    # Development commands
├── pyproject.toml              # Modern Python packaging
├── README.md                   # Main documentation
├── requirements.txt            # Optional dependencies
├── SECURITY.md                 # Security policy
└── setup.py                    # Legacy pip support
```

## Component Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    AI Live Genie                        │
└─────────────────────────────────────────────────────────┘
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼
   ┌─────────┐      ┌──────────┐      ┌──────────┐
   │   CLI   │      │ REST API │      │  Python  │
   │ Interface│      │  Server  │      │  Library │
   └─────────┘      └──────────┘      └──────────┘
        │                  │                  │
        └──────────────────┼──────────────────┘
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│    Memory    │  │  Streaming   │  │    Goals     │
│  Management  │  │   Platform   │  │  Management  │
│              │  │     Data     │  │              │
└──────────────┘  └──────────────┘  └──────────────┘
        │                  │                  │
        └──────────────────┼──────────────────┘
                           │
                           ▼
                   ┌──────────────┐
                   │ JSON Storage │
                   │  (./data/)   │
                   └──────────────┘
```

## Module Descriptions

### Core Modules

#### `memory_manager.py`
- **ConversationalMemory**: Short-term chat history
- **LongTermMemory**: Persistent storage (facts, preferences, entities)
- **GoalsManager**: Goal tracking and progress monitoring
- **MemoryManager**: Unified interface for all memory systems

#### `streaming_data.py`
- **StreamingPlatformData**: Platform payout rates and analytics
- Supports 7 major platforms
- Earnings calculator
- Platform comparison tools
- Conversion rate tracking

#### `api_server.py`
- Flask-based REST API
- CORS enabled for cross-origin requests
- API key authentication
- 35+ endpoints
- Health check and error handling

#### `cli.py`
- Command-line interface
- Server management
- Earnings calculations
- Platform comparisons
- Goal management

## Data Flow

### Memory System Flow
```
User Input
    ↓
ConversationalMemory (short-term)
    ↓
LongTermMemory (persistent)
    ↓
JSON File Storage (./data/)
```

### Streaming Data Flow
```
Platform Request
    ↓
StreamingPlatformData
    ↓
Calculate/Compare/Convert
    ↓
Return Results
```

### API Request Flow
```
HTTP Request
    ↓
Authentication Check
    ↓
Endpoint Handler
    ↓
Memory/Streaming Module
    ↓
JSON Response
```

## File Sizes

| Category | Files | Lines of Code |
|----------|-------|---------------|
| Core Code | 5 | ~2,500 |
| Tests | 2 | ~1,000 |
| Examples | 2 | ~800 |
| Documentation | 8 | ~2,000 |
| **Total** | **17** | **~6,300** |

## Dependencies

### Core
- **None** - Uses only Python standard library

### Optional (API)
- Flask >= 2.0.0
- Flask-CORS >= 3.0.0

### Development
- pytest >= 7.0.0
- black >= 22.0.0
- pylint >= 2.12.0
- mypy >= 0.950

## Entry Points

### Command Line
```bash
ai-live-genie [command] [options]
```

### Python Import
```python
from ai_live_genie import MemoryManager, StreamingPlatformData
```

### REST API
```
http://localhost:5000/api/...
```

## Testing

- **58 total tests**
- **100% pass rate**
- **Coverage**: Core functionality
- **CI/CD**: Automated on push/PR

## Version Control

- **Git**: Version control
- **GitHub**: Repository hosting
- **GitHub Actions**: CI/CD pipeline
- **Branches**: Feature branch workflow

## Deployment

### Local Development
```bash
pip install -e ".[dev]"
make test
make serve
```

### Production
```bash
pip install ai-live-genie[api]
export AI_GENIE_API_KEY="your-secure-key"
ai-live-genie serve --host 0.0.0.0 --port 5000
```

### Docker (Future)
```dockerfile
# Dockerfile coming soon
```

## Maintenance

- **Security**: Regular dependency updates
- **Testing**: Automated CI/CD
- **Documentation**: In-code docstrings + markdown docs
- **Versioning**: Semantic versioning (SemVer)

---

For more information, see:
- [Main README](../README.md)
- [API Documentation](API_DOCUMENTATION.md)
- [Contributing Guide](../CONTRIBUTING.md)
