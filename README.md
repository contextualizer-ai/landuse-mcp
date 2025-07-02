# landuse_mcp

An MCP for retrieving land use data for a given location

## Installation

You can install the package from source:

Install proj

### For MacOS 12:
```bash
brew install --cask miniforge
conda create -n landuse python=3.10
conda activate landuse
conda install rasterio geopandas
```

```bash
uv pip install -e .
```

## Usage

You can use the CLI:

```bash
landuse_mcp 
```

Or import in your Python code:

```python
from landuse_mcp.main import create_mcp

mcp = create_mcp()
mcp.run()
```

## Development

### Local Setup

```bash
# Clone the repository
git clone https://github.com/justaddcoffee/landuse-mcp.git
cd landuse-mcp

# Install development dependencies
uv sync
```


## License

BSD-3-Clause
