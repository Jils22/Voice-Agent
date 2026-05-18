# GST Reconciliation Summary: A Step-by-Step Overview

Source: https://taxone.vyapar.com/help/articles/gst-reco-overview

[All Collection](/help)[GST Automation](/help/collections/gst-automation)[GST Reconciliation Summary: A Step-by-Step Overview](/help/articles/gst-reco-overview)

[Important Note](#important-note)[A. Sync Voucher](#a-sync-voucher)[B. GST Data](#b-gst-data)[1. Select Company & Period](#1-select-company-period)[2. Login to GST Portal](#2-login-to-gst-portal)[3. Enter OTP](#3-enter-otp)[4. View GSTR-1 Summary](#4-view-gstr-1-summary)[5. Monthly Transaction Reconciliation](#5-monthly-transaction-reconciliation)[6. Voucher-Level View](#6-voucher-level-view)[7. Vendor-Level View](#7-vendor-level-view)[🧾 Summary](#-summary)

# GST Reconciliation Summary: A Step-by-Step Overview

Use Suvit’s GST Reconciliation to track returns, compare Eligible vs. Claimed ITC, and match GSTR-1 with your sales register using Tally data reports.

### Important Note

#### A. Sync Voucher

* Click on **Sync Voucher** to fetch the latest (Sales/Purchase) data from Tally.
* Suvit will display the data available in Tally up to the time you clicked **Sync Voucher**.

![A.webp](https://strapi.suvit.io/uploads/A_0e6b7202d4.webp)

#### B. GST Data

* Suvit displays the data available on the **GST Portal**.
* Suvit will display the data available in **GST Portal** up to the time you clicked \*\*Sync \*\*.

---

#### 1. Select Company & Period

![1.webp](https://strapi.suvit.io/uploads/1_f00d8cefc6.webp)

→ Choose your desired company from the top dropdown

→ Select the financial year period (e.g., Apr 2024 – Mar 2025) to fetch data for the correct duration.

→ Click **Login to GST Portal** to connect Suvit with the GST portal using the client’s credentials.

---

#### 2. Login to GST Portal

![2.webp](https://strapi.suvit.io/uploads/2_a4f6aff6dc.webp)

→ Fill in the **GST Number** and **Username** used for the portal login.

→ Click **Get OTP** to receive an authentication code.

→ This login is required to fetch return filing data securely.

---

#### 3. Enter OTP

![3.webp](https://strapi.suvit.io/uploads/3_15c81e137a.webp)

→ Enter the OTP received on the registered mobile/email.

→ Click **Get Data** to allow Suvit to fetch GST filings and sales details.

---

#### 4. View GSTR-1 Summary

![4.webp](https://strapi.suvit.io/uploads/4_be3f08794f.webp)

* The **Summary Tab** gives you a bird’s eye view of matching status:
* Categories include:

  → **Matched** – Entries perfectly match between portal & books

  → **Manual Matched** – Entries matched manually

  → **Partially Matched** – Partial data mismatch

  → **Not in Tally/SR** – Found in portal but missing in your books

  → **Not in Portal/GSTIN** – Present in your books but not on the portal

---

#### 5. Monthly Transaction Reconciliation

![5.webp](https://strapi.suvit.io/uploads/5_cd58614b6b.webp)

→ Navigate to the **Transaction → Month View** tab.

* It compares monthly totals for:

  → GSTR-1: Invoice Count, Taxable Amount, Tax Amount

  → Sales Register: Invoice Count, Taxable Amount, Tax Amount

  → **Difference** is highlighted clearly in each row.

  → This helps detect month-wise mismatch in data.

---

#### 6. Voucher-Level View

![6.webp](https://strapi.suvit.io/uploads/6_7065521d53.webp)

→ Go to the **Transaction → Voucher View** tab.

* Each voucher entry is listed with:

  → Party name (as per GST Portal & Sales Register)

  → GSTIN match status

  → Invoice dates comparison

  → Use this view for verifying invoice-level entries line by line.

---

#### 7. Vendor-Level View

![7.webp](https://strapi.suvit.io/uploads/7_027da1b573.webp)

→ Use **Vendor View** to check reconciliation by vendor.

* Shows GSTR-1 vs. Sales Register for each vendor:

  → Invoice Count

  → Taxable & Tax Amount

  → Status like Matched / Partially Matched / Not Found

  → Helps accountants quickly pinpoint vendor-specific mismatches.

---

### 🧾 Summary

This GSTR-1 Reconciliation module helps you:

→ Cross-verify GST Portal data with your Tally/Sales Register.
→ Match data by month, voucher, or vendor.
→ Highlight mismatches and resolve them with ease.