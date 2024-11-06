from rest_framework.exceptions import ValidationError
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        if isinstance(exc, ValidationError):
            response_data = {
                "title": "Validation Error",
                "errors": []
            }
            for field, errors_list in response.data.items():
                field_errors = []
                for error in errors_list:
                    error = {
                        "code": error.code,
                        "detail": str(error)
                    }
                    field_errors.append(error)
                error_data = {
                    "field": field,
                    "field_errors": field_errors
                }
                response_data["errors"].append(error_data)
        else:
            response_data = {
                "title": response.status_text,
                "errors": [
                    {
                        "code": response.data["detail"].code,
                        "detail": str(exc)
                    }
                ]
            }

        response.data = response_data
    return response
