const solution = (nums) => {
    const n = nums.length;
    if (nums[n-1] > nums[n-2]) nums.push(nums[n-1] - nums[n-2]);
    else nums.push(nums[n-1] * 2);
    return nums;
};