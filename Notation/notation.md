# 📘 Direct Stiffness Method — Notation Convention

To maintain consistency throughout the course, we adopt the following rules.

These need to be implemented consistently across lectures

---

`##` headings should be each word capitalized

`###` headings should be lowercase

Use `\mathbf{}` for bold

---

## 🔹 1. General Rules

- **Vectors** → bold lowercase
- **Matrices** → bold uppercase
- **Element stiffness matrices** → lowercase $ \mathbf{k} $
- **Assembled global stiffness matrix** → uppercase $ \mathbf{K} $

---

## 🔹 2. Subscripts and Superscripts

- Subscript $ i $ → element index
- Subscript $ l $ → local coordinate system
- Subscript $ g $ → global coordinate system (element level)
- No subscript → assembled global system
- Superscript $ F $ → fixed-end force

---

## 🔹 3. Local Element Equation (Element $ i $)

$$
\mathbf{q}_i = \mathbf{k}_{l,i} \mathbf{v}_i + \mathbf{q}_i^{\,F}
$$

Where:

- $\mathbf{v}_i$ = local element DOFs
- $\mathbf{q}_{i}$ = local element end forces
- $\mathbf{k}_{l,i}$ = local element stiffness matrix
- $\mathbf{q}_i^{\,F}$ = local fixed-end force vector

---

## 🔹 4. Global Element Equation (Element $ i $)

$$
\mathbf{f}_i = \mathbf{k}_{g,i} \mathbf{u}_i + \mathbf{f}_i^{\,F}
$$

Where:

- $\mathbf{u}_i$ = element DOFs in global coordinates
- $\mathbf{f}_i$ = element nodal forces in global coordinates
- $\mathbf{k}_{g,i} = \mathbf{T}_i^T \mathbf{k}_{l,i} \mathbf{T}_i$
- $\mathbf{f}_i^{\,F} = \mathbf{T}_i^T \mathbf{q}_i^{\,F}$

---

## 🔹 5. Global Assembled System

$$
\mathbf{f} = \mathbf{K}\mathbf{u} + \mathbf{f}^{\,F}
$$

Where:

- $ \mathbf{u} $ = global displacement vector
- $ \mathbf{f} $ = global nodal force vector
- $ \mathbf{K} $ = assembled global stiffness matrix
- $ \mathbf{f}^{F} $ = assembled global fixed-end forces

---

## 🔹 6. Partitioned Notation

$$
\begin{bmatrix}
\mathbf{K}_{ff} & \mathbf{K}_{fr} \\
\mathbf{K}_{rf} & \mathbf{K}_{rr}
\end{bmatrix}
\begin{bmatrix}
\mathbf{u}_f \\
\mathbf{u}_r
\end{bmatrix}
= \begin{bmatrix}
\mathbf{f}_f \\
\mathbf{f}_r
\end{bmatrix}
$$

---

## 🔹 7. Geometric Nonlinearity

Residual:

$$
\mathbf{r} = \mathbf{f}_f - \mathbf{f}_{f,int}
$$

Residual, iterations:

$$
\mathbf{r}^{(i)} = \mathbf{f}_f - \mathbf{f}_{f,int}^{(i)}
$$

Displacement iteration:

$$
\Delta\mathbf{u}_f^{(i)} = \mathbf{K}_{ff}^{(i)-1} \mathbf{r}^{(i)}
$$

$$
\mathbf{u}_f^{(i+1)} = \mathbf{u}_f^{(i)} + \Delta\mathbf{u}_f^{(i)}
$$

---

## 🔹 6. Summary Table

| Level          | Displacements  | Forces         | Stiffness          |
| -------------- | -------------- | -------------- | ------------------ |
| Local element  | $\mathbf{v}_i$ | $\mathbf{q}_i$ | $\mathbf{k}_{l,i}$ |
| Global element | $\mathbf{u}_i$ | $\mathbf{f}_i$ | $\mathbf{k}_{g,i}$ |
| Global system  | $\mathbf{u}$   | $\mathbf{f}$   | $\mathbf{K}$       |

---

This convention:

- Avoids stacked superscripts
- Keeps vectors lowercase and matrices uppercase
- Clearly separates element-level and assembled quantities
- Scales cleanly to 2D trusses, beams, frames, and 3D systems

---

## 🔹 7. Fixed-End Force (FEF) Convention

Refer to nodes as b = beginning, e = end

Fixed-end forces represent element end forces caused by element loading **with all element DOFs restrained**.

They appear as additive force terms in all stiffness equations.

$$
\mathbf{v}_i =
\begin{bmatrix}
v_1 \\[4pt]
v_2 \\[4pt]
v_3 \\[4pt]
v_4 \\[4pt]
v_5 \\[4pt]
v_6
\end{bmatrix}
=\begin{bmatrix}
v_{x,b} \\[4pt]
v_{y,b} \\[4pt]
v_{\theta,b} \\[4pt]
v_{x,e} \\[4pt]
v_{y,e} \\[4pt]
v_{\theta,e}
\end{bmatrix}
$$

### FEFs do to Member Loading

$F$ superscript indicates FEFs due to temperature change.

Assume the begin node is $b$ and the end node is $e$.

$$
\mathbf{q}_i^{F} =
\begin{bmatrix}
q_1^{F} \\[4pt]
q_2^{F} \\[4pt]
q_3^{F} \\[4pt]
q_4^{F} \\[4pt]
q_5^{F} \\[4pt]
q_6^{F}
\end{bmatrix}
=\begin{bmatrix}
q_{x,b}^{F} \\[4pt]
q_{y,b}^{F} \\[4pt]
q_{m,b}^{F} \\[4pt]
q_{x,e}^{F} \\[4pt]
q_{y,e}^{F} \\[4pt]
q_{m,e}^{F}
\end{bmatrix}
=\begin{bmatrix}
N_b^{F} \\[4pt]
V_b^{F} \\[4pt]
M_b^{F} \\[4pt]
N_e^{F} \\[4pt]
V_e^{F} \\[4pt]
M_e^{F}
\end{bmatrix}
$$

### FEFs Due to Temperature

$H$ superscript indicates FEFs due to temperature change.

Assume the begin node is $b$ and the end node is $e$.

$$
\mathbf{q}^{H} =
\begin{bmatrix}
q_1^{H} \\[4pt]
q_2^{H} \\[4pt]
q_3^{H} \\[4pt]
q_4^{H} \\[4pt]
q_5^{H} \\[4pt]
q_6^{H}
\end{bmatrix}
=\begin{bmatrix}
q_{x,b}^{H} \\[4pt]
q_{y,b}^{H} \\[4pt]
q_{m,b}^{H} \\[4pt]
q_{x,e}^{H} \\[4pt]
q_{y,e}^{H} \\[4pt]
q_{m,e}^{H}
\end{bmatrix}
=\begin{bmatrix}
N_b^{H} \\[4pt]
V_b^{H} \\[4pt]
M_b^{H} \\[4pt]
N_e^{H} \\[4pt]
V_e^{H} \\[4pt]
M_e^{H}
\end{bmatrix}
$$

### FEFs Due to Fabrication Error (Initial Strain)

$E$ superscript indicates FEFs due to temperature change.

Assume the begin node is $b$ and the end node is $e$.

$$
\mathbf{q}_i^{E} =
\begin{bmatrix}
q_1^{E} \\[4pt]
q_2^{E} \\[4pt]
q_3^{E} \\[4pt]
q_4^{E} \\[4pt]
q_5^{E} \\[4pt]
q_6^{E}
\end{bmatrix}
=\begin{bmatrix}
q_{x,b}^{E} \\[4pt]
q_{y,b}^{E} \\[4pt]
q_{m,b}^{E} \\[4pt]
q_{x,e}^{E} \\[4pt]
q_{y,e}^{E} \\[4pt]
q_{m,e}^{E}
\end{bmatrix}
=\begin{bmatrix}
N_b^{E} \\[4pt]
V_b^{E} \\[4pt]
M_b^{E} \\[4pt]
N_e^{E} \\[4pt]
V_e^{E} \\[4pt]
M_e^{E}
\end{bmatrix}
$$
