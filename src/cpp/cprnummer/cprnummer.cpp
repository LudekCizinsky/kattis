#include <iostream>
#include <map>
#include <string>
using namespace std;
  
int main()
{

  map<int, int> n2n {
    {0, 4},
    {1, 3},
    {2, 2},
    {3, 7},
    {4, 6},
    {5, 5},
    {6, 4},
    {7, 3},
    {8, 2},
    {9, 1}
  };

  string num;
  cin >> num;
  int n = 0;
  int r = 0;
  for (string::size_type i = 0; i < num.size(); i++) { 
        string s = num[i];
        if (s != "-"){
          int dig = stoi(s);
          int mt = n2n[n]; 
          r += mt*dig;
          n++;
        }
  }
    
  return 0;
}
