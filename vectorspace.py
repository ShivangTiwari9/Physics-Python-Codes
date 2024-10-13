import matplotlib.pyplot as plt
import numpy as np

def plot_vector_space(basis_vectors):
    # Check if the basis vectors form a valid basis
    if len(basis_vectors) < 2 or any(len(v) != len(basis_vectors[0]) for v in basis_vectors[1:]):
        print("Invalid basis vectors.")
        return

    # Create a matrix using the basis vectors
    basis_matrix = np.array(basis_vectors)

    # Generate all possible combinations of scalar multiples of basis vectors
    vector_space = set()
    for i in range(-10, 11):
        for j in range(-10, 11):
            vector = i * basis_matrix[0] + j * basis_matrix[1]
            vector_space.add(tuple(vector))

    # Plot the vector space
    vectors = np.array(list(vector_space))
    plt.scatter(vectors[:, 0], vectors[:, 1], marker='o', label='Vector Space')

    # Plot basis vectors
    origin = np.zeros_like(basis_matrix[0])
    plt.quiver(*origin, *basis_matrix[0], scale=1, scale_units='xy', angles='xy', color='r', label='Basis Vector 1')
    plt.quiver(*origin, *basis_matrix[1], scale=1, scale_units='xy', angles='xy', color='b', label='Basis Vector 2')

    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5, alpha = 0.7)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Vector Space with Basis Vectors')
    plt.legend()
    plt.show()

# Example usage with basis vectors of your choice
basis_vectors = [
    [1,0],  # Basis vector 1
    [0, 1]   # Basis vector 2
]

plot_vector_space(basis_vectors)
