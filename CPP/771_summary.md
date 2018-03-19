## 反思错误

1. 编码出现了一个bug，int res;定义的时候没有初始化，导致错误。

## 思考过程

想了三种方法：

1. 双重for循环遍历，复杂度： m * n
2. 目前提交的，hash map：m + n
3. 通过string.find()，复杂度大于第2种方法

其中hash使用了std::map，同样的，考虑到是char，也可以使用数组或者vector实现。

##归纳类型

基础数据结构（hash）
