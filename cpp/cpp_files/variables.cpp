#include <iostream>
using namespace std;

int main() {

/*
In C++, there are different types of variables (defined with different keywords), for example:

    int - stores integers (whole numbers), without decimals, such as 123 or -123
    double - stores floating point numbers, with decimals, such as 19.99 or -19.99
    char - stores single characters, such as 'a' or 'B'. Char values are surrounded by single quotes
    string - stores text, such as "Hello World". String values are surrounded by double quotes
    bool - stores values with two states: true or false
*/

/*
Syntax
type variableName = value;
*/

  int myNum = 13;
  cout << myNum << endl;

// Variables can also be declared without immediately assigning a value

  int urNum;
  urNum = 21;
  cout << urNum << endl;

// Note that if you assign a new value to an existing variable, it will overwrite the previous value:

// Examples

  int myOtherNum = 5;               // Integer (whole number without decimals)
  double myFloatNum = 5.99;    // Floating point number (with decimals)
  char myLetter = 'D';         // Character
  string myText = "Hello";     // String (text)
  bool myBoolean = true;       // Boolean (true or false)

  cout << myOtherNum << endl;
  cout << myFloatNum << endl;
  cout << myLetter << endl;
  cout << myText << endl;
  cout << myBoolean << endl;

// cout can be used to display multiple varibles at once

cout << myText << ", I am " << myOtherNum << " years old. My name starts with " << myLetter << endl;

// To add variables together:

int x = 6;
int y = 8;
int answer = x + y;
cout << answer << endl;

// To declare more than one variable of the same type, use a comma-separated list:

int q = 2, t = 7, p = 24;
cout << q + t + p << endl;

/*
All C++ variables must be identified with unique names.

These unique names are called identifiers.

Identifiers can be short names (like x and y) or more descriptive names (age, sum, totalVolume).

Note: It is recommended to use descriptive names in order to create understandable and maintainable code
*/

// Good
int minutesPerHour = 60;

// OK, but not so easy to understand what m actually is
int m = 60;

/*
The general rules for naming variables are:

    Names can contain letters, digits and underscores
    Names must begin with a letter or an underscore (_)
    Names are case sensitive (myVar and myvar are different variables)
    Names cannot contain whitespaces or special characters like !, #, %, etc.
    Reserved words (like C++ keywords, such as int) cannot be used as names
*/

/*
When you do not want others (or yourself) to override existing variable values,
use the const keyword (this will declare the variable as "constant", which means
unchangeable and read-only)
*/

const int myCon = 15;  // myNum will always be 15
// myNum = 10;  // error: assignment of read-only variable 'myNum'

/*
   You should always declare the variable as constant when you have values that
   are unlikely to change
*/

cout << myCon;
}
