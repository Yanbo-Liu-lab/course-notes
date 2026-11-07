## 一、本章补上的第三套方程：为什么前两章还不够

前两章分别从静力学和几何学出发，推出了连续介质必须共同满足的方程：平衡（或运动）方程来自对微元体的受力分析，几何方程来自位移与应变的微分关系。这两套方程有一个共同特点——**推导时完全没有用到材料是什么**。它们描述的是"任何连续体都必须满足的约束"，而不是"这种材料在受力后会怎样变形"。

原文据此指出：仅用这些方程还不足以解决变形固体的平衡（或运动）问题，因为在推导时"并没有考虑应力和应变的内在联系"。换句话说，方程数少于待求量，定解条件不封闭。要闭合，必须补上第三套方程——**本构关系**，即物理方程，它表达的是"对每种材料而言，在一定的温度下，应力和应变之间完全确定的关系"，反映材料固有特性。

本章的任务因此是一个很具体的目标：**在弹性阶段内，建立应力与应变之间的关系**。围绕这个目标，全章的推理骨架是：

1. 先写出应力应变的**最一般非线性关系**（6 个任意函数）；
2. 用**小变形**把它在零应变处泰勒展开并截断，得到线性关系（36 个常数）；
3. 用**应变能的存在**证明常数矩阵对称，独立常数降到 21 个；
4. 用**材料对称性**继续削减：21 → 13 → 9 → 5 → 2；
5. 最后把 2 个抽象常数换成**可测量的工程常数** $E$、$\nu$、$G$，并给出应变能的具体形式；
6. 全章结论各自携带不同的前提，必须逐条区分（见第七节）。

这套骨架里有两条独立的"削减"渠道，值得先记住：**能量**削减的是常数之间的对称性，**几何对称性**削减的是常数的个数。二者互不替代。

## 二、从任意函数到线性关系：广义胡克定律的由来

**这一节解决什么问题**：应力与应变之间最一般的关系是 6 个未知函数，凭实验无法在复杂应力状态下逐一测定；我们要找一个在数学上可控、在物理上合理的简化入口。

### 2.1 最一般形式只是一个"空壳"

最一般的关系写成

$$
\sigma_i = f_i(\varepsilon_x,\varepsilon_y,\varepsilon_z,\gamma_{yz},\gamma_{xz},\gamma_{xy}),\qquad i=1,2,\cdots,6
$$

即式 (4-1)，六个应力分量各是六个应变分量的函数。原文明确说：函数 $f_i$ 取决于材料本身的物理特性，选择它们时要尽可能正确反映材料固有的物理性质。但对复杂受力情况，即使材料各向同性，也很难直接由实验确立这些函数。所以式 (4-1) 只是形式上的完备，没有可操作性。

### 2.2 小变形：从 6 个函数到 36 个常数

原文的做法是：**只考虑弹性体小变形的情况**，把式 (4-1) 在应变分量为零处展开成泰勒级数，略去二阶及以上小量。以第一式为例：

$$
\sigma_x=(f_1)_0+\left(\frac{\partial f_1}{\partial\varepsilon_x}\right)_0\varepsilon_x+\cdots+\left(\frac{\partial f_1}{\partial\gamma_{xy}}\right)_0\gamma_{xy}
$$

这里有三个关键点，缺一不可：

- $\left(\partial f_1/\partial\varepsilon_x\right)_0$ 等是偏导数在**应变全为零**处的取值，因此是常数；
- 常数项 $(f_1)_0$ 代表**初始应力**，由"无初始应力"假设取为零；
- 截断的依据是变形很小，二阶以上项是高阶小量。

对六个式子做同样处理，得到

$$
\sigma_x=C_{11}\varepsilon_x+C_{12}\varepsilon_y+C_{13}\varepsilon_z+C_{14}\gamma_{yz}+C_{15}\gamma_{xz}+C_{16}\gamma_{xy}
$$

等六式，即式 (4-2)，系数 $C_{mn}$（$m,n=1,\cdots,6$）称为**弹性常数**，共 36 个。

原文特别交代了这一步的"身份"：式 (4-2) 看起来像是纯数学演绎，但在微小变形下选择这样的关系显然是合理的；实际上可以把它看作**胡克定律在复杂受力情况下的推广**，故称**广义胡克定律**。这句话很重要——它不是从单向拉伸的实验曲线"推"出来的，而是"线性化 + 无初始应力"两条假设的产物。

### 2.3 均匀性写在常数里

若物体由非均匀材料组成，各处弹性效应不同，$C_{mn}$ 一般是坐标 $(x,y,z)$ 的函数。若物体由均匀材料组成，则"承受同样的应力必产生相同的应变，反之亦然"，反映在式 (4-2) 中就是 $C_{mn}$ 为常数。本章之后的一切讨论都默认这一条：**均匀材料**。

**易错辨析**
- 式 (4-2) 中的 $\gamma_{xy}$ 是**工程切应变**，不是张量分量 $\varepsilon_{xy}$。这就是为什么后面的各向同性形式里切应力写成 $\tau_{xy}=\mu\gamma_{xy}$，而不是 $2\mu\varepsilon_{xy}$（两者等价，$\gamma_{xy}=2\varepsilon_{xy}$）。
- 36 个常数**不是**独立常数。独立与否要由能量条件（第三节）和材料对称性（第四节）决定。
- 式 (4-1) 开头的"在一定的温度下"是前提的一部分：本章不讨论温度变化引起的应变。

## 三、能量渠道一：应变能的存在与格林公式

**这一节解决什么问题**：\(C_{mn}\) 有 36 个，是否存在内在约束？答案来自热力学——如果应力可以从一个"势"求导得到，常数矩阵就必然对称。这一节同时给本构关系一个能量形式的表述。

### 3.1 从热力学第一定律到内能密度

取物体内任一有限部分（区域 $V$，表面 $S$）。热力学第一定律说：外力作的功，一部分变成动能，一部分变成内能，同时还要计入吸放热：

$$
\frac{\mathrm{d}W}{\mathrm{d}t}=\frac{\mathrm{d}E_{\mathrm{k}}}{\mathrm{d}t}+\frac{\mathrm{d}V_{\mathrm{I}}}{\mathrm{d}t}-\frac{\mathrm{d}Q}{\mathrm{d}t}
$$

即式 (4-3)。若为**绝热过程**（无热量损失、不吸热），外力功全部转为动能和内能，得式 (4-4)。

接下来是本章最漂亮的一段推导，思路分四步：

1. 写出动能及其变化率（式 a、b）；
2. 写出体力和面力在 $\mathrm{d}t$ 内作的功（式 c、d）；
3. 对**面力功**用面力边界条件 (2-4) 代入，再用**高斯积分公式**把面积分化为体积分。化出来的体积分里出现两类项：一类含应力的空间偏导数，另一类是 $\sigma_x\partial\varepsilon_x/\partial t+\cdots+\tau_{xy}\partial\gamma_{xy}/\partial t$；
4. 利用**运动方程** (2-5)，把第一类项与惯性项抵消，得到式 (g)；再与式 (4-4) 比较、消去动能项，得到

$$
\frac{\mathrm{d}V_{\mathrm{I}}}{\mathrm{d}t}=\iiint_V\left(\sigma_x\frac{\partial\varepsilon_x}{\partial t}+\sigma_y\frac{\partial\varepsilon_y}{\partial t}+\sigma_z\frac{\partial\varepsilon_z}{\partial t}+\tau_{yz}\frac{\partial\gamma_{yz}}{\partial t}+\tau_{xz}\frac{\partial\gamma_{xz}}{\partial t}+\tau_{xy}\frac{\partial\gamma_{xy}}{\partial t}\right)\mathrm{d}V
$$

即式 (h)。再引入内能密度 $v_{\mathrm{I}}$，使 $V_{\mathrm{I}}=\iiint_V v_{\mathrm{I}}\,\mathrm{d}V$，代入式 (h)。由于区域 $V$ 可以任意选取，被积函数必须逐点相等，于是

$$
\frac{\partial v_{\mathrm{I}}}{\partial t}=\sigma_x\frac{\partial\varepsilon_x}{\partial t}+\sigma_y\frac{\partial\varepsilon_y}{\partial t}+\sigma_z\frac{\partial\varepsilon_z}{\partial t}+\tau_{yz}\frac{\partial\gamma_{yz}}{\partial t}+\tau_{xz}\frac{\partial\gamma_{xz}}{\partial t}+\tau_{xy}\frac{\partial\gamma_{xy}}{\partial t}
$$

固定 $x,y,z$，即得 $\mathrm{d}t$ 时间内内能密度的增量

$$
\mathrm{d}v_{\mathrm{I}}=\sigma_x\mathrm{d}\varepsilon_x+\sigma_y\mathrm{d}\varepsilon_y+\sigma_z\mathrm{d}\varepsilon_z+\tau_{yz}\mathrm{d}\gamma_{yz}+\tau_{xz}\mathrm{d}\gamma_{xz}+\tau_{xy}\mathrm{d}\gamma_{xy}
$$

**这一步是整节的转折点**：内能密度是状态的单值函数，所以 $\mathrm{d}v_{\mathrm{I}}$ 必须是**全微分**。全微分条件立刻给出

$$
\sigma_x=\frac{\partial v_{\mathrm{I}}}{\partial\varepsilon_x},\quad
\sigma_y=\frac{\partial v_{\mathrm{I}}}{\partial\varepsilon_y},\quad
\sigma_z=\frac{\partial v_{\mathrm{I}}}{\partial\varepsilon_z},\quad
\tau_{yz}=\frac{\partial v_{\mathrm{I}}}{\partial\gamma_{yz}},\quad
\tau_{xz}=\frac{\partial v_{\mathrm{I}}}{\partial\gamma_{xz}},\quad
\tau_{xy}=\frac{\partial v_{\mathrm{I}}}{\partial\gamma_{xy}}
$$

即式 (4-5)，原文称为**弹性体在绝热情况下以能量形式表示的物理方程**。

### 3.2 等温过程：熵与自由能

等温情况下要换一个热力学函数。原文引入熵：变形过程中热量的增加有两个来源——外界输入与内部热源，以及物体自身对变形和热流的阻力所耗功转换的热量，两者分别引起 $\mathrm{d}S_{\mathrm{e}}$ 和 $\mathrm{d}S_{\mathrm{i}}$，总增量 $\mathrm{d}S=\mathrm{d}S_{\mathrm{e}}+\mathrm{d}S_{\mathrm{i}}$，其中 $\mathrm{d}S_{\mathrm{e}}=\mathrm{d}Q/T$（$T$ 为热力学温度），$\mathrm{d}S_{\mathrm{i}}$ 称产熵。

热力学第二定律：一切热力学过程都不会使产熵减少，即 $\mathrm{d}S_{\mathrm{i}}\geqslant 0$。**对塑性变形等不可逆过程 $\mathrm{d}S_{\mathrm{i}}>0$；对弹性变形等可逆过程 $\mathrm{d}S_{\mathrm{i}}=0$**。因此弹性变形下 $\mathrm{d}S=\mathrm{d}Q/T$，即 $\mathrm{d}Q/\mathrm{d}t=T\,\mathrm{d}S/\mathrm{d}t$。等温过程又有 $\mathrm{d}T/\mathrm{d}t=0$，把它代回式 (4-3)，得

$$
\frac{\mathrm{d}W}{\mathrm{d}t}=\frac{\mathrm{d}E_{\mathrm{k}}}{\mathrm{d}t}+\frac{\mathrm{d}}{\mathrm{d}t}(V_{\mathrm{I}}-TS)
$$

引入**自由能密度** $v_{\mathrm{F}}=v_{\mathrm{I}}-T\eta$（$\eta$ 为单位体积的熵），重复绝热过程同样的处理，得到

$$
\sigma_x=\frac{\partial v_{\mathrm{F}}}{\partial\varepsilon_x},\quad \tau_{yz}=\frac{\partial v_{\mathrm{F}}}{\partial\gamma_{yz}},\ \cdots
$$

即式 (4-6)，等温情况下物理方程的能量形式。

### 3.3 统一写法：格林公式

式 (4-5) 与式 (4-6) 形式完全相同，可以统一写成

$$
\sigma_x=\frac{\partial v_{\varepsilon}}{\partial\varepsilon_x},\quad
\sigma_y=\frac{\partial v_{\varepsilon}}{\partial\varepsilon_y},\quad
\sigma_z=\frac{\partial v_{\varepsilon}}{\partial\varepsilon_z},\quad
\tau_{yz}=\frac{\partial v_{\varepsilon}}{\partial\gamma_{yz}},\quad
\tau_{xz}=\frac{\partial v_{\varepsilon}}{\partial\gamma_{xz}},\quad
\tau_{xy}=\frac{\partial v_{\varepsilon}}{\partial\gamma_{xy}}
$$

即式 (4-7)，缩写为

$$
\sigma_{ij}=\frac{\partial v_{\varepsilon}}{\partial\varepsilon_{ij}}
$$

即式 (4-7)$'$。这里 $v_{\varepsilon}$ 是**应变能密度**——由于变形而储存于物体内单位体积的弹性势能。它的具体所指随过程而异：

- 绝热情况：$v_{\varepsilon}=v_{\mathrm{I}}-v_{\mathrm{I}0}$，内能密度的增量；
- 等温情况：$v_{\varepsilon}=v_{\mathrm{F}}-v_{\mathrm{F}0}$，自由能密度的增量；

$v_{\mathrm{I}0}$、$v_{\mathrm{F}0}$ 是自然状态（无应力状态）下的值，自然状态下 $v_{\varepsilon}=0$。

式 (4-7) 称**格林公式**。原文给出了它的适用边界，这一段务必逐字记住：**它是通过热力学第一定律和第二定律导出的，因此不受变形大小和材料性能的限制，也不需无初始应力的假设**。这与式 (4-2) 形成鲜明对照——式 (4-2) 是"小变形 + 无初始应力 + 线性"的产物，而格林公式比它宽得多：非线性弹性、大变形都成立，只是要求过程可逆（弹性变形满足这一条）。

### 3.4 线性弹性下应变能密度的齐二次性

若应力与应变呈线性关系（式 4-2），由式 (4-7) 可见 $v_{\varepsilon}$ 必是应变分量的**齐二次函数**。由齐次函数的欧拉定理并利用式 (4-7)，

$$
2v_{\varepsilon}=\sigma_x\varepsilon_x+\sigma_y\varepsilon_y+\sigma_z\varepsilon_z+\tau_{yz}\gamma_{yz}+\tau_{xz}\gamma_{xz}+\tau_{xy}\gamma_{xy}
$$

即

$$
v_{\varepsilon}=\frac{1}{2}\left(\sigma_x\varepsilon_x+\sigma_y\varepsilon_y+\sigma_z\varepsilon_z+\tau_{yz}\gamma_{yz}+\tau_{xz}\gamma_{xz}+\tau_{xy}\gamma_{xy}\right)=\frac{1}{2}\sigma_{ij}\varepsilon_{ij}
$$

即式 (4-8) 与 (4-8)$'$。整个物体的应变能为

$$
V_{\varepsilon}=\iiint_V v_{\varepsilon}\,\mathrm{d}V
$$

即式 (4-9)。系数 $\tfrac12$ 的来历值得留意：线性关系下应力随应变从零线性增长，做功是"三角形面积"而非"矩形面积"。

**易错辨析**
- 格林公式 (4-7) 的普适性和式 (4-2) 的线性化前提**不是一回事**。常有人拿"格林公式不受变形大小限制"去为式 (4-2) 的普适性辩护，这是混淆了两条不同的结论。
- $v_{\varepsilon}$ 是**单位体积**的应变能（密度），$V_{\varepsilon}$ 才是整个物体的应变能，量纲差一个体积。
- 式 (4-8) 只在**线性**弹性下成立；非线性弹性材料的 $v_{\varepsilon}$ 不等于 $\tfrac12\sigma_{ij}\varepsilon_{ij}$。

## 四、能量渠道二：常数矩阵的对称性与 21 个常数

**这一节解决什么问题**：把"存在应变能"这一条翻译成对 $C_{mn}$ 的具体约束，把 36 个常数减到 21 个。

这一步的证明很短，但方法要看清：**把式 (4-7) 与式 (4-2) 联立，然后交叉求二阶偏导**。

以 $C_{25}$ 与 $C_{52}$ 为例。将式 (4-7) 的 $\sigma_y$ 与式 (4-2) 第二式联立：

$$
\frac{\partial v_{\varepsilon}}{\partial\varepsilon_y}=C_{21}\varepsilon_x+C_{22}\varepsilon_y+C_{23}\varepsilon_z+C_{24}\gamma_{yz}+C_{25}\gamma_{xz}+C_{26}\gamma_{xy}
$$

两边对 $\gamma_{xz}$ 求偏导，得 $\dfrac{\partial^2 v_{\varepsilon}}{\partial\varepsilon_y\partial\gamma_{xz}}=C_{25}$。

再将式 (4-7) 的 $\tau_{xz}$ 与式 (4-2) 第五式联立，两边对 $\varepsilon_y$ 求偏导，得 $\dfrac{\partial^2 v_{\varepsilon}}{\partial\gamma_{xz}\partial\varepsilon_y}=C_{52}$。

由于二阶偏导数可交换次序，故 $C_{25}=C_{52}$。对其余各组同样处理，得

$$
C_{mn}=C_{nm}
$$

于是独立常数个数为 $6+\dfrac{30}{2}=21$。**对极端各向异性体，只有 21 个独立弹性常数。**

这里的逻辑要点是：偏导可交换的数学依据，正是 $v_{\varepsilon}$ 作为状态函数的存在，也就是能量守恒。所以常说"21 个"是**能量给的**，而不是几何给的。下一节继续削减常数，用的才是几何。

## 五、几何渠道：材料对称性如何把 21 削到 2

**这一节解决什么问题**：真实材料的内部结构往往带有某种对称性。若把坐标作相应的镜像或旋转后，材料的弹性行为"看起来一样"，那么式 (4-2) 的形式必须保持不变，这就强制一批常数为零或相等。方法全章统一，只有三步：

1. 设定某个平面为弹性对称面，作相应的坐标变换；
2. 用式 (2-8)（应力变换）与式 (3-10)（应变变换）写出新系下的应力、应变分量；
3. 代回旧系的关系式，要求**形式不变**，从而得到常数的方程。

先明确两个名词：若物体内每一点都存在这样一个平面，和该面对称的两个方向弹性相同，则该平面称**弹性对称面**；垂直于弹性对称面的方向称**弹性主方向**。

### 5.1 一个弹性对称面：21 → 13

设 $Oyz$ 平面为弹性对称面，即 $x$ 轴为弹性主方向。作 $x'\to-x$、$y'\to y$、$z'\to z$ 的坐标变换（方向余弦 $l_1=-1$，$m_2=n_3=1$，其余为零）。变换结果是

$$
\sigma_{x'}=\sigma_x,\ \sigma_{y'}=\sigma_y,\ \sigma_{z'}=\sigma_z;\qquad
\tau_{y'z'}=\tau_{yz},\ \tau_{x'z'}=-\tau_{xz},\ \tau_{x'y'}=-\tau_{xy}
$$

$$
\varepsilon_{x'}=\varepsilon_x,\ \varepsilon_{y'}=\varepsilon_y,\ \varepsilon_{z'}=\varepsilon_z;\qquad
\gamma_{y'z'}=\gamma_{yz},\ \gamma_{x'z'}=-\gamma_{xz},\ \gamma_{x'y'}=-\gamma_{xy}
$$

即正分量与 $yz$ 面上的切分量不变，含 $x$ 的两个切分量变号。把这些代入式 (4-2) 并要求与式 (4-2) 形式相同，比较系数得

$$
C_{15}=C_{16}=C_{25}=C_{26}=C_{35}=C_{36}=C_{45}=C_{46}=0
$$

共 8 个为零，**常数从 21 减到 13**。简化后的形式（式 f）有一个显著特征：前四式只含 $\varepsilon_x,\varepsilon_y,\varepsilon_z,\gamma_{yz}$，后两式只含 $\gamma_{xz},\gamma_{xy}$——含 $x$ 的切变形与其余分量"脱钩"了。

### 5.2 再加一个对称面：正交各向异性，13 → 9

再设 $Oxz$ 平面也是弹性对称面，即 $y$ 轴为弹性主方向。作 $y'\to-y$ 的变换，此时 $\tau_{y'z'}=-\tau_{yz}$、$\tau_{x'y'}=-\tau_{xy}$，其余不变。代回式 (f) 比较，得

$$
C_{14}=C_{24}=C_{34}=C_{56}=0
$$

再减 4 个，得式 (4-10)：

$$
\begin{aligned}
\sigma_x&=C_{11}\varepsilon_x+C_{12}\varepsilon_y+C_{13}\varepsilon_z\\
\sigma_y&=C_{21}\varepsilon_x+C_{22}\varepsilon_y+C_{23}\varepsilon_z\\
\sigma_z&=C_{31}\varepsilon_x+C_{32}\varepsilon_y+C_{33}\varepsilon_z\\
\tau_{yz}&=C_{44}\gamma_{yz},\qquad \tau_{xz}=C_{55}\gamma_{xz},\qquad \tau_{xy}=C_{66}\gamma_{xy}
\end{aligned}
$$

原文还附带一个漂亮的结论：若互相垂直的 3 个平面中有 2 个是弹性对称面，则第三个平面必然也是弹性对称面——再设 $Oxy$ 为对称面不会得到新结果。至此常数剩 9 个，这类弹性体称**正交各向异性弹性体**。

式 (4-10) 的物理含义要读懂：**当坐标轴方向与弹性主方向一致时，正应力只与正应变有关，切应力只与对应的切应变有关**；拉压与剪切之间，以及不同平面内的切应力与切应变之间，都不存在耦合。各种增强纤维复合材料、木材属于此类。反过来说，一旦坐标轴偏离弹性主方向，这种"解耦"就消失了——这正是复合材料的本构必须指定材料主轴方向的原因。

### 5.3 横观各向同性：9 → 6 → 5

在正交各向异性基础上，若每一点都有一个弹性对称轴，即每一点都有一个各向同性平面（面内各方向弹性相同），则称**横观各向同性弹性体**。设 $Oxy$ 平面为各向同性平面，$z$ 轴为弹性对称轴。

**第一步**：让坐标系绕 $z$ 轴旋转 $90^\circ$。代回式 (4-10)，要求形式不变，得

$$
C_{11}=C_{22},\qquad C_{13}=C_{23},\qquad C_{44}=C_{55}
$$

常数降到 6 个。

**第二步**：再让坐标系绕 $z$ 轴旋转任意角 $\varphi$。这一步用的是 $xy$ 面内的应力、应变变换：

$$
\tau_{x'y'}=\frac{1}{2}(\sigma_y-\sigma_x)\sin2\varphi+\tau_{xy}\cos2\varphi,\qquad
\gamma_{x'y'}=(\varepsilon_y-\varepsilon_x)\sin2\varphi+\gamma_{xy}\cos2\varphi
$$

旋转后式 (4-10) 的第六式 $\tau_{x'y'}=C_{66}\gamma_{x'y'}$ 仍须成立。代入并用 $\tau_{xy}=C_{66}\gamma_{xy}$ 化简，得 $\sigma_y-\sigma_x=2C_{66}(\varepsilon_y-\varepsilon_x)$；而由式 (4-10) 前两式相减得 $\sigma_y-\sigma_x=(C_{11}-C_{12})(\varepsilon_y-\varepsilon_x)$。两式比较，得

$$
2C_{66}=C_{11}-C_{12}
$$

常数再减 1 个，**横观各向同性体有 5 个独立常数**，应力应变关系为

$$
\begin{aligned}
\sigma_x&=C_{11}\varepsilon_x+C_{12}\varepsilon_y+C_{13}\varepsilon_z\\
\sigma_y&=C_{12}\varepsilon_x+C_{11}\varepsilon_y+C_{13}\varepsilon_z\\
\sigma_z&=C_{13}\varepsilon_x+C_{13}\varepsilon_y+C_{33}\varepsilon_z\\
\tau_{yz}&=C_{44}\gamma_{yz},\qquad \tau_{xz}=C_{44}\gamma_{xz},\qquad \tau_{xy}=\tfrac12(C_{11}-C_{12})\gamma_{xy}
\end{aligned}
$$

即式 (4-11)。层状结构的地壳可认为是横观各向同性的。

请注意 $2C_{66}=C_{11}-C_{12}$ 这个关系式的**身份**：它恰恰是"面内各向同性"的数学标志——平面内正应力与切应力之间、以及面内两个方向之间的关系被绑定成各向同性体的形式。它在下一步会被原样继承。

### 5.4 各向同性：5 → 2

各向同性的物理含义是"沿物体各个方向看，弹性性质完全相同"，数学上就是**应力应变关系在所有方位的坐标系中都一样**。

式 (4-11) 描述的材料，$Oxy$ 既是各向同性面又是弹性对称面，但面内弹性与 $z$ 向弹性仍可不同。各向同性要求二者也相同。为此以式 (4-11) 为基础，再作一次交换 $y$ 与 $z$ 的坐标变换（$x'\to x$、$y'\to z$、$z'\to y$），此时

$$
\sigma_{x'}=\sigma_x,\ \sigma_{y'}=\sigma_z,\ \sigma_{z'}=\sigma_y;\qquad
\tau_{y'z'}=-\tau_{yz},\ \tau_{x'z'}=-\tau_{xy},\ \tau_{x'y'}=\tau_{xz}
$$

应变分量同样交换。代回式 (4-11) 并要求形式不变，比较得

$$
C_{12}=C_{13},\qquad C_{11}=C_{33},\qquad C_{44}=\tfrac12(C_{11}-C_{12})
$$

于是**各向同性弹性体只有 2 个独立弹性常数**。

把上述关系代入式 (4-11) 并整理，用 $\theta=\varepsilon_x+\varepsilon_y+\varepsilon_z$ 记体应变，令

$$
C_{12}=\lambda,\qquad C_{11}-C_{12}=2\mu
$$

得

$$
\begin{aligned}
\sigma_x&=\lambda\theta+2\mu\varepsilon_x, & \tau_{yz}&=\mu\gamma_{yz}\\
\sigma_y&=\lambda\theta+2\mu\varepsilon_y, & \tau_{xz}&=\mu\gamma_{xz}\\
\sigma_z&=\lambda\theta+2\mu\varepsilon_z, & \tau_{xy}&=\mu\gamma_{xy}
\end{aligned}
$$

即式 (4-12)，缩写为

$$
\sigma_{ij}=\lambda\varepsilon_{kk}\delta_{ij}+2\mu\varepsilon_{ij}
$$

即式 (4-12)$'$。这就是**各向同性弹性体的广义胡克定律**，$\lambda$、$\mu$ 称**拉梅常数**。

原文由此顺手得到一条重要性质：**在各向同性体内各点，应力主方向与应变主方向一致**。理由很直接——把坐标轴取到与某点的应变主方向重合，所有切应变分量为零；由式 (4-12) 后三式，切应力分量也必为零，故这三个方向同时是应力主方向。

### 5.5 削减链汇总

| 材料对称性 | 独立常数 | 关键依据或置零条件 |
|---|---|---|
| 极端各向异性 | 21 | $C_{mn}=C_{nm}$（应变能存在） |
| 一个弹性对称面 | 13 | 8 个含下标 5、6 的耦合项为零 |
| 正交各向异性 | 9 | 再加 4 个为零，解耦为三组 |
| 横观各向同性 | 5 | $C_{11}=C_{22}$、$C_{13}=C_{23}$、$C_{44}=C_{55}$、$2C_{66}=C_{11}-C_{12}$ |
| 各向同性 | 2 | $C_{12}=C_{13}$、$C_{11}=C_{33}$、$C_{44}=\frac12(C_{11}-C_{12})$ |

**易错辨析**
- "各向同性只有 2 个常数"不等于"$\lambda$ 与 $\mu$ 相等"，两个常数仍然彼此独立；被绑定的是 $C_{44}$ 与 $C_{11},C_{12}$ 这一类组合关系。
- 正交各向异性中的"正应力只与正应变耦合"，前提是**坐标轴与弹性主方向一致**；换到任意方位就不再成立。
- 横观各向同性的 5 个常数中不含 $C_{66}$——它是被 $C_{11},C_{12}$ 决定的，不是第 6 个独立量。
- 削减链的每一步都是"要求形式不变"这一条在起作用，而不是"对称性让材料变软"这类模糊说法。

## 六、两张面孔：拉梅常数与工程常数

**这一节解决什么问题**：$\lambda$、$\mu$ 是推导出来的抽象常数，实验室给不出它们。必须把式 (4-12)/(4-14) 与简单拉伸、纯剪这两类**可测**试验接通，并由此读出各常数的物理意义与取值限制。

### 6.1 体应变定律

把式 (4-12) 前三式相加：

$$
\Theta=\sigma_x+\sigma_y+\sigma_z=(3\lambda+2\mu)\theta
$$

即式 (4-13)，称**体应变定律**。它说明：各向同性线弹性体中，体积应力与体应变成正比，比例系数 $3\lambda+2\mu$ 只由两个拉梅常数决定（原文未引入体积模量记号，该系数即体积模量的 3 倍）。

利用式 (4-13)，把式 (4-12) 反解成应变用应力表示：

$$
\varepsilon_x=\frac{\sigma_x}{2\mu}-\frac{\lambda}{2\mu(3\lambda+2\mu)}\Theta,\qquad
\gamma_{yz}=\frac{1}{\mu}\tau_{yz}
$$

等六式，即式 (4-14)。

### 6.2 由简单拉伸定出 $E$ 与 $\nu$

式 (4-12)/(4-14) 必须包含简单拉伸的特例。取拉伸方向为 $x$ 轴，则 $\sigma_y=\sigma_z=\tau_{yz}=\tau_{xz}=\tau_{xy}=0$，代入式 (4-14) 得

$$
\varepsilon_x=\frac{\lambda+\mu}{\mu(3\lambda+2\mu)}\sigma_x,\qquad
\varepsilon_y=\varepsilon_z=-\frac{\lambda}{2\mu(3\lambda+2\mu)}\sigma_x,\qquad
\gamma_{yz}=\gamma_{xz}=\gamma_{xy}=0
$$

而简单拉伸试验给出 $\varepsilon_x=\sigma_x/E$、$\varepsilon_y=\varepsilon_z=-\nu\sigma_x/E$（$E$ 为杨氏模量，$\nu$ 为泊松比）。两者比较，得

$$
E=\frac{\mu(3\lambda+2\mu)}{\lambda+\mu},\qquad \nu=\frac{\lambda}{2(\lambda+\mu)}
$$

即式 (4-15)；反解为

$$
\lambda=\frac{E\nu}{(1+\nu)(1-2\nu)},\qquad \mu=\frac{E}{2(1+\nu)}
$$

即式 (4-16)。

### 6.3 由纯剪定出 $G$

取切应力作用于 $Oxy$ 平面，则除 $\tau_{xy}$ 外应力全为零，代入式 (4-14) 得 $\varepsilon_x=\varepsilon_y=\varepsilon_z=\gamma_{yz}=\gamma_{xz}=0$、$\gamma_{xy}=\tau_{xy}/\mu$。而纯剪试验给出 $\gamma_{xy}=\tau_{xy}/G$（$G$ 为切变模量）。比较即得

$$
\mu=G
$$

即式 (4-17)。可见**拉梅第二常数 $\mu$ 就是切变模量**。

### 6.4 用 $E$、$\nu$ 写出的胡克定律

把式 (4-16) 代入式 (4-14) 并整理：

$$
\varepsilon_x=\frac{1}{E}\left[\sigma_x-\nu(\sigma_y+\sigma_z)\right],\qquad
\gamma_{yz}=\frac{2(1+\nu)}{E}\tau_{yz}
$$

等六式，即式 (4-18)，缩写为

$$
\varepsilon_{ij}=\frac{1}{E}\left[(1+\nu)\sigma_{ij}-\nu\sigma_{kk}\delta_{ij}\right]
$$

即式 (4-18)$'$。由式 (4-18)，体应变定律又可写成

$$
\theta=\frac{1-2\nu}{E}\Theta
$$

即式 (4-19)。

### 6.5 常数数量与取值限制

原文明确了两点，都很关键：

- **独立常数只有 2 个**。$E$、$\nu$、$G$ 三者不独立：由式 (4-16) 的 $\mu=E/[2(1+\nu)]$ 与式 (4-17) 的 $\mu=G$，立得 $G=\dfrac{E}{2(1+\nu)}$。所以对线性各向同性材料，测两个常数就够了；测三个则构成一次校验。
- **取值范围**：根据试验，$E>0$、$0<\nu<\tfrac12$，所以 $\lambda>0$、$\mu>0$。由式 (4-16) 可见，$\nu<\tfrac12$ 正是让 $\lambda$ 的分母 $(1-2\nu)$ 保持为正的条件，从而 $\lambda>0$、$3\lambda+2\mu>0$，体应变定律的系数为正——这与第六节将给出的 $v_{\varepsilon}\geqslant0$ 相互呼应。$\nu$ 若趋近 $\tfrac12$，$(1-2\nu)\to0$，材料将表现为不可压缩状态，这一情形的具体处理原文未展开。

**常数换算式**

| 已知 | 求得 | 关系式 |
|---|---|---|
| $\lambda,\mu$ | $E,\nu$ | $E=\mu(3\lambda+2\mu)/(\lambda+\mu)$，$\nu=\lambda/[2(\lambda+\mu)]$ |
| $E,\nu$ | $\lambda,\mu$ | $\lambda=E\nu/[(1+\nu)(1-2\nu)]$，$\mu=E/[2(1+\nu)]$ |
| $\mu$ | $G$ | $G=\mu=E/[2(1+\nu)]$ |

**易错辨析**
- $\lambda$ 是拉梅第一常数，**不是**杨氏模量，也不是体积模量；在简单拉伸下 $\varepsilon_x=\sigma_x/E$ 里出现的才是 $E$。
- 把 $\mu$ 与 $G$ 当成两个独立常数去"分别测量"，是常见误解；它们数值相等。
- 式 (4-18) 的三个正应变式里，方括号内是 $\sigma_x-\nu(\sigma_y+\sigma_z)$，**不是** $\sigma_x-\nu\sigma_x$ 之类；泊松效应来自另外两个方向的应力。
- 式 (4-19) 中左边是体应变 $\theta$、右边是体积应力 $\Theta$，两者不能混写。

## 七、应变能密度的具体形式与正定性

**这一节解决什么问题**：式 (4-8) 只是应变能密度的一般表达式，还需要用应变或应力把它写成可计算的形式，并回答"它是否恒正"。

把式 (4-12) 或式 (4-18) 代入 $2v_{\varepsilon}=\sigma_x\varepsilon_x+\cdots+\tau_{xy}\gamma_{xy}$，得以应变表示的形式：

$$
2v_{\varepsilon}=\lambda\theta^2+2\mu\left(\varepsilon_x^2+\varepsilon_y^2+\varepsilon_z^2\right)+\mu\left(\gamma_{yz}^2+\gamma_{xz}^2+\gamma_{xy}^2\right)
$$

等号右端也可等价整理为

$$
2v_{\varepsilon}=(\lambda+2\mu)\left(\varepsilon_x^2+\varepsilon_y^2+\varepsilon_z^2\right)+2\lambda\left(\varepsilon_y\varepsilon_z+\varepsilon_x\varepsilon_z+\varepsilon_x\varepsilon_y\right)+\mu\left(\gamma_{yz}^2+\gamma_{xz}^2+\gamma_{xy}^2\right)
$$

即式 (4-20)。两者是同一个式子的两种整理方式，不是两个不同结论。

以应力表示的形式为

$$
2v_{\varepsilon}=\frac{1}{E}\left[\sigma_x^2+\sigma_y^2+\sigma_z^2-2\nu(\sigma_y\sigma_z+\sigma_x\sigma_z+\sigma_x\sigma_y)+2(1+\nu)\left(\tau_{yz}^2+\tau_{xz}^2+\tau_{xy}^2\right)\right]
$$

即式 (4-21)。

由式 (4-20) 可得一个重要结论：

$$
v_{\varepsilon}\geqslant 0
$$

即**应变能密度总是正的**（在自然状态下为零，其余状态大于零）。这实际上是"应变能是个正定二次型"的表述，与 $\mu>0$、$3\lambda+2\mu>0$ 是同一件事的两种说法。

原文习题 4-2 要求证明的对偶关系也值得记一笔：在满足广义胡克定律时，有

$$
\varepsilon_x=\frac{\partial v_{\varepsilon}}{\partial\sigma_x},\quad\cdots,\quad
\gamma_{xy}=\frac{\partial v_{\varepsilon}}{\partial\tau_{xy}}
$$

即应变可由 $v_{\varepsilon}$ 对相应应力分量求偏导得到。它与格林公式 $\sigma_{ij}=\partial v_{\varepsilon}/\partial\varepsilon_{ij}$ 互为对偶：一个是"应力是应变能的应变梯度"，一个是"应变是应变能的应力梯度"。**注意二者的前提不同**：格林公式只需可逆（弹性），对偶关系则要求应力和应变之间是线性关系，$v_{\varepsilon}$ 是齐二次函数。

## 八、本章结论的适用边界

**这一节解决什么问题**：本章结论密集，每一条都挂着自己的前提。混用前提是本课程最常见的错误来源，所以把它们集中列出。

| 结论 | 成立前提 |
|---|---|
| 式 (4-2) 广义胡克定律 | 小变形、无初始应力、材料均匀、一定温度 |
| $C_{mn}=C_{nm}$，21 个常数 | 式 (4-2) 的前提下，加应变能存在 |
| 各向异性各档常数数目 | 式 (4-2) 的前提，加相应的材料对称性 |
| 式 (4-12)/(4-18) 各向同性胡克定律 | 上述前提，加各向同性 |
| 体应变定律 (4-13)/(4-19) | 各向同性、线弹性 |
| 应力主方向与应变主方向一致 | 各向同性、线弹性（式 4-12 之后） |
| 式 (4-7) 格林公式 | 弹性（可逆）过程，**不要求小变形、不要求线性、不要求无初始应力** |
| 式 (4-8) $v_{\varepsilon}=\frac12\sigma_{ij}\varepsilon_{ij}$ | 应力应变线性关系 |
| $v_{\varepsilon}\geqslant0$ | 线弹性、各向同性（由式 4-20 得出） |

几点需要一并明确的边界：

- **本章没有讨论平面应力、平面应变这类二维简化下的本构形式**。这些简化要结合具体问题的应力或应变状态才能做，属于后续章节的内容，本章不涉及。
- **本章不讨论温度变化引起的应变**。原文只在总述中交代"在一定的温度下"，即把温度当作固定条件；热应力的本构修正不在本章范围。
- **各向异性体只给了 $C_{mn}$ 形式**，没有像各向同性那样换算成一套工程常数（如 $E_1,E_2,\nu_{12},G_{12}$）。工程上常用这种写法，但本章原文未给出。
- **曲线坐标下的形式未给出**：原文把极坐标、柱坐标、球坐标形式的各向同性广义胡克定律列为习题 4-4，正文没有展开。需要时可按张量分量与原坐标分量的对应关系改写式 (4-12)，但这一步不属于本章已建立的结论。
- 本章的"弹性"始终指**线弹性、小变形**（格林公式一节除外）。一旦进入塑性，$\mathrm{d}S_{\mathrm{i}}>0$，可逆性丧失，格林公式的前提即告失效——原文在讨论产熵时已明确点出这一分界。

把上述边界记住，本章的核心其实可以压成一句话：**本构关系是唯一携带材料信息的方程；它的线性形式来自小变形假设，它的常数个数来自材料对称性，它的常数之间的对称性来自能量，而它的具体数值只能由试验给出。**