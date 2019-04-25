/* You may assume no duplicate exists in the array. */
#include <vector>
using namespace std;
class Solution {
public:
  int findMin(vector<int> &nums) {
    auto left = nums.begin(), right = nums.end() - 1;
    auto mid = left;
    while (*left > *right) {
      mid = (right - left) / 2 + left;
      if (*mid < *left) {
        right = mid;
      } else {
        left = mid + 1;
      }
    }
    return *left;
  }
};
