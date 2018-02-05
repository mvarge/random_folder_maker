# Random Folder Maker
Program to generate a random folder tree.

## About
Useful for scenarios where you need to simulate a large tree of folders, subfolders and files.

The program relies on random samples so you can get different results depending of the maximum of folder, depth and files that you set up. You can use it both as a command line or a Python module.

## How to use it

Calling as a command line:

```
$ python tree_creator.py -n parent_folder -p 3 -d 3 -f 3
$ find parent_folder/
parent_folder/
parent_folder/comprehendo
parent_folder/comprehendo/copia.txt
parent_folder/comprehendo/spectaculum
parent_folder/comprehendo/spectaculum/differtus.txt
parent_folder/comprehendo/spectaculum/fortuna.txt
parent_folder/comprehendo/spectaculum/persolvo
parent_folder/comprehendo/spectaculum/persolvo/creta.txt
parent_folder/comprehendo/spectaculum/persolvo/demitto
parent_folder/comprehendo/spectaculum/persolvo/proprius.txt
parent_folder/comprehendo/spectaculum/persolvo/templovium.txt
parent_folder/consuo
parent_folder/consuo/congrego.txt
parent_folder/consuo/muto.txt
parent_folder/consuo/pes
parent_folder/consuo/pes/tricesimus
parent_folder/consuo/pes/tricesimus/crur
parent_folder/consuo/pes/tricesimus/praebeo.txt
parent_folder/consuo/vesica.txt
```

## Author
Marcelo Marques da Silva Varge (marcelo.varge@gmail.com)
