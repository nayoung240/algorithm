class Solution:
    '''
    - 두 점이 같은 선상에 있는지 확인하려면 기울기를 계산해야 합니다. 
    - 기울기 공식은 (y2 - y1) / (x2 - x1)
    - key point: never use devision to judge whether 3 points are on a same line or not, use the multiplication instead !!
    - (x1 - x0) / (y1 - y0) == (x2 - x1) / (y2 - y1) - This will result in floating points which is not desirable for comparison.
    - (x1 - x0) * (y2 - y1) == (x2 - x1) * (y1 - y0) - Avoid floating points using multiplication.
    '''
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        stock_len = len(stockPrices)
        stockPrices.sort(key = lambda x: (x[0], x[1]))
        
        if stock_len == 1:
            return 0
        
        pre_delta_y = stockPrices[0][1] - stockPrices[1][1]
        pre_delta_x = stockPrices[0][0] - stockPrices[1][0]
        answer = 1
        
        for i in range(1, stock_len-1):
            cur_delta_y = stockPrices[i][1] - stockPrices[i+1][1]
            cur_delta_x = stockPrices[i][0] - stockPrices[i+1][0]
            
            if pre_delta_y * cur_delta_x != pre_delta_x * cur_delta_y:
                answer += 1
                pre_delta_x = cur_delta_x
                pre_delta_y = cur_delta_y
        
        return answer
