# Contributing to landuse-mcp

Thank you for your interest in contributing to landuse-mcp! This document provides guidelines for contributing to the project.

## Development Setup

1. **Fork and Clone**
   ```bash
   git clone https://github.com/your-username/landuse-mcp.git
   cd landuse-mcp
   ```

2. **Set up Development Environment**
   ```bash
   # Install uv if you haven't already
   curl -LsSf https://astral.sh/uv/install.sh | sh
   
   # Install development dependencies
   make dev
   ```

3. **Verify Installation**
   ```bash
   # Run tests to ensure everything works
   make test-coverage
   
   # Run code quality checks
   make format lint mypy
   ```

## Development Workflow

### Making Changes

1. **Create a Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make Your Changes**
   - Follow the existing code style and patterns
   - Add tests for new functionality
   - Update documentation if needed

3. **Test Your Changes**
   ```bash
   # Run all tests
   make test-coverage
   
   # Run code quality checks
   make format lint mypy
   
   # Test MCP protocol
   make test-mcp test-mcp-extended
   ```

4. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "feat: add your feature description"
   ```

### Code Quality Standards

- **Code Formatting**: We use `black` and `ruff` for code formatting
- **Linting**: `ruff` checks for code quality issues
- **Type Checking**: `mypy` ensures type safety
- **Testing**: `pytest` with coverage reporting
- **Dependencies**: `deptry` checks for unused dependencies

Run all quality checks:
```bash
make format lint mypy deptry
```

### Testing

- Write tests for all new functionality
- Ensure existing tests still pass
- Aim for high test coverage
- Include both unit tests and integration tests

```bash
# Run tests with coverage
make test-coverage

# Run integration tests
make test-integration
```

### Documentation

- Update README.md if adding new features
- Add docstrings to all public functions
- Update CHANGELOG.md with your changes
- Include usage examples for new features

## Submitting Changes

1. **Push Your Branch**
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Create a Pull Request**
   - Use a clear, descriptive title
   - Include a detailed description of your changes
   - Link to any related issues
   - Ensure all CI checks pass

3. **Review Process**
   - Maintainers will review your pull request
   - Address any feedback or requested changes
   - Once approved, your changes will be merged

## Code Style Guidelines

### Python Code Style

- Follow PEP 8 conventions
- Use type hints for all function parameters and return values
- Keep functions focused and single-purpose
- Use descriptive variable and function names

### Docstring Style

```python
def get_land_cover(lat: float, lon: float, start_date: str, end_date: str) -> Optional[Dict]:
    """
    Get land use data for a given latitude and longitude.

    Args:
        lat: Latitude of the point (-90 to 90)
        lon: Longitude of the point (-180 to 180)
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format

    Returns:
        dict: Land use data with classification systems and ENVO terms
        or None if things go wrong
    """
```

### Commit Message Format

Use conventional commits format:
- `feat:` for new features
- `fix:` for bug fixes
- `docs:` for documentation changes
- `test:` for test additions/changes
- `refactor:` for code refactoring
- `chore:` for maintenance tasks

## Reporting Issues

When reporting bugs or requesting features:

1. **Check Existing Issues**: Search for similar issues first
2. **Use Issue Templates**: Follow the provided templates
3. **Provide Context**: Include relevant details about your environment
4. **Include Examples**: Provide code examples or steps to reproduce

## Getting Help

- **GitHub Issues**: For bugs and feature requests
- **Discussions**: For questions and general discussion
- **Documentation**: Check README.md and code comments

## Release Process

Releases are handled by maintainers:

1. Update version in pyproject.toml
2. Update CHANGELOG.md
3. Create a Git tag
4. GitHub Actions automatically publishes to PyPI

## License

By contributing to landuse-mcp, you agree that your contributions will be licensed under the MIT License.