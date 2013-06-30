from setuptools import setup, find_packages

TEST_REQUIREMENTS = (
    'mock',
)

from contact_form import __version__

setup(
    name="django-contact-form-fc",
    version=__version__,
    author="Ilya Baryshev",
    description="Django Contact Form using class based views.",
    long_description=open('README.rst', 'r').read(),
    url="https://github.com/futurecolors/django-contact-form",
    packages=find_packages(exclude=["example*"]),
    include_package_data=True,
    install_requires=[
        'django-templated-email>=0.4.7,<0.5',
    ],
    tests_require=TEST_REQUIREMENTS,
    zip_safe=False,

    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
    ],
)
