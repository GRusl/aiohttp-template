# AIOHTTP template

Understandable AIOHTTP template

## Opportunities

* 📃 [jinja2](https://github.com/aio-libs/aiohttp-jinja2)
* 🐢 [tortoise-orm](https://tortoise.github.io) as a database library
* 🧱 App structure
* ⚙ Simple setup
* 🔮 template / static

## Usage

* 💾 [Create](https://github.com/GRusl/aiohttp-template/generate) repo from this template
* 🐍 Installing dependencies: `pip install -r requirements.txt`

## Run project

* Run project via `python app.py`
* Open [http://localhost:8080](http://localhost:8080)

## Project structure

```bash
your_project_name
├── app  # Folder with projects
│   ├── __init__.py
│   └── core  # Main app (use it as an application template)
│       ├── views.py  # Main views (for core app)
│       └── router.py  # Main router (for core app)
├── setup_app.py  # Configuring components
├── app.py  # The main startup file
├── settings.py  # Main configuration settings for project
├── templates  # Templates content
│   ├── core  # Markup for core application pages
│   │   └── index.html  # Page markup for core.index
│   ├── includes  # Imported html templates
│   │   ├── header.html  # Basic header markup
│   │   └── footer.html  # Basic footer markup
│   └── base.html  # Basic html template
└── static  # Static content
    ├── app  # Static content for apps
    │   └── core
    │       └── index.css  # Styles for the core.index page
    └── favicon.ico
```

# Feedback

☎ You can [write](https://t.me/Gruslans) me to suggest ideas for improvement or correction
