#include <iostream>
using namespace std;


/*
int main() {
    int x = 10;
    int y = 3;
    int z = x + y;
    z++;
    ++z;
    cout << "x + y = " << z;
    return 0;
}
*/

int main(){
    double sales = 95000;
    cout << "Sales: EUR" << sales << endl;

    const double stateTaxRate = .04;
    double stateTax = sales * stateTaxRate;
    cout << "State Tax: EUR" << stateTax << endl;

    const double countyTaxRate = .02;
    double countyTax = sales * countyTaxRate;
    cout << "State Tax: EUR" << countyTax << endl;

    double totalTax = stateTax + countyTax;
    cout << "Total Tax: EUR" << totalTax << endl;

    return 0;
}