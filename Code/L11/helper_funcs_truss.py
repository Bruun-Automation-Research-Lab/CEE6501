import numpy as np


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


def k_global_2d_truss(E, A, L, c_x, c_y):
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
