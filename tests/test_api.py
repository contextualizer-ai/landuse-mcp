from src.landuse_mcp.main import get_soil_type, get_landuse_dates, get_land_cover


def test_get_soil_type():
    """Test soil type function with known coordinates."""
    # Test with Alabama coordinates (should return "Cambisols")
    soil = get_soil_type(32.95047, -87.393259)
    assert soil is not None
    assert isinstance(soil, str)

    # Test with ocean coordinates (should return "Water")
    soil_ocean = get_soil_type(0, 0)
    assert soil_ocean is not None
    assert isinstance(soil_ocean, str)


def test_get_landuse_dates():
    """Test landuse dates function with known coordinates."""
    # Test with Death Valley coordinates
    dates = get_landuse_dates(36.5322649, -116.9325408)
    assert dates is not None
    assert isinstance(dates, list)
    assert len(dates) > 0
    # Check that dates are in YYYY-MM-DD format
    for date in dates[:3]:  # Test first 3 dates
        assert len(date.split('-')) == 3


def test_get_land_cover():
    """Test land cover function with known coordinates."""
    # Test with Death Valley coordinates between 2001-2002
    data = get_land_cover(36.5322649, -116.9325408, "2001-01-01", "2002-01-01")
    assert data is not None
    assert isinstance(data, dict)
