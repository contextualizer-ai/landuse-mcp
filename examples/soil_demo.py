#!/usr/bin/env python3
"""
Soil classification demonstration script.

This script tests soil type determination with multiple locations
to demonstrate that the soil classification functionality is working correctly.
"""

from landuse_mcp.main import get_soil_type


def main():
    print("🌱 SOIL CLASSIFICATION TEST")
    print("==========================")
    print("Testing soil type determination with multiple locations...")
    print()
    
    test_cases = [
        (32.95047, -87.393259, 'Alabama'),
        (0, 0, 'Ocean'),
        (40.7128, -74.0060, 'New York'),
        (51.5074, -0.1278, 'London'),
        (-33.8688, 151.2093, 'Sydney')
    ]
    
    print(f"{'Location':<15}\t{'Coordinates':<20}\t{'Soil Type':<15}\tStatus")
    print("=" * 70)
    
    all_passed = True
    for lat, lon, location in test_cases:
        result = get_soil_type(lat, lon)
        status = '✅' if result is not None else '❌'
        if result is None:
            all_passed = False
        coord_str = f"({lat:8.4f}, {lon:9.4f})"
        print(f"{location:<15}\t{coord_str:<20}\t{result or 'FAILED':<15}\t{status}")
    
    print()
    if all_passed:
        print("✅ Soil classification is working correctly!")
        return 0
    else:
        print("❌ Some soil classifications failed!")
        return 1


if __name__ == "__main__":
    exit(main())