#include <iostream>
using namespace std;


int main() {
    cout << "Enter temperature in Celsius: ";
    double tempCelsius;
    double tempFarenheit;

    cin >> tempCelsius;

    tempFarenheit = (tempCelsius * 9/5) +32;
    cout << tempCelsius <<  " degrees C = " << tempFarenheit << " degrees F" << endl;
    return 0;
}