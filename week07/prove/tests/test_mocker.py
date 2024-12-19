def test_mocking_example(mocker):
    mock_func = mocker.Mock(return_value=42)
    result = mock_func()
    assert result == 42
    mock_func.assert_called_once()
