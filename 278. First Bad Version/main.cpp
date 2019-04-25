// Forward declaration of isBadVersion API.
bool isBadVersion(int version);

class Solution {
public:
  int firstBadVersion(int n) {
    // 事实上，在最后一般需要判断。但这题确定target存在。
    int left = 1, right = n, mid;
    while (left < right) {
      mid = (right - left) / 2 + left;
      if (isBadVersion(mid)) {
        right = mid;
      } else {
        left = mid + 1;
      }
    }
    return left;
  }
};
