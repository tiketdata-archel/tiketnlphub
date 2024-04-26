# Project Description

TiketNLPHub is a NLP library focused for fast experiments without having worry or think too much on the preprocessing side. It provides basic and simple text preprocessing methods that are commonly applied in tiket.com's NLP project.

# Quick Start
```
>>> from tiketnlphub.preprocessing.cleaner import remove_digits, remove_hashtags
>>> from tiketnlphub.preprocessing.re_pattern import RegexString
>>> text = remove_digits("I spent 2 nights here and it was really good")
>>> text
I spent  nights here and it was really good
>>> text = remove_hashtags("thank you #JWMariott its been a pleasure to stay in your hotel!")
>>> text
thank you  its been pleasure to stay in your hotel!
```

