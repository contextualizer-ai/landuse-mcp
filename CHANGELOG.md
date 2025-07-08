# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Comprehensive build and test infrastructure based on oak-mcp best practices
- GitHub Actions workflows for CI/CD and PyPI publishing
- Makefile with development, testing, and release targets
- Enhanced pyproject.toml with modern Python packaging standards
- Code quality tools: ruff, black, mypy, pytest-cov
- MCP protocol testing capabilities
- Professional README with comprehensive documentation
- MIT License file

### Changed
- Migrated from rasterio to nmdc-geoloc-tools for geospatial processing
- Updated dependencies to use nmdc-geoloc-tools
- Enhanced test suite with better coverage and integration tests
- Improved project structure following Python packaging best practices

### Fixed
- Import paths in test files
- Tool registration in FastMCP server

## [0.1.0] - 2024-XX-XX

### Added
- Initial release of landuse-mcp
- Basic MCP server functionality
- Land cover data retrieval using NLCD
- Soil type classification
- Temporal land use data queries
- FastMCP integration
- Basic test suite