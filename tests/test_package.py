import pytest
from esimaccess_python import Package, authenticate
from unittest.mock import patch

@pytest.fixture
def mock_client():
    with patch('esimaccess_python.authenticate') as mock_authenticate:
        mock_client = mock_authenticate.return_value
        yield mock_client

def test_package_list(mock_client):
    mock_package = Package(mock_client)
    mock_package.list = lambda: [{"id": 1, "name": "Test Package"}]

    result = mock_package.list()

    assert isinstance(result, list)
    assert len(result) > 0
    assert result[0]["name"] == "Test Package"

    print(result)
