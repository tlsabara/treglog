from setuptools import setup

setup(
    name = 'treglog',
    version = '2.0.6',
    author = 'Thiago Sabará',
    author_email = 'thi.sil.sab@gmail.com',
    packages = ['treglog'],
    description = 'Um simples projeto de logs, para pequenos projetos',
    long_description = 'Um simples projeto de logs, para pequenos projetos. '
                        + 'Consegue criar modos de debug para log em arquivo e em tela.',
    url = 'https://github.com/tlsabara/treglog/',
    project_urls = {
        'Código fonte': 'https://github.com/tlsabara/treglog/blob/main/treglog/treglog.py',
        'Download': 'https://github.com/tlsabara/treglog/blob/main/docs/versions'
        },
    
    keywords = 'log tlog treglog',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Portuguese (Brazilian)',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Internationalization',
        'Topic :: Scientific/Engineering :: Physics'
    ]
    
)