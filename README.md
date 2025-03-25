## [codethesaur.us](http://codethesaur.us/)
Website that will compare language features side by side.

## Why would you want this?
Good question. If there's an aspect of a language you don't know, you can compare a languages you know with a language you do. It's a good way to quickly learn a new language, or use it as a quick reference to remember things by.

Learn more about some of the considerations behind this on the [Project Architecture](https://docs.codethesaur.us/website/project-architecture/) docs page.

## Documentation

Learn everything you'd need to know about how the project is built, how to install and run it, how to contribute, and more over at the [Documentation](https://docs.codethesaur.us/) site!

## Cloning and running it locally

Check out our [Installation/Running Locally](https://docs.codethesaur.us/install/quick_start/) page on our documentation.

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/codethesaurus/codethesaur.us.git
   cd codethesaur.us
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the development server:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

5. Open your browser and go to `http://127.0.0.1:8000/` to see the application running.

## Usage

1. Visit the home page to see the available language features.
2. Use the "Learn a Language" section to compare concepts side-by-side with a language you know and one you don't.
3. Use the "See a Reference Sheet" section for a quick and easy way to remind yourself how to do something.

## Contributing

Check out the [Contributing Guide](https://docs.codethesaur.us/contributing/) to learn more about how you can help add more language data, fix bugs, or add features!

## Is this project available for Hacktoberfest contributions?

Yes! The Code Thesaurus code and documentation projects are both enabled for Hacktoberfest contributions.

## Code of Conduct

All contributors are required to follow the [Code Thesaurus Code of Conduct](https://docs.codethesaur.us/code_of_conduct/).

## Questions?

If it's related to an issue, write a comment on the issue or email us at coreteam@codethesaur.us.

You can also reach out on Twitter [@codethesaurus](https://twitter.com/codethesaurus).

You could also email the core team (coreteam@codethesaur.us).
