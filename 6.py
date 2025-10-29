from typing import Tuple, Optional
import numpy as np
from numba import njit

# Directions: up, right, down, left
DIRECTIONS = np.array([
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0)
], dtype=np.int32)

# Map from direction index to next index when rotating right
ROTATE_RIGHT_IDX = np.array([1, 2, 3, 0], dtype=np.int32)


@njit
def simulate_guard_numba(
    data: np.ndarray,
    width: int,
    height: int,
    start_x: int,
    start_y: int,
    extra_obstacle: Optional[Tuple[int, int]] = None
) -> Tuple[np.ndarray, bool]:
    """
    Numba-accelerated guard simulation.
    Returns:
        visited_positions: boolean mask of visited cells
        loop_detected: True if guard loops forever
    """
    # Copy data so we can modify it
    grid = data.copy()

    if extra_obstacle is not None:
        ox, oy = extra_obstacle
        grid[oy, ox] = ord('#')

    visited = np.zeros((height, width), dtype=np.bool_)
    states_seen = set()  # Numba supports sets of tuples in nopython mode

    x, y = start_x, start_y
    dir_idx = 0  # start facing up

    while True:
        state = (x, y, dir_idx)
        if state in states_seen:
            return visited, True
        states_seen.add(state)
        visited[y, x] = True

        dx, dy = DIRECTIONS[dir_idx]
        nx, ny = x + dx, y + dy

        if nx < 0 or nx >= width or ny < 0 or ny >= height:
            return visited, False

        if grid[ny, nx] == ord('#'):
            dir_idx = ROTATE_RIGHT_IDX[dir_idx]
        else:
            x, y = nx, ny


class GuardMap:
    def __init__(self, filename: str):
        self.data, self.width, self.height = self._load_map(filename)
        self.start_x = self.data_str.find("^") % self.width
        self.start_y = self.data_str.find("^") // self.width

    @staticmethod
    def _load_map(filename: str) -> Tuple[np.ndarray, int, int]:
        with open(filename) as f:
            lines = [line.strip() for line in f]
        height = len(lines)
        width = len(lines[0])
        # Store as 2D numpy array of ASCII codes for Numba speed
        grid = np.array([[ord(c) for c in line] for line in lines], dtype=np.int32)
        return grid, width, height

    @property
    def data_str(self) -> str:
        return "".join(chr(c) for row in self.data for c in row)

    def part1(self) -> int:
        visited, _ = simulate_guard_numba(
            self.data, self.width, self.height, self.start_x, self.start_y
        )
        return visited.sum()

    def part2(self) -> int:
        visited, _ = simulate_guard_numba(
            self.data, self.width, self.height, self.start_x, self.start_y
        )
        total = 0
        for py in range(self.height):
            for px in range(self.width):
                if not visited[py, px]:
                    continue
                if (px, py) == (self.start_x, self.start_y):
                    continue
                _, looped = simulate_guard_numba(
                    self.data, self.width, self.height, self.start_x, self.start_y, (px, py)
                )
                if looped:
                    total += 1
        return total


if __name__ == "__main__":
    gm = GuardMap("data/6.txt")
    print("Part 1:", gm.part1())
    print("Part 2:", gm.part2())

