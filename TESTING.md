# Testing Guide for landuse-mcp

This document describes the comprehensive testing framework for landuse-mcp, based on oak-mcp best practices.

## Test Structure

### Core API Tests (`tests/test_api.py`)
Basic functionality tests for the core MCP tools:
- `test_get_soil_type()` - Soil type retrieval functionality
- `test_get_landuse_dates()` - Available dates functionality
- `test_get_land_cover()` - Land cover data retrieval

### MCP Protocol Tests (`tests/test_mcp_protocol.py`)
Protocol implementation and integration tests:
- `test_mcp_tool_registration()` - Verify MCP tools are properly registered
- `test_mcp_tool_schemas()` - Validate function signatures and schemas
- `test_error_handling()` - Error handling for invalid inputs
- `test_coordinate_validation()` - Boundary condition testing
- `test_date_format_validation()` - Date format validation
- `test_realistic_workflow()` - End-to-end workflow testing

### Real-World Integration Tests (`tests/test_real_world_integration.py`)
Comprehensive geospatial analysis workflows:

#### Agricultural Analysis
- `test_agricultural_land_analysis()` - Multi-step agricultural land assessment
- Tests soil suitability, temporal patterns, and land cover classification

#### Urban Development
- `test_urban_development_analysis()` - City planning and development analysis
- Historical land use changes and construction suitability

#### Environmental Assessment
- `test_environmental_impact_assessment()` - Protected area monitoring
- Environmental baseline data and impact assessment

#### Coastal Management
- `test_coastal_zone_management()` - Coastal erosion and zone analysis
- Multi-temporal coastal change detection

#### Climate Analysis
- `test_climate_change_indicators()` - Climate impact through land use changes
- Long-term vegetation and land cover changes

#### Disaster Risk
- `test_disaster_risk_assessment()` - Emergency planning and risk assessment
- Wildfire risk and disaster preparedness applications

#### Comparative Analysis
- `test_cross_region_comparative_analysis()` - Multi-region policy analysis
- Cross-regional data comparison for policy making

#### Comprehensive Workflow
- `test_comprehensive_geospatial_workflow()` - Full-stack geospatial intelligence
- Complete multi-temporal, multi-source analysis

## Running Tests

### Quick Test Commands

```bash
# Run all tests with coverage
make test-coverage

# Run basic API tests
make test-integration

# Run MCP protocol tests
make test-mcp-protocol

# Run real-world integration tests
make test-real-world-integration
```

### Specific Integration Tests

```bash
# Agricultural analysis
make test-agricultural-analysis

# Urban development analysis
make test-urban-development

# Environmental impact assessment
make test-environmental-impact

# Coastal zone management
make test-coastal-management

# Climate change indicators
make test-climate-indicators

# Disaster risk assessment
make test-disaster-risk

# Cross-region comparative analysis
make test-comparative-analysis

# Comprehensive geospatial workflow
make test-comprehensive-workflow
```

### MCP Server Testing

```bash
# Test MCP protocol handshake
make test-mcp

# Extended MCP protocol testing
make test-mcp-extended
```

### Development Workflow

```bash
# Complete development testing
make all

# Individual quality checks
make format lint mypy deptry
```

## Test Markers

Tests use pytest markers for organization:

- `@pytest.mark.integration` - Integration tests requiring external services
- `@pytest.mark.slow` - Tests that take longer to execute

Run specific marker groups:
```bash
# Run only integration tests
uv run pytest -m integration

# Skip slow tests
uv run pytest -m "not slow"
```

## Coverage Requirements

The project maintains high test coverage:
- Target: 90%+ coverage
- Current: 91% coverage
- HTML reports: `htmlcov/index.html`

## Test Configuration

### Pytest Configuration (`pyproject.toml`)
```toml
[tool.pytest.ini_options]
minversion = "7.0"
addopts = "-ra -q --strict-markers"
testpaths = ["tests"]
markers = [
    "slow: marks tests as slow",
    "integration: marks tests as integration tests",
]
```

### Coverage Configuration (`pyproject.toml`)
```toml
[tool.coverage.run]
source = ["src"]
omit = ["src/landuse_mcp/_version.py"]

[tool.coverage.report]
exclude_lines = [
    "pragma: no cover",
    "def __repr__",
    "if __name__ == .__main__.:",
]
```

## Error Handling

Tests are designed to handle service unavailability gracefully:
- Functions may return `None` if external services are unavailable
- Tests verify type correctness when data is available
- No tests should crash due to network issues

## Continuous Integration

GitHub Actions automatically run:
- All test suites across Python 3.10, 3.11, 3.12
- Code quality checks (black, ruff, mypy)
- Coverage reporting
- MCP protocol validation

## Writing New Tests

### Guidelines
1. Follow existing test patterns
2. Use descriptive test names
3. Add appropriate markers (`@pytest.mark.integration`)
4. Handle service unavailability gracefully
5. Include real-world coordinates for integration tests
6. Document test purpose and expected outcomes

### Example Test Structure
```python
@pytest.mark.integration
def test_new_geospatial_workflow():
    """Test description and purpose."""
    print("\n🌍 WORKFLOW NAME")
    
    # Test coordinates
    lat, lon = 40.7128, -74.0060
    
    # Step 1: Initial data gathering
    result = get_some_data(lat, lon)
    if result is not None:
        assert isinstance(result, expected_type)
        # Additional assertions
    
    # Step 2: Follow-up analysis
    # ...
    
    print("✅ Workflow completed successfully")
```

## Best Practices

1. **Realistic Test Data**: Use real geographical coordinates
2. **Graceful Degradation**: Handle service unavailability
3. **Comprehensive Coverage**: Test all major workflows
4. **Performance Awareness**: Mark slow tests appropriately
5. **Documentation**: Explain test purpose and methodology
6. **Workflow Simulation**: Mirror real-world usage patterns

This testing framework ensures landuse-mcp provides reliable geospatial intelligence for AI agents across diverse use cases and environments.