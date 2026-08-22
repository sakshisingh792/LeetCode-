class Solution:
    def maximum69Number (self, num: int) -> int:
        temp=num
        placevaluesix=-1
        placeval=0
        while temp>0:
            rem=temp%10
            if rem==6:
                placevaluesix=placeval

            temp =temp//10
            placeval+=1


        if placevaluesix==-1:
            return num
        else:
            return num+3*(pow(10,placevaluesix))            
        