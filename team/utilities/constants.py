def field_missing_error_message(field):
    return f" '{field}' is a required field"


ApiResponseMessages = {
    "EMAIL_REQUIRED": "Email is a required field",
    "SUPERUSER_IS_STAFF_TRUE": "Superuser must have is_staff=True.",
    "SUPERUSER_IS_SUPERUSER_TRUE": 'Superuser must have is_superuser=True',
    "UNATHORIZED_ERROR": "Current user does not have access for the task",
    "INVALID_ACCOUNT_TYPE": "Required Account Type is invalid",
}

account_types = {
    "SUPER_ADMIN": 1,
    "MANAGER": 2,
    "EMPLOYEE": 3
}

e_account_types = {
    1: "SUPER_ADMIN",
    2: "MANAGER",
    3: "EMPLOYEE"
}
