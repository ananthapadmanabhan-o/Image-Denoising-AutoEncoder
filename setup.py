from setuptools import setup,find_packages

VERSION = '0.0.1'
AUTHOR_NAME = 'ananthapadmanabhan-o'
AUTHOR_EMAIL = 'ananthan51ah@gmail.com'
SRC_REPO = 'denoisingEncoder'
REPO_NAME = 'Image-Denoising-AutoEncoder'



setup(
    name=SRC_REPO,
    version=VERSION,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    url=f'https://github.com/{AUTHOR_NAME}/{REPO_NAME}',
    package_dir={'':'src'},
    packages=find_packages(where='src')
)
