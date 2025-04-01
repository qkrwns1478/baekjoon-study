#include <iostream>
int main(){
    int t;
    std::cin >> t;
    for(int i = 1; i <= t; i++) {
        int a, b;
        std::cin >> a >> b;
        std::cout << "Case " << i <<": " << a+b << std::endl;
    }
    return 0;
}