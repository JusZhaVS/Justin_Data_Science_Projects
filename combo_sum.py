def backtrack(start, path total):
    if (total == target):
        res.append(path[:])
        return
    
    if (total > target):
        return
    


backtrack(0, [], 0)

return res