from fastapi.testclient import TestClient
from services.api.main import app

client = TestClient(app)

def test_export_incidents_geojson_structure():
    response = client.get("/api/v1/incidents/export/geojson")
    assert response.status_code == 200
    
    data = response.json()
    assert data["type"] == "FeatureCollection"
    assert "features" in data
    assert len(data["features"]) > 0
    
    first_feature = data["features"][0]
    assert first_feature["type"] == "Feature"
    assert first_feature["geometry"]["type"] == "Point"
    assert len(first_feature["geometry"]["coordinates"]) == 2
    assert "id" in first_feature["properties"]
