## NumpadVtuber

Change your photo appearance using the numpad on your keyboard, which you rarely use.

#### Usage

1. Collect several (up to 10) images.
2. If the images have the same unique and nontransparent background, put them directly into `images` folder and rename them to `[0-9].png` accordingly.
3. Otherwise if they have transparent background, you can put them in `raw` folder and use `bg_prep.py` to preprocess.
4. Run `python display.py`.
5. Have fun!

#### TODO

1. Custom key binding configuration.
2. GIF display
3. Image folder recursive enumeration.
4. Fix bugs.
5. Give credits to the example images.

#### Known Bugs

1. The picture cannot update when the window is minimalized.

 