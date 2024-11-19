#include <iostream>
#include <windows.h>
#include <iomanip>
#include <string>

using namespace std;

void encabezado() {
	SetConsoleOutputCP(1252);

	int dia, mes, ano;
	long long ruc;
	string nombre;

	cout << "Ingrese su RUC: ";
	cin >> ruc;
	cout << "Ingrese su Nombre: ";
	cin.ignore();
	getline(cin,nombre);
	cout << "Ingrese la Fecha(dd/mm/aa): ";
	cin >> dia >> mes >> ano;

	cout << "--------------------------------" << endl << "            FACTURA" << endl << "--------------------------------" << endl<<endl;
	cout << "N° de Factura:              0001" << endl;
	cout << "Fecha de emisión:     " << dia << "/" << mes << "/" << ano << endl << endl << "--------------------------------" << endl;
	cout << "        DATOS DEL CLIENTE" << endl << "--------------------------------" << endl;
	cout << "Cliente:           " << nombre << endl;
	cout << "RUC:               " << ruc << endl << endl << "--------------------------------" << endl;
}

void detalles() {
	
	string pro1, pro2, pro3;
	float precio1, precio2, precio3, subT, total;

	cout << "     DETALLES DE LA FACTURA     " << endl << "--------------------------------" << endl << "Descripción" << endl;
	cout << "--------------------------------" << endl;
	cin.ignore();
	getline(cin,pro1);
	cout << "    $";
	cin >> precio1;
	cin.ignore();
	getline(cin,pro2);
	cout << "    $";
	cin >> precio2;
	cin.ignore();
	getline(cin,pro3);
	cout << "    $";
	cin >> precio3;

	subT = precio1 + precio2 + precio3;
	total = subT * 1.12;

	cout << "--------------------------------" << endl;
	cout << "Subtotal               $" << subT << endl;
	cout << "--------------------------------" << endl;
	cout << "IVA                    $" << subT*0.12 << endl;
	cout << "--------------------------------" << endl;
	cout << "Total                  $" << fixed << setprecision(2) << total << endl;
	cout << "--------------------------------" << endl;

}

int main() {

	encabezado();
	detalles();

	return 0;
}
