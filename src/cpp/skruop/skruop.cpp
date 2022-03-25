#include <iostream>
#include <string>
using namespace std;
  
int main()
{
  string ns;
  getline(cin, ns);
  int n = stoi(ns);
   
  int vol = 7;

  for (int i = 0; i < n; i++) {
    string s;
    getline(cin,s);   
    if (s == "Skru op!" && vol < 10) {
      vol++;
    }
    else if (s == "Skru ned!" && vol > 0){
      vol--;
    }
  }

  cout << vol << endl;

  return 0;
}
