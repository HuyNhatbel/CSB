def find_elements(nums):
    limits = len(nums) // 3
    
    count_times = {}
    for numbers in nums:
        if numbers in count_times:
            count_times[numbers] += 1
        else:
            count_times[numbers] = 1
    
    result = []
    for numbers, times in count_times.items():
        if times > limits:
            result.append(numbers)
    
    return result