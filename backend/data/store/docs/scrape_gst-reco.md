# GST Reconciliation

Source: https://taxone.vyapar.com/help/articles/gst-reco

[All Collection](/help)[GST Automation](/help/collections/gst-automation)[GST Reconciliation](/help/articles/gst-reco)

[1. Check Monthly Differences](#1-check-monthly-differences)[2. Filter by Reco Status](#2-filter-by-reco-status)[3. Add Voucher](#3-add-voucher)[4. Fill Voucher Details](#4-fill-voucher-details)[5. Sync with Suvit](#5-sync-with-suvit)[✅ Done!](#-done-)[Follow the same flow for GSTR2B](#follow-the-same-flow-for-gstr2b)

# GST Reconciliation

GSTR-1 Reconciliation & Voucher Entry (Simplified Guide). This guide explains how to check differences in GSTR-1 and Sales Register and how to fix mismatches by adding missing vouchers directly from Suvit.

#### 1. Check Monthly Differences

![1.webp](https://strapi.suvit.io/uploads/1_fee419874c.webp)

* Go to the **Month View** under GSTR1 > Transaction.

  → You’ll see differences in **Total Invoice**, **Taxable Amount**, and **Tax Amount** for each month.

  → This helps you quickly identify which months have mismatched or missing data.

  → Click on Desired **Month** to check the **Transcation**.

---

#### 2. Filter by Reco Status

![2.webp](https://strapi.suvit.io/uploads/2_8f19d8d76d.webp)

* Use the **Reco Status** filter in **Voucher View**.
* You can filter vouchers by:

  → Matched

  → Manual-Matched

  → Partially-Matched

  → Not In Tally

  → Not In Portal
* Helps focus only on problematic entries.

---

#### 3. Add Voucher

![3.webp](https://strapi.suvit.io/uploads/3_27afded116.webp)

* For vouchers marked **Not In Tally**, click the ➕ **Add Voucher** button in the **Action** column.

→ This lets you manually create missing entries right inside Suvit.

---

#### 4. Fill Voucher Details

![4.webp](https://strapi.suvit.io/uploads/4_424d14447f.webp)

* A popup form will appear with the following:

  → **Voucher No., Date, Party Name, GSTIN**

  → **Item Details**:

  → Item Name, Ledger, HSN, Quantity, Rate

  → **Ledger Details**:

  → Add Sales Account & Tax Ledgers like SGST, CGST

  → Double-check all amounts before saving.
* Click the **Save & Close** button at the bottom of the form.

  → This saves your entry and closes the popup.

  → Now the entry is matched and synced with your records.

---

#### 5. Sync with Suvit

![5.webp](https://strapi.suvit.io/uploads/5_16db716ec9.webp)

* After saving, click the **Saved & Synced** button to ensure the new voucher reflects in GSTR1.

→ This will update your match status from "Not in Tally" to "Matched".

→ Keep doing this for all missing records.

---

### ✅ Done!

That’s it! You’ve now matched missing invoices by creating vouchers from within Suvit — no need to go to Tally manually.

#### Follow the same flow for **GSTR2B**