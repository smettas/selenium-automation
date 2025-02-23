import pytest

@pytest.mark.parametrize("browser", ["chrome","edge"])
@pytest.mark.usefixtures("browsers")
class BaseTest:
    pass     # Empty for now, but useful for future test setups


"""
🔹 Comments:

1.Ensures that each test class gets a browser instance.
2.Uses @pytest.mark.usefixtures("browsers") to automatically apply the browser fixture.
3.Can be expanded later for common test setup logic.

"""