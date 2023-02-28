def Product_of_Array_Except(nums):
    left_product = []
    for i in range(len(nums)):
        if i == 0:
            left_product.append(nums[i])
        else:
            left_product.append(left_product[i-1]*nums[i])

    right_product = []
    j=0
    for i in range(len(nums)-1,-1,-1):
        if i == 0:
            right_product.append(nums[i])
        else:
            right_product.append(right_product[i-1]*nums[i])
        j+=1
        right_product = right_product[::-1]

    result = []
    for i in range(0,len(num)):
        if i== 0

    


    return nums
    




nums = [1,2,3,4]
print(Product_of_Array_Except(nums))