def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
  return [points[i] for d, i in sorted([(math.sqrt(x**2 + y**2), i) for i, [x, y] in enumerate(points)])[:k]]
