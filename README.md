# eCASA Core Platform 🏡💳

Welcome to the main repository for eCASA, the premier platform for cute rental listings and home sales. 

> ⚠️ **URGENT NOTICE (August 2026):** Following the acquisition of the ApexFin platform, all teams are currently redirected to integrating automated rent processing. The hard deadline for this integration is **this Friday**.

---

## 🛠️ Project Structure

*   `/api` - Backend REST endpoints and webhooks for payment routing.
*   `/services` - Core business logic for real estate listings and transaction processors.
*   `/ui` - Frontend React components for the listing engine and payment dashboard.

## 🚀 Quick Start

### Prerequisites
*   Python 3.11+
*   Node.js 18+

### Backend Setup
1. Clone the repository:
   ```bash
   git clone [https://github.com/ecasa-dev/ecasa-rent-payments.git](https://github.com/ecasa-dev/ecasa-rent-payments.git)
   cd ecasa-rent-payments
   ```
2. Set up your virtual environment and install these dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

### Frontend Setup
Navigate to the UI directory and install these packages:

```bash
cd ui
npm install
```

## 🛑 Recent Integration Notes (Read Before Committing)

*   **Fintech Webhooks:** `api/webhooks/payment.py` is currently listening to temporary sandbox events. Do not use production signing keys in local testing.
*   **Database Sync:** Sarah resolved the race condition in `services/listings.py`. If your local environment fails to sync property statuses, clear your local Redis cache.
  
## 👥 Contributors

*   Izzy (Lead Platform Engineer)
*   Alex M. (Fintech Integration Lead)
*   Sarah T. (UI/UX & Listings Engine)
*   Devon K. (Backend / Infrastructure)