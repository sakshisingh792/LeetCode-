class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1],reverse=True)
        total=0
        for box, unit in boxTypes:
            boxes_to_take=min(box,truckSize)
            total+=boxes_to_take*unit
            truckSize-=boxes_to_take

            if truckSize==0:
                break
        return total        
        