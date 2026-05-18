# IMS

Source: https://taxone.vyapar.com/help/articles/ims

[All Collection](/help)[GST Automation](/help/collections/gst-automation)[IMS](/help/articles/ims)

[1. What is the Document Summary?](#1-what-is-the-document-summary-)[2. Reco Summary – Match Overview](#2-reco-summary-match-overview)[Voucher View – Check Row-Wise Mismatches](#voucher-view-check-row-wise-mismatches)[Link Mismatched Invoices](#link-mismatched-invoices)[Sync Tally If No Invoice Found](#sync-tally-if-no-invoice-found)[3. Take Action on Entries](#3-take-action-on-entries)[Understand Upload Status (TBS)](#understand-upload-status-tbs-)[4. Add Missing Voucher to PR](#4-add-missing-voucher-to-pr)[Fill Voucher Details](#fill-voucher-details)[5. Track Who Took Action](#5-track-who-took-action)[6. Vendor view](#6-vendor-view)[What does the Vendor View show?](#what-does-the-vendor-view-show-)[✅ Summary](#-summary)

# IMS

🔄 IMS (Invoice Matching System) in Suvit – Simple Guide for Easy Reconciliation.
IMS helps you compare GST Portal data with your Purchase Register (PR) to spot and fix mismatches. Here’s how to use it step-by-step with helpful visuals.

📋 IMS – Document Summary Tab (Your First Screen in IMS)
This is the first view when you open IMS module in Suvit. It shows the summary of your documents — sorted by Document Type like B2B or CN (Credit Note).

### 1. What is the Document Summary?

This tab gives you a bird’s eye view of how many invoices are matched, pending, or need your action — document type wise.

![a.webp](https://strapi.suvit.io/uploads/a_b795071277.webp)
→ Document Type: This shows the type of documents – like B2B or CN (Credit Note).

→ Total Invoices: Total number of GST invoices available under each type.

→ Tax Value: The combined taxable value of all these invoices.

### 2. Reco Summary – Match Overview

![1.webp](https://strapi.suvit.io/uploads/1_28b7c874c5.webp)

This is your starting point to check what's matched and what's not.

→ **Matched** – Data perfectly matches between GST and PR.

→ **Manual Matched** – You’ve manually linked the entries.

→ **Partially Matched** – Some values differ.

→ **Not In Tally/PR** – Missing in your Purchase Register or Tally data.

#### Voucher View – Check Row-Wise Mismatches

Voucher View shows invoice-level details under the **Action** tab.

 
→ Click the **eye icon (👁️)** to view full mismatch details.

---

#### Link Mismatched Invoices

![2.webp](https://strapi.suvit.io/uploads/2_850c316a95.webp)

To begin reconciliation:

 
→ Click **Link** under the PR column for the mismatched row.

![3.webp](https://strapi.suvit.io/uploads/3_7f404f9164.webp)

→ This opens a panel showing the GST invoice and lets you match it to an existing PR invoice.

#### Sync Tally If No Invoice Found

![4.webp](https://strapi.suvit.io/uploads/4_7ef23fd2ac.webp)

Can’t find the invoice to link?

 
→ Go to the **Sync Invoice** tab

→ Click **Sync** to pull the latest data from Tally

Then try linking again.

---

### 3. Take Action on Entries

![5.webp](https://strapi.suvit.io/uploads/5_3bdf81a6fe.webp)

Use the **Take Action** dropdown:

→ **Accept** – Confirm the invoice is fine

→ **Reject** – Not acceptable due to mismatch

→ **Pending** – Yet to take action

#### Understand Upload Status (TBS)

![6.webp](https://strapi.suvit.io/uploads/6_84eb9f79d3.webp)

TBS = **To Be Submitted**

→ This tag appears after you’ve matched or accepted the invoice.

→ It signals that the invoice is ready for submission.

---

### 4. Add Missing Voucher to PR

![7.webp](https://strapi.suvit.io/uploads/7_e8cb9372a7.webp)

Some GST Portal invoices may not exist in your PR.

 
→ Click the **plus (➕)** icon and select **Add Voucher**

#### Fill Voucher Details

![8.webp](https://strapi.suvit.io/uploads/8_66c5eee4e3.webp)

Add full voucher info:

→ Supplier Invoice No, Date, Party Name, GST No, etc.

→ Ledger Details & Tax Breakdown

→ Then click **Save & Close**

---

### 5. Track Who Took Action

![9.webp](https://strapi.suvit.io/uploads/9_284107b371.webp)

→ Click the **clock icon** under Action column

→ It shows who accepted/rejected the invoice and when
 
![10.webp](https://strapi.suvit.io/uploads/10_4937f21248.webp)

---

### 6. Vendor view

![11.webp](https://strapi.suvit.io/uploads/11_38d5cd63db.webp)

📇 IMS – Vendor View Screen (See Vendor-wise Mismatch)
This view gives you a vendor-wise breakdown of how your GST Portal data matches with your Purchase Register (PR).

#### What does the Vendor View show?

* 1. This tab helps you compare IMS data and PR data vendor by vendor.

→ Vendor: Name of the supplier and their GSTIN

→ IMS Section: Shows how many invoices and how much tax value was found from GST portal

→ Purchase Register Section: Shows how many entries were found in your PR data

→ Status Columns:

```
 - Matched – Entries match exactly

 - Partially Matched – Some differences exist

 - Not in PR – Data is missing in PR

 - Not in Portal – Data is missing in GST portal
```

* 2. How does this screen help?

→ It lets you:

```
 - Identify vendors with mismatches quickly
```

```
 - Focus on those with “Not in PR” to take action

 - See overall tax difference between IMS & PR
```

✅ Use Case Example:
If vendor "DIPAK KIRYANA STORES" has 4 invoices “Not in PR”, that means invoices exist in GST portal but not in your purchase register — so you can now add missing vouchers or link existing ones.

---

### ✅ Summary

Suvit IMS helps CAs and teams:

* Quickly match GST invoices with Purchase Register
* Accept, reject, or link entries
* Add missing vouchers easily
* Track every action taken

This keeps your GST records accurate and team actions transparent!