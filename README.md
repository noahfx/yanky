# yanky -- Easy and Simple copy and paste Python module for GNU/Linux systems

In order to get yanky fully functional either one of the following software
needs to be installed in your system:
 * xsel: http://www.vergenet.net/~conrad/software/xsel
 * xclip: https://sourceforge.net/projects/xclip
 
 In Debian based systems they can be installed via the package manager.
 
Usage:

```
from yanky import copy, paste

#Copy text to OS clipboard
copy('Text to be copied to clipboard')

#Paste from OS clipboard

text_from_cb = paste()
```
