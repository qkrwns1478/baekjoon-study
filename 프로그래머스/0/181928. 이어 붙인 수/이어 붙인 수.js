function solution(num_list) {
    let odds = '';
    let even = '';
    
    for (let i = 0; i < num_list.length; i++) {
        if (num_list[i] % 2)
            odds += num_list[i].toString();
        else
            even += num_list[i].toString();
    }
    
    return Number(odds) + Number(even);
}