def test_get_activities_returns_all_activities_successfully(client):
    """Test that getting all activities returns a successful response with activity data."""
    response = client.get("/activities")
    assert response.status_code == 200
    activities = response.json()
    assert isinstance(activities, dict)
    assert len(activities) == 9  # Based on the app.py, there are 9 activities


def test_get_activities_response_contains_expected_activity_fields(client):
    """Test that each activity in the response contains all expected fields."""
    response = client.get("/activities")
    activities = response.json()

    # Check one activity as an example (Chess Club)
    chess_club = activities.get("Chess Club")
    assert chess_club is not None
    assert "description" in chess_club
    assert "schedule" in chess_club
    assert "max_participants" in chess_club
    assert "participants" in chess_club
    assert isinstance(chess_club["participants"], list)


def test_get_activities_returns_correct_number_of_activities(client):
    """Test that the activities endpoint returns exactly 9 activities."""
    response = client.get("/activities")
    activities = response.json()
    assert len(activities) == 9