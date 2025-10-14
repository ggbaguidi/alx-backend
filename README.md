# ALX BACKEND

This repository contains a set of small backend projects and exercises used for learning and practicing common backend concepts in Python and Node.js. Each subfolder is a standalone exercise or mini-project covering a focused topic (pagination, caching, i18n, and a Redis-backed queuing system).

## Contents

- `0x00-pagination/` — Python exercises that demonstrate dataset pagination techniques (simple pagination, hypermedia pagination, and deletion-resilient pagination).
- `0x01-caching/` — Python implementations of different cache replacement policies (FIFO, LIFO, LRU, MRU, LFU) and a `base_caching.py` helper.
- `0x02-i18n/` — A Flask application and templates that demonstrate internationalization (i18n) using Flask-Babel. Includes translation files and examples of locale negotiation.
- `0x03-queuing_system_in_js/` — A Node.js project that demonstrates using Redis and Kue to build a simple queuing system, plus example Express integration and tests.

Each folder contains its own README with learning objectives and resources. See the folder README files for the theory behind each exercise.

## Quick start (Linux / zsh)

The repository contains both Python and Node.js projects. The following steps cover basic setup and how to run each part locally on a Linux machine using `zsh`.

Prerequisites

- Python 3.8+ (python3)
- pip
- virtualenv or venv (recommended)
- Node.js (12+) and npm
- Redis server (for the queuing exercises)

Install system-level packages (Debian/Ubuntu example):

```bash
# update package index
sudo apt update

# install redis and python build tooling
sudo apt install -y redis-server python3-venv python3-pip

# (optional) verify node is installed; if not, install Node.js via your preferred method
node -v || echo "Install Node.js (https://nodejs.org/)"
```

Start Redis (if installed as a system service):

```bash
sudo systemctl enable --now redis-server
sudo systemctl status --no-pager redis-server
```

### 0x00-pagination (Python)

This folder contains small Python scripts that implement pagination helpers and examples. They are simple scripts and exercises; there is no project-wide dependency file.

Example usage:

```bash
# create and activate a venv (recommended)
python3 -m venv .venv
source .venv/bin/activate

# run an example script (runs with the current Python interpreter)
python3 0x00-pagination/1-simple_pagination.py
python3 0x00-pagination/2-hypermedia_pagination.py
```

Notes:

- The scripts are intended as exercises and may print results or define helper functions to be inspected or imported. Open the files to see how the helper functions are used.

### 0x01-caching (Python)

This folder contains implementations of caching policies and a `base_caching.py` file used as a starting point for the exercises.

Example usage:

```bash
source .venv/bin/activate  # use the same venv from above (or create a new one)

# run a cache exercise file
python3 0x01-caching/0-basic_cache.py
python3 0x01-caching/1-fifo_cache.py
```

Notes:

- These modules are exercises demonstrating different replacement policies. They are typically small and self-contained.

### 0x02-i18n (Flask + Flask-Babel)

This folder contains a small Flask app and templates configured for internationalization. Translation files are included under the `translations/` folder.

Install the Python dependencies and run the app:

```bash
source .venv/bin/activate
pip install --upgrade pip
pip install Flask Flask-Babel pytz

# from the repository root (works with zsh)
export FLASK_APP=0x02-i18n/app.py
export FLASK_ENV=development
flask run

# By default Flask will be available at http://127.0.0.1:5000
```

Notes and tips:

- The `templates/` folder contains sample templates that demonstrate parameterized strings and locale-aware formatting. The `translations/` folder already contains `.po` files for `en` and `fr`.
- If you modify translations, use `pybabel` (not included) or the `Flask-Babel` workflow to extract and compile messages.

### 0x03-queuing_system_in_js (Node.js + Redis + Kue)

This is a Node project demonstrating use of Redis and Kue for background job processing. The `package.json` contains useful npm scripts.

Install and run:

```bash
# from repository root
cd 0x03-queuing_system_in_js
npm install

# make sure redis is running (see above)
# run the development server using the provided npm `dev` script
npm run dev

# run tests
npm test
```

Available scripts (from `package.json`):

- `npm run dev` — start development with `nodemon` + `babel-node` (requires the devDependencies installed)
- `npm test` — run Mocha tests (the project includes an `8-job.test.js` file)
- `npm run lint` / `npm run check-lint` — linting helpers (requires `eslint` and configs)

Notes:

- The queue uses Redis and the `kue` package. Ensure Redis is running before starting the app or worker processes.
- If Redis is running on a non-standard host or port, update the Redis client configuration inside the Node scripts.

## Development and testing notes

- This repository is a collection of learning exercises. Most folders contain single-file examples rather than full production-ready services.
- There is no single test runner at the root level. The Node project contains Mocha tests. Python exercises are typically intended to be executed directly or used by unit tests you may add.

## Contributing

If you'd like to add improvements or fixes:

1. Fork the repository and create a branch for your change.
2. Add or update README/documentation where relevant.
3. Open a pull request with a clear description of the change.

## Troubleshooting

- If a Python script fails because a package is missing, create/activate a virtual environment and install the packages listed above.
- If Node scripts fail, ensure `npm install` completed successfully and the required devDependencies are available.
- If Redis-related errors appear, ensure the Redis server is running and reachable.

## License

This repository does not include a formal license file. Check with the original author/owner for license terms before using code in production.

---

If you'd like, I can also:

- Add a `requirements.txt` (or `pyproject.toml`) for the Python parts with the minimal packages used.
- Create small run scripts or Makefile targets to streamline setup.

Let me know if you'd like any of those added.

# ALX BACKEND
