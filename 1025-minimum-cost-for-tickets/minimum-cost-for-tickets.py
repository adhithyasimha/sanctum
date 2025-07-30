class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        day_set=set(days)
        last_day=days[-1]

        dp=[0]*(last_day+31)

        for day in range(last_day,0,-1):
            if day in day_set:
                dp[day]=min(
                    costs[0]+dp[day+1],
                    costs[1]+dp[day+7],
                    costs[2]+dp[day+30]  
                )
        
            else:
                dp[day]=dp[day+1]

        return dp[1]

