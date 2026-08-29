class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = 0
        candidtate = 0
        
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                tank = 0
                candidtate = i + 1
        
        residual = tank
        for j in range(candidtate):
            residual += gas[j] - cost[j]
            if residual < 0:
                return -1
        return candidtate