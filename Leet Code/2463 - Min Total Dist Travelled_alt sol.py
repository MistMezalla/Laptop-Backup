"""
Below is a recursive algorithm that will likely generate a TLE for the given constraints.

Time Complexity Analysis:
    -> Sorting: O(n log n) for sorting the robots and O(m log m) for sorting the factories.
    -> Flattening the factory 2D table: O(k * m), where m is the number of factories and k is the maximum capacity of
    any factory.
        -> In the worst case, k = O(n) if all robots could potentially be assigned to factories.
    -> Recursive Calls:
        -> The recursive function `_calculate_min_distance` will have an exponential time complexity of O(2^(n + l)),
           where n is the number of robots and l is the total number of flattened factory slots (l = sum of capacities
           of all factories).
        -> In the worst case, this results in O(2^(n + n * m)) calls, which is highly inefficient for large inputs.
            -> well power of 2 coz choice to choose a factory or discard it.
Overall, the recursive solution without memoization leads to an exponential time complexity, which would not be
feasible for large input sizes.
"""
class Solution_1:
    def minimumTotalDistance(self, robot, factory):
        # Sort robots and factories by position
        robot.sort()
        factory.sort()

        # Flatten factory positions according to their capacities
        factory_positions = []
        for f in factory:
            for i in range(f[1]):
                factory_positions.append(f[0])

        # Recursively calculate minimum total distance
        return self._calculate_min_distance(0, 0, robot, factory_positions)

    def _calculate_min_distance(
        self, robot_idx, factory_idx, robot, factory_positions
    ):
        # All robots assigned
        if robot_idx == len(robot):
            return 0
        # No factories left to assign
        if factory_idx == len(factory_positions):
            return 1e12

        # Option 1: Assign current robot to current factory
        assign = abs(
            robot[robot_idx] - factory_positions[factory_idx]
        ) + self._calculate_min_distance(
            robot_idx + 1, factory_idx + 1, robot, factory_positions
        )

        # Option 2: Skip current factory for the current robot
        skip = self._calculate_min_distance(
            robot_idx, factory_idx + 1, robot, factory_positions
        )

        # Take the option with the minimum distance
        return min(assign, skip)

'''
-> Below is Top Down Dp based approach:-
    -> Now this stores the results of min path len pertaining to a robot[i] and factory[j] in 2D DP table.
    -> Now for the `_calculate_min_distance` function when the function recurses for O(n * l); 
    where l = O(len(flattened_factory table)) = O(n * m)
    -> T(n) = O(n**2 * m) now for const time access from DP table now.
'''
class Solution_2:
    def minimumTotalDistance(
        self, robot: list[int], factory: list[list[int]]
    ) -> int:
        robot.sort()
        factory.sort(key=lambda x: x[0])
        factory_positions = []
        for f in factory:
            factory_positions.extend([f[0]] * f[1])
        robot_count = len(robot)
        factory_count = len(factory_positions)

        dp = [[None] * (factory_count + 1) for _ in range(robot_count + 1)]

        def _calculate_min_distance(robot_idx: int, factory_idx: int) -> int:
            if dp[robot_idx][factory_idx] is not None:
                return dp[robot_idx][factory_idx]
            if robot_idx == robot_count:
                dp[robot_idx][factory_idx] = 0
                return 0
            if factory_idx == factory_count:
                dp[robot_idx][factory_idx] = int(1e12)
                return int(1e12)

            assign = abs(
                robot[robot_idx] - factory_positions[factory_idx]
            ) + _calculate_min_distance(robot_idx + 1, factory_idx + 1)

            skip = _calculate_min_distance(robot_idx, factory_idx + 1)

            dp[robot_idx][factory_idx] = min(assign, skip)
            return dp[robot_idx][factory_idx]

        return _calculate_min_distance(0, 0)

'''
-> Below is Bottom Up DP approach, here in this case the memory overhead regarding the recursive stack calls is 
improved by iterative approach (a general notion to improve the recursive approach by the iterative methods).
'''
class Solution_3:
    def minimumTotalDistance(self, robot, factory):
        # Sort robots and factories by position
        robot.sort()
        factory.sort(key=lambda x: x[0])

        # Flatten factory positions according to their capacities
        factory_positions = []
        for f in factory:
            for _ in range(f[1]):
                factory_positions.append(f[0])

        robot_count, factory_count = len(robot), len(factory_positions)
        dp = [[0] * (factory_count + 1) for _ in range(robot_count + 1)]

        # Initialize base cases
        for i in range(robot_count):
            dp[i][factory_count] = 1e12  # No factories left

        # Fill DP table bottom-up
        for i in range(robot_count - 1, -1, -1):
            for j in range(factory_count - 1, -1, -1):
                # Option 1: Assign current robot to current factory
                assign = abs(robot[i] - factory_positions[j]) + dp[i + 1][j + 1]

                # Option 2: Skip current factory for the current robot
                skip = dp[i][j + 1]

                dp[i][j] = min(assign, skip)  # Take the minimum option

        # Minimum distance starting from first robot and factory
        return dp[0][0]  

sol = Solution_3()
print(sol.minimumTotalDistance(robot = [1,3,6], factory = [[1,2],[6,1]]))