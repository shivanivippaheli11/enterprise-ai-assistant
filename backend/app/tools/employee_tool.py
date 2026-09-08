class EmployeeTool:
    """
    Provides employee information to the AI assistant.
    """

    def __init__(self):
        # Temporary mock employee data.
        # Later this can come from a database or HR API.
        self.employees = {
            "EMP001": {
                "name": "Alex",
                "department": "Engineering",
                "role": "Software Developer"
            },
            "EMP002": {
                "name": "Rahul",
                "department": "Human Resources",
                "role": "HR Specialist"
            }
        }

    def get_employee_info(
        self,
        employee_id: str
    ):
        """
        Return employee information for the given employee ID.
        """

        employee = self.employees.get(employee_id)

        if not employee:
            return {
                "success": False,
                "message": "Employee not found."
            }

        return {
            "success": True,
            "employee_id": employee_id,
            "name": employee["name"],
            "department": employee["department"],
            "role": employee["role"]
        }