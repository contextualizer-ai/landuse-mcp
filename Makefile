.PHONY: test-coverage clean install dev format lint all server build upload-test upload release deptry mypy test-mcp test-mcp-extended test-integration

# Default target
all: clean install dev test-coverage format lint mypy deptry build test-mcp test-mcp-extended test-integration test-mcp-protocol

# Install everything for development
dev:
	uv sync --group dev

# Install production only
install:
	uv sync

# Run tests with coverage
test-coverage:
	uv run pytest --cov=landuse_mcp --cov-report=html --cov-report=term tests/

# Clean up build artifacts
clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf src/*.egg-info

# Run server mode
server:
	uv run python src/landuse_mcp/main.py

# Format code with black
format:
	uv run black src/ tests/

# Lint code with ruff
lint:
	uv run ruff check --fix src/ tests/

# Check for unused dependencies
deptry:
	uvx deptry .

# Type checking
mypy:
	uv run mypy src/

# Build package with hatch
build:
	uv run hatch build

# Upload to TestPyPI (using token-based auth)
upload-test:
	uv run twine upload --repository testpypi dist/*

# Upload to PyPI (using token-based auth - set TWINE_PASSWORD environment variable first)
upload:
	uv run twine upload dist/*

# Complete release workflow
release: clean test-coverage build upload

# Integration Testing
test-integration:
	@echo "🌍 Testing landuse integration..."
	uv run pytest tests/test_api.py -v

# Real-world Integration Testing
test-real-world-integration:
	@echo "🌐 Testing real-world integration..."
	uv run pytest tests/test_real_world_integration.py -v

test-agricultural-analysis:
	@echo "🌾 Testing agricultural land analysis..."
	uv run pytest tests/test_real_world_integration.py::test_agricultural_land_analysis -v -s

test-urban-development:
	@echo "🏙️ Testing urban development analysis..."
	uv run pytest tests/test_real_world_integration.py::test_urban_development_analysis -v -s

test-environmental-impact:
	@echo "🌿 Testing environmental impact assessment..."
	uv run pytest tests/test_real_world_integration.py::test_environmental_impact_assessment -v -s

test-coastal-management:
	@echo "🌊 Testing coastal zone management..."
	uv run pytest tests/test_real_world_integration.py::test_coastal_zone_management -v -s

test-climate-indicators:
	@echo "🌡️ Testing climate change indicators..."
	uv run pytest tests/test_real_world_integration.py::test_climate_change_indicators -v -s

test-disaster-risk:
	@echo "🚨 Testing disaster risk assessment..."
	uv run pytest tests/test_real_world_integration.py::test_disaster_risk_assessment -v -s

test-comparative-analysis:
	@echo "🌍 Testing cross-region comparative analysis..."
	uv run pytest tests/test_real_world_integration.py::test_cross_region_comparative_analysis -v -s

test-comprehensive-workflow:
	@echo "🌐 Testing comprehensive geospatial workflow..."
	uv run pytest tests/test_real_world_integration.py::test_comprehensive_geospatial_workflow -v -s

# MCP Protocol Testing
test-mcp-protocol:
	@echo "🔧 Testing MCP protocol implementation..."
	uv run pytest tests/test_mcp_protocol.py -v

# MCP Server testing
test-mcp:
	@echo "Testing MCP protocol handshake..."
	echo '{"jsonrpc": "2.0", "method": "initialize", "params": {"protocolVersion": "1.0", "capabilities": {"tools": {}}, "clientInfo": {"name": "test-client", "version": "1.0.0"}}, "id": 1}' | timeout 3 uv run python src/landuse_mcp/main.py 2>/dev/null | head -1

test-mcp-extended:
	@echo "Testing MCP protocol initialization..."
	@(echo '{"jsonrpc": "2.0", "method": "initialize", "params": {"protocolVersion": "2025-03-26", "capabilities": {"tools": {}}, "clientInfo": {"name": "test-client", "version": "1.0.0"}}, "id": 1}'; \
	 sleep 0.1; \
	 echo '{"jsonrpc": "2.0", "method": "tools/list", "id": 2}'; \
	 sleep 0.1; \
	 echo '{"jsonrpc": "2.0", "method": "tools/call", "params": {"name": "get_land_cover", "arguments": {"lat": 36.5322649, "lon": -116.9325408, "start_date": "2001-01-01", "end_date": "2002-01-01"}}, "id": 3}') | \
	timeout 5 uv run python src/landuse_mcp/main.py 2>/dev/null | head -10

# Demo functionality  
demo:
	@echo "🚀 LANDUSE-MCP DEMO"
	@echo "==================="
	@echo "Getting land cover for Death Valley (36.5322649, -116.9325408)..."
	uv run python -c "from landuse_mcp.main import get_land_cover; print(get_land_cover(36.5322649, -116.9325408, '2001-01-01', '2002-01-01'))"
	@echo ""
	@echo "✅ Landuse-MCP provides geospatial land use data for AI agents!"

# LANDUSE MCP - Claude Desktop config:
#   Add to ~/Library/Application Support/Claude/claude_desktop_config.json:
#   {
#     "mcpServers": {
#       "landuse-mcp": {
#         "command": "uvx",
#         "args": ["landuse-mcp"],
#         "cwd": "/path/to/landuse-mcp"
#       }
#     }
#   }
#
# Claude Code MCP setup:
#   claude mcp add -s project landuse-mcp uvx landuse-mcp
#
# Goose setup:
#   goose session --with-extension "uvx landuse-mcp"