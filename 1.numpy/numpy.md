## numpy

[toc]



##### 1.ndarray属性:

- ndarray.shape: 数组维度的元组（形状）

- ndarray.ndim: 数组维数

- ndarray.size: 数组中元素的数量

- ndarray.itemsize: 一个数组元素的长度（字节）

- ndarray.dtype: 数组元素的类型

- 整数：int64

- 浮点数: float64

 

##### 2.数组生成方法

- 0/1数组：

  `np.zeros(shape) #np.zeros((3,4))`

​        `np.ones(shape)`  

- 从现有数组中生成:

​		`np.array(), np.copy() 为深拷贝`

​		`np.asarray()为浅拷贝`

- 生成固定范围的数组：

   [0,10]等距离生成100个元素: `np.linspace(0,10, 100)`

  生成区间[a, b) 步长为c的数组: `np.arange(a, b , c)`

 

##### 3.均匀分布和高斯分布

- 均匀分布（Uniform Distrebution)

  - 生成方法：

    (1)`np.random.rand(n)`: 返回[0.0, 1.0]内的一组均匀分布的数组(n个)

    (2)`np.random.uniform(low, high, size)`

    low:采样下界, high：采样上界, size：样本数目

  - 高斯分布

    生成方法：

    (1)`np.random.randn(n)`

    (2)`np.random.normal(loc, scale, size)`

    Loc:概率分布的均值, scale：概率分布的标准差, size：输出的shape

    

##### 4.数组形状修改：

- ndarray.reshape(shape）：返回新shape的数组

- ndarray.resize(shape）：无返回值，对原始的ndarray修改

- ndarray.T : 返回转置后的数组

  

##### 5.类型修改

- ndarray.astype(类型)：包括"int32", "float64"等

- ndarray.tostring(): 转化成字符串序列化到本地

- 数组去重：np.unique(arr): 返回去重后的新一维数组

  

##### 6.逻辑运算

- arr > a : 返回arr中大于a的一个布尔值数组

- arr[arr>a] : 返回arr中大于a的数据构成的一维数组

- np.all(): 括号内全为真则返回真，有一个为假则返回false

- np.any() : 括号内全为假则返回假，有一个为真则返回真

- np.where(): 三元预算符, 判断同时赋值

  如：np.where(arr>0, 1, 0)

  复合逻辑运算：

  - 与：np.logical_and(): 括号为一系列表达式

  - 或：np.logical_or() 

 

##### 7.统计运算

统计指标函数：min, max, mean, median, var, std

np.函数名

ndarray.方法名

axis参数：axis=0代表列，axis=1代表行

最大值最小值的索引函数：

np.argmax(arr, axis=)

np.argmin(arr, axis=)

 

##### 8.数组间的运算

numpy中不同维度数组是可以进行运算的，只要满足广播机制

广播机制：1. 数组拥有相同形状-->（3，4）+（3，4）

​					2. 当前维度相等--->（3，4）+（4，）

​					3. 当前维度有一个是1--->(3,1,5)+(1,3,5)

 

##### 9. 矩阵运算

matrix，和array（数组）的区别是矩阵必须是二维的。

（1）ndarray存储矩阵

（2）np.mat()存储矩阵

如：np.mat([[1, 2, 3], [4, 5, 6]]) -->matrix([[1, 2, 3], [4, 5, 6]])

（3）矩阵乘法

当类型为ndarray时，调用np.matmul（a, b）或np.dot(a, b)计算，或a @ b计算

当类型为matrix时，直接a * b即可



##### 10.合并与分割

（1）合并

​	np.hstack(arr)：按行合并

​	如：a = np.array([1,2,3]), b = np.array([4,5,6])

​	np.hstack((a,b)) ---> array([1,2,3,4,5,6])

​	np.vstack(arr)：按列合并

​	如a=np.array([[1], [2], [3]]), b= np.array([[4], [5], [6]])

​	np.vstack((a,b)) ----> array([[1],[2],[3],[4],[5],[6]])

 

​	np.concatenate():

​	axis = 0按列合并：a = array([[1,2],[3,4]]), b=array([[5,6]])

​	np.concatenate((a,b), axis=0) -->array([[1,2],[3,4],[5,6]])

​	axis按行合并：

​	np.concatenate((a,b.T), axis=1)--->

​	array([1,2,5],[3,4,6]])

（2）分割

​	np.split(arr，indices_or_sections，axis=0)

​	如：x = np.arange（9.0）

​	np.split（x，3）--> [array([0,1,2],array([3,4,5]),array([6,7,8])]

​	x = np.arange（8.0）

​	np.split（x，[3，5，6，10]) --->

​	[array([0,1,2]), array([3,4]), array([5]), array([6,7]),array()]

 

##### 11.IO操作和数据处理

​	numpy读取数据:

​	np.genfromtxt('xxx.csv', delimiter = ','): 读取时会保存成一个ndarray数组，但字符串读取会出问题，解释称缺失值：nan
