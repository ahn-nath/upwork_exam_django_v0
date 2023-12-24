# Upwork - Entry Exam

## Goal
Working Django DRF API with a User and Profile models and schemas.

## Instructions
1. Clone this repository (don't fork: you will be disqualified)
2. Complete the tasks below adhering to the requirements
3. Submit a pull request with your solution in your cloned repository (don't submit a PR here: you will be disqualified)
4. Deliver a GitHub repository with your solution (it can be private, just give access to @arielaco)

## Tasks
- [x] Create a [User](###User) and [Profile](###Profile) models and schemas 
- [ ] Develop a REST API via DRF exposing CRUD endpoints for both models
- [ ] Test at least 2 endpoints
- [ ] Point DRF docs to root path
- [X] Create requirements file
- [ ] Add a section on `README.md` with setup (venv), install (pip), run and testing instructions

### User
- Email as username
- Can have multiple profiles
- Can have a list of favorite profiles

### Profile
- It has a name and a description
- Belongs to a user

## Requirements
- Use English for all code, comments, commit messages, and documentation
- Delete dead code (unrelated to tasks)
- All API responses must be JSON
- Implement proper folder structure
- Validation must be done via serializers
- Use multiple commits (when possible, use conventional commit messages)
