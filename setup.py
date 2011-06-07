from distutils.core import setup

setup(
    name = "django-placemat",
    url = "http://github.com/sebleier/django-placemat",
    author = "Sean Bleier",
    author_email = "sebleier@gmail.com",
    version = "0.1a",
    packages = ["placemat"],
    description = "Backend companion to placemat.js",
    classifiers = [
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
        "Environment :: Web Environment",
        "Framework :: Django",
    ],
)

