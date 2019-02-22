# Contributing to this Project

Any contributions to this repository in the form of bug reports, bug fix, suggestions and feature requests
are warmly welcomed as long as it does not hamper the tests and coverage report.


## Getting Started

Follow the following steps to get started contributing to this project.

 1. Fork the repository on GitHub.
 2. Clone your fork to your computer:

        git clone https://github.com/your_username_here/django-flatpickr.git
        cd django-flatpickr
        git checkout -b name-of-your-bugfix-or-feature

 3. Create a virtual environment of your choice and activate it.
 4. Install yarn dev-dependencies.

        yarn install

 5. Install the pip-dependencies and run migrations for dev project.

        yarn dev:install
        yarn dev:migrate

 6. Now you can run the dev project on localhost:8000 to see the changes you make in action real-time.

        yarn dev


## Testing

 1. Run the tests by the following command.

        yarn test

 2. See the coverage report by the following command.

        yarn coverage

