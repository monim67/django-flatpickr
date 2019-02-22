from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name='django-flatpickr',
    version='1.0.0',
    description='Flatpickr based DatePickerInput, TimePickerInput and '
                'DateTimePickerInput with date-range-picker functionality '
                'for django >= 2.0',
    long_description=readme(),
    url='https://github.com/monim67/django-flatpickr',
    author='Munim Munna',
    author_email='monim67@yahoo.com',
    license='MIT',
    keywords='django flatpickr date-picker time-picker datetime-picker '
             'date-range-picker',
    packages=['flatpickr'],
    install_requires=[
        'django>=2.0',
    ],
    python_requires='>=3.4',
    package_data={
        'flatpickr': []
    },
    include_package_data=True,
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
        'Environment :: Web Environment',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT Software License',
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Framework :: Django',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.0',
    ],
)
