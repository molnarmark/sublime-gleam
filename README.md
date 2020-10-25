# Gleam Sublime

Syntax Definition & **gleam format** support for the [Gleam](http://gleam.run) Programming Language in Sublime Text.

## Installation

If this package is found on [Package Control](http://packagecontrol.io), then press `CTRL + Shift + P` inside Sublime, type `Gleam` and press enter.

Otherwise, go to your `Packages` folder, and execute

```bash
git clone git@github.com:molnarmark/sublime-gleam.git
```

## Settings

`format_on_save` is enabled by default, to disable head over to

- Preferences
- Package Settings
- Gleam
- Gleam Settings
- change `format_on_save` to false

If you prefer using a key binding to format, add this to your **Sublime Keymap** with the preferred key:

```json
{ "keys": ["<key>"], "command": "gleam_fmt" }
```

Alternatively, you can also format via the menu, `CTRL + Shift + P` and select the `Gleam: Format` option.

### Enjoy!
