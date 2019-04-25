class Solution {
public:
  int findMin(vector<int> &nums) {
    if (nums.empty()) {
      return 0;
    }
    auto arr_begin = nums.begin();
    auto arr_end = nums.end() - 1;
    if (*arr_end > *arr_begin) {
      return *arr_begin;
    }
    auto mid = (arr_end - arr_begin) / 2 + arr_begin;
    while (arr_begin != arr_end) {
      if (arr_end - arr_begin == 1)
        return *arr_end;
      mid = (arr_end - arr_begin) / 2 + arr_begin;

      if (*arr_begin == *mid && *arr_begin == *arr_end)
        return *min_element(arr_begin, arr_end + 1);

      if (*mid < *arr_begin) {
        // 在前一半
        arr_end = mid;
      } else {
        // 在后一半
        arr_begin = mid;
      }
    }
    return *arr_begin;
  }
};
