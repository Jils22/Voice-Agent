# Auto-Mapping Excel sheet data with SUVIT configuration

Source: https://taxone.vyapar.com/help/articles/auto-mapping-purchase

[All Collection](/help)[Purchase and Purchase Return](/help/collections/purchase-and-purchase-return)[Auto-Mapping Excel sheet data with SUVIT configuration](/help/articles/auto-mapping-purchase)

[🧠 What is Auto-Mapping in Suvit?](#-what-is-auto-mapping-in-suvit-)[🪜 Step-by-Step Guide to Auto-Mapping](#-step-by-step-guide-to-auto-mapping)[✅ Step 1: Field Mapping](#-step-1-field-mapping)[🔧 A → Use of Configuration](#-a-use-of-configuration)[✅ Step 2: GST Mapping (Tax Ledger)](#-step-2-gst-mapping-tax-ledger-)[🧾 Option 1: Choose from Tally](#-option-1-choose-from-tally)[📄 Option 2: Use Excel Column](#-option-2-use-excel-column)[✅ GST Auto Calculation?](#-gst-auto-calculation-)[📝 GST Manual Calculation (From Excel)](#-gst-manual-calculation-from-excel-)[✅ Step 3: Ledger Mapping](#-step-3-ledger-mapping)[📚 You May Find This Useful:](#-you-may-find-this-useful-)

# Auto-Mapping Excel sheet data with SUVIT configuration

In Suvit, Sales/Purchase Excel data is auto-mapped using keywords and past patterns. Learn how to make the most of the Auto Mapping feature in this guide.

#### 🧠 What is Auto-Mapping in Suvit?

Auto-Mapping is Suvit’s smart assistant that **automatically connects your Excel sheet to Tally**.
It reads your column names and suggests the right fields — so you don’t need to do everything manually.
Even better? Suvit remembers your choices for next time!

Once you upload your **Purchase or Purchase Return Excel sheet**, the next screen is the **Mapping screen**.
Here’s how it works:

---

### 🪜 Step-by-Step Guide to Auto-Mapping

---

### ✅ Step 1: Field Mapping

![2 mapping.png](https://strapi.suvit.io/uploads/2_mapping_04dded3132.png)

* Here’s what you’ll see:

  → **Choose your Data Type**: With items or without items? For this example, we select **Without Item**.

  → **Mapped Fields**: Suvit auto-matched these with Tally.

  → **Unmapped Fields**: You need to select matching Tally fields for these.

  → **Your Sheet Header**: These are your Excel column titles.

  → **Tally Fields**: These are Tally’s fields — link them to your columns.

  → **Your Sheet Data**: Shows 3 sample rows from your Excel to double-check everything.

  → Click **Next** to move to the GST Mapping step.

---

#### 🔧 A → Use of Configuration

* You can also map special fields like:

  → **Voucher Date & Number**

  → **Party (Buyer or Consignee)**

  → **Invoice Date**, **Carrier Name**, **Lading Number**, etc.

  → Even **Export Details**, **Tracking Number**, **Vehicle Number**, and **Cost Centres**
* [How to Use Configuration – Learn More](https://help.suvit.io/articles/configuring-other-settings-suvit-sales-sales-return)

---

### ✅ Step 2: GST Mapping (Tax Ledger)

* If you’ve done this earlier, Suvit will apply saved mappings here too.

#### 🧾 Option 1: Choose from Tally

![3.1 no map.png](https://strapi.suvit.io/uploads/3_1_no_map_04320ba255.png)

→ If set to **No**, choose the **Tally GST Ledger** manually from the dropdown.

---

#### 📄 Option 2: Use Excel Column

![3 map.png](https://strapi.suvit.io/uploads/3_map_4e4bb1c0a3.png)

→ If set to **Yes**, link the column that contains GST Ledger names (from Excel).

---

### ✅ GST Auto Calculation?

![2 YES AMT IMG.png](https://strapi.suvit.io/uploads/2_YES_AMT_IMG_62827e041b.png)

→ If set to **Yes**, Suvit calculates SGST, CGST, and IGST using the settings already in Tally.

→ Learn how Tally decides GST rates: [Learn More](https://help.tallysolutions.com/tally-prime/excise-for-dealers/ed-hierarchy/)

---

### 📝 GST Manual Calculation (From Excel)

![4 gstamt.png](https://strapi.suvit.io/uploads/4_gstamt_858c247005.png)

→ If set to **No**, Suvit picks GST amounts from the Excel sheet.

→ You can even match the values and add a narration for reference.

```
📌 Note: Mapping SGST, CGST, and IGST is mandatory.  
You can also map **Round-Off Ledger** if needed.
```

---

### ✅ Step 3: Ledger Mapping

![5 other.png](https://strapi.suvit.io/uploads/5_other_c057c69d8d.png)

* Here, you can link fields like:

→ **Round-Off**

→ **Discount**

→ **Freight / Delivery Charges**

→ Choose the right Excel column and the matching Tally ledger.

* Finally, click **Save & Proceed** to move ahead.

---

### 📚 You May Find This Useful:

Want to know how to send your mapped purchase data to Tally?

👉 [Learn More](https://help.suvit.io/articles/purchase-process)