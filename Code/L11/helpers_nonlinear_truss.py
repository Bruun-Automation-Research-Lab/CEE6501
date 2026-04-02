import numpy as np


def geometry_from_nodes(n1, n2):
    """
    Return the length and direction cosines of a 2D truss element
    defined by its two nodes.

    Parameters
    ----------
    n1 : (2,) ndarray
        Coordinates of node 1, in the form [x1, y1]
    n2 : (2,) ndarray
        Coordinates of node 2, in the form [x2, y2]

    Returns
    -------
    L : float
        Original element length
    c_x : float
        Cosine of original element angle
    c_y : float
        Sine of original element angle
    """
    dx = n2[0] - n1[0]
    dy = n2[1] - n1[1]
    L = np.sqrt(dx**2 + dy**2)
    c_x = dx / L
    c_y = dy / L

    T = np.array([-c_x, -c_y, c_x, c_y], dtype=float)

    return L, c_x, c_y, T


def cosines_from_degrees(theta_deg):
    """
    Return c_x and c_y from an angle in degrees.

    Parameters
    ----------
    theta_deg : float
        Angle in degrees, measured counterclockwise from the +x axis

    Returns
    -------
    c_x : float
        cos(theta)
    c_y : float
        sin(theta)
    """
    theta_rad = np.radians(theta_deg)
    c_x = np.cos(theta_rad)
    c_y = np.sin(theta_rad)
    return c_x, c_y


def k_global_2d_truss_elastic(E, A, L, c_x, c_y):
    """
    Material part of the tangent stiffness matrix for a 2D truss element
    in global coordinates.

    DOF order:
        [u1, v1, u2, v2]

    Parameters
    ----------
    E : float
        Young's modulus
    A : float
        Cross-sectional area
    L : float
        Original element length
    c_x : float
        Cosine of current element angle
    c_y : float
        Sine of current element angle

    Returns
    -------
    k : (4,4) ndarray
        Global material tangent stiffness matrix
    """
    EA_L = E * A / L

    k = EA_L * np.array(
        [
            [c_x**2, c_x * c_y, -(c_x**2), -c_x * c_y],
            [c_x * c_y, c_y**2, -c_x * c_y, -(c_y**2)],
            [-(c_x**2), -c_x * c_y, c_x**2, c_x * c_y],
            [-c_x * c_y, -(c_y**2), c_x * c_y, c_y**2],
        ],
        dtype=float,
    )

    return k


def k_global_2d_truss_geometric(q, L_bar, c_x, c_y):
    """
    Geometric part of the tangent stiffness matrix for a 2D truss element
    in global coordinates.

    DOF order:
        [u1, v1, u2, v2]

    Parameters
    ----------
    q : float
        Current axial force in the element
        (positive in tension)
    L_bar : float
        Current deformed element length
    c_x : float
        Cosine of current element angle
    c_y : float
        Sine of current element angle

    Returns
    -------
    k_g : (4,4) ndarray
        Global geometric tangent stiffness matrix
    """
    k_g = (q / L_bar) * np.array(
        [
            [c_y**2, -c_x * c_y, -(c_y**2), c_x * c_y],
            [-c_x * c_y, c_x**2, c_x * c_y, -(c_x**2)],
            [-(c_y**2), c_x * c_y, c_y**2, -c_x * c_y],
            [c_x * c_y, -(c_x**2), -c_x * c_y, c_x**2],
        ],
        dtype=float,
    )

    return k_g
