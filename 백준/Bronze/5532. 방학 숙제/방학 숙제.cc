#include<iostream>
int main(){
    int L;
    int A;
    int B;
    int C;
    int D;
    std::cin >> L;
    std::cin >> A;
    std::cin >> B;
    std::cin >> C;
    std::cin >> D;
    int kor = A / C;
    int mat = B / D;
    if(A % C > 0){
        kor++;
    }
    if(B % D > 0){
        mat++;
    }
    int answer = L - std::max(kor, mat);
    std::cout << answer << std::endl;
    return 0;
}