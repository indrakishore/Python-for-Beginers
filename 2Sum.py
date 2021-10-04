def twoSum(nums, target):
    ans = {}
    for i in range(len(nums)):
       if target - nums[i] in ans:
          return [ans[target - nums[i]],i]
       else:
          ans[nums[i]]=i
            
if __name__ == "__main__":
    input_list = [2,8,12,15] 
    print(twoSum(input_list, 20))
