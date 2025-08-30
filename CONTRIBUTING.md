# Contributing to Flood Detection System

We love your input! We want to make contributing to this project as easy and transparent as possible, whether it's:

- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features
- Becoming a maintainer

## Development Process

We use GitHub to host code, to track issues and feature requests, as well as accept pull requests.

### Pull Requests

1. Fork the repo and create your branch from `main`.
2. If you've added code that should be tested, add tests.
3. If you've changed APIs, update the documentation.
4. Ensure the test suite passes.
5. Make sure your code lints.
6. Issue that pull request!

### Development Setup

1. **Clone your fork**
   ```bash
   git clone https://github.com/yourusername/flood-detection-system.git
   cd flood-detection-system
   ```

2. **Install dependencies**
   ```bash
   npm install
   cd backend && pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   cp .env.local.example .env.local
   cp backend/.env.example backend/.env
   # Add your API keys
   ```

4. **Start development servers**
   ```bash
   # Terminal 1 - Backend
   cd backend && python start.py
   
   # Terminal 2 - Frontend
   npm run dev
   ```

### Code Style

- **Frontend**: Follow TypeScript/React best practices
- **Backend**: Follow PEP 8 Python style guide
- Use meaningful variable names and add comments for complex logic
- Ensure proper error handling

### Commit Messages

Use clear and meaningful commit messages:
- feat: add new feature
- fix: bug fixes
- docs: documentation changes
- style: formatting changes
- refactor: code refactoring
- test: adding tests
- chore: maintenance tasks

## Any contributions you make will be under the MIT Software License

When you submit code changes, your submissions are understood to be under the same [MIT License](LICENSE) that covers the project.

## Report bugs using GitHub's [issue tracker](https://github.com/yourusername/flood-detection-system/issues)

We use GitHub issues to track public bugs. Report a bug by [opening a new issue](https://github.com/yourusername/flood-detection-system/issues/new).

**Great Bug Reports** tend to have:

- A quick summary and/or background
- Steps to reproduce
- What you expected would happen
- What actually happens
- Notes (possibly including why you think this might be happening, or stuff you tried that didn't work)

## License

By contributing, you agree that your contributions will be licensed under its MIT License.
