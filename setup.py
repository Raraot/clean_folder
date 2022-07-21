from setuptools import setup, find_packages

setup(
    name='clean_folder',
    version='0.0.7',
    description='My homework 7 sort_file function',
    author='Suprunets Volodymyr',
    author_email='raraot@gmail.com',
    license='MIT',
    packages=find_packages(),
    entry_points={'console_scripts':['clean-folder=clean_folder.clean:main']},
    classifiers=[
        "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
    ]
)