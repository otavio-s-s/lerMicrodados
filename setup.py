from setuptools import setup

setup(name='lerMicrodados',
    version='0.1',
    url='https://github.com/otavio-s-s/lerMicrodados',
    license='MIT License',
    author='Otávio Silveira',
    long_description=['readme.md'],
    long_description_content_type="text/markdown",
    author_email='otavios.s@hotmail.com',
    keywords=['Microdados', 'PNAD', 'POF'],
    description='Este pacote contém funções para leitura de microdados da POF e PNAD.',
    packages=['lerMicrodados'],
    install_requires=['pandas', 'zipfile'])