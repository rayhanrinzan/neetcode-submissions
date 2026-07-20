class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        def mul(lst):
            product = lst.pop(0)
            while len(lst) > 0:
                product *= lst.pop(0)
            return(product)
        products = []
        for i in range(len(nums)):
            lst = nums.copy()
            lst.pop(i)
            products.append(mul(lst))
        return(products)
            
        