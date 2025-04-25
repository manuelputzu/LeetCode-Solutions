def running_sum(nums):
    growing_total = 0 #variable stores the cummulative sum
    result_list = [] #list stores each cummulative sum
    for num in nums: #iterate through each element in the list
        growing_total += num #calculate the cummulative sum
        result_list.append(growing_total) #store each sum in the list
    return result_list #return the list with the results

nums = [1,3,4,5]
print(running_sum(nums))
    