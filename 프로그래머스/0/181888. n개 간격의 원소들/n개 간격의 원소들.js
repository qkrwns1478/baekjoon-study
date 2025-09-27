const solution = (nums, n) => {
    let answer = [];
    for (let i = 0; i < nums.length; i += n) {
        answer.push(nums[i]);
    }
    return answer;
};