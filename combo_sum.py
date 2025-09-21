def backtrack(start, path total):
    if (total == target):
        res.append(path[:])
        return
    
    if (total > target):
        return
    
    for i in range(start, len(nums)):
        path.append(nums[i])
        backtrack(i, path, total + nums[i])
        path.pop()


backtrack(0, [], 0)

return res