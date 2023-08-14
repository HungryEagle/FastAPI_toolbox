import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='toolbox',
    version='0.0.1',
    author='Venugopalan Iyengar',
    author_email='iyengarvenugopalan@gmail.com',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/HungryEagle/FastAPI_toolbox.git',
    license='MIT',
    packages=['toolbox'],
    install_requires=['requests'],
)