
# ðŸ›’ Amazon E2E Automation Project

Automated the **complete Amazon purchasing flow** using **Selenium WebDriver (Python)** with **pytest** and **Page Object Model (POM)**.  
This project simulates a real-world **end-to-end test** from login to checkout.

---

## ðŸš€ Features

âœ… **Login automation using saved cookies** (`pickle`)  
âœ… **Product Search â†’ Add to Cart â†’ Checkout**  
âœ… **Pytest Integration** with `conftest.py` for setup/teardown  
âœ… **Exception Handling** for Amazon Prime popups  
âœ… **Screenshot capture on test failures**  
âœ… **Assertions for validation checkpoints**  
âœ… **Modular POM structure with reusable locators**

---

## ðŸ§ª Test Flow

1. **Login**  
   - Loads cookies if available, else logs in with credentials.
2. **Search & Add to Cart**  
   - Searches product, selects the first result, adds to cart.
3. **Checkout**  
   - Proceeds to checkout, selects COD (Cash on Delivery) and confirms (mock).

---

## ðŸ—‚ï¸ Folder Structure

```
Amazon_E2E/
â”‚
â”œâ”€â”€ conftest.py                # Pytest setup & teardown (browser init)
â”œâ”€â”€ login_script.py            # Cookie save/load logic
â”œâ”€â”€ requirements.txt           # Project dependencies
â”‚
â”œâ”€â”€ tests/
â”‚   â””â”€â”€ TestE2E.py             # Main end-to-end test
â”‚
â”œâ”€â”€ pages/
â”‚   â”œâ”€â”€ HomePageLocators.py
â”‚   â”œâ”€â”€ LoginPageLocators.py
â”‚
â”œâ”€â”€ utils/
â”‚   â”œâ”€â”€ ItemsLocators.py
â”‚   â”œâ”€â”€ UtilitiesLocators.py  # Includes test data, cookie path, credentials
â”‚
â””â”€â”€ Login_cookies.pkl          # Saved login session (auto-created)
```

---

## ðŸ› ï¸ Technologies Used

- **Language:** Python 3.8+
- **Automation:** Selenium WebDriver
- **Test Runner:** Pytest
- **Framework:** Page Object Model (POM)
- **Extras:** `pickle`, logging, exception handling

---

## âš™ï¸ Setup Instructions

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

## âš ï¸ Note

> Replace your **email/password** in `UtilitiesLocators.py` before first run.  
> Make sure your Amazon account is working and not 2FA locked.

---

## ðŸ“¸ Screenshots (Optional)
You can include screenshots of:
- Passed test logs  
- Screenshot on test failure  
- Structure of cookie file

---

## ðŸ™ Thanks & Credits

This project was built by **S. Enay Kumar** to practice real-world QA automation skills while actively seeking a full-time QA role (Manual + Automation).  

Feel free to connect or review! ðŸ¤