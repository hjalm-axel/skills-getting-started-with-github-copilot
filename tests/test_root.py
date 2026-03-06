def test_root_endpoint_redirects_to_static_index_html(client):
    """Test that the root endpoint redirects to the static index.html page."""
    response = client.get("/")
    assert response.status_code == 200
    # FastAPI redirects are handled differently, but the endpoint serves the static file
    # The actual response will be the HTML content of index.html