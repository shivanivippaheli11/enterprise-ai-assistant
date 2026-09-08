EMPLOYEE_TOOL_SCHEMA = {
    "name": "get_employee_info",
    "description": (
        "Get information about an employee using their employee ID. "
        "Use this tool when the user asks about an employee's "
        "name, department, or role."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "employee_id": {
                "type": "string",
                "description": (
                    "The unique employee ID, "
                    "for example EMP001."
                )
            }
        },
        "required": [
            "employee_id"
        ]
    }
}