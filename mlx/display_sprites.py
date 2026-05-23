from mlx import Mlx

W, H = 800, 600
m = Mlx()
mlx_ptr = m.mlx_init()
win_ptr = m.mlx_new_window(mlx_ptr, W, H, "maze")


tiles_ptr = []
for i in range(1, 16):
    img, w, h = m.mlx_png_file_to_image(mlx_ptr, f"./sprites/s{i}.png")
    tiles_ptr.append(img)

maze = [
    [1, 1, 1],
    [4, 5, 6],
    [7, 8, 9]
]

for row_idx, row in enumerate(maze):
    for col_idx, cell in enumerate(row):
        x = col_idx * 96
        y = row_idx * 96
        tile = tiles_ptr[cell - 1]
        m.mlx_put_image_to_window(mlx_ptr, win_ptr, tile, x, y)

def exit(data):
    m.mlx_loop_exit(mlx_ptr)

m.mlx_hook(win_ptr, 33, 0, exit, None)
m.mlx_loop(mlx_ptr)
