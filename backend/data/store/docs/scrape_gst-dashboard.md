# GST Dashboard and Company Summary

Source: https://taxone.vyapar.com/help/articles/gst-dashboard

[All Collection](/help)[GST Automation](/help/collections/gst-automation)[GST Dashboard and Company Summary](/help/articles/gst-dashboard)

[Dashboard Header (Top Navigation)](#dashboard-header-top-navigation-)[1. GSTIN Summary (Top Widget Bar)](#1-gstin-summary-top-widget-bar-)[2. Filing Status: Month and Year](#2-filing-status-month-and-year)[3. Filing Summary (Total Filing Chart)](#3-filing-summary-total-filing-chart-)[4. GSTR-1 & GSTR-3B Detailed Charts](#4-gstr-1-gstr-3b-detailed-charts)[5. Notices & Alerts](#5-notices-alerts)[Company Summary](#company-summary)[1. Top Section – Company Name & Period Selection](#1-top-section-company-name-period-selection)[2. Return Filing Tracker](#2-return-filing-tracker)[3. GSTR1 Table](#3-gstr1-table)[4. GSTR3B Table](#4-gstr3b-table)[5. GSTR1 vs GSTR3B Chart](#5-gstr1-vs-gstr3b-chart)[6. GSTR2B vs GSTR3B Chart](#6-gstr2b-vs-gstr3b-chart)

# GST Dashboard and Company Summary

This dashboard is built for busy accountants and firms to quickly view compliance across all their clients, GSTINs, and filing timelines — in a single glance.

📊 Your Suvit Dashboard is your command center — it shows everything about your GSTINs, return status, deadlines, and filings in one place. Here's how to understand each section:

---

### Dashboard Header (Top Navigation)

![1.webp](https://strapi.suvit.io/uploads/1_b960c7fa20.webp)

* The top bar includes:

  → **Dashboard label** to show your current view

  → **Filing Period selector** (e.g., Apr 2025 – Mar 2026)

  → **Company stats**:

  → *Total Companies*: Number of registered companies

  → *Unsynced Companies*: Data needs syncing

---

#### 1. GSTIN Summary (Top Widget Bar)

* You’ll see colored blocks with quick stats:

  → **Total GSTIN** – All GSTINs tracked

  → **Valid GSTIN** – GSTINs verified as active

  → **Invalid GSTIN** – Marked as incorrect

  → **Active / Suspended / Cancelled** – Status-wise GSTIN count

  → Helps you track GST registration health easily.

---

#### 2. Filing Status: Month and Year

* A clear table showing:

  → GSTR-1 & GSTR-3B returns

→ Number of returns:

```
 → **Total** to be filed

 → **Pending** (still due)

 → **Completed** (already filed)
```

→ It also reminds you of **due dates**:

---

#### 3. Filing Summary (Total Filing Chart)

* A donut chart visualizing:

→ **Total Filings** (e.g., 3 tracked returns)

```
 → Breakdown of:

 → ✅ OnTime Filing

 → ⚠️ Late Filing
```

---

#### 4. GSTR-1 & GSTR-3B Detailed Charts

* These show return-wise filing:

  → For each return type:

  → Total GSTINs considered

  → Status: OnTime, Late, or Not Filed

  → Visual representation helps spot delay trends instantly.

---

#### 5. Notices & Alerts

* Placeholder widgets indicating future updates for:

  → **Notices Received**

  → **Filing Alerts & System Notices**

  → Suvit is actively improving this section.

---

### Company Summary

* This view helps CAs and tax professionals keep each client company’s filings, mismatches, and liabilities in check—month by month, chart by chart. One screen, total control!

![2.webp](https://strapi.suvit.io/uploads/2_f32ebfd700.webp)

#### 1. Top Section – Company Name & Period Selection

→ **Company Name** (e.g., Suvit) and GSTIN

→ **Period Dropdown** (Apr 2024 – Mar 2025) lets you pick the financial year you're viewing

---

#### 2. Return Filing Tracker

* Tracks both **GSTR1** and **GSTR3B** for each month

  → Green Check ✔️ = On-time Filing

  → Orange Clock 🕓 = Late Filing

  → Blue Circular Arrows 🔄 = Processing

  → Dash (—) = No Filing or Not Applicable

  → Use this grid to check return compliance status across the year

---

#### 3. GSTR1 Table

* Monthly summary of outward supplies:

  → **Month**: Filing month

  → **Total Invoice**: Number of invoices reported

  → **Taxable Amount**: Value before GST

  → **Total Tax Amount**: GST value (CGST + SGST + IGST)

---

#### 4. GSTR3B Table

* Monthly summary of summary return:

  → **Total Tax Liability**: GST to be paid

  → **ITC**: Input Tax Credit claimed

  → **Total Tax Paid**: Actual payment done

---

#### 5. GSTR1 vs GSTR3B Chart

* Visual comparison of outward liability:

  → Line 1: GSTR1 Tax Liability (sales data)

  → Line 2: GSTR3B Tax Liability (actual filed)

  → Useful for spotting mismatch in reporting

---

#### 6. GSTR2B vs GSTR3B Chart

* Compare ITC vs filed liability:

  → Line 1: GSTR2B Tax Liability (vendor data)

  → Line 2: GSTR3B Tax Liability (filed amount)

  → Helpful for input credit tracking and under/over claiming alerts

---