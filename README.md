
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
   - Proceeds to checkout, selects COD (Cash on Delivery) and confirms (mock).

---

## 🗂️ Folder Structure

```
Amazon_E2E/
│
├── conftest.py                # Pytest setup & teardown (browser init)
├── login_script.py            # Cookie save/load logic
├── requirements.txt           # Project dependencies
│
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
- **Extras:** `pickle`, logging, exception handling

---

## ⚙️ Setup Instructions

1. **Clone the Repo**
```bash
git clone https://github.com/yourusername/Amazon_E2E.git
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

## 📸 Screenshots (Optional)
You can include screenshots of:
- Passed test logs  
- Screenshot on test failure  
- Structure of cookie file

---

## 🙏 Thanks & Credits

This project was built by **S. Enay Kumar** to practice real-world QA automation skills while actively seeking a full-time QA role (Manual + Automation).  

Feel free to connect or review! 🤝
