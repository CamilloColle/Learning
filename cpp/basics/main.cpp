#include <iostream>
using namespace std;

/*
int main() {
    int file_size = 0; //always initialize variables to avoid getting random values
    int counter = 0;
    //int file_size = 0, counter = 0; //possible but bad practice
    double sales = 9.99;
    cout << "Hello World" << endl;
    return 0;
}
*/

//function to swap to variables
// Function declaration
int swap(int& a, int& b);

int main() {
    int a = 1;
    int b = 2;

    // Call the swap function
    swap(a, b);

    cout << "After swap: a = " << a << ", b = " << b << endl; // should print the swapped values
    return 0;
}

// Function definition
int swap(int& a, int& b) {
    int temp = a;
    a = b;
    b = temp;
    return a; // returning the value of one variable (a)
}