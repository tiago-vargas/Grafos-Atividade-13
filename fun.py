class Graph:
	def __init__(self, adjacency_matrix: list[list[int]]) -> None:
		m = len(adjacency_matrix)
		n = len(adjacency_matrix[0])
		assert n <= 5, "O grafo deve ter no máximo 5 vértices"
		assert m == n, "A matriz deve ser quadrada"

		self._adjacency_matrix = adjacency_matrix

	def is_planar(self) -> bool:
		has_5_vertices = self._count_vertices() == 5
		is_k_5 = has_5_vertices and self.is_regular()
		if is_k_5:
			return False
		else:
			return True

	def _count_vertices(self) -> int:
		return len(self._adjacency_matrix)

	def _count_edges(self) -> int:
		return sum(sum(row) for row in self._adjacency_matrix) // 2

	def is_regular(self) -> bool:
		"""Todos os vértices têm que ter o mesmo grau"""
		degree = sum(self._adjacency_matrix[0])
		for row in self._adjacency_matrix:
			if sum(row) != degree:
				return False
		return True
