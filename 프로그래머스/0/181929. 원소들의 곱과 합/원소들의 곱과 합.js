const solution = (nums) => {
    let mul = 1;
    let sum = 0;
    for (let i = 0; i < nums.length; i++) {
        mul *= nums[i];
        sum += nums[i];
    }
    return mul < sum * sum ? 1 : 0;
};