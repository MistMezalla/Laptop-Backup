class Solution:
    def minimize_weighted_completion(self, jobs):
        jobs.sort(key=lambda x: x[1] / x[0], reverse=True)
        total_time = 0
        current_time = 0

        for processing_time, weight in jobs:
            current_time += processing_time
            total_time += weight * current_time

        return total_time


sol = Solution()

jobs = [(3, 10), (1, 5), (2, 7), (4, 2)]
print(sol.minimize_weighted_completion(jobs))

# Test case 1: No jobs
jobs1 = []
print("Test Case 1 (No Jobs):", sol.minimize_weighted_completion(jobs1))

# Test case 2: Single job
jobs2 = [(5, 10)]
print("Test Case 2 (Single Job):", sol.minimize_weighted_completion(jobs2))

# Test case 3: Jobs with zero weight
jobs3 = [(3, 0), (2, 0), (4, 0)]
print("Test Case 3 (Jobs with Zero Weight):", sol.minimize_weighted_completion(jobs3))

#invaid as processing time > 0 and weight >=0
# # Test case 4: Jobs with zero time
# jobs4 = [(0, 10), (0, 5), (0, 7)]
# print("Test Case 4 (Jobs with Zero Time):", sol.minimize_weighted_completion(jobs4))

# Test case 5: All jobs have the same time and weight
jobs5 = [(3, 10), (3, 10), (3, 10)]
print("Test Case 5 (Same Time and Weight):", sol.minimize_weighted_completion(jobs5))

# Test case 6: Large weights and times
jobs6 = [(1000000, 5000000), (2000000, 3000000), (1500000, 4000000)]
print("Test Case 6 (Large Weights and Times):", sol.minimize_weighted_completion(jobs6))

