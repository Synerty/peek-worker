import os
import shutil
from setuptools import setup

pip_package_name = "peek-worker"
py_package_name = "peek_worker"
package_version = '0.0.0'

egg_info = "%s.egg-info" % pip_package_name
if os.path.isdir(egg_info):
    shutil.rmtree(egg_info)

if os.path.isfile('MANIFEST'):
    os.remove('MANIFEST')

excludePathContains = ('__pycache__', 'node_modules', 'platforms', 'dist')
excludeFilesEndWith = ('.pyc', '.js', '.js.map', '.lastHash')
excludeFilesStartWith = ()


def find_package_files():
    paths = []
    for (path, directories, filenames) in os.walk(py_package_name):
        if [e for e in excludePathContains if e in path]:
            continue

        for filename in filenames:
            if [e for e in excludeFilesEndWith if filename.endswith(e)]:
                continue

            if [e for e in excludeFilesStartWith if filename.startswith(e)]:
                continue

            paths.append(os.path.join(path[len(py_package_name) + 1:], filename))

    return paths

package_files = find_package_files()

setup(
    name=pip_package_name,
    packages=[py_package_name],
    package_data={'': package_files},
    entry_points={
        'console_scripts': [
            'run_peek_worker = peek_worker.run_peek_worker:main',
            'winsvc_peek_worker = peek_worker.winsvc_peek_worker:main',
        ],
    },
    install_requires=["peek-platform"],
    zip_safe=False,version=package_version,
    description='Peek Platform - Worker Service',
    author='Synerty',
    author_email='contact@synerty.com',
    url='https://github.com/Synerty/%s' % pip_package_name,
    download_url='https://github.com/Synerty/%s/tarball/%s' % (
        pip_package_name, package_version),
    keywords=['Peek', 'Python', 'Platform', 'synerty'],
    classifiers=[
        "Programming Language :: Python :: 3.5",
    ],
)
