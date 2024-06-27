//escribir un programa que ordene un array de enteros 
#include<iostream>
#include<algorithm>
using std::endl;
using std::cout;
using std::sort;
void ordenar (){
    
    int nr[] = {28,34,54,89,12};
     std::sort(nr , nr + 5);
    for (int i= 0; i < 5; ++i )
        cout << "numero"<< ": "<< nr[i] << endl;
}

int main (){

    ordenar();

    return 0;
}
