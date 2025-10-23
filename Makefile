.PHONY: help install install-dev test test-verbose lint format clean build docs serve

help:
	@echo "AI Live Genie - Development Commands"
	@echo ""
	@echo "Available commands:"
	@echo "  make install      - Install package in development mode"
	@echo "  make install-dev  - Install with development dependencies"
	@echo "  make test         - Run all tests"
	@echo "  make test-verbose - Run tests with verbose output"
	@echo "  make lint         - Run code linters"
	@echo "  make format       - Format code with Black"
	@echo "  make clean        - Remove build artifacts and cache files"
	@echo "  make build        - Build distribution packages"
	@echo "  make serve        - Start the API server"
	@echo "  make example      - Run the example demo"

install:
	pip install -e .

install-dev:
	pip install -e ".[dev]"

test:
	python -m pytest tests/ -v

test-verbose:
	python -m pytest tests/ -vv

test-coverage:
	python -m pytest tests/ --cov=src/ai_live_genie --cov-report=html --cov-report=term
	@echo "Coverage report generated in htmlcov/index.html"

lint:
	pylint src/ai_live_genie/
	@echo "Linting complete"

format:
	black src/ tests/ examples/
	@echo "Code formatting complete"

format-check:
	black --check src/ tests/ examples/

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	@echo "Cleaned build artifacts"

build: clean
	python -m build
	@echo "Build complete - packages in dist/"

serve:
	@echo "Starting API server..."
	ai-live-genie serve

example:
	python examples/example_usage.py

# Development workflow
dev-setup: install-dev
	@echo "Development environment ready!"

dev-test: format-check lint test

# Quick checks before commit
pre-commit: format lint test
	@echo "All checks passed! Ready to commit."

# Full CI simulation
ci: clean install-dev format-check lint test-coverage
	@echo "CI checks complete!"
