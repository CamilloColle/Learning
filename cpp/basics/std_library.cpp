#include <iostream>
#include <cmath>

using namespace std;

/*
int main(){ 
    double result = floor(1.2);
    double power = pow(3, 3);
    cout << result << endl << power << endl;
    return 0;
}
*/

int main () {
    cout << "Enter circle radius: ";
    double radius = 0;
    double area = 0;
    const double pi = 3.14;

    cin >> radius;
    area = pow(radius, 2) * pi;
    cout << "The area of your circle is: " << area << endl;
    return 0;
}