class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        ans = float('inf')

        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):

                # Land -> Water
                finish_land = landStartTime[i] + landDuration[i]

                start_water = max(finish_land, waterStartTime[j])

                total1 = start_water + waterDuration[j]

                # Water -> Land
                finish_water = waterStartTime[j] + waterDuration[j]

                start_land = max(finish_water, landStartTime[i])

                total2 = start_land + landDuration[i]

                ans = min(ans, total1, total2)

        return ans
        