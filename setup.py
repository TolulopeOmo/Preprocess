import setuptools

with open('README.md', 'r') as file:
	long_description = file.read()



setuptools.setup(
	name = 'Preprocess',  #this should be unit
	version = '0.0.3',
	author = 'Tolulope Omosefunmi',
	author_email = 'omosefunmiblessing@gmail.com',
	description = 'This is preprocessing package',
	long_description = long_description,
	long_description_content_type = 'text/markdown',
	packages = setuptools.find_packages(),
	classifiers = [
	'Programming Lanaguage :: Python :: 3'
	'License :: OSI Approved :: MIT License'
	'Operating System :: OS independent'],
	python_requires = '>=3.5'
	)
