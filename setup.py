from setuptools import setup, find_packages

setup(name='django-notificare',
    version='0.1.0',
    description='Notificare Python client',
    #long_description = read('README.rst'),
    author='Sander van de Graaf',
    url='https://github.com/svdgraaf/django-notificare',
    install_requires=('requests',),
    packages=find_packages(),
    include_package_data=True,
)
