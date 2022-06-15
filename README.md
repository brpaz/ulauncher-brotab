# Brotab Ulauncher Extension

> Control your browser tabs directly from Ulauncher with [Brotab](https://github.com/balta2ar/brotab).

[![Ulauncher Extension](https://img.shields.io/badge/Ulauncher-Extension-yellowgreen.svg?style=for-the-badge)](https://ext.ulauncher.io/)
[![CI Status](https://img.shields.io/github/workflow/status/brpaz/ulauncher-brotab/CI?color=orange&label=actions&logo=github&logoColor=orange&style=for-the-badge)](https://github.com/brpaz/ulauncher-brotab)
[![license](https://img.shields.io/github/license/brpaz/ulauncher-brotab.svg?style=for-the-badge)](LICENSE)



## Demo

![Demo](demo.gif)

## Requirements

* [Ulauncher](https://github.com/Ulauncher/Ulauncher) > 5.0
* Python >= 3

Before installing this extension make sure you have [Brotab](https://github.com/balta2ar/brotab) installed and working as specified on their README. Otherwise this extension won´t work.

You also need to have some Python packages installed on your system.

You can do so, by running the following command:

```sh
pip install --user memoization==0.4.0
```

In some systems, you might need to run `pip3` instead of `pip`.

## Install

Open ulauncher preferences window -> extensions -> add extension and paste the following url:

```
https://github.com/brpaz/ulauncher-brotab
```

## Usage

Use the keyword **brotab** to list your tabs. Clicking on an item will switch the browser to the specified active tab)

You can also close existing tabs by using `cl`, `cltab` or `cttab` keywords instead of `brotab`


## Development

```
git clone https://github.com/brpaz/ulauncher-brotab
make link
```

The `make link` command will symlink the cloned repo into the appropriate location on the ulauncher extensions folder.

To see your changes, stop ulauncher and run it from the command line with: `make dev`.

The output will display something like this:

```
2020-11-15 10:24:16,869 | WARNING | ulauncher.api.server.ExtensionRunner: _run_process() | VERBOSE=1 ULAUNCHER_WS_API=ws://127.0.0.1:5054/ulauncher-brotab PYTHONPATH=/usr/lib/python3.8/site-packages /usr/bin/python3 /home/bruno/.local/share/ulauncher/extensions/ulauncher-brotab/main.py
```

Open another terminal window and execute the command displayed, "starting at VERBOSE=1". This will activate the extension.

To see your changes, CTRL+C the previous command and run it again to refresh.

## FAQ

### My extension doesnt install: Key Error

This error usually indicates a missing Python package in your system. Please [read](https://ulauncher-extension-doesnt-install-and-now.netlify.app/).

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 💛 Support the project

If this project was useful to you in some form, I would be glad to have your support.  It will help to keep the project alive and to have more time to work on Open Source.

The sinplest form of support is to give a ⭐️ to this repo.

You can also contribute with [GitHub Sponsors](https://github.com/sponsors/brpaz).

[![GitHub Sponsors](https://img.shields.io/badge/GitHub%20Sponsors-Sponsor%20Me-red?style=for-the-badge)](https://github.com/sponsors/brpaz)


Or if you prefer a one time donation to the project, you can simple:

<a href="https://www.buymeacoffee.com/Z1Bu6asGV" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a>

## Author

👤 **Bruno Paz**

* Website: [brunopaz.dev](https://brunopaz.dev)
* Github: [@brpaz](https://github.com/brpaz)
* Twitter: [@brunopaz88](https://twitter.com/brunopaz88)

## 📝 License

Copyright © 2020 [Bruno Paz](https://github.com/brpaz).

This project is [MIT](https://opensource.org/licenses/MIT) licensed.

<a href="https://www.flaticon.com/free-icons/tab" title="tab icons">Tab icons created by Freepik - Flaticon</a>
