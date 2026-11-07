## 一、本章的位置：只研究“变形本身”

在外力或温度变化作用下，物体内部各部分之间产生相对运动，这种运动形态称为变形。弹性力学要解一个完整问题，需要两套彼此独立的刻画：一套是**应力状态理论**，回答一点处各方向的内力集度如何随方向变化；另一套就是本章的**应变状态理论**，回答一点处的变形如何随方向变化，以及变形与位移之间必须满足什么关系。

本章的任务只有两个：

1. **分析一点的应变状态**——即一点处的变形能否用有限几个量描述，这些量在转轴时如何变化，是否存在使切应变为零的特殊方向。
2. **建立几何方程和应变协调方程**——前者把应变与位移的微分关系写出来，后者指出六个应变分量不能彼此独立、任意给定。

要特别注意本章的方法论特点：它**只从几何学观点研究变形本身，不涉及产生变形的原因（力、温度）和物体的物理性能**。这个特点带来两个直接后果，也决定了整章的基调：

- 本章所有结论对**一切连续介质**都成立，不限于线弹性材料，甚至不限于固体——只要是连续介质，几何方程和协调方程都成立；
- 正因为不涉及本构关系，本章**不能单独求解任何弹性力学问题**。它提供的是运动学一侧的全部约束，必须与应力理论、本构方程、边界条件联立才有意义。

因此读本章时，凡是遇到“必须满足”的论断，多半来自几何或连续性，而非来自材料；凡是本章给不出的量（例如应变与应力的联系），都应意识到那属于后面的本构内容。

## 二、出发点：把“连续”翻译成数学

这一节解决一个问题：既然要研究变形，第一个必须写下来的数学对象是什么？答案是**位移场**，而它不是随便什么函数，必须继承物体的连续性假设。

设物体原占区域 $D$，变形后占 $D_1$。连续性假设要求变形前连续的物体变形后仍连续，这在数学上就意味着：$D$ 内每一点连续地变到 $D_1$ 内的相应点，且两者一一对应。于是若 $P(x,y,z)$ 变到 $P_1(x_1,y_1,z_1)$，则 $x_1,y_1,z_1$ 必须是 $x,y,z$ 的**单值连续函数**。把坐标对应相减，定义位移分量

$$
u = x_1(x,y,z)-x,\quad v = y_1(x,y,z)-y,\quad w = z_1(x,y,z)-z
$$

显然 $u,v,w$ 也必须是 $x,y,z$ 的单值连续函数。为后面运算需要，原文进一步假定它们**具有连续到三阶的偏导数**。

这两条要求（单值连续、足够光滑）不是技术性修饰，而是全章的骨架：

- **光滑性**：几何方程要对位移求一阶偏导，协调方程要再求一次，而“由应变反求位移”要做线积分并要求混合偏导可交换，所以需要二阶乃至三阶连续偏导。
- **单值性**：这是“变形后仍是连续体”这一物理事实的数学表达。§3-6 的整节论证，本质上都是在追问：给定应变场，积分出来的位移是否单值？在什么条件下单值？

一个理解上的提醒：位移场里既包含物体位置的变化（刚体运动），也包含形状的变化。这两部分在本章不会被“扔掉”，而是会在下一节被**干净地分离**——这正是应变理论能够成立的关键一步。

## 三、一点邻域：变形如何被分解

这一节解决本章最核心的问题：**如何用有限个量描绘一点邻近的变形？** 思路是“化整为零”：把物体分割成无数个棱边平行于坐标轴的微分平行六面体；若每个微元的变形已知，整个物体的变形就已知。暂不考虑微元变形后的方位，则其变形只剩两件事——**棱边的伸长或缩短**，以及**棱边间夹角的变化**。前者用正应变（伸长率）度量，后者用切应变度量：

$$
\varepsilon_x = \frac{M'A'-MA}{MA},\qquad \gamma_{yz}=\frac{\pi}{2}-\angle C'M'B'
$$

其余四个分量按 $x,y,z$ 与 $A,B,C$ 的对应关系轮换给出。这样定义的 6 个量称为应变分量。要注意此时的定义是“几何定义”，还没有和位移挂钩。

### 3.1 为什么会冒出 9 个偏导数

要建立应变与位移的关系，先看清一件事：6 个应变分量实际上是由位移分量的 **9 个一阶偏导数**决定的，即相对位移张量

$$
\begin{pmatrix}
\dfrac{\partial u}{\partial x} & \dfrac{\partial u}{\partial y} & \dfrac{\partial u}{\partial z}\\[2mm]
\dfrac{\partial v}{\partial x} & \dfrac{\partial v}{\partial y} & \dfrac{\partial v}{\partial z}\\[2mm]
\dfrac{\partial w}{\partial x} & \dfrac{\partial w}{\partial y} & \dfrac{\partial w}{\partial z}
\end{pmatrix}
$$

原文在此处给出一个很强的结论：对于**单连通物体**，若相对位移张量已知，且位移分量具有二阶或二阶以上连续偏导，则可积分求得连续单值的位移分量；这表明**相对位移张量完全确定了物体的变形情况**。

这是全章第一个“适用前提”很重的结论：它要求单连通，也要求足够光滑。多连通情形下积分可能出多值，后面 §3-6 会看到同样的困难以另一种形式出现。

### 3.2 9 = 6 + 3：对称与反对称的分裂

9 个量与 6 个应变量之间差着 3 个自由度。这 3 个自由度是什么？引入转动矢量

$$
\boldsymbol{\omega} = \nabla\times \boldsymbol{U},\qquad
\omega_x = \frac{\partial w}{\partial y}-\frac{\partial v}{\partial z},\quad
\omega_y = \frac{\partial u}{\partial z}-\frac{\partial w}{\partial x},\quad
\omega_z = \frac{\partial v}{\partial x}-\frac{\partial u}{\partial y}
$$

称为转动分量。利用几何方程与上式，相对位移张量可以分解为两个张量之和：一个是**对称张量**，其分量正是 $\varepsilon_x,\varepsilon_y,\varepsilon_z,\tfrac12\gamma_{xy},\tfrac12\gamma_{xz},\tfrac12\gamma_{yz}$，表示微元体的纯变形，称为**应变张量**；另一个是**反对称张量**，元素只由 $\omega_x,\omega_y,\omega_z$ 组成，表示微元体的刚性转动，即变形后微元体方位的变化。

### 3.3 位移的三段式分解

把上述分解用到一条微分线段 $AB$ 上（$A$ 为基点，$B$ 的坐标增量为 $\mathrm{d}x,\mathrm{d}y,\mathrm{d}z$），对 $B$ 点位移作泰勒展开并略去二阶以上项，再按应变、转动重组，就得到

$$
u' = u + \Big(\varepsilon_x\mathrm{d}x+\tfrac12\gamma_{xy}\mathrm{d}y+\tfrac12\gamma_{xz}\mathrm{d}z\Big)
+\Big(-\tfrac12\omega_z\mathrm{d}y+\tfrac12\omega_y\mathrm{d}z\Big)
$$

$v',w'$ 按轮换写出。由此可以逐项读出物理意义。设想 $A$ 的无限小邻域是绝对刚性的（令应变分量为零），则由刚体运动学，与 $A$ 邻近的 $B$ 点位移只由两部分组成：随基点 $A$ 的平移，以及微元绕 $A$ 转动在 $B$ 点产生的位移。对照上式，$u,v,w$ 是平移部分，含 $\omega$ 的项是转动部分。于是结论成形：

与 $A$ 无限邻近的 $B$ 点，其位移由三部分组成——

1. 随同 $A$ 点的**平移位移**；
2. 绕 $A$ 点**刚性转动**在 $B$ 点产生的位移；
3. 由 $A$ 点邻近微元体的**变形**在 $B$ 点引起的位移。

第三部分正是含应变分量的项。这一步的意义在于：它把“刚体位移”和“相对变形”从一个混在一起的位移场里彻底分开了，而分解的依据仅仅是偏导数的对称化与反对称化，不需要任何材料假设。

### 3.4 关于转动分量的一条重要提醒

原文特意强调：$\omega_x,\omega_y,\omega_z$ 是**坐标的函数**，表示体内各处微元体的刚性转动；但对整个物体而言，它们**属于变形的一部分**。这 3 个分量与 6 个应变分量合在一起，才全面反映物体的变形。

这句话划清了一条容易越过的界线：

| 对象 | 是否属于变形 | 说明 |
|---|---|---|
| $\tfrac12\omega_i$（角位移矢量分量） | 是 | 各点可不同，反映微元方位变化 |
| 各点共同的刚体平移 | 否 | 常矢量，不改变形状 |
| 整体刚体转动 | 否 | 仅在 $\omega_i$ 为常矢量时出现 |

也就是说，“刚体转动”四个字描述的是微元的**局部**运动学性质，不能据此把 $\omega$ 从变形描述中剔除；只有当 $\omega$ 在整个物体上是常矢量时，它才退化为整体刚体转动。

## 四、几何方程：应变与位移的微分关系

这一节解决上一节遗留的问题：§3.1 只说到“9 个偏导决定变形”，还没写出 6 个应变分量各自等于哪些偏导的组合。几何方程就是这组关系。

### 4.1 推导中做了什么，为什么能做

推导的关键简化有两次，都必须交代清楚，因为它们也构成了本章结论的适用前提。

**第一次简化（几何上的）**：变形前与坐标轴平行的微分线段 $MA,MB,MC$，变形后一般各自旋转了一个角度。但所考虑的是**小变形**，并且假设位移中已扣除纯属物体位置变化的那部分，于是这些线段的转角极其微小。因此可以用 $M'A',M'B',M'C'$ 在各坐标轴上的**投影长度**代替它们的实际长度，用各投影间夹角代替实际夹角，而不会带来明显误差。

**第二次简化（代数上的）**：在计算转角正切时出现形如 $\dfrac{\partial v/\partial x}{1+\partial u/\partial x}$ 的式子，因小变形下 $\partial u/\partial x$ 与 1 相比是一小量，略去不计。

把微元投影到 $Oxy$ 平面即可完成计算。设 $M(x,y,z)$，棱边长 $\mathrm{d}x,\mathrm{d}y,\mathrm{d}z$，由泰勒展开（略去二阶以上无穷小），$A$ 点位移为 $u+\frac{\partial u}{\partial x}\mathrm{d}x$、$v+\frac{\partial v}{\partial x}\mathrm{d}x$，于是投影长度变为 $\mathrm{d}x+\frac{\partial u}{\partial x}\mathrm{d}x\approx M'A'$，从而

$$
\varepsilon_x = \frac{M'A'-MA}{MA}\approx\frac{\mathrm{d}x+\frac{\partial u}{\partial x}\mathrm{d}x-\mathrm{d}x}{\mathrm{d}x}=\frac{\partial u}{\partial x}
$$

同理 $\varepsilon_y=\partial v/\partial y$，$\varepsilon_z=\partial w/\partial z$。$\varepsilon_x>0$ 表示线段伸长，反之缩短。

切应变则由两段转角相加得到。记 $\alpha_{yx}$ 为与 $Ox$ 轴平行的线段向 $Oy$ 轴转过的角度，$\alpha_{xy}$ 反之，则

$$
\gamma_{xy}=\frac{\pi}{2}-\angle B'M'A'\approx\alpha_{xy}+\alpha_{yx}
=\frac{\partial u}{\partial y}+\frac{\partial v}{\partial x}
$$

$\alpha_{yx}>0$ 表示 $v$ 随 $x$ 增加，即该线段从 $Ox$ 正向朝 $Oy$ 正向旋转；$\alpha_{xy}$ 同理。故 $\gamma_{xy},\gamma_{xz},\gamma_{yz}$ **大于零表示角度缩小，小于零表示角度扩大**——这一点与正应变的符号习惯不同，做题时最容易弄反。

### 4.2 结果与两种写法

轮换 $x,y,z$ 与 $u,v,w$，得几何方程（柯西方程）：

$$
\varepsilon_x=\frac{\partial u}{\partial x},\quad
\varepsilon_y=\frac{\partial v}{\partial y},\quad
\varepsilon_z=\frac{\partial w}{\partial z}
$$

$$
\gamma_{yz}=\frac{\partial w}{\partial y}+\frac{\partial v}{\partial z},\quad
\gamma_{xz}=\frac{\partial u}{\partial z}+\frac{\partial w}{\partial x},\quad
\gamma_{xy}=\frac{\partial v}{\partial x}+\frac{\partial u}{\partial y}
$$

若把后三式两边同除以 2，并记

$$
\varepsilon_{yz}=\tfrac12\gamma_{yz},\qquad \varepsilon_{xz}=\tfrac12\gamma_{xz},\qquad \varepsilon_{xy}=\tfrac12\gamma_{xy}
$$

则六式可统一为一个张量等式：

$$
\varepsilon_{ij}=\frac{1}{2}\left(u_{i,j}+u_{j,i}\right)
$$

### 4.3 正反两个方向的难度极不对称

几何方程给出的关系是“位移 → 应变”易、“应变 → 位移”难：

- 已知 $u,v,w$，只需按上式求偏导，直接得到 6 个应变分量，且结果唯一。
- 已知 6 个应变分量反求位移，则需要解一个**含 6 个方程、只有 3 个未知函数的偏微分方程组**。方程数超过未知函数数，方程组可能矛盾；即使不矛盾，解也只在相差一个刚体位移的意义下确定。

这个不对称正是下一节“应变分量不能任意给定”的来源，也是 §3-6 协调方程要处理的全部内容。原文把反向问题专门放到 §3-6 研究，结构上是有意的。

## 五、应变是张量：转轴变换与任意方向伸长率

这一节解决“一点的应变状态”这个提法的确切含义。既然对同一个点，坐在不同坐标系里会读出 6 个不同的数，就必须回答：这些数随坐标系怎样变？变完之后什么东西没变？

先建立位移矢量的变换。设新老坐标轴夹角的方向余弦由矩阵 $(l_i,m_i,n_i)$（$i=1,2,3$）给出，则位移分量按矢量规律变换：

$$
u'=ul_1+vm_1+wn_1,\quad
v'=ul_2+vm_2+wn_2,\quad
w'=ul_3+vm_3+wn_3
$$

再用方向导数公式 $\dfrac{\partial}{\partial x'}=\left(l_1\dfrac{\partial}{\partial x}+m_1\dfrac{\partial}{\partial y}+n_1\dfrac{\partial}{\partial z}\right)$，把 $\varepsilon_{x'}=\partial u'/\partial x'$ 展开，并代入几何方程，就得到新坐标系下的应变分量。以正应变为例：

$$
\varepsilon_{x'}=\varepsilon_x l_1^2+\varepsilon_y m_1^2+\varepsilon_z n_1^2
+\gamma_{yz}m_1n_1+\gamma_{xz}l_1n_1+\gamma_{xy}l_1m_1
$$

切应变分量（如 $\gamma_{x'y'}$）结构相同，只是每项改为两组方向余弦之积，且交叉项系数为 2：

$$
\gamma_{x'y'}=2\left(\varepsilon_x l_1l_2+\varepsilon_y m_1m_2+\varepsilon_z n_1n_2\right)
+\gamma_{yz}\left(m_1n_2+m_2n_1\right)+\gamma_{xz}\left(l_1n_2+l_2n_1\right)+\gamma_{xy}\left(l_1m_2+l_2m_1\right)
$$

若仍以 $n_{i'i}$ 统记 9 个方向余弦，并注意到 $\varepsilon_{ij}=\tfrac12\gamma_{ij}$，则上述一堆式子压缩成一句：

$$
\varepsilon_{i'j'}=\varepsilon_{ij}\,n_{i'i}\,n_{j'j}
$$

这就说明：6 个应变分量组成的集合服从与应力分量完全相同的二阶张量变换规律，因此它是一个**二阶张量**，称为应变张量。由此可以给出“应变状态”的严格含义：转轴后各个分量都变了，但它们作为一个整体所描绘的一点变形状态不变。

同一套工具还能回答一个更直接的问题：过一点沿任意方向 $(l,m,n)$ 的微分线段，其伸长率是多少？答案是

$$
\varepsilon_r=\varepsilon_x l^2+\varepsilon_y m^2+\varepsilon_z n^2+\gamma_{yz}mn+\gamma_{xz}ln+\gamma_{xy}lm
$$

这条式子的地位值得强调：它是“一点应变状态”这一概念的操作性定义——只要知道该点 6 个应变分量，就能算出**任意方向**的伸长率，无需再作任何实验或假设。反之，工程上由几个方向实测伸长率反推 6 个分量，依据的也正是这一类关系式（原文习题 3-5 正是此意）。

## 六、主应变与应变张量不变量

这一节解决上一节自然引出的问题：既然分量随坐标系改变，能否找到一个坐标系，使**切应变全为零**，只剩下三个正应变？等价地说：过一点是否存在 3 个互相垂直的方向，沿它们的微分线段变形后只改变长度、夹角仍保持直角？

### 6.1 一个直观例子先说清“存在”这件事

考察均匀直杆的简单拉伸，比较杆内两个小单元体：$A$ 的方位完全任意，$B$ 有一对表面垂直于杆轴。变形后，$A$ 不仅棱边长度改变，棱边夹角也改变；而 $B$ 只是棱边长度改变，而各棱边之间仍保持垂直。

对复杂受力物体内的任一点，同样可以找到 3 个互相垂直的方向，使沿这 3 个方向的微分线段在变形后仍保持垂直。具有这种性质的方向称为**应变主方向**，沿该方向微分线段的伸长率称为**主应变**。在上面的例子中，小单元体 $B$ 的三条垂直棱边方向就是应变主方向，它们的伸长率就是主应变。

这里有一条不能省的细节：过一点、沿三个主方向的微分线段，变形后虽仍互相垂直，但由于微元体的刚性转动，它们一般**已经整体转过同一个角度**，因而与原方向不再平行（小单元体 $B$ 属特殊情况）。所以“主方向”指的是**变形前**的方向；讨论主方向时，必须先把这部分刚性转动从方向变化中剥离出去。这正是下面推导的关键一步。

### 6.2 推导要点：为什么要令转动分量为零

设方向 $(l,m,n)$ 为某点 $A$ 的应变主方向，过 $A$ 沿该方向作长度为 $r$ 的微分线段 $AB$，则 $B$ 的坐标为 $(x+rl,\,y+rm,\,z+rn)$。变形后线段变为 $A'B'$，长度为 $r'$，方向为 $(l',m',n')$。写出 $A'$、$B'$ 的坐标，对 $B'$ 的位移作泰勒展开并略去二阶以上微量，即得矢量 $\widehat{A'B'}$ 的三个分量；两边同除以 $r'$，左边成为单位矢量，右边方括号内的三个分量就是方向余弦 $l',m',n'$。

再由主应变定义 $\varepsilon=(r'-r)/r$，得 $r'=(1+\varepsilon)r$，代入并把 $(1+\varepsilon)^{-1}$ 展开为 $1-\varepsilon+\varepsilon^2-\cdots$。在小变形下 $\partial u/\partial x$ 等与 $\varepsilon$ 均为小量，略去二次以上项，得到 $l',m',n'$ 与 $l,m,n$ 的线性关系；再按 §3-2 中从泰勒展开式化到位移分解式的同样手法重组，即可把它写成“转动部分＋应变部分”的形式。

至此做关键一步：$(l',m',n')$ 与 $(l,m,n)$ 一般不一致，但前面已说明，偏离**只由微元体的刚性转动引起**。于是令 $\omega_x=\omega_y=\omega_z=0$，两者方向一致，即 $l'=l,\;m'=m,\;n'=n$。移项整理后得到应变主方向满足的方程：

$$
\begin{aligned}
(\varepsilon_x-\varepsilon)l+\tfrac12\gamma_{xy}m+\tfrac12\gamma_{xz}n &= 0\\
\tfrac12\gamma_{xy}l+(\varepsilon_y-\varepsilon)m+\tfrac12\gamma_{yz}n &= 0\\
\tfrac12\gamma_{xz}l+\tfrac12\gamma_{yz}m+(\varepsilon_z-\varepsilon)n &= 0
\end{aligned}
$$

值得强调的是：**这组方程里只有应变分量，没有转动分量**。这从数学上确认了“主方向、主应变是纯变形概念”，与微元整体的刚性方位变化无关。

### 6.3 特征方程与不变量

上式是关于 $l,m,n$ 的齐次线性方程组。要有非零解，系数行列式必须为零。展开后得到关于 $\varepsilon$ 的三次方程：

$$
\varepsilon^3-J_1\varepsilon^2+J_2\varepsilon-J_3=0
$$

其中

$$
J_1=\varepsilon_x+\varepsilon_y+\varepsilon_z
$$

$$
J_2=\varepsilon_y\varepsilon_z+\varepsilon_z\varepsilon_x+\varepsilon_x\varepsilon_y
-\tfrac14\left(\gamma_{yz}^2+\gamma_{xz}^2+\gamma_{xy}^2\right)
$$

$J_3$ 为以应变张量六个分量为元素的三阶行列式。$J_1,J_2,J_3$ 依次称为应变张量的第一、第二、第三不变量。其“不变”的含义与应力张量相同（转轴后取值不变），原文直接类比，不再赘述。

方程有三个实根，分别记作 $\varepsilon_1,\varepsilon_2,\varepsilon_3$，即三个主应变；把每个根代回主方向方程，配合 $l^2+m^2+n^2=1$，即可定出相应的主方向。

### 6.4 三种重根情况

与主应力完全平行地，有三种情形：

| 情形 | 主方向的确定程度 |
|---|---|
| $\varepsilon_1\neq\varepsilon_2\neq\varepsilon_3$ | 三个主方向必相互垂直，且各自唯一 |
| $\varepsilon_1=\varepsilon_2\neq\varepsilon_3$ | 与 $\varepsilon_3$ 对应的方向必垂直于另两个；垂直于该方向的**任何**方向都是主方向 |
| $\varepsilon_1=\varepsilon_2=\varepsilon_3$ | 任何方向均为主方向，三个主方向可垂直也可不垂直 |

三种情形共同的结论是：**过物体内任何一点，至少可以找到三个互相垂直的应变主方向**。这条存在性结论只依赖应变张量的对称性，与材料无关，因此对一切连续介质成立。

## 七、体应变

这一节只解决一个具体问题：变形后微元体的**单位体积改变**是多少？

取棱边长为 $\mathrm{d}x,\mathrm{d}y,\mathrm{d}z$ 的微分平行六面体，原体积 $V=\mathrm{d}x\,\mathrm{d}y\,\mathrm{d}z$。变形后棱边伸长或缩短，棱边夹角也改变。但由于**切应变引起的体积改变是高阶微量，可以略去不计**，故只需计入三条棱边的伸缩：

$$
V^*=\mathrm{d}x(1+\varepsilon_x)\,\mathrm{d}y(1+\varepsilon_y)\,\mathrm{d}z(1+\varepsilon_z)
\approx V\left(1+\varepsilon_x+\varepsilon_y+\varepsilon_z\right)
$$

于是体应变

$$
\theta=\frac{V^*-V}{V}=\varepsilon_x+\varepsilon_y+\varepsilon_z
=\frac{\partial u}{\partial x}+\frac{\partial v}{\partial y}+\frac{\partial w}{\partial z}
$$

这里有三个要点，都不宜略过：

1. **$\theta$ 在数值上等于第一不变量 $J_1$**。这给了不变量最直观的物理解释：体应变与坐标系选取无关，是纯粹的变形度量。
2. **结论依赖小变形近似**，用了两次：略去切应变引起的体积改变（高阶量），以及略去应变乘积项 $\varepsilon_x\varepsilon_y$ 等。因此上式不是精确的体积比公式。
3. 符号含义：$\theta>0$ 表示微元体膨胀，$\theta<0$ 表示缩小；若物体内 $\theta$ 处处为零，则变形后体积不变，称为**等容变形**。

需要留意边界：$\theta$ 只度量体积变化，完全不反映形状畸变——一个纯剪切的微元 $\theta=0$，却明显改变了形状。本章不进一步区分体积改变与形状改变（原文未展开），但把这层区分记在心里，后面引入本构关系时会用到。

## 八、应变协调方程

这一节回答全章最有深度的问题：**6 个应变分量能不能任意给定？**

由几何方程可见，6 个应变分量都由 3 个位移分量表示，因此它们之间必然存在内在联系。这个事实的重要性在于正反两个方向的不对称：

- 已知位移求应变，只是求导，容易且唯一；
- 若纯粹从数学角度任意给出一组“应变分量”，柯西方程就是**含 6 个方程、只有 3 个未知函数**的偏微分方程组。方程个数超过未知函数个数，方程组可能是矛盾的。

要使方程组不矛盾，6 个应变分量必须满足一定条件。这就是协调方程的来历：它不是新假设，而是**消去位移后的必然产物**。

### 8.1 消去位移的两条路径

**路径一（同类正应变交叉求导）**：把 $\varepsilon_x=\partial u/\partial x$ 对 $y$ 求二阶导、$\varepsilon_y=\partial v/\partial y$ 对 $x$ 求二阶导，相加，右边恰是 $\dfrac{\partial^2}{\partial x\partial y}\left(\dfrac{\partial u}{\partial y}+\dfrac{\partial v}{\partial x}\right)$，即得

$$
\frac{\partial^2\varepsilon_x}{\partial y^2}+\frac{\partial^2\varepsilon_y}{\partial x^2}
=\frac{\partial^2\gamma_{xy}}{\partial x\partial y}
$$

**路径二（由切应变反凑混合导数）**：把三个切应变表达式分别对 $x$、$y$、$z$ 求一阶导，后两式相加再减去前一式，得

$$
2\frac{\partial^2 u}{\partial y\partial z}
=-\frac{\partial\gamma_{yz}}{\partial x}+\frac{\partial\gamma_{xz}}{\partial y}+\frac{\partial\gamma_{xy}}{\partial z}
$$

两边再对 $x$ 求一阶导，并利用 $\varepsilon_x=\partial u/\partial x$，得

$$
2\frac{\partial^2\varepsilon_x}{\partial y\partial z}
=\frac{\partial}{\partial x}\left(-\frac{\partial\gamma_{yz}}{\partial x}
+\frac{\partial\gamma_{xz}}{\partial y}+\frac{\partial\gamma_{xy}}{\partial z}\right)
$$

轮换 $x,y,z$，由这两条路径共得 6 个关系式，即应变协调方程（**圣维南方程**）：

$$
\frac{\partial^2\varepsilon_x}{\partial y^2}+\frac{\partial^2\varepsilon_y}{\partial x^2}
=\frac{\partial^2\gamma_{xy}}{\partial x\partial y},\qquad
\frac{\partial^2\varepsilon_y}{\partial z^2}+\frac{\partial^2\varepsilon_z}{\partial y^2}
=\frac{\partial^2\gamma_{yz}}{\partial y\partial z}
$$

$$
\frac{\partial^2\varepsilon_z}{\partial x^2}+\frac{\partial^2\varepsilon_x}{\partial z^2}
=\frac{\partial^2\gamma_{xz}}{\partial z\partial x}
$$

$$
2\frac{\partial^2\varepsilon_x}{\partial y\partial z}
=\frac{\partial}{\partial x}\!\left(-\frac{\partial\gamma_{yz}}{\partial x}
+\frac{\partial\gamma_{xz}}{\partial y}+\frac{\partial\gamma_{xy}}{\partial z}\right)
$$

$$
2\frac{\partial^2\varepsilon_y}{\partial z\partial x}
=\frac{\partial}{\partial y}\!\left(-\frac{\partial\gamma_{xz}}{\partial y}
+\frac{\partial\gamma_{xy}}{\partial z}+\frac{\partial\gamma_{yz}}{\partial x}\right)
$$

$$
2\frac{\partial^2\varepsilon_z}{\partial x\partial y}
=\frac{\partial}{\partial z}\!\left(-\frac{\partial\gamma_{xy}}{\partial z}
+\frac{\partial\gamma_{yz}}{\partial x}+\frac{\partial\gamma_{xz}}{\partial y}\right)
$$

### 8.2 几何意义与必要性

协调方程有很直观的几何解释。想象把物体分割成无数个小平行六面体，让每个小单元体按给定的应变分量各自变形。如果这些应变分量不满足一定关系，变形后这些小单元体**就无法重新拼合成连续体**，中间会出现很小的裂缝。要能拼回去，应变分量就必须满足协调方程。

因此，**应变分量满足应变协调方程是保证物体连续的必要条件**——任何真实的变形场都自动满足它，这一点不依赖任何材料假设。

### 8.3 充分性：为什么单连通物体上反过来也成立

充分性要证的是：若应变分量满足协调方程，对单连通物体一定能通过几何方程的积分求得**单值连续**的位移分量。

证明思路是逐层剥开：

1. 求位移可归结为求它们的各个一阶偏导。其中 $\partial u/\partial x=\varepsilon_x$ 直接给出；其余如 $\partial u/\partial y$、$\partial u/\partial z$ 等不能直接由几何方程读出，但**作为函数，它们对 $x,y,z$ 的一阶偏导都可用应变分量表示**。例如 $\partial u/\partial y$ 的三个一阶偏导经化简后分别等于 $\partial\varepsilon_x/\partial y$、$\partial\gamma_{xy}/\partial y-\partial\varepsilon_x/\partial x$ 以及形如 $\tfrac12\left(-\partial\gamma_{yz}/\partial x+\partial\gamma_{xz}/\partial y+\partial\gamma_{xy}/\partial z\right)$ 的组合，右边视为已知量，记作 $A,B,C$。
2. 于是问题变成：线积分 $\int A\,\mathrm{d}x+B\,\mathrm{d}y+C\,\mathrm{d}z$ 能否给出单值连续的 $\partial u/\partial y$？其**充分必要条件**是 $\dfrac{\partial B}{\partial z}=\dfrac{\partial C}{\partial y}$、$\dfrac{\partial A}{\partial z}=\dfrac{\partial C}{\partial x}$、$\dfrac{\partial A}{\partial y}=\dfrac{\partial B}{\partial x}$。
3. 把 $A,B,C$ 代入，恰好得到协调方程中的相应三式。对 $\partial u/\partial z,\partial v/\partial x,\partial v/\partial z,\partial w/\partial x,\partial w/\partial y$ 同样处理，每个量得 3 个条件，共 18 个；但其中**只有 6 个是不同的**，正是协调方程的六式。
4. 这些一阶偏导既然都单值连续，再积分一次即得位移分量。

所以对**单连通**物体，协调方程既是必要条件又是充分条件。顺带地，上述论证也以更严密的方式再次证明了必要性。

### 8.4 多连通物体：为什么只到“必要”为止

对多连通物体（例如带孔的物体），总可以作适当截面使其变成单连通区域，上述结论在割开后完全适用：应变满足协调方程，就一定能在**割开后的区域**里求得单值连续的 $u,v,w$。

问题出在跨截面处：当点 $(x,y,z)$ 分别从截面两侧趋于截面上同一点时，一般会得到不同的值，记作 $u^+,v^+,w^+$ 与 $u^-,v^-,w^-$。物体变形后要仍是连续体，这个跳开必须在物理上不允许，于是必须补充条件

$$
u^+=u^-,\qquad v^+=v^-,\qquad w^+=w^-
$$

因此，对多连通物体，**协调方程只是物体连续的必要条件，加上上述补充条件后才充分**。这两类物体的区别，是本章唯一一处“单连通”前提真正改变结论强弱的地方，务必分清。

### 8.5 指标写法

六式还可紧凑地写成一个张量等式：

$$
\varepsilon_{ij,kl}\,\varepsilon_{ikm}\,\varepsilon_{jln}=0
$$

其中 $\varepsilon_{ikm}$、$\varepsilon_{jln}$ 是笛卡儿坐标系中的置换符号：指标按 $1,2,3;\,2,3,1;\,3,1,2$ 顺序排列时取 $+1$，按逆序排列时取 $-1$，有两个或三个指标重复时取 $0$。$m,n$ 有 $11,22,33,12,23,31$ 六种选择，展开即得上面六式。

## 九、易混辨析

**（1）工程切应变与张量切应变差一个因子 2。**
定义 $\varepsilon_{xy}=\tfrac12\gamma_{xy}$，其余同理。这不是书写习惯问题：只有取 $\tfrac12$，$\varepsilon_{ij}=\tfrac12(u_{i,j}+u_{j,i})$ 与 $\varepsilon_{i'j'}=\varepsilon_{ij}n_{i'i}n_{j'j}$ 才成立。用工程切应变写变换式时交叉项系数为 1，用张量分量写时自动吸收因子 2；**两套写法混用必然丢因子 2**。

**（2）正应变与切应变的符号习惯相反。**
$\varepsilon_x>0$ 表示线段**伸长**；$\gamma_{xy}>0$ 表示夹角**缩小**（因为 $\gamma_{xy}=\pi/2-\angle B'M'A'$）。

**（3）“小变形”指位移梯度小，不是位移小。**
线性化的实质是略去 $\partial u/\partial x$ 与 1 相比的量、略去转角的二次项。一根细长杆可以有相当大的位移而应变很小，只要转角与梯度足够小，几何方程仍成立。

**（4）转动分量 $\omega_i$ 属变形描述的一部分。**
$\tfrac12\omega_i$ 是微元体角位移矢量的分量，$\omega_i$ 本身则是它的两倍。$\omega_i$ 是坐标的函数，反映各点微元方位的差异，不能当作刚体位移剔除；只有当它是常矢量时才对应整体刚体转动。求主方向时把它“抹掉”，只是因为它造成了方向偏离，与主方向的定义无关。

**（5）主方向指变形前的方向。**
主方向线段变形后仍互相垂直，但通常不与原方向平行。若误把变形后的方向当主方向，会以为切应变不为零，结论全错。

**（6）协调方程是“必要”还是“充分”，取决于单连通性。**
单连通：充要；多连通：仅必要，须补充位移跨截面连续的条件。此外，协调方程保证的是位移单值，**不是位移唯一**——解中仍含积分常数，即整体刚体位移，须由边界条件定出（原文习题中“任意常数不需定出”即此意）。

**（7）本章不涉及本构，不能由应变推应力。**
应变主方向与应力主方向是两个独立的概念，本章既未给出、也无从给出二者是否重合的结论——那取决于材料性质，属后续本构关系的范畴。

## 十、本章结论的适用边界

把全章的“前提”集中列一遍，比记住任何单个公式都重要：

| 前提 | 影响哪些结论 |
|---|---|
| 连续介质假设 | 几何方程、协调方程对一切连续介质成立 |
| 位移单值连续、连续到三阶偏导 | 协调方程的推导；由应变积分求位移 |
| 小变形 | 几何方程线性化、投影代替实长、转角正切线性化 |
| 小变形（再次） | 体应变略去切应变高阶项与应变乘积项 |
| 单连通 | 协调方程才是连续的充分条件；相对位移张量可积出单值位移 |
| 多连通 | 需补充 $u^+=u^-$、$v^+=v^-$、$w^+=w^-$ |
| 纯几何、不涉本构 | 不能单独求应力或位移，须与其他方程联立 |

归纳起来，本章提供的是一条从运动学出发的完整链条：**位移场 → 相对位移张量 → （对称化）应变张量＋（反对称化）转动 → 几何方程 → 转轴变换与任意方向伸长率 → 主应变与不变量 → 体应变 → 协调方程**。链条上每一环都只用了几何与连续性，没有一处用到材料性质，因此它的适用范围远超线弹性理论；但也正因为如此，链条止于“可能的变形场”，至于哪种变形场实际发生，必须交给应力理论、本构方程和边界条件共同回答。

最后交代一条本章未覆盖的边界：以上全部结论都建立在小变形前提上。当转动与位移梯度不再是小量时，应变与位移的关系需要保留非线性项（有限变形理论），本章的线性几何方程与协调方程不再适用——这一情形原文未展开，此处仅作提示。