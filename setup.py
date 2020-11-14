from setuptools import setup

with open("README.md", "r") as fh:
    readme = fh.read()

setup(name='lerMicrodados',
    version='0.6',
    url='https://github.com/otavio-s-s/lerMicrodados',
    license='MIT License',
    author='Otávio Silveira',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='otavios.s@hotmail.com',
    keywords=['Microdados', 'PNAD', 'POF'],
    description='Este pacote contém funções para leitura de microdados da POF e PNAD.',
    packages=['lerMicrodados'],
    install_requires=['pandas'])
