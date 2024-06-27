//hacer un programa que detecte palindromos
#include <iostream>
#include <string>
#include <algorithm>
using std::cout;
using std::endl;
using std::cin;
using std::string;
using std::reverse;
void palindromos(){
    string palabra,palabraInver;
    
    cout<<"Ingrese una palabra o nr que quieras saber si es que es un palindromo o no: "; getline(cin,palabra);
    
    palabraInver = palabra;

    reverse(palabraInver.begin(), palabraInver.end());

    if (palabra == palabraInver){

        cout<<"La palabra o nr ingresado es un palindromo";
    }
    else {

        cout<<"La palabra o nr ingresado no es un palidromo";
    }
    
    }


int main (){

    palindromos();

    return 0;
}