# Ch1
## binery Search
最壞的情況是需要找log2 n次，0(log n)
- 當名單增長時，binery search會突然快許多

## 大0符號
- 代表演算法執行速度的特殊符號
- 代表最壞情況，而不是平均情況

### 常見的大0符號
- 0(log n)二進位搜尋
- 0(n)簡易搜尋
- 0(n * log n), quicksort快速排序演算法
- 0(n^2),慢速排序演算法，選擇排序法
- 0(n!),超慢速演算法



### Array 語法
- a[start:end] # items start through end-1
- a[start:]    # items start through the rest of the array
- a[:end]      # items from the beginning through end-1
- a[:]         # a copy of the whole array

## 補充
### 演算法的時間複雜度分為以下三種狀況：
- 最佳狀況(best case)時間複雜度: 考慮演算法執行時所需要的最少執行步驟數。
- 最差狀況(worst case)時間複雜度: 考慮演算法執行時所需要的最多執行步驟數。
- 平均狀況(average case)時間複雜度: 考慮所有可能狀況下演算法執行時所需要的平均步驟數。


<br>

# Ch2 選擇排序演算法
## 連結串列與陣列
- 用預留一定空間的記憶體的方法可以避免常常把已儲存的資料搬家
  - 但可能一直沒用到保留的記憶體造成浪費
  - 如果超過預留的記憶體還是要搬家


### 連結串列
- 資料可以分散存在記憶體任何角落
- 存入第一項時也存入第二項的位址，以此類推串起來
- 但如果只要知道最後一個資料還是必須從第一個開始讀
- 速度:讀取速度慢，插入速度快
  - 讀取 0(n)
  - 插入 0(1)
- 當清單需要頻繁插入，用串列

### 陣列
- 使用索引可以快速讀取
- 隨機讀取以陣列為首選
- 速度:讀取速度快，插入速度慢
  - 讀取 0(1)
  - 插入 0(n)
- 當清單需要頻繁讀取，用陣列
- 當要用binery search，只能用陣列


## 插入清單中間
- 串列：只需變更前一元素的位址指向即可
- 陣列：必須移動所有其餘元素，沒有空間的話甚至要全部搬離
- 每插入一比資料在陣列就要重新排序
- 要注意的是，要了解讀取及插入的詳細步驟才可以分辨那個比較快，如ex2.1，都需要讀取每筆資料，或ex2.2都需要讀取第一筆資料，當然一樣快


## 選擇排序
- 0(n^2)

### pop()
函数用于移除列表中的一个元素（默认最后一个元素），

<br>

# Ch3 遞迴演算法
## 遞迴
- 遞迴是指函數呼叫自身，目的在於讓解決辦法更明確，使用遞迴得不到任何效能的好處。
- 迴圈可能有助於提升程式效能，遞迴可能有助於提升程式設計師效益，應視你所處的情境決定何者重要


### 基本情況與遞迴情況 Basic case & Recursive case
- Basic case: 不會再呼叫自身
- Recursive case: 一直呼叫自身
```
def countDown(i):
  print (i)
  if i <= 0:   # Basic case
    return
  else:        # Recursive case
    countDown(i-1)
```

## 堆疊 Call Stack
- 一種後進先出(Last-In-First-Out, LIFO)的排程，堆疊提供push & pop兩個動作
- 如要插入項目會放在最頂端
- 要讀取項目則移除最頂端的項目

### 呼叫堆疊
- 這種呼叫堆疊不需由使用者追蹤為檢查的資料，資料由追蹤改為堆疊，實際運用非常簡便
- 缺點：如果堆疊太高，表示電腦裡存著許多函式呼叫的資訊，儲存這些資訊就必須佔用大量記憶體。
- 改進：改寫成迴圈或尾端遞迴
- 每個程序在呼叫堆疊只有一定的可用空間，如果程式超出空間則發生stack overflow而停止執行。

<br>

# Ch4 快速排序演算法 Quicksort
## 各個擊破法
- 將問題分做最小單位，基本情況很可能就是空陣列或含有一個元素的陣列
- 步驟：
  1. 確定最單純的基本情況
  2. 分割或縮減問題，直到將問題轉變成基本情況
- 以空陣列或含有一個元素的陣列試試看

## 快速排序
- 有些陣列根本不需排序喔～
- 空陣列和含有一個元素的陣列都使基本情況，照原樣回傳陣列，不需排序
```
def quicksort(arr):
  if len(arr) <2
    return arr
```
- 分割：
  1. 取第一個值為基準值
  2. 比基準值大的就丟到一個空陣列
- 分割後得到
  1. 小於基準值的子陣列
  2. 基準值
  3. 大於基準值的子陣列
- 子陣列再分割下去
- 歸納證明法：每次執行歸納證明都須完成基本情況和歸納情況兩個步驟

## 合併排序和快速排序
- c*n，c是一個常數，代表演算法耗費的某個固定的時間量
- c可能很重要，這正是快速排序比合併排序還快的原因
但對簡易搜尋和二進位搜尋c無關緊要，因為0(log n)和0(n)差太多

## 平均情況和最壞情況
- 已 quicksort為例，最佳情況即是平均情況，0(n log n)
- 最壞情況為0(n^2)


## 語法
### 特殊表达式
```
def larger(num1, num2):
    return num1 if num1 > num2 else num2
```
- 我们可以这样理解这种表达式：
return num1, if num1 is larger than num2.
else, return num2.
- 另外，我们还可以在赋值等多种情况下使用这种表达式：
```
a = 10
b = 20

c = a if a > b else b
```


### 在List comprehension中使用if
```
numbers = [x for x in range(100) if x % 3 == 0]
print(numbers)
```
- 上述代码会将100之内能被3整除的数字作为一个list赋值给numbers。
- List comprehension的原理是这样的：首先将range(100)的结果赋值给x。

然后使用if判断出所有x内的能整除3的数字、并将这个值作为一个list赋值给x。

最后，将x赋值给numbers。一个复杂的表达式使用一条语句就这么完成了。


### array相加
```
array = [1,2] + [3,4] + [5,6]
print (array)   #[1, 2, 3, 4, 5, 6]
```
- js會得出"1,23,45,6"


<br>

# Ch5 雜湊表 Hash Table
- 雜湊表用來建立項目之間的對應關係

## 雜湊函數
- 雜湊函數指的是輸入字串(或任何資料)輸出數字的函數
  - 一樣的字串必須得到一樣的數字，反之亦然
- 再由數字(陣列的索引值)對應到陣列的值
- 重點是一對一，建立一個項目與另一個項目的關係，還可以濾除重複項目
```
book = dict()
book['apple'] = 0.67
book['milk'] = 1.49
```


### 使用案例
- 每個網址轉成ip，過程稱為DNS resolution
- 投票，電話簿


### 雜湊表用作快取
- 記住資料，而非指示伺服器工作
- 讓網站記住而非重新計算資料，更快又減輕負荷，

## 碰撞 Collision
- 事實上不大可能每個字串都對應到陣列中的某個位置，因此利用連結串列 eg: apple, avocado
- 但萬一所有資料都是a，搜尋速度就變慢了
- 重點：雜湊函數在雜湊表上均勻的完成鍵的對應


## 效能
- 在平均情胯下，雜湊表的耗費的時間為0(1)
- 避開碰撞:確保低負載係數，選用好的雜湊函數

### 負載係數
- 雜湊表的項目數/儲存槽總數
- 一旦負載係數較高(0.7)，為避免碰撞產生，就就要增加儲存槽，稱為Resizing


<br>


# Ch6 廣度優先搜尋法
- 搜尋兩點之間最短距離，eg：西洋棋如何用最少移動次數獲勝，拼字檢查，地圖上兩點距離
- 演算法尋找的必定是最短路徑，必須完成兩個步驟
  1. 建立圖形模型
  2. 再用廣度優先法解決問題

## 圖形概述
- 圖形由點和邊組成，指出不同物件如何相互連接

## 廣度優先搜尋
1. 兩點是否存在路徑
2. 哪一條是最短路徑
- 須先搜尋一等連接再搜尋二等連接，所以必須加入順序搜尋，此方法對應的資料結構為Queue

## Queue 宁列
- 宁列結構為先進先出，像排隊一樣
- 查看某個點後務必確保不會再查看相同的人防止進入迴圈

### 執行時間
- 0(點 ＋ 邊) => 0(V+E)

### 拓樸排序
- B取決於A，先有A，再有B
- 圖示樹狀的，不會有邊往回指


## 語法
### popleft()
- Remove and return an element from the left side of the deque. If no elements are present, raises an IndexError.

### if not checkname in searched
- same as ```if checkname not in searched```

<br>


# Ch7 Dijkstra's algorithm 代克斯托演算法
- 廣度優先搜尋會找最少路徑，代克斯托法可以找出最快路徑
- 每個會加上權重weight
1. 尋找最容易抵達的節點，也就是花費最少時間
2. 更新該節點相鄰的節點成本
3. 對每個節點執行相同步驟
4. 計算最後路徑
- 僅適用有向無環圖Directed Acyclic Graph，意思是不走迴路，不然永遠找不到最短路徑
- 邊不能有負權重，有負權重要用Bellman-Ford Algorithm


### keys()
returns a list of all the available keys in the dictionary.


<br>


# Ch8 貪婪演算法(一種近似演算法)
- 排課問題，挑最早結束的課程，下一堂也是如此，以此類推
- 背包問題，每次都挑最貴又能放入背包的東西
- 電台問題，電台必須覆蓋最多尚未覆蓋的州
- 雖然不是最佳解，但也近似了
- 評定標準為，速度快慢＆與最佳解的接近程度
- 企圖大道局部最佳化，並寄望能達到全域最佳
- 廣度優先搜尋和代克思托演算法都是貪婪演算法


## NP完備問題
- 先確認問題是否為ＮＰ問題
    - 是：用近似演算法處理，否則算不完
    - 否：找適合的演算法
- 如何判斷問題是否為ＮＰ問題
  - 項目很多
  - 計算Ｘ的所有組合
  - 無法將Ｘ分割成更小的分子，所以必須計算Ｘ的所有狀況。
  - 涉及序列(旅行推銷員)
  - 涉及集合/覆蓋(電台問題)
  - 能把問題當作集合覆蓋或旅行推銷員，就一定是ＮＰ問題
- 目前尚無演算法能解決NP完備問題，所以用近似演算法
- 貪婪演算法容易撰寫而且執行快，是理想的近似演算法


## 程式
- 清單不可有重複項目



## 語法
### add()
- 隨機家的？？


### set()
- Constructs a new empty Set object.



- 連集 fruit | vegetable
- 交集 fruit & vegetable
- 差集 fruit - vegetable
- ^ 排除相同元素（XOR）運算
- >測試左集合是否為右集 合的父集
- 使用<測試左集合是否為右集合的子集

### items()
- This method returns a list of tuple pairs.


### for loop with key value

```
for key, value in d.items():
```

<br>


# Ch9 動態規劃演算法
- 從子問題著手解決所有問題
- 以欄或列為主可能會影響結果
- 不能處理部分拿取的問題，這問題要用貪婪演算法
- 在受限情況下找最佳解很好用
- 只適用可將問題分割成離散子問題的應用，不適用於相互依存的子問題


## 導出動態規劃解答
- 每個動態解答都會用到方格
- 格子裡得值通常是最佳化對象
- 每個格子都是一個子問題，如何將問題分割成子問題，有助方格確立
- 沒有一定計算公式

## 最常共用子計算
- 用處：拼字檢查，物種或疾病DNA相似度，Diff的功能(eg: git diff)，著作權保護資料，自動換行功能(eg:Microsoft word)


# Ch10 Ｋ最近鄰演算法
- KNN用於分類和回歸，且與檢視Ｋ最近相鄰有關。
  - 分類：歸類為群組
  - 回歸：預測回應/數字

## 建立推薦系統
1. 先將所有使用者畫在圖形上
2. 怎麼知道不同使用者的相似程度，特徵萃取
- 推薦統的裡的項目可以分配權中
- 應用:機器學習，垃圾郵件過濾器，預測股票行情(？)

### 特徵萃取
- 將項目轉換成可以相互比較的數字清單
- 用畢氏定理，但不限維度
- 問題 每個使用者評分的慷慨程度不同，可以使用正規化演算法修正，便可在同一尺度衡量
