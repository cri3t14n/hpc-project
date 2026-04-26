from os.path import join, dirname, abspath
import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = dirname(abspath(__file__))
PARENT = dirname(HERE)
sys.path.insert(0, PARENT)

from simulate import load_data, jacobi  


LOAD_DIR = "/dtu/projects/02613_2025/data/modified_swiss_dwellings/"
OUT_DIR = HERE


def load_building_ids(load_dir):
    with open(join(load_dir, "building_ids.txt"), "r") as f:
        return f.read().splitlines()


def save_simulation_figure(bid, u0, interior_mask, u_final, out_dir):
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    im0 = axes[0].imshow(u0[1:-1, 1:-1], cmap="hot", vmin=0, vmax=25)
    axes[0].set_title(f"Building {bid}: initial domain")
    axes[0].set_xlabel("x")
    axes[0].set_ylabel("y")
    fig.colorbar(im0, ax=axes[0], fraction=0.046, pad=0.04)

    im1 = axes[1].imshow(interior_mask, cmap="gray")
    axes[1].set_title(f"Building {bid}: interior mask")
    axes[1].set_xlabel("x")
    axes[1].set_ylabel("y")
    fig.colorbar(im1, ax=axes[1], fraction=0.046, pad=0.04)

    im2 = axes[2].imshow(u_final[1:-1, 1:-1], cmap="hot", vmin=5, vmax=25)
    axes[2].set_title(f"Building {bid}: simulation result")
    axes[2].set_xlabel("x")
    axes[2].set_ylabel("y")
    fig.colorbar(im2, ax=axes[2], fraction=0.046, pad=0.04)

    plt.tight_layout()

    out_path = join(out_dir, f"{bid}_simulation.png")
    plt.savefig(out_path, dpi=200, bbox_inches="tight")
    plt.close(fig)

    print(f"Saved figure to: {out_path}")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)

    building_ids = load_building_ids(LOAD_DIR)

    if len(sys.argv) > 1:
        n_buildings = int(sys.argv[1])
    else:
        n_buildings = 4

    selected_ids = building_ids[:n_buildings]

    MAX_ITER = 20_000
    ABS_TOL = 1e-4

    print(f"Visualizing simulation results for first {n_buildings} building(s): {selected_ids}")

    for bid in selected_ids:
        u0, interior_mask = load_data(LOAD_DIR, bid)
        u_final = jacobi(u0, interior_mask, MAX_ITER, ABS_TOL)
        save_simulation_figure(bid, u0, interior_mask, u_final, OUT_DIR)


if __name__ == "__main__":
    main()