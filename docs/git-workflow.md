# Git Workflow

## Branching

The `main` branch contains stable project code.

Feature development is done on a separate feature branch:

`feature/day2-profile`

## Development Workflow

1. Clone the repository.
2. Create a feature branch.
3. Make the required changes.
4. Check changes using `git status`.
5. Stage changes using `git add`.
6. Create a meaningful commit using `git commit`.
7. Push the feature branch to the remote repository.
8. Fetch or pull the latest changes when required.
9. Resolve merge conflicts if they occur.
10. Create a Pull Request for code review.
11. Merge the approved changes into `main`.

## Common Commands

```bash
git clone <repository-url>
git switch -c feature/day2-profile
git status
git add .
git commit -m "add profile test"
git push -u origin feature/day2-profile
git fetch origin
git pull origin main
git merge main
