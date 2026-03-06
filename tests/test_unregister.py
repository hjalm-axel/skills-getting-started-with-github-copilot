def test_user_can_unregister_from_activity_successfully(client):
    """Test that a user can successfully unregister from an activity they are signed up for."""
    # First sign up
    client.post("/activities/Chess Club/signup?email=unregister@example.com")

    # Then unregister
    response = client.delete("/activities/Chess Club/participants?email=unregister@example.com")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "removed" in data["message"].lower()


def test_unregister_decreases_participant_count(client):
    """Test that unregistering from an activity decreases the participant count."""
    # Sign up first
    client.post("/activities/Chess Club/signup?email=count@example.com")

    # Get count after signup
    response = client.get("/activities")
    activities = response.json()
    count_after_signup = len(activities["Chess Club"]["participants"])

    # Unregister
    client.delete("/activities/Chess Club/participants?email=count@example.com")

    # Check count decreased
    response = client.get("/activities")
    activities = response.json()
    count_after_unregister = len(activities["Chess Club"]["participants"])
    assert count_after_unregister == count_after_signup - 1


def test_unregister_from_nonexistent_activity_returns_not_found(client):
    """Test that unregistering from a nonexistent activity returns a 404 error."""
    response = client.delete("/activities/Nonexistent Activity/participants?email=test@example.com")
    assert response.status_code == 404
    data = response.json()
    assert "detail" in data
    assert "not found" in data["detail"].lower()


def test_unregister_nonexistent_participant_returns_not_found(client):
    """Test that unregistering a participant who is not signed up returns a 404 error."""
    response = client.delete("/activities/Chess Club/participants?email=notsignedup@example.com")
    assert response.status_code == 404
    data = response.json()
    assert "detail" in data
    assert "not found" in data["detail"].lower()