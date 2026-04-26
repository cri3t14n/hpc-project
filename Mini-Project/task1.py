from os.path import join
import sys

import numpy as np
import matplotlib.pyplot as plt


LOAD_DIR = "/dtu/projects/02613_2025/data/modified_swiss_dwellings/"


def load_building_ids(load_dir):
    """Load all building IDs from building_ids.txt."""
    with open(join(load_dir, "building_ids.txt"), "r") as f:
        return f.read().splitlines()


def load_floorplan(load_dir, bid):
    domain = np.load(join(load_dir, f"{bid}_domain.npy"))
    interior = np.load(join(load_dir, f"{bid}_interior.npy"))
    return domain, interior


def visualize_floorplan(bid, domain, interior):
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))

    im0 = axes[0].imshow(domain, cmap="hot")
    axes[0].set_title(f"Building {bid}: domain")
    axes[0].set_xlabel("x")
    axes[0].set_ylabel("y")
    fig.colorbar(im0, ax=axes[0], fraction=0.046, pad=0.04)

    im1 = axes[1].imshow(interior, cmap="gray")
    axes[1].set_title(f"Building {bid}: interior mask")
    axes[1].set_xlabel("x")
    axes[1].set_ylabel("y")
    fig.colorbar(im1, ax=axes[1], fraction=0.046, pad=0.04)

    plt.tight_layout()
    plt.show()


def print_basic_info(bid, domain, interior):
    print(f"\nBuilding ID: {bid}")
    print(f"domain shape: {domain.shape}, dtype: {domain.dtype}")
    print(f"interior shape: {interior.shape}, dtype: {interior.dtype}")
    print(f"domain unique values: {np.unique(domain)}")
    print(f"number of interior points: {np.sum(interior)}")


def main():
    building_ids = load_building_ids(LOAD_DIR)

    if len(sys.argv) > 1:
        n_buildings = int(sys.argv[1])
    else:
        n_buildings = 3

    selected_ids = building_ids[:n_buildings]

    print(f"Loaded {len(building_ids)} total building IDs")
    print(f"Visualizing first {n_buildings} building(s): {selected_ids}")

    for bid in selected_ids:
        domain, interior = load_floorplan(LOAD_DIR, bid)
        print_basic_info(bid, domain, interior)
        visualize_floorplan(bid, domain, interior)


if __name__ == "__main__":
    main()