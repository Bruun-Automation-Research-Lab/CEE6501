import numpy as np
import matplotlib.pyplot as plt


def plot_original_and_deformed_shape_2d(
    elements,
    coords_original,
    coords_deformed,
    show_node_labels=True,
    label_deformed_only=False,
    title="Original and Deformed Shape",
    figsize=(7, 6),
):
    """
    Plot the original and deformed 2D shapes of a structure.

    Parameters
    ----------
    elements : dict[int, tuple[int, int]]
        Element dictionary in the form
        {element_id: (start_node, end_node)}.
    coords_original : dict[int, tuple[float, float]]
        Original nodal coordinates in the form
        {node_id: (x, y)}.
    coords_deformed : dict[int, tuple[float, float]]
        Deformed nodal coordinates in the form
        {node_id: (x, y)}.
    show_node_labels : bool, optional
        If True, show node labels on the plot.
    label_deformed_only : bool, optional
        If True, label only the deformed nodes.
    title : str, optional
        Plot title.
    figsize : tuple, optional
        Figure size.

    Returns
    -------
    fig : matplotlib.figure.Figure
        Matplotlib figure object.
    ax : matplotlib.axes.Axes
        Matplotlib axes object.
    """
    fig, ax = plt.subplots(figsize=figsize)

    first = True
    for _, (i, j) in elements.items():
        ax.plot(
            [coords_original[i][0], coords_original[j][0]],
            [coords_original[i][1], coords_original[j][1]],
            linestyle=":",
            linewidth=1.0,
            color="black",
            label="Original" if first else "",
        )
        first = False

    first = True
    for _, (i, j) in elements.items():
        ax.plot(
            [coords_deformed[i][0], coords_deformed[j][0]],
            [coords_deformed[i][1], coords_deformed[j][1]],
            linestyle="-",
            linewidth=2.5,
            color="black",
            label="Deformed" if first else "",
        )
        first = False

    ax.scatter(
        [coords_original[node][0] for node in coords_original],
        [coords_original[node][1] for node in coords_original],
        s=20,
        color="black",
    )
    ax.scatter(
        [coords_deformed[node][0] for node in coords_deformed],
        [coords_deformed[node][1] for node in coords_deformed],
        s=30,
        color="black",
    )

    if show_node_labels:
        if not label_deformed_only:
            for node, (x, y) in coords_original.items():
                ax.text(x, y, f" {node}", va="bottom", ha="left")
        for node, (x, y) in coords_deformed.items():
            ax.text(x, y, f" {node}", va="top", ha="left")

    ax.set_aspect("equal")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title(title)
    ax.legend()
    ax.grid(True)

    return fig, ax


def build_full_branch_node_matrix(elements):
    """
    Build the full branch-node incidence matrix C_s from a branch list.

    Parameters
    ----------
    elements : dict[int, tuple[int, int]]
        Dictionary of elements in the form
        {element_id: (start_node, end_node)}.

    Returns
    -------
    C_s : np.ndarray
        Full branch-node incidence matrix.
    """
    n_nodes = max(max(start, end) for start, end in elements)
    m = len(elements)

    C_s = np.zeros((m, n_nodes), dtype=int)

    for r, (start, end) in enumerate(elements):
        C_s[r, start - 1] = 1
        C_s[r, end - 1] = -1

    return C_s


def partition_branch_node_matrix(C_s, free_nodes):
    """
    Partition the full branch-node matrix into free and fixed parts.

    Parameters
    ----------
    C_s : np.ndarray
        Full branch-node incidence matrix with columns ordered by
        node number: node 1, node 2, ..., node n.
    free_nodes : list[int]
        List of free node labels (1-indexed).

    Returns
    -------
    C : np.ndarray
        Incidence matrix associated with free nodes.
    C_f : np.ndarray
        Incidence matrix associated with fixed nodes.
    """
    free_idx = [node - 1 for node in free_nodes]
    fixed_idx = [j for j in range(C_s.shape[1]) if j not in free_idx]

    C = C_s[:, free_idx]
    C_f = C_s[:, fixed_idx]

    return C, C_f


def build_coordinate_vectors(nodes, free_nodes, fixed_nodes, is_3d=False):
    """
    Build free-node and fixed-node coordinate vectors from a coordinate dict

    Parameters
    ----------
    nodes : dict[int, tuple[float, ...]]
        Dictionary mapping 1-based node label -> (x, y) for 2D
        or (x, y, z) for 3D.
    free_nodes : list[int]
        List of free node labels (1-based).
    fixed_nodes : list[int]
        List of fixed node labels (1-based).
    is_3d : bool, optional
        If True, also build z-coordinate vectors.

    Returns
    -------
    x : np.ndarray
        Free-node x-coordinate vector, shape (n_free, 1).
    y : np.ndarray
        Free-node y-coordinate vector, shape (n_free, 1).
    z : np.ndarray or None
        Free-node z-coordinate vector, shape (n_free, 1), or None in 2D.
    x_f : np.ndarray
        Fixed-node x-coordinate vector, shape (n_fixed, 1).
    y_f : np.ndarray
        Fixed-node y-coordinate vector, shape (n_fixed, 1).
    z_f : np.ndarray or None
        Fixed-node z-coordinate vector, shape (n_fixed, 1), or None in 2D.
    """
    x = np.array([nodes[node][0] for node in free_nodes], dtype=float).reshape(
        -1, 1
    )
    y = np.array([nodes[node][1] for node in free_nodes], dtype=float).reshape(
        -1, 1
    )

    x_f = np.array(
        [nodes[node][0] for node in fixed_nodes], dtype=float
    ).reshape(-1, 1)
    y_f = np.array(
        [nodes[node][1] for node in fixed_nodes], dtype=float
    ).reshape(-1, 1)

    z = None
    z_f = None

    if is_3d:
        z = np.array(
            [nodes[node][2] for node in free_nodes], dtype=float
        ).reshape(-1, 1)
        z_f = np.array(
            [nodes[node][2] for node in fixed_nodes], dtype=float
        ).reshape(-1, 1)

    return x, y, z, x_f, y_f, z_f


def build_branch_coordinate_differences(
    C, C_f, x, y, x_f, y_f, z=None, z_f=None, is_3d=False
):
    """
    Build branch coordinate-difference vectors.

    Parameters
    ----------
    C : np.ndarray
        Branch-node matrix associated with free nodes.
    C_f : np.ndarray
        Branch-node matrix associated with fixed nodes.
    x : np.ndarray
        Free-node x-coordinate vector.
    y : np.ndarray
        Free-node y-coordinate vector.
    x_f : np.ndarray
        Fixed-node x-coordinate vector.
    y_f : np.ndarray
        Fixed-node y-coordinate vector.
    z : np.ndarray, optional
        Free-node z-coordinate vector for 3D.
    z_f : np.ndarray, optional
        Fixed-node z-coordinate vector for 3D.
    is_3d : bool, optional
        If True, also compute z-direction branch differences.

    Returns
    -------
    u : np.ndarray
        Branch x-coordinate differences.
    v : np.ndarray
        Branch y-coordinate differences.
    w : np.ndarray or None
        Branch z-coordinate differences in 3D, or None in 2D.
    """
    u = C @ x + C_f @ x_f
    v = C @ y + C_f @ y_f

    w = None
    if is_3d:
        w = C @ z + C_f @ z_f

    return u, v, w


def calculate_branch_lengths_from_differences(u, v, w=None):
    """
    Calculate branch lengths from branch coordinate-difference vectors.

    Parameters
    ----------
    u : np.ndarray
        Branch x-coordinate differences, shape (m, 1).
    v : np.ndarray
        Branch y-coordinate differences, shape (m, 1).
    w : np.ndarray, optional
        Branch z-coordinate differences, shape (m, 1).

    Returns
    -------
    length : np.ndarray
        Branch length vector, shape (m, 1).
    """
    if w is None:
        length = np.sqrt(u**2 + v**2)
    else:
        length = np.sqrt(u**2 + v**2 + w**2)

    return length


def create_node_force_vectors(nodes_loads, free_nodes, is_3d=False):
    """
    Build the free-node load vectors in the x-, y-, and optionally z-dirs.

    Parameters
    ----------
    nodes_loads : dict[int, tuple[float, ...]]
        Dictionary of nodal loads in the form
        {node_id: (p_x, p_y)} for 2D or
        {node_id: (p_x, p_y, p_z)} for 3D,
        using 1-based node labels.
    free_nodes : list[int]
        List of free node labels (1-based).
    is_3d : bool, optional
        If True, also build the z-direction load vector.

    Returns
    -------
    p_x : np.ndarray
        Free-node load vector in the x-direction, shape (n_free, 1).
    p_y : np.ndarray
        Free-node load vector in the y-direction, shape (n_free, 1).
    p_z : np.ndarray or None
        Free-node load vector in the z-direction, shape (n_free, 1),
        or None in 2D.
    """
    p_x = np.array(
        [nodes_loads[node][0] for node in free_nodes], dtype=float
    ).reshape(-1, 1)
    p_y = np.array(
        [nodes_loads[node][1] for node in free_nodes], dtype=float
    ).reshape(-1, 1)

    p_z = None
    if is_3d:
        p_z = np.array(
            [nodes_loads[node][2] for node in free_nodes], dtype=float
        ).reshape(-1, 1)

    return p_x, p_y, p_z


def update_node_coordinates(nodes, free_nodes, x, y, z=None, is_3d=False):
    """
    Create a new node dictionary with updated coordinates for the free nodes.

    Parameters
    ----------
    nodes : dict[int, tuple[float, ...]]
        Original node coordinates in the form
        {node_id: (x, y)} for 2D or {node_id: (x, y, z)} for 3D,
        using 1-based node labels.
    free_nodes : list[int]
        List of free node labels (1-based), ordered consistently with x, y,
        and optionally z.
    x : np.ndarray
        Solved free-node x-coordinate vector, shape (n_free, 1) or (n_free,).
    y : np.ndarray
        Solved free-node y-coordinate vector, shape (n_free, 1) or (n_free,).
    z : np.ndarray, optional
        Solved free-node z-coordinate vector, shape (n_free, 1) or (n_free,).
    is_3d : bool, optional
        If True, update 3D coordinates.

    Returns
    -------
    nodes_new : dict[int, tuple[float, ...]]
        Updated node dictionary with solved coordinates for free nodes
        and original coordinates for fixed nodes.
    """
    x = np.asarray(x).ravel()
    y = np.asarray(y).ravel()

    if is_3d:
        z = np.asarray(z).ravel()

    nodes_new = dict(nodes)

    for i, node in enumerate(free_nodes):
        if is_3d:
            nodes_new[node] = (float(x[i]), float(y[i]), float(z[i]))
        else:
            nodes_new[node] = (float(x[i]), float(y[i]))

    return nodes_new
