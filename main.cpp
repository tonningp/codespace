#include <iostream>
#include <string>
using namespace std;

int main() {
   string passwdStr;
   int i;
	int lengthStr;
   
   cin >> passwdStr;
   i = 0;
   lengthStr = 0;
   // asdfjHgV&69NvX
   // asdfjpHgV&69NvX
   while( i != string::npos ) {
      i = passwdStr.find("asdf");
      if( i != string::npos) {
          passwdStr.replace(i,4,"");
      }
   }
   lengthStr = passwdStr.size();
   cout << "Remaining string: " << passwdStr << endl;
	cout << "Length: " << lengthStr << endl;
   
   return 0;
}
