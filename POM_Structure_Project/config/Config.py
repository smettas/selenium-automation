

class Config:

    # Base URL for the application
    BASE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    # Login credentials for testing
    USER_NAME = "Admin"
    PASSWORD = "admin123"

    # Default timeout for waiting for elements
    TIME_OUT = 10

    # After login Current URL
    AFTER_LOGIN_URL="https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

"""
🔹 Comments:

1.Stores configuration settings like base URL, credentials, and timeouts.
2.Helps in centralized maintenance so that changes can be made in one place instead of updating multiple test files.
"""