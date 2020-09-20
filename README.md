# Sample Test Cases

### Installation:

Install all necessera python packages with pip:
```bash
pip3 install --user -r requirements.txt
```

To use ui selenium tests you need Selenium WebDriver.
If you want to use Chrome like I do, you need to install chromedriver.
You can download it for your version of Chrome from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).

Be sure to save it to the following folder:
```bash
ui-testing/drivers/
```

In case you use ***Firefox***, change following line in ```main.py```:
```python
self.driver = webdriver.Chrome(DRIVER_PATH)
```
with:
```
self.driver = webdriver.Firefox()
```

### Usage:

#### UI Testing:
```bash
cd ui-testing && python3 main.py
```

#### API testing:
```bash
cd api-testing && pytest -v 0?_test.py
```
