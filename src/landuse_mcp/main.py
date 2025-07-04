################################################################################
# landuse_mcp/main.py
# This module provides a FastMCP wrapper for the database_name API
# cribbed from Mark Miller's code [here](https://github.com/microbiomedata/external-metadata-awareness/blob/1cf68ade4bf2e90612f8c1a0aa028226332b9e71/notebooks/studies_exploration/predict_env_local_scale_from_nlcd_geotiff.ipynb#L35)
################################################################################
import zipfile
from typing import Any, Dict, List, Optional, Union
from fastmcp import FastMCP
import rasterio
from rasterio.warp import transform
from pathlib import Path
import urllib.request


# Constants
NLCD_URL = "https://www.mrlc.gov/downloads/sciweb1/shared/mrlc/data-bundles/Annual_NLCD_LndCov_2024_CU_C1V1.zip"
DATA_DIR = Path("data")
ZIP_FILENAME = DATA_DIR / "Annual_NLCD_LndCov_2024_CU_C1V1.zip"
EXTRACTED_TIF_NAME = "Annual_NLCD_LndCov_2024_CU_C1V1.tif"
EXTRACTED_TIF_PATH = DATA_DIR / EXTRACTED_TIF_NAME


def _ensure_nlcd_data():
    """Download and extract NLCD GeoTIFF and auxiliary files if not already present.
    """
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    expected_files = [
        "Annual_NLCD_LndCov_2024_CU_C1V1.tif",
        "Annual_NLCD_LndCov_2024_CU_C1V1.tif.aux.xml",
        "Annual_NLCD_LndCov_2024_CU_C1V1.xml"
    ]

    missing_files = [f for f in expected_files if not (DATA_DIR / f).exists()]

    if missing_files:
        print(f"Missing NLCD data files: {missing_files}. Downloading and extracting...")
        urllib.request.urlretrieve(NLCD_URL, ZIP_FILENAME)
        with zipfile.ZipFile(ZIP_FILENAME, 'r') as zip_ref:
            zip_ref.extractall(DATA_DIR)
        print("Download and extraction complete.")
    else:
        print("NLCD data already present.")


# Function to get land cover value from NLCD
def get_land_cover(lat, lon, dataset=EXTRACTED_TIF_PATH) -> Optional[int]:
    """
    Given a latitude and longitude and a GeoTIFF dataset, retrieve and return data
    for the lat/long

    Args:
        lat: latitude of the point
        lon: longitude of the point
        dataset: GeoTIFF dataset to query (EXTRACTED_TIF_PATH by default)

    Returns:
        int: Land cover value at the specified latitude and longitude
        or None if things go wrong

    """
    try:
        with rasterio.open(str(dataset)) as src:
            # Transform coordinates to the GeoTIFF's CRS
            dst_crs = src.crs
            lon_transformed, lat_transformed = transform('EPSG:4326', dst_crs, [lon], [lat])
            
            # Query the pixel value at the transformed coordinate
            coords = [(lon_transformed[0], lat_transformed[0])]
            for val in src.sample(coords):
                return int(val[0])
                
    except Exception as e:
        print(f"Error processing point ({lat}, {lon}): {e}")
        return None


# MAIN SECTION
# Create the FastMCP instance
mcp = FastMCP("landuse_mcp")

# Register all tools
mcp.tool(get_land_cover)


def main():
    """Main entry point for the application."""
    _ensure_nlcd_data()
    mcp.run()


if __name__ == "__main__":
    main()
