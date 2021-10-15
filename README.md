# cookiecutter-napari-plugin

Minimal [Cookiecutter] template for authoring [napari] plugins.

This is a customized minimal minimal version maintained by [BiA-PoL](https://physics-of-life.tu-dresden.de/bia). 
If you're interested in the original, more flexible napari plugin template, please check [cookiecutter-napari-plugin](https://github.com/napari/cookiecutter-napari-plugin)/

**NOTE: This repo is not meant to be cloned/forked directly!  Please read "Getting Started" below**

## Getting Started

### Create your plugin package

Install [Cookiecutter] and generate a new napari plugin project:

```bash
pip install cookiecutter
cookiecutter https://github.com/biapol/cookiecutter-napari-plugin
```

Cookiecutter prompts you for information regarding your plugin
(A new folder will be created in your current working directory):

```bash
full_name [Napari Developer]: Ramon y Cajal
email [yourname@example.com]: ramon@cajal.es
github_username_or_organization [githubuser]: neuronz52
# NOTE: for packages whose primary purpose is to be a napari plugin, we
# recommend using the 'napari-' prefix in the package name.
# If your package provides functionality outside of napari, you may
# choose to leave napari out of the name.
plugin_name [napari-foobar]: napari-growth-cone-finder
module_name [growth_cone_finder]: napari_growth_cone_finder
short_description [A simple plugin to use with napari]:
Select license:
1 - BSD-3
2 - MIT
3 - Mozilla Public License 2.0
4 - Apache Software License 2.0
5 - GNU LGPL v3.0
6 - GNU GPL v3.0
Choose from 1, 2, 3, 4, 5, 6 (1, 2, 3, 4, 5, 6) [1]:
```

You just created a minimal napari plugin, complete with tests
and ready for automatic deployment!

For more detailed information on each prompt see the [prompts reference](./PROMPTS.md).

```no-highlight
napari-growth-cone-finder/
│
├── LICENSE
├── MANIFEST.in
├── napari_growth_cone_finder.py
├── README.md
├── requirements.txt
└── setup.py
```

### Initialize a git repository in your package

NOTE: This is important not only for version management, but also if you want to
pip install your package locally for testing with `pip install -e .`. (because
the version of your package is managed using git tags,
[see below](#automatic-deployment-and-version-management))

```bash
cd napari-growth-cone-finder
git init
git add .
git commit -m 'initial commit'
```
    
### Upload it to github

1. Create a [new github repository]

2. Add your newly created github repo as a remote and push:

    ```bash
    # here, continuing with the example above...
    # but replace with your own username and repo name

    git remote add origin https://github.com/neuronz52/napari-growth-cone-finder.git
    git push -u origin master
    ```

## Resources

Please consult the [napari plugin
docs](https://napari.org/plugins/stable/index.html) for more information on
how to create a plugin.

## Issues

If you encounter any problems with this cookiecutter template, please [file an
issue] along with a detailed description.

## License

Distributed under the terms of the [BSD-3] license, `cookiecutter-napari-plugin`
is free and open source software.

[napari organization]: https://github.com/napari/
[gitter_badge]: https://badges.gitter.im/Join%20Chat.svg
[gitter]: https://gitter.im/napari/cookiecutter-napari-plugin?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge (Join Chat on Gitter.im)
[travis_badge]: https://travis-ci.org/napari/cookiecutter-napari-plugin.svg?branch=master
[travis]: https://travis-ci.org/napari/cookiecutter-napari-plugin (See Build Status on Travis CI)
[docs_badge]: https://readthedocs.org/projects/cookiecutter-napari-plugin/badge/?version=latest
[documentation]: https://cookiecutter-napari-plugin.readthedocs.io/en/latest/ (Documentation)
[Cookiecutter]: https://github.com/audreyr/cookiecutter
[napari]: https://github.com/napari/napari
[PyPI]: https://pypi.org/
[tox]: https://tox.readthedocs.io/en/latest/
[file an issue]: https://github.com/biapol/cookiecutter-napari-plugin/issues
[Sphinx]: http://sphinx-doc.org/
[MkDocs]: http://www.mkdocs.org/
[MIT]: http://opensource.org/licenses/MIT
[MPL v2.0]: https://www.mozilla.org/media/MPL/2.0/index.txt
[BSD-3]: http://opensource.org/licenses/BSD-3-Clause
[GNU GPL v3.0]: http://www.gnu.org/licenses/gpl-3.0.txt
[GNU LGPL v3.0]: http://www.gnu.org/licenses/lgpl-3.0.txt
[Apache v2.0]: http://www.apache.org/licenses/LICENSE-2.0
[Travis CI]: https://travis-ci.com/
[AppVeyor]: http://www.appveyor.com/
[PyPA Code of Conduct]: https://www.pypa.io/en/latest/code-of-conduct/
[Shortbread]: https://github.com/audreyr/cookiecutter/releases/tag/1.4.0
[osi_certified]: https://opensource.org/trademarks/osi-certified/web/osi-certified-120x100.png
[OSI]: https://opensource.org/
[github actions]: https://github.com/features/actions
[new github repository]: https://help.github.com/en/github/getting-started-with-github/create-a-repo
[setuptools_scm]: https://github.com/pypa/setuptools_scm
