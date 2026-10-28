"""Ocean data ingestion adapters and utilities."""
from packages.ocean_data.base_adapter import BaseDataIngestionAdapter
from packages.ocean_data.noaa_coral_adapter import NOAACoralBleachingAdapter

__all__ = ["BaseDataIngestionAdapter", "NOAACoralBleachingAdapter"]
