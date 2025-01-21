def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the grid.
    
    Args:
    grid (List[List[int]]): A 2D list representing the grid, where
                            0 represents water and 1 represents land.
    
    Returns:
    int: The perimeter of the island.
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # Found a land cell
                # Start with 4 sides
                perimeter += 4
                
                # Check for adjacent land cells and subtract sides
                if i > 0 and grid[i - 1][j] == 1:  # Top neighbor
                    perimeter -= 1
                if i < rows - 1 and grid[i + 1][j] == 1:  # Bottom neighbor
                    perimeter -= 1
                if j > 0 and grid[i][j - 1] == 1:  # Left neighbor
                    perimeter -= 1
                if j < cols - 1 and grid[i][j + 1] == 1:  # Right neighbor
                    perimeter -= 1
    
    return perimeter

