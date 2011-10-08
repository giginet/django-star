# -*- coding: utf-8 -*-
#
# setup.py
# created by giginet on 2011/10/07
#
from setuptools import setup
setup(  name          = 'django-star',
        description   = 'Django plugin for adding a star to Django model object universally.',
        version       = '0.999',
        keywords      = "django hatena star",
        author        = 'giginet',
        author_email  = 'giginet.net@gmail.com',
        classifiers   = (
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Programming Language :: Python',
            'Topic :: Internet :: WWW/HTTP',
            ),
        url           = r'https://github.com/giginet/django-star',
        download_url  = r'https://github.com/giginet/django-star/tarball/master',
        license       = 'BSD',
        package_data  = {'star' : ['templates/star/*.html']},
        packages      = ('star', 'star.api', 'star.templatetags',),
        include_package_data = True,
        dependency_links = (
            r"https://bitbucket.org/lambdalisue/django-piston/get/a40885f1da15.tar.gz#egg=django-piston",
        ),
)

