# Image to ASCII

A simple and easy to use program, made using pillow to convert Images into ASCII 
based text format.

## ASCII Conversion demo

<details>
<summary>Image</summary>

![Cat Image](https://github.com/janaSunrise/image-to-ascii/blob/main/cat.jpg)

</details>

<details>
<summary>ASCII Output</summary>

```txt
&&&%%%%%??????????????*************+++++++++++++++
&&%%%%%%?????????????**************+++++++++++++++
&&%%%%%????????????****************+++++++++++++++
&%%%%%????????????****************++++++++++++++++
&%%%%?????????????****************++++++++++++++++
&%%%%?????????????****************++++++++++++++++
%%%%%?????????????**?*********?****+++++++++++++++
??????????????????*?%%*******%&?****++++++++++++++
******????????????*?%&%*****%&&%******++++++++++++
**********??????????%%&&?%?%S&S&*******+++++++++++
**+++++++**********?&?%#####S&S&**********++++++++
++++++++++++++*****?&%%&SS#SSS#&+++*++++++++++++++
+++++++++++++++++++?#%%&&SSSSS#%++++++++++++++++++
+++++++++++++++++++*S&&&?%&SSS#%++++++++++++++++++
+++++++++++++++++++*%&&S**%&SSS%++++++++++++++++++
+++++++++++++++++++?&&&S?+%#SSS%++++++++++++++++++
++++++++++++++****+*?%&&*;%SSS??++++++++++++++++++
++++++++**?%%%&&&&%%?%?*;*??%%%*++++++++++++++++++
+++++++*%SSSSSSSSSSS**+;+?*++**+++++++++++++++++;+
++++++*%S#SS########*;+;+**+++++++++++++++++++++++
+++++*?S#SSSS##@@##S?;;++++++++**+++++++++++++++++
++++**%##SSSSS#####S?*;;+++++++**+++++++++++++++++
++++**?SSSSSS######&%*+++++++++*?+++++++++++++++;+
+++***?%SSSSSSS###S%%?*++****++?%*++++++++++++++++
+++++**?&SSSSSSSSS%%%????****+*%%%++++++++++++++++
+++++++*?&SSSSSSS&%%%%?%%?*+*+*%&&&*++++++++++++++
++++++++**?&S#S#S&&&&&%&&%****?&S##&?*++++++++++++
+++++++++++**%&S&&S&S&%&#&?***%S#@##S&*++++++++;;;
++++++++++++++**%SSS&*+*S#S%*?%%&%%%?*;;;;;;;;;;;;
+++++++;;++++++++*??+;+++%*++;;;;;;;;;;;;;;;;;;;;;
++++++;;++++++;;;;+;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;+
+++++++++++;;;++++;;;;;+++++++;;;;;;;;;;;;;;;;;;++
*+++++++;;;;;+++;;;;;++++++++;;;;;;;;;;;;;;;;;++++
```

</details>

## Installation and usage

Pipenv package manager is used here to bundle the dependencies and manage them.
To install the dependencies, you need to use `pipenv sync -d`. It installs pillow.

You can use the function inside `to_ascii.py` called `image_to_ascii` for conversion,
and integrating in your program, And test it using the test script given (`test.py`) by 
running it with the positional arguments.

Here are the steps to run it.
- Enable the virtual env: `pipenv shell`
- Run the demo: `python test.py <IMAGE PATH>`

And it should print out the ASCII format of the image.

<div align="center">
Made by Sunrit Jana with <3
</div>
