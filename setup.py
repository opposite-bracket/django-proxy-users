from distutils.core import setup

setup(
    name='django-proxy-user',
    version='0.1.0',
    author='Jesus Rodriguez',
    author_email='jesus.rodriguez.ravelo@gmail.com',
    packages=['django-proxy-user'],
    url='https://github.com/jturo/django-proxy-users.git',
    license='LICENSE.txt',
    description='Authentication extension to enable proxy users in django.',
    long_description=open('README.txt').read(),
    install_requires=[
        "Django >= 1.4.1",
    ],
)
