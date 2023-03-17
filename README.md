## Short description
UI test of https://demowebshop.tricentis.com/

## Introduction

This repository contains sets of UI tests of basic web elements on the example of demowebshop Tricentis. All tests were designed with a usage of Page Object Model pattern and Selenium Webdriver in Python.

## Set-up
1) Install all requirements: 
 ```
 pip3 install -r requirements
 ```
2) Download ChromeWebdriver compatible with your current browser version (https://chromedriver.chromium.org/downloads)

3) Run tests through the terminal or code editor:

## Tests description

* Test Catalogue Operations: Browsing catalogue, testing boundary quantity values, checking item available options (colors, quantity, model etc)
* Test CS: Checking contains and length in "Blog" section
* Test Registration: Performing full process of registration of a new user, checking validation fields 
* Test Searching and Sorting: Checking and validating of sorting and searching options
* Test URLS: Checking status code of main links
* Test Wishlist: Checking wishlist related options and actions
