#include <iostream>
using std::cout;
using std::cin;
using std::endl;
using namespace std;



int main (){
    int nr1 , nr2, resultado;
    cout <<"Ingrese un numero que desea sumar: "; cin>>nr1;
    cout <<"Ingrese otro nr que desee sumar con el anterior: "; cin>>nr2;
    resultado = nr1 + nr2;
    cout<<"\nLa suma entre ambos numeros es de:"<<resultado<<endl;

    return 0;
}



