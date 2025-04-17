class Solution {
public:
    int kConcatenationMaxSum(vector<int>& arr, int k) {
         int m_sum = 0, sz = arr.size();
    for (auto i = 0, sum = 0; i < min(2, k) * sz; ++i) {
        sum = max(sum + arr[i % sz], arr[i % sz]);
        m_sum = max(m_sum, sum);
    }
    return ((long long)m_sum + 
        max(0ll, accumulate(begin(arr), end(arr), 0ll) * max(0, k - 2))) % 1000000007;
    }
};