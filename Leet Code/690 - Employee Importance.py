class Employee:
    def __init__(self, id: int, importance: int, subordinates: list[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: list['Employee'], id: int) -> int:
        adj_list = {}
        emp_imp = {}

        for emp in employees:
            adj_list[emp.id] = emp.subordinates
            emp_imp[emp.id] = emp.importance

        visited = set()

        def dfs(node: int) -> int:
            if node in visited:
                return 0
            visited.add(node)
            total_importance = emp_imp[node]
            for neighbour in adj_list[node]:
                total_importance += dfs(neighbour)
            return total_importance

        return dfs(id)


# Helper function to create Employee objects from the input format
def create_employees(data):
    employees = []
    for emp_data in data:
        employees.append(Employee(emp_data[0], emp_data[1], emp_data[2]))
    return employees


# Test cases
sol = Solution()

# Test case 1
employees = create_employees([[1, 5, [2, 3]], [2, 3, []], [3, 3, []]])
print(sol.getImportance(employees, 1))  # Expected output: 11

# Test case 2
employees = create_employees([[1, 2, [5]], [5, -3, []]])
print(sol.getImportance(employees, 5))  # Expected output: -3

# Test case 3
employees = create_employees([[1, 2, [5]], [5, -3, [4]], [2, 3, [1]], [4, -1, [1, 2]]])
print(sol.getImportance(employees, 1))  # Expected output: -3
