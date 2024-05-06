<a name="readme-top"></a>
<!--
Back to top hyperlink
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

TiketNLPHub is a NLP library focused for fast experiments without having worry or think too much on the preprocessing side. It provides basic and simple text preprocessing methods that are commonly applied in tiket.com's NLP project.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

### Installation

```
pip install git+https://github.com/tiketdata-archel/tiketnlphub.git@main
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

```
>>> from tiketnlphub.preprocessing.cleaner import remove_digits, remove_hashtags
>>> text = remove_digits("I spent 2 nights here and it was really good")
>>> text
I spent  nights here and it was really good
>>> text = remove_hashtags("thank you #JWMariott its been a pleasure to stay in your hotel!")
>>> text
thank you  its been pleasure to stay in your hotel!
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Archel Taneka - archel.sutanto@tiket.com

Project Link: [https://github.com/tiketdata-archel/tiketnlphub](https://github.com/tiketdata-archel/tiketnlphub)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/tiketdata-archel/tiketnlphub.svg?style=for-the-badge
[contributors-url]: https://github.com/tiketdata-archel/tiketnlphub/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/tiketdata-archel/tiketnlphub.svg?style=for-the-badge
[forks-url]: https://github.com/tiketdata-archel/tiketnlphub/network/members
[stars-shield]: https://img.shields.io/github/stars/tiketdata-archel/tiketnlphub.svg?style=for-the-badge
[stars-url]: https://github.com/tiketdata-archel/tiketnlphub/stargazers
[issues-shield]: https://img.shields.io/github/issues/tiketdata-archel/tiketnlphub.svg?style=for-the-badge
[issues-url]: https://github.com/tiketdata-archel/tiketnlphub/issues
[license-shield]: https://img.shields.io/github/license/tiketdata-archel/tiketnlphub.svg?style=for-the-badge
[license-url]: https://github.com/tiketdata-archel/tiketnlphub/blob/master/LICENSE.txt
