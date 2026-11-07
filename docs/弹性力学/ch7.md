## 一、换坐标的理由：形状与受载的对称性

原文开篇给出一个方法论判断：坐标系的选择“不影响对问题本质的描绘，但将直接关系到解决问题的难易程度”。矩形梁、矩形截面水坝、三角形水坝这类直边几何，边界在直角坐标里就是 $x=\text{const}$ 或 $y=\text{const}$，边界条件可直接写成应力分量等于给定值；而圆盘、厚壁圆筒、扇形板、半无限平面，边界是圆周与径向线，若硬用直角坐标，边界方程会变成 $\sqrt{x^{2}+y^{2}}=a$ 这类形式，边界条件难以直接使用。

所以本章要做的其实是两项工作：把平衡、几何、物理（连同协调）这几类方程用贴合边界的语言重写一遍；再在新形式的边界条件下解一批典型问题。极坐标不改变力学规律本身。

需要注意，翻译不等于把 $x$ 换成 $\rho$、$y$ 换成 $\varphi$。极坐标微分单元体的两条“边长”不相等（$\rho\,\mathrm{d}\varphi$ 与 $(\rho+\mathrm{d}\rho)\mathrm{d}\varphi$），两个径向平面的法线也不平行。这两点几何事实是极坐标方程中处处出现 $1/\rho$、以及平衡方程里出现 $(\sigma_{\rho}-\sigma_{\varphi})/\rho$ 项的真正来源。理解来源，就不必把它们当成需要死记的“附加项”。

## 二、基本方程：三处修正与一个不变的骨架

### 2.1 平衡方程：$1/\rho$ 项与 $(\sigma_\rho-\sigma_\varphi)/\rho$ 项的由来

从长柱体或薄板中割出由 $\rho$ 与 $\rho+\mathrm{d}\rho$ 两圆柱面、$\varphi$ 与 $\varphi+\mathrm{d}\varphi$ 两径向平面围成的单元体，厚度取 1。应力分量为 $\sigma_{\rho}$、$\sigma_{\varphi}$、$\tau_{\rho\varphi}=\tau_{\varphi\rho}$（互等），体力分量 $F_{\rho}$、$F_{\varphi}$。

投影到径向轴时有两类力会“斜”进来：两个径向平面上的 $\sigma_{\varphi}$，其法线与径向轴的夹角为 $\mathrm{d}\varphi/2$，取 $\sin\frac{\mathrm{d}\varphi}{2}\approx\frac{\mathrm{d}\varphi}{2}$ 后贡献 $-\sigma_{\varphi}\,\mathrm{d}\rho\,\mathrm{d}\varphi$；两个圆柱面的面积相差 $(\rho+\mathrm{d}\rho)\mathrm{d}\varphi-\rho\,\mathrm{d}\varphi=\mathrm{d}\rho\,\mathrm{d}\varphi$，展开后与 $\partial\sigma_{\rho}/\partial\rho$ 项合并。除以 $\rho\,\mathrm{d}\varphi\,\mathrm{d}\rho$、略去三阶微量，得

$$
\left.\begin{array}{l}
\dfrac{\partial\sigma_{\rho}}{\partial\rho}+\dfrac{1}{\rho}\dfrac{\partial\tau_{\varphi\rho}}{\partial\varphi}+\dfrac{\sigma_{\rho}-\sigma_{\varphi}}{\rho}+F_{\rho}=0\\[6pt]
\dfrac{\partial\tau_{\rho\varphi}}{\partial\rho}+\dfrac{1}{\rho}\dfrac{\partial\sigma_{\varphi}}{\partial\varphi}+\dfrac{2\tau_{\rho\varphi}}{\rho}+F_{\varphi}=0
\end{array}\right\}\tag{7-3}
$$

第二式中 $2\tau_{\rho\varphi}/\rho$ 的出现，同样来自两圆柱面上 $\tau_{\rho\varphi}$ 的作用面积差与两径向面上 $\tau_{\varphi\rho}$ 的法线不平行。

**易错辨析**：$(\sigma_{\rho}-\sigma_{\varphi})/\rho$ 这一项常被漏写。检查办法是令 $\sigma_{\rho}=\sigma_{\varphi}=p$（各向同性压力）、$\tau=0$，此时两个方程应化为 $\partial p/\partial\rho=F_{\rho}$ 之类的静水压力形式；漏项则无法通过这个检验。

### 2.2 几何方程：环向应变的两部分与切应变中的刚体转动

径向应变直接是 $\varepsilon_{\rho}=\partial u_{\rho}/\partial\rho$。环向应变由两个互不重叠的原因叠加：

- 纯径向位移 $u_{\rho}$ 使半径 $\rho$ 变为 $\rho+u_{\rho}$，周长相对伸长率为 $u_{\rho}/\rho$；
- 纯环向位移 $u_{\varphi}$ 沿弧长的变化率为 $\dfrac{1}{\rho}\dfrac{\partial u_{\varphi}}{\partial\varphi}$。

切应变则要从“转角”角度理解：$\gamma_{\rho\varphi}=\gamma+(\beta-\alpha)$，其中 $\gamma$ 是环向微分线段向 $\rho$ 方向的转角，$\beta=\partial u_{\varphi}/\partial\rho$ 是径向线段向 $\varphi$ 方向的转角，而 $\alpha=u_{\varphi}/\rho$ 是径向线本身的整体转动。$\alpha$ 必须**减掉**，因为整体转动不产生切应变。

$$
\left.\begin{array}{l}
\varepsilon_{\rho}=\dfrac{\partial u_{\rho}}{\partial\rho}\\[6pt]
\varepsilon_{\varphi}=\dfrac{1}{\rho}\dfrac{\partial u_{\varphi}}{\partial\varphi}+\dfrac{u_{\rho}}{\rho}\\[6pt]
\gamma_{\rho\varphi}=\dfrac{1}{\rho}\dfrac{\partial u_{\rho}}{\partial\varphi}+\dfrac{\partial u_{\varphi}}{\partial\rho}-\dfrac{u_{\varphi}}{\rho}
\end{array}\right\}\tag{7-4}
$$

这里的 $-\,u_{\varphi}/\rho$ 是与直角坐标几何方程相比唯一“结构上不同”的地方，后续所有位移多值性讨论都要回到它。

### 2.3 物理方程与协调方程：形式不变，常数要换

因为物体各向同性，平面应力的胡克定律与直角坐标同形，只需把 $x,y$ 换成 $\rho,\varphi$：

$$
\left.\begin{array}{l}
\varepsilon_{\rho}=\dfrac{1}{E}\left(\sigma_{\rho}-\nu\sigma_{\varphi}\right)\\[6pt]
\varepsilon_{\varphi}=\dfrac{1}{E}\left(\sigma_{\varphi}-\nu\sigma_{\rho}\right)\\[6pt]
\gamma_{\rho\varphi}=\dfrac{2(1+\nu)}{E}\tau_{\rho\varphi}
\end{array}\right\}\tag{7-5}
$$

平面应变问题须把 $E$、$\nu$ 分别换成 $\dfrac{E}{1-\nu^{2}}$、$\dfrac{\nu}{1-\nu}$。这一替换在本章会反复使用（圆筒、曲梁、半平面沉陷都要做），是查表时最容易漏掉的一步。

协调方程方面，关键是不变量 $\sigma_{x}+\sigma_{y}=\sigma_{\rho}+\sigma_{\varphi}$。借助坐标变换求得拉普拉斯算子

$$
\nabla^{2}=\frac{\partial^{2}}{\partial\rho^{2}}+\frac{1}{\rho}\frac{\partial}{\partial\rho}+\frac{1}{\rho^{2}}\frac{\partial^{2}}{\partial\varphi^{2}}
$$

于是**体力为常量**时，应力形式的协调方程为

$$
\left(\frac{\partial^{2}}{\partial\rho^{2}}+\frac{1}{\rho}\frac{\partial}{\partial\rho}+\frac{1}{\rho^{2}}\frac{\partial^{2}}{\partial\varphi^{2}}\right)\left(\sigma_{\rho}+\sigma_{\varphi}\right)=0\tag{7-6}
$$

### 2.4 应力函数与双调和方程

**体力不计**时取应力解法，令

$$
\left.\begin{array}{l}
\sigma_{\rho}=\dfrac{1}{\rho}\dfrac{\partial U}{\partial\rho}+\dfrac{1}{\rho^{2}}\dfrac{\partial^{2}U}{\partial\varphi^{2}}\\[6pt]
\sigma_{\varphi}=\dfrac{\partial^{2}U}{\partial\rho^{2}}\\[6pt]
\tau_{\rho\varphi}=\tau_{\varphi\rho}=-\dfrac{\partial}{\partial\rho}\left(\dfrac{1}{\rho}\dfrac{\partial U}{\partial\varphi}\right)
\end{array}\right\}\tag{7-7}
$$

可直接验证它满足 (7-3)。注意 $\tau_{\rho\varphi}$ 的两种等价写法：展开式 $-\frac{1}{\rho}\frac{\partial^{2}U}{\partial\rho\partial\varphi}+\frac{1}{\rho^{2}}\frac{\partial U}{\partial\varphi}$ 与紧凑式 $-\frac{\partial}{\partial\rho}\left(\frac{1}{\rho}\frac{\partial U}{\partial\varphi}\right)$，后者求导更方便。

代入 (7-6) 得极坐标双调和方程

$$
\left(\frac{\partial^{2}}{\partial\rho^{2}}+\frac{1}{\rho}\frac{\partial}{\partial\rho}+\frac{1}{\rho^{2}}\frac{\partial^{2}}{\partial\varphi^{2}}\right)\left(\frac{\partial^{2}U}{\partial\rho^{2}}+\frac{1}{\rho}\frac{\partial U}{\partial\rho}+\frac{1}{\rho^{2}}\frac{\partial^{2}U}{\partial\varphi^{2}}\right)=0\tag{7-8}
$$

**适用范围**：$U$ 需有连续到四阶的偏导数；方程本身是体力不计、线弹性、小变形、各向同性、平面问题（应力或应变）下的结论。

于是求解路线与直角坐标完全平行：**定边界条件 → 解双调和方程求 $U$ → 由 (7-7) 求应力 → 由 (7-5) 求应变 → 由 (7-4) 积分求位移 → 用约束条件与单值性定常数**。最后一步在极坐标下会变成实质性的物理约束，而不只是定刚体位移。

## 三、轴对称：把偏微分方程降成欧拉方程

### 3.1 这一节解决什么问题

工程上大量构件的几何与受载都绕某轴回转对称，此时应力应与 $\varphi$ 无关。于是双调和方程退化为一个常微分方程，问题从“解偏微分方程”降为“解常微分方程 + 定两个常数”。这一节给出这套退化结果，并顺带澄清一个常被误解的点：**应力轴对称是否意味着位移也轴对称？**

### 3.2 应力函数与应力

设 $U=U(\rho)$，(7-8) 变为

$$
\left(\frac{\mathrm{d}^{2}}{\mathrm{d}\rho^{2}}+\frac{1}{\rho}\frac{\mathrm{d}}{\mathrm{d}\rho}\right)\left(\frac{\mathrm{d}^{2}U}{\mathrm{d}\rho^{2}}+\frac{1}{\rho}\frac{\mathrm{d}U}{\mathrm{d}\rho}\right)=0
$$

展开并乘以 $\rho^{4}$ 得欧拉方程

$$
\rho^{4}\frac{\mathrm{d}^{4}U}{\mathrm{d}\rho^{4}}+2\rho^{3}\frac{\mathrm{d}^{3}U}{\mathrm{d}\rho^{3}}-\rho^{2}\frac{\mathrm{d}^{2}U}{\mathrm{d}\rho^{2}}+\rho\frac{\mathrm{d}U}{\mathrm{d}\rho}=0
$$

作 $\rho=\mathrm{e}^{t}$ 化为常系数方程，回代 $t=\ln\rho$，通解为

$$
U=A\ln\rho+B\rho^{2}\ln\rho+C\rho^{2}+D
$$

代入 (7-7)：

$$
\left.\begin{array}{l}
\sigma_{\rho}=\dfrac{A}{\rho^{2}}+B\left(1+2\ln\rho\right)+2C\\[6pt]
\sigma_{\varphi}=-\dfrac{A}{\rho^{2}}+B\left(3+2\ln\rho\right)+2C\\[6pt]
\tau_{\rho\varphi}=\tau_{\varphi\rho}=0
\end{array}\right\}\tag{7-9}
$$

这种对称于坐标原点分布的应力称为**轴对称应力**。四项常数对应四种“基本成分”：$A$ 项是 $1/\rho^{2}$ 衰减型，$这一回复从“四项常数对应四种基本成分”处接着写下去。

## 四、轴对称问题的完整解与位移的单值性

### 3.2 续：四项常数的物理含义

式 (7-9) 中四项常数各对应一类“基本成分”，识别它们比记住公式更有用：

- $A$ 项（$\propto 1/\rho^{2}$）：衰减型，圆筒、圆环内壁受压时的主要成分；
- $B$ 项（$\propto \ln\rho$ 及 $\rho^{0}$）：随 $\ln\rho$ 缓慢变化的成分，只在**不完整圆环**中才允许保留；
- $C$ 项（常数 $2C$）：均匀应力场，相当于均匀内压或均匀温度式的外载；
- $D$ 项：只进入 $U$，不产生应力，是应力函数的平凡常数。

$B$ 项能否保留，是全章最关键的分水岭。原因要到位移里去找。

### 3.3 位移：应力轴对称 ≠ 位移轴对称

把 (7-9) 代入 (7-5)、再用 (7-4)，得三个关于 $u_{\rho},u_{\varphi}$ 的方程。先由第一式积分出 $u_{\rho}$，代入第二式积分出 $u_{\varphi}$，再用第三式分离变量，过程中会出现两个任意函数 $f(\varphi)$、$g(\rho)$ 和分离常数 $F$，最终

$$
\left.\begin{array}{l}
u_{\rho}=\dfrac{1}{E}\Big[-(1+\nu)\dfrac{A}{\rho}+(1-3\nu)B\rho+2(1-\nu)B\rho(\ln\rho-1)+2(1-\nu)C\rho\Big]\\[6pt]
\qquad\quad +I\sin\varphi+K\cos\varphi\\[6pt]
u_{\varphi}=\dfrac{4B\rho\varphi}{E}+H\rho+I\cos\varphi-K\sin\varphi
\end{array}\right\}\tag{7-10}
$$

（平面应变需作 $E\to\frac{E}{1-\nu^{2}}$、$\nu\to\frac{\nu}{1-\nu}$ 的替换。）

展开式 (7-10) 立即说明两件事：

1. **应力轴对称并不表示位移轴对称**。$I\sin\varphi+K\cos\varphi$ 项说明可以有整体平移式的刚体位移，$H\rho$ 说明可以有整体转动。
2. $u_{\varphi}$ 中出现了 $\dfrac{4B\rho\varphi}{E}$，这是 $\varphi$ 的**多值项**。若 $\varphi$ 从 $0$ 变到 $2\pi$（几何上是同一点），$u_{\varphi}$ 将增加 $\dfrac{8B\rho\pi}{E}$。在**完整的圆环**中，同一点不能有两个位移，故必须有 $B=0$。

这就是所谓的**位移单值条件**。它是极坐标（曲线坐标）特有的约束：直角坐标下 $u,v$ 的单值性是自动满足的，而极坐标下多边形项会破坏单值性，必须显式检验。本章后续至少三次用到它——曲梁纯弯曲、曲梁受径向集中力、以及由错缝焊接求预应力的两个问题。

### 3.4 几何与受载都轴对称的简化

若物体的几何形状与受力（或几何约束）也轴对称，则物体内各点没有环向位移，即对任意 $\rho,\varphi$ 有 $u_{\varphi}=0$。由 (7-10) 第二式要求 $B=H=I=K=0$，于是

$$
\left.\begin{array}{l}
\sigma_{\rho}=\dfrac{A}{\rho^{2}}+2C\\[6pt]
\sigma_{\varphi}=-\dfrac{A}{\rho^{2}}+2C\\[6pt]
\tau_{\rho\varphi}=\tau_{\varphi\rho}=0
\end{array}\right\}\tag{7-11}
$$

$$
\left.\begin{array}{l}
u_{\rho}=\dfrac{1}{E}\Big[-(1+\nu)\dfrac{A}{\rho}+2(1-\nu)C\rho\Big]\\[6pt]
u_{\varphi}=0
\end{array}\right\}\tag{7-12}
$$

至此只留下两个待定常数 $A$、$C$，恰好由内外两个边界上的 $\sigma_{\rho}$ 条件确定。这就是后面厚壁圆筒能用两行代数解出的原因。

**易错辨析**：把 (7-11) 当成“所有轴对称问题的应力公式”是错的。(7-11) 的成立前提是**几何与受载均轴对称**；若只是应力轴对称而几何不闭合（如有切口的不完整圆环），必须回到 (7-9)，保留 $B$ 项。曲梁纯弯曲就是后一种情形。

## 五、厚壁圆筒受均匀压力：拉梅解

### 4.1 这一节解决什么问题

内半径 $a$、外半径 $b$ 的长厚壁圆筒，内外壁分别受均布压力 $q_{1}$、$q_{2}$。几何与受载均轴对称，故应力取 (7-11)、位移取 (7-12) 的形式（不计刚体位移时位移也轴对称）。问题降为：用两个边界条件定 $A$、$C$。

### 4.2 定常数与结果

压力以压为正，故边界条件为

$$
\left(\sigma_{\rho}\right)_{\rho=a}=-q_{1},\qquad \left(\sigma_{\rho}\right)_{\rho=b}=-q_{2}
$$

代入 (7-11) 得两个代数方程，解出

$$
A=\frac{a^{2}b^{2}\left(q_{2}-q_{1}\right)}{b^{2}-a^{2}},\qquad C=\frac{q_{1}a^{2}-q_{2}b^{2}}{2\left(b^{2}-a^{2}\right)}
$$

回代即得拉梅解答：

$$
\left.\begin{array}{l}
\sigma_{\rho}=\dfrac{a^{2}b^{2}}{b^{2}-a^{2}}\dfrac{q_{2}-q_{1}}{\rho^{2}}+\dfrac{a^{2}q_{1}-b^{2}q_{2}}{b^{2}-a^{2}}\\[8pt]
\sigma_{\varphi}=-\dfrac{a^{2}b^{2}}{b^{2}-a^{2}}\dfrac{q_{2}-q_{1}}{\rho^{2}}+\dfrac{a^{2}q_{1}-b^{2}q_{2}}{b^{2}-a^{2}}\\[8pt]
\tau_{\rho\varphi}=\tau_{\varphi\rho}=0
\end{array}\right\}\tag{7-13}
$$

### 4.3 只受内压的情形：应力符号与危险点

取 $q_{2}=0$：

$$
\sigma_{\rho}=\frac{a^{2}q_{1}}{b^{2}-a^{2}}\left(1-\frac{b^{2}}{\rho^{2}}\right),\qquad
\sigma_{\varphi}=\frac{a^{2}q_{1}}{b^{2}-a^{2}}\left(1+\frac{b^{2}}{\rho^{2}}\right)\tag{7-14}
$$

由此可直接读出三点结论：

- 在内壁到外壁的整个区间，$\sigma_{\rho}<0$（压）、$\sigma_{\varphi}>0$（拉），即筒壁处于“径向受压、环向受拉”的状态；
- $\sigma_{\varphi}$ 的最大值在内壁 $\rho=a$ 处：
$$
\left(\sigma_{\varphi}\right)_{\max}=\frac{q_{1}\left(a^{2}+b^{2}\right)}{b^{2}-a^{2}}\tag{7-15}
$$
- 该式在 $b\to a$ 时急剧增大，说明“壁很薄时环向应力远高于内压”这一趋势；但**原文未讨论薄壁圆筒的近似公式及厚壁判据**，需要时应另查薄壁理论。

**适用前提**：等厚、长圆筒（端部效应不计）、内外壁面力均布、线弹性各向同性、小变形。平面应力或平面应变均可，差别只在 $E,\nu$ 的替换，而**应力解 (7-13) 本身与弹性常数无关**——这是本章一个值得注意的性质：轴对称拉梅解是“静定”的。

## 六、曲梁的纯弯曲：为什么中性轴不在中线上

### 5.1 这一节解决什么问题

内半径 $a$、外半径 $b$ 的矩形截面曲梁（厚度取 1），两端受弯矩 $M$。所有径向截面上的弯矩都等于 $M$，因而可认为各截面应力分布相同，即**应力与 $\varphi$ 无关**，取 (7-9) 的形式（注意：不能取 (7-11)，因为需要 $B$ 项）。

这里“轴对称应力”是一种由受力特点（弯矩处处相同）推出的合理假设，与几何是否回转对称无关——这是它与厚壁圆筒的区别所在。

### 5.2 边界条件与结果

内外侧面无面力，端面上轴力为零、弯矩为 $M$：

$$
\left.\begin{array}{l}
\left(\sigma_{\rho}\right)_{\rho=a}=0,\quad \left(\tau_{\rho\varphi}\right)_{\rho=a}=0\\[4pt]
\left(\sigma_{\rho}\right)_{\rho=b}=0,\quad \left(\tau_{\rho\varphi}\right)_{\rho=b}=0\\[4pt]
\displaystyle\int_{a}^{b}\sigma_{\varphi}\,\mathrm{d}\rho=0,\qquad \int_{a}^{b}\rho\sigma_{\varphi}\,\mathrm{d}\rho=-M
\end{array}\right\}\tag{b}
$$

将 (7-9) 代入后可看出：**轴力为零这一条件不是独立的**，它是两个侧面条件 $\left(\sigma_{\rho}\right)_{a}=\left(\sigma_{\rho}\right)_{b}=0$ 的必然结果。因此四个方程只定三个常数（这是纯弯曲“无轴力”的自洽性体现，不是方程组的缺陷）。解得

$$
A=-\frac{4M}{N}a^{2}b^{2}\ln\frac{b}{a},\quad
B=-\frac{2M}{N}\left(b^{2}-a^{2}\right),\quad
C=\frac{M}{N}\left[b^{2}-a^{2}+2\left(b^{2}\ln b-a^{2}\ln a\right)\right]
$$

$$
N=\left(b^{2}-a^{2}\right)^{2}-4a^{2}b^{2}\left(\ln\frac{b}{a}\right)^{2}
$$

代入 (7-9) 得应力：

$$
\left.\begin{array}{l}
\sigma_{\rho}=-\dfrac{4M}{N}\left(\dfrac{a^{2}b^{2}}{\rho^{2}}\ln\dfrac{b}{a}-b^{2}\ln\dfrac{b}{\rho}+a^{2}\ln\dfrac{a}{\rho}\right)\\[8pt]
\sigma_{\varphi}=\dfrac{4M}{N}\left(\dfrac{a^{2}b^{2}}{\rho^{2}}\ln\dfrac{b}{a}+b^{2}\ln\dfrac{\rho}{b}+a^{2}\ln\dfrac{a}{\rho}+b^{2}-a^{2}\right)\\[8pt]
\tau_{\rho\varphi}=\tau_{\varphi\rho}=0
\end{array}\right\}\tag{7-16}
$$

### 5.3 三条与直梁不同的结论

- 弯曲应力 $\sigma_{\varphi}$ 的最大值在**内边界** $\rho=a$ 处；
- 中性轴（$\sigma_{\varphi}=0$ 处）**偏向内边界一侧**，不在 $(\rho)=(a+b)/2$ 的中线上；
- 挤压应力 $\sigma_{\rho}$ 的最大值位置比中性轴更靠近内边界。

这三点与直梁“应力线性分布、中性轴过形心”的结论截然不同，根源是曲梁中纤维长度本身随 $\rho$ 变化；直梁公式只在 $a/b\to 1$ 的极限下才是曲梁解的近似。

### 5.4 位移与多值性：完整环与不完整环的分界

求位移时把 $A,B,C$ 代入 (7-10)，$H,K,I$ 由约束条件定。例如取 $\varphi=0$、$\rho=\rho_{0}=\frac{a+b}{2}$ 处位移为零、且该点径向线段无转角：

$$
\left(u_{\rho}\right)_{\rho=\rho_{0}}=0,\quad \left(u_{\varphi}\right)_{\rho=\rho_{0}}=0,\quad \left(\frac{\partial u_{\varphi}}{\partial\rho}\right)_{\rho=\rho_{0}}=0
$$

此时环向位移为

$$
u_{\varphi}=\frac{4B\rho\varphi}{E}-K\sin\varphi
$$

**它仍是 $\varphi$ 的多值函数**。在完整圆环中这不可能，故 $B$ 必须为零；而在**不完整圆环**（如带张角 $\alpha$ 的小切口）中，多值是允许的，而且正是它能描述“环被强行拼合”这件事。

由此得到本节最有价值的应用：带小切口的不完整圆环，用外力把两端压紧后焊合，其内将产生预应力。令切口张角 $\alpha$ 对应的环向位移 $\alpha\rho$ 与多值项增量 $\dfrac{8B\rho\pi}{E}$ 相等，得 $B=\dfrac{\alpha E}{8\pi}$，再代回 $B$ 的表达式反解：

$$
M=-\frac{\alpha E}{8\pi}\cdot\frac{\left(b^{2}-a^{2}\right)^{2}-4a^{2}b^{2}\left(\ln\dfrac{b}{a}\right)^{2}}{2\left(b^{2}-a^{2}\right)}\tag{7-17}
$$

将 (7-17) 代回 (7-16) 即得该“焊缝预应力”。思路要点：**多值项不是数学累赘，而是描述闭合位错（错缝）的物理量**。

## 七、曲梁一端受径向集中力：按载荷形式选应力函数

### 6.1 这一节解决什么问题

内半径 $a$、外半径 $b$ 的曲梁，一端固定、另一端受径向集中力 $F$（单位厚度）。按初等理论，任一截面弯矩与 $\sin\varphi$ 成正比；由 (7-7) 第二式 $\sigma_{\varphi}=\partial^{2}U/\partial\rho^{2}$ 可知 $U$ 也应与 $\sin\varphi$ 成正比。故试取

$$
U=f(\rho)\sin\varphi
$$

代入 (7-8) 得 $f$ 的方程

$$
\left(\frac{\mathrm{d}^{2}}{\mathrm{d}\rho^{2}}+\frac{1}{\rho}\frac{\mathrm{d}}{\mathrm{d}\rho}-\frac{1}{\rho^{2}}\right)\left(\frac{\mathrm{d}^{2}f}{\mathrm{d}\rho^{2}}+\frac{1}{\rho}\frac{\mathrm{d}f}{\mathrm{d}\rho}-\frac{f}{\rho^{2}}\right)=0
$$

这是可化为常系数的欧拉型方程，通解

$$
f(\rho)=A\rho^{3}+B\frac{1}{\rho}+C\rho+D\rho\ln\rho
$$

其中 $C\rho$ 项对应 $C\rho\sin\varphi=Cy$，属线性项，不产生应力，可略。

**方法要点**：这里选 $U$ 的依据不是“猜”，而是两步推理——外载形式（集中力）→ 内力形式（$M\propto\sin\varphi$）→ 应力函数的角度依赖。这与 §7-6 由边界条件含 $\cos 2\varphi$ 而取 $U=f(\rho)\cos 2\varphi$、§7-7 由量纲分析取 $U=\rho f(\varphi)$，构成同一套“按载荷形式定角度因子、按量纲定径向幂次”的方法。这是全章解题的主线索。

### 6.2 边界条件与结果

$$
\left.\begin{array}{l}
\left(\sigma_{\rho}\right)_{\rho=a}=0,\quad \left(\tau_{\rho\varphi}\right)_{\rho=a}=0\\[4pt]
\left(\sigma_{\rho}\right)_{\rho=b}=0,\quad \left(\tau_{\rho\varphi}\right)_{\rho=b}=0\\[4pt]
\left(\sigma_{\varphi}\right)_{\varphi=0}=0,\quad \displaystyle\int_{a}^{b}\left(\tau_{\varphi\rho}\right)_{\varphi=0}\mathrm{d}\rho=-F
\end{array}\right\}\tag{d}
$$

解得

$$
A=-\frac{F}{2N},\quad B=\frac{Fa^{2}b^{2}}{2N},\quad D=\frac{F}{N}\left(a^{2}+b^{2}\right),\quad
N=a^{2}-b^{2}+\left(a^{2}+b^{2}\right)\ln\frac{b}{a}
$$

$$
\left.\begin{array}{l}
\sigma_{\rho}=-\dfrac{F}{N}\left(\rho-\dfrac{a^{2}+b^{2}}{\rho}+\dfrac{a^{2}b^{2}}{\rho^{3}}\right)\sin\varphi\\[8pt]
\sigma_{\varphi}=-\dfrac{F}{N}\left(3\rho-\dfrac{a^{2}+b^{2}}{\rho}-\dfrac{a^{2}b^{2}}{\rho^{3}}\right)\sin\varphi\\[8pt]
\tau_{\rho\varphi}=\tau_{\varphi\rho}=\dfrac{F}{N}\left(\rho-\dfrac{a^{2}+b^{2}}{\rho}+\dfrac{a^{2}b^{2}}{\rho^{3}}\right)\cos\varphi
\end{array}\right\}\tag{7-18}
$$

注意 $\sigma_{\rho}$ 与 $\tau_{\rho\varphi}$ 的括号内容完全相同，只是 $\sin\varphi$ 与 $\cos\varphi$ 之别——这来自 $\sigma_{\rho}=\frac{1}{\rho}U_{,\rho}+\frac{1}{\rho^{2}}U_{,\varphi\varphi}$ 与 $\tau_{\rho\varphi}=-\frac{\partial}{\partial\rho}\left(\frac{1}{\rho}U_{,\varphi}\right)$ 的结构对应。

### 6.3 位移与两个预应力问题

位移由 (7-5)、(7-4) 积分得

$$
\left.\begin{array}{l}
u_{\rho}=\dfrac{2D}{E}\varphi\cos\varphi+\dfrac{\sin\varphi}{E}\Big[A\rho^{2}(1-3\nu)+\dfrac{B}{\rho^{2}}(1+\nu)+D(1-\nu)\ln\rho\Big]\\[6pt]
\qquad\quad +K\sin\varphi+L\cos\varphi\\[6pt]
u_{\varphi}=\dfrac{2D}{E}\varphi\sin\varphi-\dfrac{\cos\varphi}{E}\Big[A\rho^{2}(5+\nu)+\dfrac{B}{\rho^{2}}(1+\nu)-D(1-\nu)\ln\rho\Big]\\[6pt]
\qquad\quad +\dfrac{D(1+\nu)}{E}\cos\varphi+K\cos\varphi-L\sin\varphi+H\rho
\end{array}\right\}\tag{7-19}
$$

含 $\varphi\cos\varphi$、$\varphi\sin\varphi$ 的项仍是多值项，完整圆环中必须 $D=0$。原文用 (7-19) 处理两类预应力：

- **径向细缝错开 $\delta$**：取缝下表面 $\varphi=0$、上表面 $\varphi=2\pi$，由 $\delta=\left(u_{\rho}\right)_{\varphi=2\pi}-\left(u_{\rho}\right)_{\varphi=0}$ 得 $\delta=-\dfrac{4D\pi}{E}$，与 $D$ 的表达式联立得所需力
$$
F=-\frac{NE\delta}{4\pi\left(a^{2}+b^{2}\right)}
$$
  代回 (7-18) 即得应力。
- **切口两表面平行、距离 $\delta$ 的圆环合拢**：原文用了一个很漂亮的分解技巧——在环上再切一条水平径向缝，把切出的四分之一环平移 $\delta$ 使切口合拢，此时环内无应力；再迫使水平缝下表面反向错动 $\delta$ 并焊合，得到完整圆环。于是所求应力与前一情形**只差一个符号**。这类“先构造一个无应力状态、再把差额作为加载”的叠加思路，值得单独记住。

## 八、小圆孔的应力集中：把边界条件拆成两部分

### 7.1 这一节解决什么问题

无限大（近似）平板在 $x$ 方向受均匀拉力 $q$，板中有半径 $a$ 的小圆孔。孔的存在扰动应力场，但由**圣维南原理**，影响只限于孔附近。于是在离孔心 $b$（$b\gg a$）的同心圆周上，可认为应力已与无孔时相同：

$$
\left.\begin{array}{l}
\left(\sigma_{\rho}\right)_{\rho=b}=q\cos^{2}\varphi=\dfrac{q}{2}\left(1+\cos 2\varphi\right)\\[6pt]
\left(\tau_{\rho\varphi}\right)_{\rho=b}=-\dfrac{q}{2}\sin 2\varphi
\end{array}\right\}\tag{a}
$$

### 7.2 叠加分解：均匀部分 + $\cos 2\varphi$ 部分

式 (a) 的右端可拆为两项，分别求解后相加：

**（1）均匀部分 $q/2$**：它是圆环外壁受压的轴对称问题，直接套拉梅解 (7-13)，取 $q_{1}=0$、$q_{2}=-q/2$，并令 $a/b\approx 0$：

$$
\sigma_{\rho}=\frac{b^{2}}{b^{2}-a^{2}}\frac{q}{2}\left(1-\frac{a^{2}}{\rho^{2}}\right),\quad
\sigma_{\varphi}=\frac{b^{2}}{b^{2}-a^{2}}\frac{q}{2}\left(1+\frac{a^{2}}{\rho^{2}}\right),\quad
\tau_{\rho\varphi}=0
$$

**（2）随 $\varphi$ 变化部分** $\frac{q}{2}\cos 2\varphi$、$-\frac{q}{2}\sin 2\varphi$：按角度依赖取

$$
U=f(\rho)\cos 2\varphi
$$

代入 (7-8) 得欧拉方程

$$
\rho^{4}\frac{\mathrm{d}^{4}f}{\mathrm{d}\rho^{4}}+2\rho^{3}\frac{\mathrm{d}^{3}f}{\mathrm{d}\rho^{3}}-9\rho^{2}\frac{\mathrm{d}^{2}f}{\mathrm{d}\rho^{2}}+9\rho\frac{\mathrm{d}f}{\mathrm{d}\rho}=0
$$

通解 $f(\rho)=A\rho^{2}+B\rho^{4}+\dfrac{C}{\rho^{2}}+D$。四个常数对应孔边条件（$\sigma_{\rho}=\tau_{\rho\varphi}=0$）与远场条件各两个，恰好封闭。令 $a/b\approx 0$ 解得

$$
A=-\frac{q}{4},\quad B=0,\quad C=-\frac{a^{4}q}{4},\quad D=\frac{a^{2}q}{2}
$$

两部分相加即基尔施（Kirsch）型解答：

$$
\left.\begin{array}{l}
\sigma_{\rho}=\dfrac{q}{2}\left(1-\dfrac{a^{2}}{\rho^{2}}\right)+\dfrac{q}{2}\left(1+\dfrac{3a^{4}}{\rho^{4}}-\dfrac{4a^{2}}{\rho^{2}}\right)\cos 2\varphi\\[8pt]
\sigma_{\varphi}=\dfrac{q}{2}\left(1+\dfrac{a^{2}}{\rho^{2}}\right)-\dfrac{q}{2}\left(1+\dfrac{3a^{4}}{\rho^{4}}\right)\cos 2\varphi\\[8pt]
\tau_{\rho\varphi}=\tau_{\varphi\rho}=-\dfrac{q}{2}\left(1-\dfrac{3a^{4}}{\rho^{4}}+\dfrac{2a^{2}}{\rho^{2}}\right)\sin 2\varphi
\end{array}\right\}\tag{7-20}
$$

### 7.3 应力集中因子

孔边 $\rho=a$ 处 $\sigma_{\rho}=\tau_{\rho\varphi}=0$（自由孔边，必然），而

$$
\sigma_{\varphi}=q-2q\cos 2\varphi
$$

在 $\varphi=\pm\dfrac{\pi}{2}$（垂直于拉力方向的两点）取最大值

$$
\left(\sigma_{\varphi}\right)_{\max}=3q
$$

故集中因子 $K=\dfrac{\left(\sigma_{\varphi}\right)_{\max}}{q}=3$。若板在两个方向同时均匀受拉，$K=2$（原文留作练习，此处不展开）。

**适用前提要说明**：$a/b\to 0$（板相对孔无限大）、单向均匀拉伸、圆孔、孔边自由、线弹性小变形、无其他孔干涉。**原文未给出有限板宽的修正系数，也未讨论椭圆孔或其他孔形**；工程上板宽有限时必须另查修正曲线，不能直接取 $K=3$。

**易错辨析**：孔边的 $\sigma_{\rho}=0$ 容易让人误以为“孔边不危险”。实际上危险的是 $\sigma_{\varphi}$，它恰在孔边最大，且是远场应力的 3 倍。判断危险点要看哪个分量在边界上非零。

## 九、尖劈与 $1/\rho$ 型奇异：量纲分析先行

### 8.1 这一节解决什么问题

中心角 $\alpha$、下端伸向无穷的尖劈，顶点受集中力 $F$（与中心线成 $\beta$ 角）或集中力偶 $M$。这类问题的边界是两条径向直线，用极坐标时边界条件恰好落在 $\sigma_{\varphi}$、$\tau_{\varphi\rho}$ 上，非常方便。困难在于：不知道应力函数该取什么形式。

### 8.2 用量纲分析定 $\rho$ 的幂次

$F$ 的量纲为 $\mathrm{MT^{-2}}$，$\rho$ 为 $\mathrm{L}$，$\alpha,\beta,\varphi$ 无量纲。要使应力分量量纲正确，各应力只能取 $\dfrac{F}{\rho}N(\alpha,\beta,\varphi)$ 的形式，即**应力中 $\rho$ 只能出现负一次幂**。又由 (7-7) 可见应力函数中 $\rho$ 的幂次比应力高两次，故

$$
U=\rho f(\varphi)
$$

代入 (7-8)：

$$
\frac{1}{\rho^{3}}\left[\frac{\mathrm{d}^{4}f}{\mathrm{d}\varphi^{4}}+2\frac{\mathrm{d}^{2}f}{\mathrm{d}\varphi^{2}}+f\right]=0
$$

解得 $f=A\cos\varphi+B\sin\varphi+\varphi\left(C\cos\varphi+D\sin\varphi\right)$。其中 $A\rho\cos\varphi=Ax$、$B\rho\sin\varphi=By$ 是线性项，不产生应力，可略去，故

$$
U=\rho\varphi\left(C\cos\varphi+D\sin\varphi\right)\tag{b}
$$

### 8.3 结果与“纯径向应力状态”

$$
\left.\begin{array}{l}
\sigma_{\rho}=\dfrac{2}{\rho}\left(D\cos\varphi-C\sin\varphi\right)\\[6pt]
\sigma_{\varphi}=0\\[6pt]
\tau_{\rho\varphi}=\tau_{\varphi\rho}=0
\end{array}\right\}\tag{c}
$$

这里出现了本章一个很特殊的应力状态：$\sigma_{\varphi}=\tau_{\rho\varphi}=0$ 恒成立，于是**两条径向边界上的无面力条件自动满足**，只剩顶点的合力条件待用。同时，各点主应力为一个径向应力与零，主方向为 $\rho$ 方向与 $\varphi$ 方向——应力沿径向呈 $1/\rho$ 奇异。

因此常数只能靠**整体平衡**定：取任一圆柱面以上部分为隔离体，由 $\sum F_{x}=0$、$\sum F_{y}=0$ 得

$$
D\left(\alpha+\sin\alpha\right)+F\cos\beta=0,\qquad C\left(-\alpha+\sin\alpha\right)+F\sin\beta=0
$$

解得

$$
C=\frac{F\sin\beta}{\alpha-\sin\alpha},\qquad D=-\frac{F\cos\beta}{\alpha+\sin\alpha}
$$

于是

$$
\left.\begin{array}{l}
\sigma_{\rho}=-\dfrac{2F\cos\beta\cos\varphi}{\left(\alpha+\sin\alpha\right)\rho}-\dfrac{2F\sin\beta\sin\varphi}{\left(\alpha-\sin\alpha\right)\rho}\\[8pt]
\sigma_{\varphi}=0\\[8pt]
\tau_{\rho\varphi}=\tau_{\varphi\rho}=0
\end{array}\right\}\tag{7-21}
$$

$\beta=0$ 时应力对称于 $x$ 轴，$\beta=\dfrac{\pi}{2}$ 时反对称于 $x$ 轴。

**集中力偶**情形：量纲分析给出应力中 $\rho$ 只能出现负二次幂，故 $U$ 与 $\rho$ 无关，取 $U=f(\varphi)$，同样步骤得

$$
\left.\begin{array}{l}
\sigma_{\rho}=\dfrac{2M\sin 2\varphi}{\left(\sin\alpha-\alpha\cos\alpha\right)\rho^{2}}\\[8pt]
\sigma_{\varphi}=0\\[8pt]
\tau_{\rho\varphi}=\tau_{\varphi\rho}=-\dfrac{M\left(\cos 2\varphi-\cos\alpha\right)}{\left(\sin\alpha-\alpha\cos\alpha\right)\rho^{2}}
\end{array}\right\}\tag{7-22}
$$

### 8.4 解的边界在哪里

$\sigma_{\rho}\propto 1/\rho$（集中力）、$\propto 1/\rho^{2}$（集中力偶），在顶点 $\rho\to 0$ 处无界。这说明**线弹性解在集中力作用点附近失效**：真实材料会在该处进入塑性或形成接触区，实际应力有限。原文本章未讨论这一修正，只需知道“顶点附近的解不能直接用于强度判断”即可。

另一个要注意的点是 $\alpha-\sin\alpha$、$\sin\alpha-\alpha\cos\alpha$ 这两个分母：在小角尖劈或特定角下它们会趋于零或变号，意味着解的形态发生定性改变。原文未展开，此处仅作提示。

## 十、弹性半平面：弗拉芒解及其推论

### 9.1 这一节解决什么问题

半平面边界上受垂直集中力（单位厚度荷载 $F$）——即布西内斯克–符拉芒问题。它不需要重新推导：**把尖劈解取 $\alpha=\pi,\ \beta=0$ 即得**。这是本章结构上很经济的一处安排：半平面被看作张角 $\pi$ 的尖劈。

### 9.2 应力及其两个几何特征

$$
\sigma_{\rho}=-\frac{2F\cos\varphi}{\pi\rho},\qquad \sigma_{\varphi}=0,\qquad \tau_{\rho\varphi}=\tau_{\varphi\rho}=0\tag{7-23}
$$

由此可读出两个特征：

1. **过体内任一点且与矢径垂直的微分面都是主平面**（该面上切应力为零）；
2. **直径过力作用点 $O$、与 $x$ 轴重合的圆周上各点径向应力相等**：圆上 $\rho=d\cos\varphi$，故 $\dfrac{\cos\varphi}{\rho}=\dfrac{1}{d}$，代入得 $\sigma_{\rho}=-\dfrac{2F}{\pi d}=\text{const}$。

特征 2 是“压力泡”式分布的数学来源：等应力线是一族过 $O$ 的圆。

转换为直角坐标（$x$ 为深度、$y$ 为水平向）：

$$
\sigma_{x}=-\frac{2F}{\pi}\frac{x^{3}}{\left(x^{2}+y^{2}\right)^{2}},\quad
\sigma_{y}=-\frac{2F}{\pi}\frac{xy^{2}}{\left(x^{2}+y^{2}\right)^{2}},\quad
\tau_{xy}=-\frac{2F}{\pi}\frac{x^{2}y}{\left(x^{2}+y^{2}\right)^{2}}\tag{7-24}
$$

沿某一水平面：$\left(\sigma_{x}\right)_{\max}=\dfrac{2F}{\pi x}$（在 $Ox$ 轴上），最大切应力出现在离 $x$ 轴 $\dfrac{x}{\sqrt{3}}$ 处，值为 $\dfrac{2F}{\pi x}\cdot\dfrac{9}{16\sqrt{3}}$。这解释了地基中塑性区为何先从一定深度处开始（原文未展开塑性，仅给应力值）。

### 9.3 位移与沉陷：为什么只能求相对沉陷

把 (7-23) 代入 (7-5)、(7-4) 积分，利用对称性 $\left(u_{\varphi}\right)_{\varphi=0}=0$ 定出 $H=K=0$：

$$
\left.\begin{array}{l}
u_{\rho}=-\dfrac{2F}{\pi E}\cos\varphi\ln\rho-\dfrac{(1-\nu)F}{\pi E}\varphi\sin\varphi+I\cos\varphi\\[6pt]
u_{\varphi}=\dfrac{2F}{\pi E}\sin\varphi\ln\rho-\dfrac{(1-\nu)F}{\pi E}\varphi\cos\varphi+\dfrac{(1+\nu)F}{\pi E}\sin\varphi-I\sin\varphi
\end{array}\right\}\tag{7-25}
$$

取 $\varphi=\pm\dfrac{\pi}{2}$ 得表面点 $M$ 的沉陷

$$
-\left(u_{\varphi}\right)_{\varphi=\frac{\pi}{2}}=-\frac{2F}{\pi E}\ln\rho-\frac{(1+\nu)F}{\pi E}+I
$$

$I$ 是铅垂方向的刚体位移；半平面不受铅垂约束时 $I$ 不能确定，**因而绝对沉陷不能确定，只能求相对沉陷**。在边界上任取距作用点 $s$ 的基点 $B$，相减得

$$
\eta=\frac{2F}{\pi E}\ln\frac{s}{\rho}\tag{7-26}
$$

这是本章唯一出现对数型沉降公式的地方：它随 $\rho$ 对数发散，正是“半平面无限延伸、无基准面”这一理想化的直接后果，而不是计算错误。平面应变时仍需作 $E,\nu$ 的替换。

### 9.4 叠加：分布荷载、切向力与力偶

- **分布荷载**：把 $\mathrm{d}F=q(\eta)\,\mathrm{d}\eta$ 当作集中力，注意 (7-24) 中的 $x$、$y$ 应换成求应力点与荷载作用点的铅垂、水平距离 $x$ 与 $y-\eta$，积分得
$$
\left.\begin{array}{l}
\sigma_{x}=-\dfrac{2}{\pi}\displaystyle\int_{-b}^{a}\dfrac{qx^{3}\,\mathrm{d}\eta}{\left[x^{2}+\left(y-\eta\right)^{2}\right]^{2}}\\[8pt]
\sigma_{y}=-\dfrac{2}{\pi}\displaystyle\int_{-b}^{a}\dfrac{qx\left(y-\eta\right)^{2}\,\mathrm{d}\eta}{\left[x^{2}+\left(y-\eta\right)^{2}\right]^{2}}\\[8pt]
\tau_{xy}=-\dfrac{2}{\pi}\displaystyle\int_{-b}^{a}\dfrac{qx^{2}\left(y-\eta\right)\mathrm{d}\eta}{\left[x^{2}+\left(y-\eta\right)^{2}\right]^{2}}
\end{array}\right\}\tag{7-27}
$$
  使用时须先把 $按前文，从“使用时须先把 $q$ 表示成 $\eta$ 的函数”接续。

使用时须先把 $q$ 表示成 $\eta$ 的显式函数，再逐项积分；若 $q$ 为常数且积分区段对称，则可化为初等函数。这是“集中力解 + 叠加”这一套路的典型用法：集中力解像是格林函数，工程上真正有意义的分布荷载解都由它积分或求和而得。

- **边界受任意方向集中力**：在 (7-21) 中取 $\alpha=\pi$ 即可，$\beta$ 自由。
- **边界受切向集中力**：再取 $\beta=\dfrac{\pi}{2}$，得
$$
\sigma_{\rho}=-\frac{2F\sin\varphi}{\pi\rho},\qquad \sigma_{\varphi}=0,\qquad \tau_{\rho\varphi}=\tau_{\varphi\rho}=0\tag{7-28}
$$
- **边界受集中力偶**：在 (7-22) 中取 $\alpha=\pi$，得
$$
\left.\begin{array}{l}
\sigma_{\rho}=\dfrac{2M\sin 2\varphi}{\pi\rho^{2}}\\[6pt]
\sigma_{\varphi}=0\\[6pt]
\tau_{\rho\varphi}=\tau_{\varphi\rho}=\dfrac{M\left(\cos 2\varphi+1\right)}{\pi\rho^{2}}
\end{array}\right\}\tag{7-29}
$$

这几种情形共用同一个特点：**应力状态是纯径向的**（$\sigma_{\varphi}=\tau_{\rho\varphi}=0$），只是径向应力对 $\varphi$ 的依赖不同（$\cos\varphi$、$\sin\varphi$、$\sin 2\varphi$ 等）。所以判断一个解是否属于这一族，看一眼 $\sigma_{\varphi}$ 是否为零即可。

**适用前提**：半平面、线弹性、各向同性、小变形；集中力是理想化荷载，实际荷载须按圣维南原理换算成等效力系后使用；平面应力与平面应变只差 $E,\nu$ 的替换；在 $\rho\to 0$ 处应力无界，该点附近解失效。

## 十一、极坐标与直角坐标的对照：何时换、换了以后哪些东西变了

把全章内容压成一张对照表，比逐条背结论更有用：

| 项目 | 直角坐标 | 极坐标 |
| --- | --- | --- |
| 适配几何 | 矩形、直边、三角形 | 圆、圆环、扇形、半平面 |
| 平衡方程 | 常系数 | 含 $1/\rho$ 与 $(\sigma_\rho-\sigma_\varphi)/\rho$ |
| 边界条件 | 通常要合成面力 | 圆周/径向边上直接等于应力分量 |
| 位移单值性 | 自动满足 | 需显式检验（多值项） |

再看三条贯穿全章的线索：

**（1）方程结构相同，算子不同。** 双调和方程的形式不变，只是拉普拉斯算子换成极坐标形式；协调方程用的是应力不变量 $\sigma_{x}+\sigma_{y}=\sigma_{\rho}+\sigma_{\varphi}$。因此“应力函数 + 双调和方程”这套解法完全平移过来，只有算子需要重写。

**（2）解的“基本积木”固定。** 全章所有应力函数都由少数几块拼成：$A\ln\rho+B\rho^{2}\ln\rho+C\rho^{2}$（轴对称）、$A\rho^{2}+B\rho^{4}+C/\rho^{2}+D$（$\cos2\varphi$ 型）、$A\rho^{3}+B/\rho+C\rho+D\rho\ln\rho$（$\sin\varphi$ 型）、$\rho\varphi\left(C\cos\varphi+D\sin\varphi\right)$（尖劈）、$f(\varphi)$（力偶）。选哪一块，取决于**外载的角度分布**与**量纲对 $\rho$ 幂次的要求**，而不是试凑。

**（3）多值项与奇异性是两个必须交代的“边界”。** 多值项（$\frac{4B\rho\varphi}{E}$、$\frac{2D}{E}\varphi\cos\varphi$ 等）在完整闭合体中被单值性条件否决，在不完整体（带切口、不完整环）中则合法，并且正是描述错缝预应力的工具。奇异性（$\sigma\sim F/\rho$、$M/\rho^{2}$）出现在集中力、集中力偶作用点和尖劈顶点，标志线弹性解在该处失效。

最后把最易错的几处集中列出：

- **忘了平面应变的常数替换**：圆筒位移、曲梁位移、半平面沉陷都要做 $E\to\frac{E}{1-\nu^{2}}$、$\nu\to\frac{\nu}{1-\nu}$；而拉梅应力解与曲梁应力解本身不含 $E,\nu$。
- **把 (7-11) 当通用轴对称公式**：它要求几何与受载都轴对称；曲梁纯弯曲必须保留 $B$ 项。
- **在完整圆环中保留多值位移项**：$B\ne 0$ 或 $D\ne 0$ 时必须检查单值性。
- **漏写 $(\sigma_{\rho}-\sigma_{\varphi})/\rho$**：用静水压力状态可快速自检。
- **把 $K=3$ 当普适值**：它是无限大板、单向拉伸、圆孔、孔边自由这一组前提下的结果。
- **把孔边 $\sigma_{\rho}=0$ 当“不危险”**：危险的是孔边 $\sigma_{\varphi}$。
- **在半平面问题中求“绝对沉陷”**：无基准面时只有相对沉陷 (7-26) 有意义。

至此，本章的逻辑可以一句话概括：**先按边界形状换一套语言，把三大类方程翻译过去；再用“角度因子由载荷定、径向幂次由量纲定”的规则挑选应力函数；最后用边界条件、整体平衡与位移单值性三类约束定常数，并随时交代解在集中力点、尖劈顶点和完整/不完整环之间的适用边界。**