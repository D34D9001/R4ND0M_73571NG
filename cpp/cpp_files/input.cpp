#include <iostream>
using namespace std;

int main() {
  string userName;
  cout << "What's your name?\n>> ";
// cin is used with '>>' to store user input as a variable
  cin >> userName;
  cout << "Hi, " << userName << "!";
  return 0;
}
