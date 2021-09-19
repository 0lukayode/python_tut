
## Virtual environments

[Virtual environments](https://docs.python.org/3.7/tutorial/venv.html) allow you to install packages into an isolated folder. This allows you to better manage versions.

To create a virtual environment, decide upon a directory where you want to place it, and run the venv module as a script with the directory path:

``` 
    python3 -m venv env
```
This would create a v_env directory 

Once you’ve created a virtual environment, you may activate it.

On Windows, run:

```
    env\Scripts\activate.bat
```
On Unix or MacOS, run:

```
    source env/bin/activate
```