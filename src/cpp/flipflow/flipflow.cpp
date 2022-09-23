#include <iostream>

int main()
{
  int t, lower, upper, n, a0, a1, diff, actualDiff;
  bool isLowerUp = false;
  
  std::cin >> t >> lower >> n;
  upper = 0;
  a0 = 0;

  for (int i = 0; i < n; i++) {
     
    std::cin >> a1;
    diff = a1 - a0; 

    if (isLowerUp) {
      actualDiff = diff > lower ? lower : diff;
      isLowerUp = false;
      lower -= actualDiff;
      upper += actualDiff;
    }
    else {
      actualDiff = diff > upper ? upper : diff;
      isLowerUp = true;
      lower += actualDiff;
      upper -= actualDiff;
    }
     
    a0 = a1;   
  }
  
  int tmp = isLowerUp ? lower - (t - a0) : upper - (t - a0);
  int res = tmp < 0 ? 0 : tmp;
  std::cout << res << std::endl;

  return 0;
}
