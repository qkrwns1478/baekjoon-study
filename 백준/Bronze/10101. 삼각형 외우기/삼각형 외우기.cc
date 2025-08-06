#include <iostream>
using namespace std;

int main() {
  int x, y, z;
  cin >> x;
  cin >> y;
  cin >> z;
  if (x == 60 && y == 60 && z == 60) cout << "Equilateral" << endl;
  else if (x + y + z == 180) {
    if (x == y || y == z || z == x) cout << "Isosceles" << endl;
    else cout << "Scalene" << endl;
  }
  else cout << "Error" << endl;
  return 0;
}