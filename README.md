# Brotab Ulauncher Extension

[![Ulauncher Extension](https://img.shields.io/badge/Ulauncher-Extension-yellowgreen.svg?style=for-the-badge)](https://ext.ulauncher.io/)
[![CI Status](https://img.shields.io/github/workflow/status/brpaz/ulauncher-brotab/CI?color=orange&label=actions&logo=github&logoColor=orange&style=for-the-badge)](https://github.com/brpaz/ulauncher-brotab)
[![license](https://img.shields.io/github/license/brpaz/ulauncher-brotab.svg?style=for-the-badge)](LICENSE)

> Control your browser tabs directly from Ulauncher with [Brotab](https://github.com/balta2ar/brotab).

## Demo

![Demo](demo.gif)

## Requirements

* [Ulauncher](https://github.com/Ulauncher/Ulauncher) > 5.0
* Python >= 3

Before installing this extension make sure you have [Brotab](https://github.com/balta2ar/brotab) installed and working as specified on their README. Otherwise this extension won´t work.

## Install

Open ulauncher preferences window -> extensions -> add extension and paste the following url:

```
https://github.com/brpaz/ulauncher-brotab
```

## Usage

Use the keyword **brotab** to list your tabs. Clicking on an item will switch the browser to the specified active tab)

The tabs are cached for 1m. You can force a refresh by typing `brotab :` and select the "Refresh tabs" option from the list.

## Development

```
git clone https://github.com/brpaz/ulauncher-brotab
make link
```

The `make link` command will symlink the cloned repo into the appropriate location on the ulauncher extensions folder.

To see your changes, stop ulauncher and run it from the command line with: `make dev`.

## Contributing

All contributions are welcome. Just open an issue and/or create a PR.

If you like my work, feel free to "Buy me a Coffee"

<a href="https://www.buymeacoffee.com/Z1Bu6asGV" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a>

## License

MIT &copy; Bruno Paz
