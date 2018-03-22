## 归纳类型

二进制位操作

## 思考

更高效率的解法：

```
class Solution {
public:

    int hammingDistance(int x, int y) {
        int dist = 0, n = x ^ y;
        while (n) {
            ++dist;
            n &= n - 1;
        }

        return dist;
    }
}
```


核心就是 n & (n - 1) 将最右边一位的 1 转为 0
