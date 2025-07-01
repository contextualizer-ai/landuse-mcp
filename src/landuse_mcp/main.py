################################################################################
# landuse_mcp/main.py
# This module provides a FastMCP wrapper for the database_name API
################################################################################
import json
from typing import Any, Dict, List, Optional, Union
from fastmcp import FastMCP
import pandas as pd
import rasterio
from rasterio.warp import transform
import pprint

from oaklib import get_adapter

# 2024 Land use data
# https://www.mrlc.gov/downloads/sciweb1/shared/mrlc/data-bundles/Annual_NLCD_LndCov_2024_CU_C1V1.zip
# make an init file to pre-download the NLCD 2024 data



# Function to get land cover value from NLCD
def get_land_cover(lat, lon, dataset):
    try:
        # Transform coordinates to the GeoTIFF's CRS
        dst_crs = dataset.crs  # CRS of the GeoTIFF
        lon_transformed, lat_transformed = transform('EPSG:4326', dst_crs, [lon], [lat])

        # Query the pixel value at the transformed coordinate
        coords = [(lon_transformed[0], lat_transformed[0])]
        for val in dataset.sample(coords):
            return int(val[0])
    except Exception as e:
        print(f"Error processing point ({lat}, {lon}): {e}")
        return None

# MCP TOOL SECTION
def sample_tool_function(
    parameter1: str,
    parameter2: int = 10
) -> List[Dict[str, Any]]:
    """
    Sample tool function to demonstrate how to create a tool for your MCP.

    Args:
        parameter1: Description of parameter1
        parameter2: Description of parameter2, with default value

    Returns:
        List[Dict[str, Any]]: List of records matching the criteria
    """
    # Example of how to use the API wrapper
    filter_criteria = {"field1": parameter1, "field2": {"$gt": parameter2}}

    records = fetch_records_paged(
        endpoint="your_endpoint",
        filter_criteria=filter_criteria,
        max_records=parameter2,
    )

    # Process records if needed
    processed_records = []
    for record in records:
        # Process each record
        processed_record = {
            "id": record.get("id"),
            "name": record.get("name"),
            # Add other fields as needed
        }
        processed_records.append(processed_record)

    return processed_records


# MAIN SECTION
# Create the FastMCP instance
mcp = FastMCP("landuse_mcp")

# Register all tools
mcp.tool(sample_tool_function)


def main():
    """Main entry point for the application."""
    mcp.run()


if __name__ == "__main__":
    main()
