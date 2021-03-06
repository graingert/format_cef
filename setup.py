from setuptools import setup

setup(
    name='format_cef',
    packages=['format_cef'],
    decsription=(
        'A small helper for formatting ArcSight Common Event Format (CEF) '
        'compliant messages'),
    keywords=['cef', 'logging'],
    url='https://github.com/Osirium/format_cef',
    version='0.0.3',
    install_requires=[],
    tests_require=['pytest'],
    test_suite='pytest')
