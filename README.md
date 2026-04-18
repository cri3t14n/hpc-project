# Wall Heating Project

Project repository for the 02613 mini-project on steady-state wall heating simulation using the Jacobi method.

## Team
- Cristian Placinta
- Tobias Mikkelsen
- Emile Hourman
- Valeria Bubuioc

## Project goals
We investigate the performance of different implementations for solving the 2D steady-state heat equation on building floorplans from the Modified Swiss Dwellings dataset.

We compare:
- Reference NumPy implementation
- CPU parallelization over floorplans
- Numba JIT CPU implementation
- Numba CUDA implementation
- CuPy GPU implementation

We also analyze the resulting temperature statistics across the dataset.

## Repository structure
- `src/` implementation code
- `scripts/` helper scripts to run experiments
- `jobs/` batch scripts for cluster timing
- `notebooks/` exploratory notebooks
- `results/` generated outputs
- `reports/` report material
- `tests/` correctness tests

## Setup

### Using venv
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt