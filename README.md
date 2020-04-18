# Primely Package

<!-- ##### Analyse your paycheck -->

[![Generic badge](https://img.shields.io/badge/python-v3.7.4-336E9F.svg)](https://shields.io/)

<!-- ![Theme image](demo/output/income_timechart.png) -->
![Theme image](images/primely_package.jpg)

## Getting Started
<!-- TODO: Update below dates every time you commit!  -->
**Update(April 18, 2020)**: Paycheck at where I work is published by a PDF file. Just reading them, might be enough for checking errors, but do you not want to see *trends* over time?

This package can provide a json response where a series of paychecks are organized and stored in one file. Download and try putting your pdf file in the suggested folder where instructed below.

### Prerequisites
* Paycheck downloaded (in pdf format). 
* You are either my colleague or/and work at the same company. Because **this package only works for paychecks from where I work now**.


### Installing
There's two way you could use this package.
1. Git clone this repository.
2. Extract from tarball.

#### 1. Git clone
Git clone this package.
```bash
$ git clone https://github.com/yoshiki-o0/primely_package.git
```

Move to the home directory of the package.

Install dependent packages.
```bash
$ pip install requirements.txt
```


#### 2. Extract from tarball
Download tarball from `primely_package/dist/<package_name>`.

Move to the work directory where tarball is set.
```bash
$ cd <path_to_work_dir>
```

Extract the package.
```bash
$ tar -zxvf <package_name>
```

## Running the test
### Analyse your data
Set your pdf files at `data/pdf`.

Run <br>
```bash
$ python <package_home_dir_path>/main.py
```


### Check your json
If the process completes successfully, the json response could be checked at `data/output/report/paycheck_timechart.json`.


## Built With
* [pdfminor.six](https://github.com/pdfminer/pdfminer.six) - Used to extract text from pdf files.

## Polished With
* pepe8, flake8, (Comming soon) pylint
* (Comming soon) Unittest

## Licence
PaycheckGraph is freely available for free non-commercial use and may be redistributed under conditions. Please, see the licence for further details.