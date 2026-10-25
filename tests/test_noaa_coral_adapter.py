import pytest
from packages.ocean_data.noaa_coral_adapter import NOAACoralBleachingAdapter

def test_noaa_coral_adapter_fetch_and_normalize():
    adapter = NOAACoralBleachingAdapter()
    raw_records = adapter.fetch_raw_data()
    assert len(raw_records) > 0

    first_record = raw_records[0]
    normalized = adapter.normalize_record(first_record)

    assert normalized.latitude == first_record["latitude"]
    assert normalized.longitude == first_record["longitude"]
    assert normalized.source == "NOAA Coral Reef Watch"
    assert "dhw_degree_weeks" in normalized.data
    assert normalized.data["dhw_degree_weeks"] == first_record["dhw_degree_weeks"]
