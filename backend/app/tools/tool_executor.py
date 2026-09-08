from app.tools.employee_tool import EmployeeTool


class ToolExecutor:
    """
    Executes tools requested by the AI model.
    """

    def __init__(self):
        self.employee_tool = EmployeeTool()

        # Register available tools.
        # The key is the name Gemini uses.
        self.tools = {
            "get_employee_info": self.employee_tool.get_employee_info
        }

    def execute(
        self,
        tool_name: str,
        arguments: dict
    ):
        """
        Execute a registered tool using the supplied arguments.
        """

        tool = self.tools.get(tool_name)

        if not tool:
            return {
                "success": False,
                "message": f"Unknown tool: {tool_name}"
            }

        try:
            result = tool(**arguments)

            return result

        except Exception as error:
            return {
                "success": False,
                "message": f"Tool execution failed: {error}"
            }