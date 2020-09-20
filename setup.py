from distutils.core import setup
f=open('README.md')
des=f.read()
f.close()
setup(
  name = 'share_secret',         
  packages = ['share_secret'],   
  version = '0.1',    
  license='GPLv3',        
  description = 'share secrets with ease.', 
  long_description=des,
  author = 'Anish M',                  
  author_email = 'aneesh25861@gmail.com',     
  url = 'https://github.com/anish-m-code/share_secret',  
  download_url = 'https://github.com/Anish-M-code/share_secret/archive/v0.1.tar.gz',    
  keywords = ['Secret sharing', 'cryptography'],  
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)

