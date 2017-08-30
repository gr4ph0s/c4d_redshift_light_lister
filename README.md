# c4d_redshift_light_lister
A light lister for Redshift to Cinema 4D, note this project is a bit old, don't judge my code style on this one.

## Preview
The version showed in the video is the v1, some features was added since it.
[Redshift C4D Light Lister](https://vimeo.com/213734948)

## Download
You can download the actual version on github or if you prefer a zip [here](http://graphos.xyz/files/Plugin/graph_redshift_light_lister/graph_redshift_lightlister.zip)
- Unizip in your c4d plugin folder
- Enjoy !

## Features
- List all c4d lights
- Acces to all light parameter throught an UI
- Easily choose wich parameter to display in the UI
- Order lights independantly from the scene order

## About source code
My initial idea was to do a lights lister for any render engine. 
But due to a c4d limitation of wich scroll bar is actually scrolled I was not able to synchronize scroll bar for each render engine.
So I end up with 1 plugin for each render engine.
This end's to mess a bit the class structure since is mainly thinked for multiple render engine, but when I will have some time I will do 
- Code Cleaning
- Comment
- Port it to C++ and make a light lister for all renders engines in one plugin :)
