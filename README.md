# Amazon E2E Automation

End-to-end UI test suite for Amazon.ae built with Selenium WebDriver (Python), Pytest, and Page Object Model.

Covers the full purchase flow: login via saved cookies → search → select product → add to cart → checkout.

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3 | Language |
| Selenium WebDriver | Browser automation |
| Pytest | Test framework |
| pytest-html | HTML report generation |
| webdriver-manager | Auto ChromeDriver management |
| python-dotenv | Environment variable management |

---

## Project Structure

```
Amazon_E2E/
│
├── pages/
│   ├── HomePageLocators.py       # Homepage element locators (search, sign-in, cart)
│   └── LoginPageLocators.py      # Login page element locators (email, password, submit)
│
├── utils/
│   ├── ProductLocators.py        # Product-specific locators and test data
│   └── SharedLocators.py         # Shared locators used across multiple tests
│
├── tests/
│   ├── test_e2e.py               # Full E2E flow: search → cart → checkout → assert URL
│   └── test_cart_items.py        # Cart flow: search → add to cart → assert item in cart
│
├── sessions/
│   └── Login_cookies.pkl         # Saved login session (git-ignored)
│
├── screenshots/
│   ├── passed/                   # Screenshots captured at end of successful runs
│   └── failed/                   # Screenshots auto-captured on test failure
│
├── reports/                      # Auto-generated HTML reports (git-ignored)
│
├── login_script.py               # Run once to authenticate and save session cookies
├── conftest.py                   # Browser setup, teardown, failure screenshot hook
├── pytest.ini                    # Pytest configuration
├── requirements.txt
└── .env                          # Credentials — not committed
```

---

## Test Coverage

| Test | Flow |
|------|------|
| `test_purchase_flow` | Search → Select product → Add to cart → Checkout → Assert URL |
| `test_add_item_to_cart` | Search → Select product → Add to cart → Assert item in cart |

---

## Design Decisions

**Cookie-based login:** Amazon's login flow includes passkey and OTP challenges that break standard automation. Cookies are captured once via `login_script.py` and reused across all test runs, bypassing the auth flow reliably.

**Checkout re-auth:** Amazon requires re-authentication before payment even with a valid session (`max_auth_age=900`). The E2E test asserts the checkout redirect is reached — stopping before payment is intentional for a production environment.

**No negative tests:** Amazon's UI prevents invalid flows at the DOM level — the checkout button is removed when the cart is empty, and search always returns results regardless of input. Forced negative scenarios were evaluated and excluded as they would not reflect real application behavior.

---

## Setup & Run

**1. Clone the repo**
```bash
git clone https://github.com/chenchuenay/Amazon_E2E.git
cd Amazon_E2E
```

**2. Create virtual environment**
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Create `.env` file**
```
AMAZON_USERNAME=your_email@example.com
AMAZON_PASSWORD=yourpassword
```

**5. Save login cookies (first time only)**
```bash
python login_script.py
```

**6. Run all tests**
```bash
pytest -v
```

**7. Run a specific test**
```bash
pytest tests/test_e2e.py -v
```

HTML report is auto-generated at `reports/report.html` after every run.
Screenshots are captured to `screenshots/passed/` on success and `screenshots/failed/` on failure.

---

## Notes

- Cookies expire periodically — re-run `login_script.py` if tests fail at login
- Amazon UI changes frequently — locators may need updating if tests break after an Amazon deployment

---

## Author

Built by **Enay Kumar** as part of a QA automation portfolio.