# CEE6501

## 📅 Week 1 — Course Introduction & Software Setup

This week introduces the course structure and establishes the core software tools we will use throughout the semester.

### 📖 Lectures

#### Introduction

Course scope, learning objectives, expectations, and semester structure.

- 🌐 **Slides (HTML):** [L1_intro.slides.html](Lectures/L1/L1_intro.slides.html)
- 📄 **Slides (PDF):** [L1_intro.pdf](Lectures/L1/L1_intro.pdf)
- 📓 **Notebook:** [L1_intro.ipynb](Lectures/L1/L1_intro.ipynb)

#### Git & GitHub Fundamentals

Version control, collaboration workflows, and course repository setup.

- 🌐 **Slides (HTML):** [L1_software_git.slides.html](Lectures/L1/L1_software_git.slides.html)
- 📄 **Slides (PDF):** [L1_software_git.pdf](Lectures/L1/L1_software_git.pdf)
- 📓 **Notebook:** [L1_software_git.ipynb](Lectures/L1/L1_software_git.ipynb)

#### Python & Conda Environment Setup

Setup of Python and Conda environments and introduction to the core computational tools used in the course.

- 🌐 **Slides (HTML):** [L1_software_python.slides.html](Lectures/L1/L1_software_python.slides.html)
- 📄 **Slides (PDF):** [L1_software_python.pdf](Lectures/L1/L1_software_python.pdf)
- 📓 **Notebook:** [L1_software_python.ipynb](Lectures/L1/L1_software_python.ipynb)

#### VScode Setup

Configuration of VS Code for Python development, Jupyter notebooks, and course workflows.

- 🌐 **Slides (HTML):** [L1_software_VScode.slides.html](Lectures/L1/L1_software_VScode.slides.html)
- 📄 **Slides (PDF):** [L1_software_VScode.pdf](Lectures/L1/L1_software_VScode.pdf)
- 📓 **Notebook:** [L1_software_VScode.ipynb](Lectures/L1/L1_software_VScode.ipynb)
- **Extra Code:** [L1_JupyterTest.ipynb](Code/L1/L1_JupyterTest.ipynb)
  [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Bruun-Automation-Research-Lab/CEE6501/blob/main/Code/L1/L1_JupyterTest.ipynb)

### 📝 Assignments

**How to Complete Assignements:** [L1_assignments.pdf](Lectures/L1/L1_assignments.pdf)

- ✍️ **Written Assignment:** [A1_written.md](Assignments/A1_written.md)
- 💻 **Coding Assignment:**
  [A1_code.ipynb](Assignments/A1_code.ipynb)[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Bruun-Automation-Research-Lab/CEE6501/blob/main/Assignments/A1_code.ipynb)

---

---

## 📅 Week 2 — Matrix Operations & Linear Systems

This week introduces matrices as fundamental mathematical objects and develops the core tools needed to work with linear
systems. We focus on matrix notation, operations, and the logic of solving systems of equations, progressing from
conceptual understanding to practical computational implementation in Python.

Students will learn how matrices represent linear mappings, how matrix properties influence solution strategies, and why
factorization-based solvers are central to numerical computation.

### 📖 Lectures

#### Matrix Representation and Operations

This lecture introduces matrices as linear mappings, covering notation, indexing, matrix–vector products, and
fundamental matrix operations used throughout structural analysis.

- 🌐 **Slides (HTML):** [L2_1_matrices.slides.html](Lectures/L2/L2_1_matrices.slides.html)
- 📄 **Slides (PDF):** [L2_1_matrices.pdf](Lectures/L2/L2_1_matrices.pdf)
- 📓 **Notebook:** [L2_1_matrices.ipynb](Lectures/L2/L2_1_matrices.ipynb)

#### Linear System Solution Methods

This lecture develops direct and iterative methods for solving linear systems, emphasizing elimination, factorization,
and solver efficiency for large-scale engineering problems.

- 🌐 **Slides (HTML):** [L2_2_solvers.slides.html](Lectures/L2/L2_2_solvers.slides.html)
- 📄 **Slides (PDF):** [L2_2_solvers.pdf](Lectures/L2/L2_2_solvers.pdf)
- 📓 **Notebook:** [L2_2_solvers.ipynb](Lectures/L2/L2_2_solvers.ipynb)

### Extra In-Class Code

- [L2_OperationCount.ipynb](Code/L2/L2_OperationCount.ipynb)
  [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Bruun-Automation-Research-Lab/CEE6501/blob/main/Code/L2/L2_OperationCount.ipynb)
- [L2_IterationPractice.ipynb](Code/L2/L2_IterationPractice.ipynb)
  [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Bruun-Automation-Research-Lab/CEE6501/blob/main/Code/L2/L2_IterationPractice.ipynb)

### 📝 Assignments

See Lecture 1 for how to complete assignments guide.

- ✍️ **Written Assignment:** [A2_written.md](Assignments/A2_written.md)
- 💻 **Coding Assignment:**
  [A2_code.ipynb](Assignments/A2_code.ipynb)[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Bruun-Automation-Research-Lab/CEE6501/blob/main/Assignments/A2_code.ipynb)

---

---

## 📅 Week 3 — Direct Stiffness Method I (Trusses)

This week introduces the **Direct Stiffness Method (DSM)** for planar trusses. We begin by developing the **local
behavior** of a single axial member and then extend those ideas to **global truss analysis**, including coordinate
transformations, stiffness assembly, boundary conditions, and recovery of member forces.

### 📖 Lectures

#### Part 1 — Local Behavior of an Axial Element

This lecture builds the axial bar element from first principles: truss DOFs and sign conventions, local vs global
coordinates, axial kinematics and statics, the $2 \times 2$ local stiffness matrix, a brief preview of flexibility, and
the local $4 \times 4$ element stiffness form (local-only; not yet transformed).

- 🌐 **Slides (HTML):** [L3_1_AxialElement.slides.html](Lectures/L3/L3_1_AxialElement.slides.html)
- 📄 **Slides (PDF):** [L3_1_AxialElement.pdf](Lectures/L3/L3_1_AxialElement.pdf)
- 📓 **Notebook:** [L3_1_AxialElement.ipynb](Lectures/L3/L3_1_AxialElement.ipynb)

#### Part 2 — The Direct Stiffness Method (DSM) for Trusses

This lecture begins to develop the full DSM workflow for trusses: local-to-global transformations using direction
cosines, deriving the global element stiffness $[k]_g = [T]^T [k'] [T]$, and manually assemblying the global stiffness
matrix of the structure to solve the unknown joint displacements.

- 🌐 **Slides (HTML):** [L3_2_Trusses.slides.html](Lectures/L3/L3_2_Trusses.slides.html)
- 📄 **Slides (PDF):** [L3_2_Trusses.pdf](Lectures/L3/L3_2_Trusses.pdf)
- 📓 **Notebook:** [L3_2_Trusses.ipynb](Lectures/L3/L3_2_Trusses.ipynb)

### Extra In-Class Code

- [L3_1_exercise_BLANK.ipynb](Code/L3/L3_1_exercise_BLANK.ipynb)
  [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Bruun-Automation-Research-Lab/CEE6501/blob/main/Code/L3/L3_1_exercise_BLANK.ipynb)
- [L3_1_exercise_SOLVED.ipynb](Code/L3/L3_1_exercise_SOLVED.ipynb)
  [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Bruun-Automation-Research-Lab/CEE6501/blob/main/Code/L3/L3_1_exercise_SOLVED.ipynb)

### 📝 Assignments

See Lecture 1 for how to complete assignments guide.

- ✍️ **Written Assignment:** [A3_written.md](Assignments/A3_written.md)
- 💻 **Coding Assignment:**
  [A3_code.ipynb](Assignments/A3_code.ipynb)[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Bruun-Automation-Research-Lab/CEE6501/blob/main/Assignments/A3_code.ipynb)

---

---

## 📅 Week 4 — Direct Stiffness Method II (Trusses)

This week continues the **Direct Stiffness Method (DSM)** for planar trusses. TEXT

### 📖 Lectures

#### Part 1 — TEXT

global stiffness assembly by scatter-add, why unsupported structures yield singular $[K]$, application of supports via
partitioning, solving for displacements and reactions, and recovery of member axial forces in local coordinates.

- 🌐 **Slides (HTML):** [L4_1.slides.html](Lectures/L4/L4_1.slides.html)
- 📄 **Slides (PDF):** [L4_1.pdf](Lectures/L4/L4_1.pdf)
- 📓 **Notebook:** [L4_1.ipynb](Lectures/L4/L4_1.ipynb)

#### Part 2 — TEXT

text

- 🌐 **Slides (HTML):** [L4_2.slides.html](Lectures/L4/L4_2.slides.html)
- 📄 **Slides (PDF):** [L4_2.pdf](Lectures/L4/L4_2.pdf)
- 📓 **Notebook:** [L4_2.ipynb](Lectures/L4/L4_2.ipynb)

### Extra In-Class Code

TBD

<!-- - [L3_1_exercise_BLANK.ipynb](Code/L3/L3_1_exercise_BLANK.ipynb)
  [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Bruun-Automation-Research-Lab/CEE6501/blob/main/Code/L3/L3_1_exercise_BLANK.ipynb)
- [L3_1_exercise_SOLVED.ipynb](Code/L3/L3_1_exercise_SOLVED.ipynb)
  [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Bruun-Automation-Research-Lab/CEE6501/blob/main/Code/L3/L3_1_exercise_SOLVED.ipynb) -->

### 📝 Assignments

See Lecture 1 for how to complete assignments guide.

- ✍️ **Written Assignment:** [A4_written.md](Assignments/A4_written.md)
- 💻 **Coding Assignment:**
  [A4_code.ipynb](Assignments/A4_code.ipynb)[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Bruun-Automation-Research-Lab/CEE6501/blob/main/Assignments/A4_code.ipynb)

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
