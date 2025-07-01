
# 🛒 Amazon E2E Automation Project

Automated the **complete Amazon purchasing flow** using **Selenium WebDriver (Python)** with **pytest** and **Page Object Model (POM)**.  
This project simulates a real-world **end-to-end test** from login to checkout.

---

## 🚀 Features

✅ **Login automation using saved cookies** (`pickle`)  
✅ **Product Search → Add to Cart → Checkout**  
✅ **Pytest Integration** with `conftest.py` for setup/teardown  
✅ **Exception Handling** for Amazon Prime popups  
✅ **Screenshot capture on test failures**  
✅ **Assertions for validation checkpoints**  
✅ **Modular POM structure with reusable locators**

---

## 🧪 Test Flow

1. **Login**  
   - Loads cookies if available, else logs in with credentials.
2. **Search & Add to Cart**  
   - Searches product, selects the first result, adds to cart.
3. **Checkout**  
   - Proceeds to checkout

---

## 🗂️ Folder Structure

```
Amazon_E2E/
│
├── conftest.py                # Pytest setup & teardown (browser init)
├── login_script.py            # Cookie save/load logic
├── requirements.txt           # Project dependencies
│
├── screenshots
├── tests/
│   └── TestE2E.py             # Main end-to-end test
│
├── pages/
│   ├── HomePageLocators.py
│   ├── LoginPageLocators.py
│
├── utils/
│   ├── ItemsLocators.py
│   ├── UtilitiesLocators.py  # Includes test data, cookie path, credentials
│
└── Login_cookies.pkl          # Saved login session (auto-created)
```

---

## 🛠️ Technologies Used

- **Language:** Python 3.8+
- **Automation:** Selenium WebDriver
- **Test Runner:** Pytest
- **Framework:** Page Object Model (POM)
- **Extras:** `pickle`, screenshots, exception handling

---

## ⚙️ Setup Instructions

1. **Clone the Repo**
```bash
git clone https://github.com/chenchuenay/Amazon_E2E.git
cd Amazon_E2E
```

2. **Install Dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the Tests**
```bash
pytest tests/TestE2E.py
```

4. **Login First Time (if cookies not saved)**
- Edit credentials in `UtilitiesLocators.py`
- Run `login_script.py` manually to save cookies

---

## ⚠️ Note

> Replace your **email/password** in `UtilitiesLocators.py` before first run.  
> Make sure your Amazon account is working and not 2FA locked.

---

## 📸 Screenshots
___
The following screenshots have been added to the screenshots/ folder to visually support the test flow and reports:
>	•	✅ login_cookie_sucess.png – After successful login and cookie save
>	•	🖥️ Login_cookies_terminal.png – Terminal output confirming cookies saved
>	•	🛒 passed_01-07-25_14-34-18.png – End-to-end test successful (Product flow)
>	•	🛒 passed_01-07-25_14-44-10.png – Another successful run of the test flow
>	•	❌ Test_failed.png – Screenshot captured when test failed (simulated failure)
>	•	📄 Test_Failure_html_report.png – HTML report showing failed test case
>	•	🖥️ Test_failure_terminal.png – Terminal output for failed test case
>	•	✅ test_passed_01-07-25_14-15-05.png – Successful test run screenshot
>	•	📄 Test_passed_html_report.png – HTML report showing successful test case
>	•	🖥️ test_passed_terminal.png – Terminal output for a passed test run

---

## 🙏 Thanks & Credits

This project was built by **S. Enay Kumar** to practice real-world QA automation skills while actively seeking a full-time QA role (Manual + Automation).  

Feel free to connect or review! 🤝
