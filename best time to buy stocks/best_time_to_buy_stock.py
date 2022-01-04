def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    l = 0
    h = 1
    maxpro = 0

    while h < len(prices):
        if prices[l] < prices[h]:
            profit = prices[h] - prices[l]
            maxpro = max(maxpro, profit)
        else:
            l = h
        h += 1
    return maxpro
arr = [7,1,5,3,6,4]
print(maxProfit(arr))

# time complicity O(N)
# space complicity O(1)