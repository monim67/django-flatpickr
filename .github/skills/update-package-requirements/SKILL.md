---
name: update-package-requirements
description: 'Only use to update requirements of the released package for example python version or main dependencies. Do not use to update other dependencies, use poetry instead.'
---

# Update Package Requirements

## Adding or Dropping a Python Version

- In `pyproject.toml` → `[project] requires-python`: adjust the version range.
- In `pyproject.toml` → `[project] classifiers`: add/remove the `Programming Language :: Python :: 3.x` entries so they match the supported versions.
- In `pyproject.toml` → `[tool.black] target-version`: add/remove the `pyXYZ` entry.
- If the **minimum** version changed: update `[tool.isort] py_version` (compact form, e.g. `"310"` for 3.10). Also update `README.rst` prerequisite line.
- Switch env, regenerate lock, and reinstall:
   ```bash
   poetry env use <new-version>
   poetry lock
   poetry install
   ```
- Verify with `poetry run poe lint` and `poetry run poe test-cov`. If these fail due to outdated dependencies, update them and retry.
- In `pyproject.toml` → `[tool.tox] env_list`: add/remove the version entry (e.g. `"3.14"`).
- In `tests/pip-constraints.txt`: adjust the `python_version` conditions to match the supported range, following the [constraint file pattern](#pip-constraintstxt-pattern).
- In `.github/workflows/build.yml` → `pre-build` matrix: set to the latest supported version.
- In `.github/workflows/build.yml` → `build` matrix: list all remaining supported versions except the one in `pre-build`.
- Do a final sweep to check for any outdated refereces and report to user.


## Updating Production Dependencies

- Edit the version constraint for the package under `[project] dependencies` in `pyproject.toml`.
- Resolve and reinstall:
   ```bash
   poetry update <package-name>
   poetry install
   ```
- Verify with `poetry run poe lint` and `poetry run poe test-cov`.
- Update prerequisites in README.rst if necessary.
- Search the project for any other references to the old version and report to user.


## Adding or Dropping a Django Major Version

- In `pyproject.toml` → `[project] dependencies`: adjust the version constraint (e.g. bump the upper bound to `"Django>=2,<7"` when adding, or raise the lower bound to `"Django>=3,<7"` when dropping Django 2).
- In `pyproject.toml` → `[project] classifiers`: add/remove the `Framework :: Django :: N.0` entry to match.
- In `tests/pip-constraints.txt`: re-derive all rows following the [constraint file pattern](#pip-constraintstxt-pattern) — dropping a major removes its row entirely; the remaining rows still pair one Django major per supported Python version in lockstep.
- Resolve and reinstall:
   ```bash
   poetry update Django
   poetry install
   ```
  Note: `poetry install` resolves against the full supported Python range, so it won't necessarily pick up the new Django major locally if it requires a newer Python floor than `requires-python` — that's expected.
- Verify with `poetry run poe lint` and `poetry run poe test-cov`.
- Update the minimum Django prerequisite in README.rst only if the **minimum** supported version changed.
- Search the project for any other stale Django version references (e.g. `.github/copilot-instructions.md`) and report to user.


## `tests/pip-constraints.txt` Pattern

Each supported Python version in `[tool.tox] env_list` is paired with exactly one Django major version, incrementing both in lockstep from the lowest supported Python version (paired with the lowest supported Django major) up to the highest (paired with the newest Django major, left unbounded with `>=`). All older rows stay bounded between their floor and the next row's floor. Example:

```
<this goes up incrementing both Python and Django versions in lockstep>
django==3.* ; python_version >= "3.11" and python_version < "3.12"
django==2.* ; python_version >= "3.10" and python_version < "3.11"
```

When adding/dropping a Python version or a Django major, re-derive the full set of rows from scratch using this pairing rather than editing individual lines in isolation.
