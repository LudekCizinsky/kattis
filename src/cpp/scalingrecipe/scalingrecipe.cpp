#include <string>
#include <ctype.h>
#include <iostream>
#include <vector>
#include <sstream>

// This function is from:
// https://www.fluentcpp.com/2017/04/21/how-to-split-a-string-in-c/
std::vector<std::string> split(const std::string s, char delimiter)
{
   std::vector<std::string> tokens;
   std::string token;
   std::istringstream tokenStream(s);
   while (std::getline(tokenStream, token, delimiter))
   {
      tokens.push_back(token);
   }
   return tokens;
}

int main()
{
  std::string s;
  std::getline(std::cin, s); 
  
  char del = ' ';
  std::vector<std::string> line1 = split(s, del);
  int n = stoi(line1[0]);
  double x = stoi(line1[1]);
  double y = stoi(line1[2]);
  double r = y/x;
  // std::cout << r << std::endl;
 
  for (int i = 0; i < n; i++)
  {
    std::string raw;
    getline(std::cin, raw);
    int ingr = stoi(raw);
    int res = ingr*r;
    std::cout << res << std::endl;
  }

  return 0;
}
