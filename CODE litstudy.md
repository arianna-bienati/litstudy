# Litstudy for dummies

## How to install and config?

> [!warning]
> Unfortunately, for a dummie like me, the [installation guide](https://nlesc.github.io/litstudy/installation.html) was laconic and the 'Import litstudy' section in the [example usage](https://nlesc.github.io/litstudy/example.html) contained info that were not applicable in my case. Thus this 'for dummies' super detailed guide 😅

```ad-info
I was working on a macOS Sonoma 14.5, with Apple silicon M2 Pro chip.
To edit the Jupyter notebook I wanted to use to show case my wonderful literature review I was using VSCode, version: 1.90.0. I had a virtual environment set up, clean.
```
 
### Litstudy

So, as a first step I tried to install litstudy, running `pip install litstudy`.
After that I wanted to import it and I checked the example usage to know something more:

```
# Import other libraries
import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbs

[...]

# Import litstudy
path = os.path.abspath(os.path.join('..'))
if path not in sys.path:
    sys.path.append(path)

import litstudy
```

So the example usage tells you to import all these things (which I didn't) and then to set the path. Now, I don't know what these lines of code actually do, but when I see a path I am always suspicious, so I asked chatGPT. Here's the answer:

> This code snippet ensures that the parent directory of the current script is included in the Python module search path (`sys.path`). This allows the current script to import modules that are located in the parent directory.

Right, but why should I do this?

>Including the parent directory in the `sys.path` is typically done to facilitate module imports in the following scenarios [...]

and then:

>**When not to use this approach**: **Virtual Environments**: Relying too much on manipulating `sys.path` can cause issues when deploying or running in different environments. Using virtual environments and proper package management (e.g., `pip`, `setuptools`) is generally more robust.

Right, so I understood that, since I was using a virtual environment, I shouldn't mess up with the sys.path. Fair enough. 

So I simply imported litstudy with `import litstudy` and an error occurred 😩
```
# ["ImportError: cannot import name 'triu' from 'scipy.linalg'"]
```

Oh no! And what is this now? Well searching a bit around I understood that in scipy 1.13 'triu' was deprecated, however gensim did not set its dependencies to scipy to an older version that was not affected by this change yet. So, when you use gensim and your scipy version is 1.13 then you get this error. Solution found on [StackOverflow](https://stackoverflow.com/questions/78279136/importerror-cannot-import-name-triu-from-scipy-linalg-when-importing-gens): just install an older version of scipy!

Easy? No. Even though I tried to `pip install "scipy<1.13"` the already installed package (how, I don't know) and the newly installed package conflicted. So much that when I tried to check the version with `scipy.__version__` it said that it was using 1.13.1; however when I tried to uninstall the package with `pip uninstall scipy` the package that was uninstalled was 1.12. Crazy things can happen with packages 😲

However after a little bit of negotiation with chatgpt, we found the solution: new environment, first install scipy (right version) in this new env and then litstudy. 

In the terminal (in vscode Terminal > new terminal), I checked the pip and python versions with: 

```
which python 
which pip
```

then I needed to create a clean virtual environment in the same folder I was working with:

```
python -m venv myenv
source myenv/bin/activate
```

I installed the version of scipy still with the triu function inside:

```
pip install "scipy<1.13"
```

and checked **in the .ipynb** if the right version was installed. It outputted 1.12

```
import scipy
print("SciPy version:", scipy.__version__)
```

after that I could regularly `pip install litstudy` and `import litstudy` normally. No issues found 🎉

### pybliometrics

I wanted to use Scopus for retrieving potentially relevant papers for my literature review. I already had a Scopus API key with the university, however it did not cost me much to get the API... it was more challenging to set up the university VPN ahaha

Supposing that you have a Scopus API and supposing that you're using a VPN or you are on site, then the pybliometrics [config page](https://pybliometrics.readthedocs.io/en/stable/configuration.html) really helped out. 
I followed the instructions and `import pybliometrics`and then `pybliometrics.scopus.init()`. In vscode the procedure is guided: I think you need to enter your API key and then press enter another time and that's it! You can start doing your queries! 


