# CEE6501

## 📅 Week 1 — Course Introduction & Software Setup

This week introduces the course structure and establishes the core software tools we will use throughout the semester.

### 📖 Lectures

#### Introduction

Course scope, learning objectives, expectations, and semester structure.

- 📄 **Slides (PDF):** [L1_intro.pdf](Lectures/L1/L1_intro.pdf)
- 📓 **Notebook:** [L1_intro.ipynb](Lectures/L1/L1_intro.ipynb)

#### Git & GitHub Fundamentals

Version control, collaboration workflows, and course repository setup.

- 📄 **Slides (PDF):** [L1_software_git.pdf](Lectures/L1/L1_software_git.pdf)
- 📓 **Notebook:** [L1_software_git.ipynb](Lectures/L1/L1_software_git.ipynb)

#### Python & Conda Environment Setup

Setup of Python and Conda environments and introduction to the core computational tools used in the course.

- 📄 **Slides (PDF):** [L1_software_python.pdf](Lectures/L1/L1_software_python.pdf)
- 📓 **Notebook:** [L1_software_python.ipynb](Lectures/L1/L1_software_python.ipynb)

#### VS Code Setup

Configuration of VS Code for Python development, Jupyter notebooks, and course workflows.

- 📄 **Slides (PDF):** [L1_software_VScode.pdf](Lectures/L1/L1_software_VScode.pdf)
- 📓 **Notebook:** [L1_software_VScode.ipynb](Lectures/L1/L1_software_VScode.ipynb)

### Extra In-Class Code

- [L1_JupyterTest.ipynb](Code/L1/L1_JupyterTest.ipynb)
  [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Bruun-Automation-Research-Lab/CEE6501/blob/main/Code/L1/L1_JupyterTest.ipynb)

### 📝 Assignments

**How to Complete Assignments:** [L1_assignments.pdf](Lectures/L1/L1_assignments.pdf)

#### Submission File Naming

Please use the following naming formats:

- **Written:** `StudentName_A#_written.pdf`
- **Coding (Colab / Jupyter):** `StudentName_A#_code.ipynb`

#### Assignment Files

- ✍️ **Written Assignment:** [A1_written.md](Assignments/A1_written.md)
- 💻 **Coding Assignment:** [A1_code.ipynb](Assignments/A1_code.ipynb)
  [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Bruun-Automation-Research-Lab/CEE6501/blob/main/Assignments/A1_code.ipynb)

---

---

## 📅 Week 2 — Matrix Operations & Linear Systems

This week introduces matrices as fundamental mathematical objects and develops the core tools required to work with
linear systems of equations. We focus on matrix notation and operations, the interpretation of matrices as linear
mappings, and the logical structure of solving linear systems, progressing from conceptual understanding to practical
computational implementation in Python.

Emphasis is placed on how matrix properties influence solution strategies and why factorization-based solvers form the
foundation of efficient numerical computation.

Kassimali – Chapter 2; additional discussion of Cholesky factorization in §9.9 (not used for the lecture)  
McGuire – Chapter 11, §11.1–11.3

### 📖 Lectures

#### Matrix Representation and Operations

This lecture introduces matrices as linear mappings, covering notation, indexing, matrix–vector products, and
fundamental matrix operations used throughout structural analysis.

- 📄 **Slides (PDF):** [L2_1_matrices.pdf](Lectures/L2/L2_1_matrices.pdf)
- 📓 **Notebook:** [L2_1_matrices.ipynb](Lectures/L2/L2_1_matrices.ipynb)

#### Linear System Solution Methods

This lecture develops direct and iterative methods for solving linear systems, emphasizing elimination, factorization,
and solver efficiency for large-scale engineering problems.

- 📄 **Slides (PDF):** [L2_2_solvers.pdf](Lectures/L2/L2_2_solvers.pdf)
- 📓 **Notebook:** [L2_2_solvers.ipynb](Lectures/L2/L2_2_solvers.ipynb)

### Extra In-Class Code

- [L2_OperationCount.ipynb](Code/L2/L2_OperationCount.ipynb)
  [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Bruun-Automation-Research-Lab/CEE6501/blob/main/Code/L2/L2_OperationCount.ipynb)
- [L2_IterationPractice.ipynb](Code/L2/L2_IterationPractice.ipynb)
  [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Bruun-Automation-Research-Lab/CEE6501/blob/main/Code/L2/L2_IterationPractice.ipynb)

### 📝 Assignments

Use standard submission naming from Week 1.

#### Assignment Files

- ✍️ **Written Assignment:** [A2_written.md](Assignments/A2_written.md)
- 💻 **Coding Assignment:** [A2_code.ipynb](Assignments/A2_code.ipynb)
  [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Bruun-Automation-Research-Lab/CEE6501/blob/main/Assignments/A2_code.ipynb)

---

---

## 📅 Week 3 — Direct Stiffness Method (Trusses)

This week introduces the **Direct Stiffness Method (DSM)** for plane trusses. We begin by deriving the **local
behavior** of an axial truss member from first principles and then extend these concepts to **global truss analysis**.
Topics include coordinate transformations between local and global systems, manual assembly of the global stiffness
matrix for the free nodes of the structure based on equilibrium and compatibility-based formulation.

Kassimali – Chapter 3, §3.1–3.7; additional discussion of Cholesky factorization in §9.9 (not used in the lecture)  
McGuire – Chapter 2, §2.3–2.4

### 📖 Lectures

#### Part 1 — Local Behavior of an Axial Element

This lecture builds the axial bar element from first principles: truss DOFs and sign conventions, local vs global
coordinates, axial kinematics and statics, the $2 \times 2$ local stiffness matrix, a brief preview of flexibility, and
the local $4 \times 4$ element stiffness form (local-only; not yet transformed).

- 📄 **Slides (PDF):** [L3_1_AxialElement.pdf](Lectures/L3/L3_1_AxialElement.pdf)
- 📓 **Notebook:** [L3_1_AxialElement.ipynb](Lectures/L3/L3_1_AxialElement.ipynb)

#### Part 2 — The Direct Stiffness Method (DSM) for Trusses I

This lecture begins to develop the full DSM workflow for trusses: local-to-global transformations using direction
cosines, deriving the global element stiffness $[k]_g = [T]^T [k'] [T]$, and manually assembling the global stiffness
matrix of the structure to solve the unknown joint displacements.

- 📄 **Slides (PDF):** [L3_2_Trusses.pdf](Lectures/L3/L3_2_Trusses.pdf)
- 📓 **Notebook:** [L3_2_Trusses.ipynb](Lectures/L3/L3_2_Trusses.ipynb)

### Extra In-Class Code

- [L3_1_exercise_BLANK.ipynb](Code/L3/L3_1_exercise_BLANK.ipynb)
  [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Bruun-Automation-Research-Lab/CEE6501/blob/main/Code/L3/L3_1_exercise_BLANK.ipynb)
- [L3_1_exercise_SOLVED.ipynb](Code/L3/L3_1_exercise_SOLVED.ipynb)
  [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Bruun-Automation-Research-Lab/CEE6501/blob/main/Code/L3/L3_1_exercise_SOLVED.ipynb)

### 📝 Assignments

Use standard submission naming from Week 1.

#### Assignment Files

- ✍️ **Written Assignment:** [A3_written.md](Assignments/A3_written.md)
- 💻 **Coding Assignment:** [A3_code.ipynb](Assignments/A3_code.ipynb)
  [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Bruun-Automation-Research-Lab/CEE6501/blob/main/Assignments/A3_code.ipynb)

---

---

## 📅 Week 4 — Direct Stiffness Method (Trusses)

This week continues the **Direct Stiffness Method (DSM)** for plane trusses, completing the full analysis workflow
introduced in Week 3. We move from element-level formulations to **system-level solution**, focusing on efficient
assembly of the global stiffness matrix, the mathematical implications of supports and constraints, and the
post-processing steps required to recover member forces and reactions.

Kassimali – Chapter 3, §3.7; additional discussion of bandedness in §9.9  
McGuire – Chapter 3, §3.2–3.4 and §11.4 (sparseness)

### 📖 Lectures

#### Part 1 — The Direct Stiffness Method (DSM) for Trusses II

This lecture completes the DSM truss workflow introduced in Week 3. We briefly review the manual construction of the
global stiffness matrix based on compatibility and force equilibrium, and then formalize the Direct Stiffness Method:
scatter–add assembly of the global stiffness matrix, enforcement of boundary conditions, solution for unknown joint
displacements and support reactions, and recovery of member axial forces.

- 📄 **Slides (PDF):** [L4_1_Trusses.pdf](Lectures/L4/L4_1_Trusses.pdf)
- 📓 **Notebook:** [L4_1_Trusses.ipynb](Lectures/L4/L4_1_Trusses.ipynb)

#### Part 2 — Implementing the DSM for Plane Trusses in Python

This lecture implements the full DSM workflow in Python. We translate the manual procedure into a clear, reusable
software structure: data definitions (nodes, elements, DOF maps), element stiffness computation, scatter–add assembly
into global arrays, application of boundary conditions via partitioning, solution for displacements and reactions, and
post-processing for element force recovery. The emphasis is on building a larger, readable piece of analysis software by
implementing each DSM step explicitly and validating intermediate results along the way.

- 📄 **Slides (PDF):** [L4_2_Implementation.pdf](Lectures/L4/L4_2_Implementation.pdf)
- 📓 **Notebook:** [L4_2_Implementation.ipynb](Lectures/L4/L4_2_Implementation.ipynb)

#### Part 3 — Matrix Sparsity and Bandwidth (Extra Topic)

This lecture explores computational and modeling extensions to the DSM, including **sparsity and bandwidth of the
stiffness matrix**, the impact of DOF ordering on solver performance

- 📄 **Slides (PDF):** [L4_3_SparsityBandwidth.pdf](Lectures/L4/L4_3_SparsityBandwidth.pdf)
- 📓 **Notebook:** [L4_3_SparsityBandwidth.ipynb](Lectures/L4/L4_3_SparsityBandwidth.ipynb)

### Extra In-Class Code

- [banded_demo.ipynb](Code/L4/banded_demo.ipynb)
  [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Bruun-Automation-Research-Lab/CEE6501/blob/main/Code/L4/banded_demo.ipynb)

### 📝 Assignments

#### Submission File Naming

Use standard submission naming from Week 1.

#### Assignment Files

No Assignment this week, study for the midterm.

---

---

## 📅 Week 5 — Midterm and DSM for Space Trusses

McGuire - Chapter 5, §5.1 (3D coordinate transform)

### 📖 Lectures

This week includes an in-class midterm examination (~2.0 hours).

#### Part 1 — Space Trusses

A brief preview of extending the Direct Stiffness Method (DSM) framework to 3D truss systems, in preparation for the
upcoming assignment where this extension will be implemented computationally.

- 📄 **Slides (PDF):** [L5_1_SpaceTrusses.pdf](Lectures/L5/L5_1_SpaceTrusses.pdf)
- 📓 **Notebook:** [L5_1_SpaceTrusses.ipynb](Lectures/L5/L5_1_SpaceTrusses.ipynb)

### Extra In-Class Code

N/A

### 📝 Assignments

Use standard submission naming from Week 1.

#### Assignment Files

- ✍️ **Written Assignment:** [A5_written.md](Assignments/A5_written.md)
- 💻 **Coding Assignment:**

  [A5_code_2D.ipynb](Assignments/A5_code_2D.ipynb)
  [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Bruun-Automation-Research-Lab/CEE6501/blob/main/Assignments/A5_code_2D.ipynb)

  [A5_code_3D.ipynb](Assignments/A5_code_3D.ipynb)
  [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Bruun-Automation-Research-Lab/CEE6501/blob/main/Assignments/A5_code_3D.ipynb)

---

---

## 📅 Week 6 — Direct Stiffness Method (Beams)

This week extends the Direct Stiffness Method to beam elements, introducing bending behavior, rotational degrees of
freedom, and member loading. We move from the beam idealization and DOF definitions, to deriving the element stiffness
matrix, and finally to handling distributed loads using fixed-end forces within the global system.

Kassimali – Chapter 5, §5.1-5.2, 5.4-5.7

McGuire – Chapter 4, §4.1, 4.5 ; Chapter 5, §5.2 (FEFs), 5.3 (Self-Straining, next year)

### 📖 Lectures

#### Part 1 — Introduction to 2D Beam Analysis

Introduces the Euler–Bernoulli beam model within the DSM framework. We define beam DOFs, establish sign conventions,
distinguish joint vs member loads, and set up the global system $\mathbf{K}\mathbf{u}=\mathbf{f}$.

- 📄 **Slides (PDF):** [L6_1_Beams.pdf](Lectures/L6/L6_1_Beams.pdf)
- 📓 **Notebook:** [L6_1_Beams.ipynb](Lectures/L6/L6_1_Beams.ipynb)

#### Part 2 — 2D Beam Element Stiffness Matrix

Develops the 4×4 beam element stiffness matrix using the unit displacement method. The lecture builds physical intuition
for the stiffness coefficients and shows how beam elements are assembled into the global system.

- 📄 **Slides (PDF):** [L6_2_PlaneFrames.pdf](Lectures/L6/L6_2_Beams_Stiffness.pdf)
- 📓 **Notebook:** [L6_2_PlaneFrames.ipynb](Lectures/L6/L6_2_Beams_Stiffness.ipynb)

#### Part 3 — Fixed End Forces (FEFs)

Introduces fixed-end forces for handling member loading. We show how beam problems can be decomposed using
superposition, convert distributed loads into equivalent nodal forces, and incorporate FEFs into the global DSM
equations.

- 📄 **Slides (PDF):** [L6_3_FEFs.pdf](Lectures/L6/L6_3_FEFs.pdf)
- 📓 **Notebook:** [L6_3_FEFs.ipynb](Lectures/L6/L6_3_FEFs.ipynb)

### Extra In-Class Code

N/A

### 📝 Assignments

Use standard submission naming from Week 1.

#### Assignment Files

N/A, 3D Truss Coding Assignment to be completed this week

---

---

## 📅 Week 7 — Direct Stiffness Method (Frames)

This week extends the **Direct Stiffness Method (DSM)** to **2D frame elements**, combining axial and bending behavior
within a single unified formulation. We build on last week’s beam theory and reintroduce axial deformation to develop
the full 6×6 frame element stiffness matrix. Emphasis is placed on **local–global transformations**, consistent
notation, and systematic assembly of complete frame systems.

Kassimali – Chapter 6, §6.1–6.5

McGuire – Chapter 4, §4.1, 4.5 ; Chapter 5, §5.1 (3D Coordinate Transformations)

### 📖 Lectures

#### Part 1 — Introduction to 2D Frame Analysis

Introduces the **plane frame element** in local coordinates. We define the six element DOFs, combine axial and flexural
stiffness contributions, and derive the full 6×6 local stiffness matrix.

- 📄 **Slides (PDF):** [L7_1_FramesLocal.pdf](Lectures/L7/L7_1_FramesLocal.pdf)
- 📓 **Notebook:** [L7_1_FramesLocal.ipynb](Lectures/L7/L7_1_FramesLocal.ipynb)

#### Part 2 — Global Formulation for 2D Frame Analysis

Develops the **coordinate transformation matrix** and shows how element stiffness matrices are mapped from local to
global coordinates. We assemble multi-member frame systems and construct the global equilibrium equations for complete
2D frame problems.

- 📄 **Slides (PDF):** [L7_2_FramesGlobal.pdf](Lectures/L7/L7_2_FramesGlobal.pdf)
- 📓 **Notebook:** [L7_2_FramesGlobal.ipynb](Lectures/L7/L7_2_FramesGlobal.ipynb)

#### Part 3 — Miscellaneous Extra Topics

Covers a set of practical and course-related topics. We review this week’s homework expectations, discuss how to prepare
clear and well-structured Markdown writeups for submitted assignments, and go over key takeaways from the midterm exam.
We also summarize and reflect on midterm course feedback, highlighting adjustments and clarifications moving forward.

- 📄 **Slides (PDF):** [L7_3_Extra.pdf](Lectures/L7/L7_3_Extra.pdf)
- 📓 **Notebook:** [L7_3_Extra.ipynb](Lectures/L7/L7_3_Extra.ipynb)

### Extra In-Class Code

- [InClass_LocalFrame.ipynb](Code/L7/InClass_LocalFrame.ipynb)
  [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Bruun-Automation-Research-Lab/CEE6501/blob/main/Code/L7/InClass_LocalFrame.ipynb)
- [Example_SolutionPresentation.md](Code/L7/Example_SolutionPresentation.md)

### 📝 Assignments

Use standard submission naming from Week 1.

#### Assignment Files

- ✍️ **Written Assignment:** [A7_written.md](Assignments/A7_written.md)
- 💻 **Coding Assignment:**

  [A7_code.ipynb](Assignments/A7_code.ipynb)
  [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Bruun-Automation-Research-Lab/CEE6501/blob/main/Assignments/A7_code.ipynb)

---

---

## 📅 Week 8 — Member Releases and Support Settlement

This week extends the Direct Stiffness Method (DSM) to handle two important practical modeling features: **member
releases** and **support settlements**. We examine how hinges modify the stiffness relationships in frame elements, and
how **prescribed support displacements** can be incorporated into the standard DSM formulation.

Kassimali – Chapter 7, §7.1

### 📖 Lectures

#### Part 1 — Member Releases

This lecture introduces **moment releases and hinged joints** in frame structures (can be extended to beams as well). We
discuss how releases affect element stiffness, how they are represented in the global system, and how fictitious
restraints can be used to stabilize the formulation when rotational stiffness is removed.

- 📄 **Slides (PDF):** [L8_1_FramesReleases.pdf](Lectures/L8/L8_1_FramesReleases.pdf)
- 📓 **Notebook:** [L8_1_FramesReleases.ipynb](Lectures/L8/L8_1_FramesReleases.ipynb)

#### Part 2 — N/A

Shorter lecture since CEE graduate student visitation day

### Extra In-Class Code

- [InClass_Exercise.ipynb](Code/L8/InClass_Exercise.ipynb)

### 📝 Assignments

Use standard submission naming from Week 1.

#### Assignment Files

- ✍️ **Written Assignment:** [A8_written.md](Assignments/A8_written.md)
- 💻 **Coding Assignment:**

  [A8_code.ipynb](Assignments/A8_code.ipynb)  
  [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Bruun-Automation-Research-Lab/CEE6501/blob/main/Assignments/A8_code.ipynb)

---

---

## 📅 Week 9 — Support Settlement, Temperature & Fit-up Forces

This week, we extend the Direct Stiffness Method (DSM) to handle several important sources of internal force that arise.
We study **prescribed support displacement**, **temperature-induced actions**, and **fabrication / fit-up errors**, and
show how each can be incorporated into the DSM workflow. We also wrap up with information and review material for
Midterm #2.

Kassimali – Chapter 7, §7.3 & 7.5

### 📖 Lectures

#### Part 1 — Support Settlement

This lecture introduces **support settlements and other prescribed displacements** within the DSM framework. We derive
the modified equilibrium equations and show how prescribed displacements enter the system naturally through the
partitioned stiffness equations, without introducing fixed-end forces or requiring the additional element-level force
manipulations used for member loads, thermal effects, or fabrication errors. For consistency with the fixed-end-force
terms used in those other cases, one can also view this contribution as an equivalent load acting on the free degrees of
freedom.

- 📄 **Slides (PDF):** [L9_1_SupportSettlement.pdf](Lectures/L9/L9_1_SupportSettlement.pdf)
- 📓 **Notebook:** [L9_1_SupportSettlement.ipynb](Lectures/L9/L9_1_SupportSettlement.ipynb)

#### Part 2 — Temperature & Fit-up Forces

This lecture introduces **temperature effects and fabrication / fit-up errors** in structural analysis. We show how
uniform temperature changes, temperature gradients, and initial fabrication errors create member deformations that are
restrained by the structure, leading to **fixed-end forces** and equivalent nodal load terms. These effects are then
incorporated into the DSM in exactly the same way as other element-level force contributions.

- 📄 **Slides (PDF):** [L9_2_Temp_and_Fab.pdf](Lectures/L9/L9_2_Temp_and_Fab.pdf)
- 📓 **Notebook:** [L9_2_Temp_and_Fab.ipynb](Lectures/L9/L9_2_Temp_and_Fab.ipynb)

#### Part 3 — Midterm #2 Information

Slides providing details about **Midterm #2**, including topic coverage, exam format, and key concepts to review. It is
intended to help you organize your studying and connect the major ideas from the recent beam and frame lectures,
including member loads, releases, support settlements, and temperature / fabrication effects.

- 📄 **Slides (PDF):** [L9_3_InfoMidterm.pdf](Lectures/L9/L9_3_InfoMidterm.pdf)
- 📓 **Notebook:** [L9_3_InfoMidterm.ipynb](Lectures/L9/L9_3_InfoMidterm.ipynb)

### Extra In-Class Code

- [InClass_Exercise.ipynb](Code/L9/InClass_Exercise.ipynb)

### 📝 Assignments

No Assignment this week, study for the 2nd midterm.

---

---

## 📅 Week 10 — Midterm and Direct Stiffness Method for 3D Frames

McGuire – Chapter 4 §4.5.2 (torsion beam); Chapter 5, §5.1 (3D coordinate transform)

Kassimali – Chapter 8 §8.2 (torsion), 8.3 (space frame)

### 📖 Lectures

This week includes an in-class midterm examination (~2.0 hours) and finishing up the linear portion of the course with
3D frame elements.

#### Part 1 — 3D Frames

A brief preview of extending the Direct Stiffness Method (DSM) framework to 3D frame systems, in preparation for the
upcoming course project, which will be based on implementing it.

- 📄 **Slides (PDF):** [L10_1_Frames3D.pdf](Lectures/L10/L10_1_Frames3D.pdf)
- 📓 **Notebook:** [L10_1_Frames3D.ipynb](Lectures/L10/L10_1_Frames3D.ipynb)

### 📝 Assignments

Use standard submission naming from Week 1.

#### Assignment Files

- ✍️ **Written Assignment:** [A10_written.md](Assignments/A10_written.md)
- 💻 **Coding Assignment:**

  [A10_code.ipynb](Assignments/A10_code.ipynb)  
  [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Bruun-Automation-Research-Lab/CEE6501/blob/main/Assignments/A10_code.ipynb)

---

---

## 📅 Week 11 — Direct Stiffness Method for Geometric Nonlinearity

McGuire – Chapter 8 §8.1.1 and 8.1.2

Kassimali – Chapter 10

### 📖 Lectures

This week includes

#### Part 1 —

A brief

- 📄 **Slides (PDF):** [L10_1_Frames3D.pdf](Lectures/L10/L10_1_Frames3D.pdf)
- 📓 **Notebook:** [L10_1_Frames3D.ipynb](Lectures/L10/L10_1_Frames3D.ipynb)

### 📝 Assignments

Use standard submission naming from Week 1.

#### Assignment Files

- ✍️ **Written Assignment:** [A10_written.md](Assignments/A10_written.md)
- 💻 **Coding Assignment:**

  [A10_code.ipynb](Assignments/A10_code.ipynb)  
  [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Bruun-Automation-Research-Lab/CEE6501/blob/main/Assignments/A10_code.ipynb)

---

---

## Creating Slides from Notebook

### command to convert notebook to presentation with hidden code

```bash
jupyter nbconvert --to slides --no-input presentation.ipynb
```

```bash
jupyter nbconvert --to slides presentation.ipynb
```

For html file to automatically open

```bash
jupyter nbconvert --to slides presentation.ipynb --post serve
```

## Generate HTML and PDF Slides from the Notebook

Before proceeding, ensure that the required **VS Code tasks and keybindings** are configured in the `.vscode/` folder.

To run the full slide export pipeline  
(**`ipynb → HTML → PDF`**, using the third task), use the following shortcuts:

- **macOS:** `Cmd + Shift + R`
- **Windows:** `Ctrl + Alt + R`
