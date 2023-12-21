import pytest
import src.service as service
import unittest.mock as mock
import requests


@mock.patch("src.service.get_team_details")
def test_get_team_details(mock_get):
    mock_get.return_value = """
    Team name: Team 0
    Members: [...]
    """
    team = service.get_team_details("team0")

    assert team == """
    Team name: Team 0
    Members: [...]
    """


@mock.patch("requests.get")
def test_get_users(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"id": 1,
                                       "name": "John Doe",
                                       "username": "johndoe"}
    mock_get.return_value = mock_response
    users = service.get_users()

    assert users == {"id": 1,
                     "name": "John Doe",
                     "username": "johndoe"}


@mock.patch("requests.get")
def test_get_users_error(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 404
    mock_get.return_value = mock_response
    with pytest.raises(requests.HTTPError) as e:
        service.get_users()