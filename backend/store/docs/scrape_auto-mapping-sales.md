# Auto Mapping Sales Excel sheet data with SUVIT configuration

Source: https://taxone.vyapar.com/help/articles/auto-mapping-sales

[All Collection](/help)[Sales and Sales Return](/help/collections/sales-and-sales-return)[Auto Mapping Sales Excel sheet data with SUVIT configuration](/help/articles/auto-mapping-sales)

[🤖 What is Auto-Mapping in Suvit?](#-what-is-auto-mapping-in-suvit-)[🪜 Steps for Auto-Mapping](#-steps-for-auto-mapping)[✅ Step 1: Field Mapping](#-step-1-field-mapping)[💰 Step 2: GST Mapping (Tax Ledger)](#-step-2-gst-mapping-tax-ledger-)[📘 Step 3: Ledger Mapping](#-step-3-ledger-mapping)[📦 You May Find This Useful](#-you-may-find-this-useful)

# Auto Mapping Sales Excel sheet data with SUVIT configuration

Learn to use the Auto Mapping option in Suvit’s Bulk Upload for Sales/Purchase. This feature simplifies field mapping for faster, error-free data upload.

### 🤖 What is Auto-Mapping in Suvit?

Auto-mapping is Suvit's smart helper! It **automatically matches** your Excel sheet data to the right Tally fields.
Once you map things once, Suvit remembers it for your future uploads.

---

![1sales4.png](https://strapi.suvit.io/uploads/1sales4_e47be02491.png)

---

### 🪜 Steps for Auto-Mapping

---

#### ✅ Step 1: Field Mapping

![2 mapping.png](https://strapi.suvit.io/uploads/2_mapping_d6da01a116.png)

* First, choose whether your data has items or not.

  → For example, choose **Without Item** if there are no product details.
* Here's what you’ll see:

  → **Mapped Fields** – Suvit found a match for these.

  → **Unmapped Fields** – You need to match these with the correct Tally field.

  → **Your Sheet Header** – These are your Excel column titles.

  → **Tally Fields** – These are from Tally. Match them with your data.

  → **Your Sheet Data** – Shows sample values to help you double-check.

→ Click **Next** to go to **GST Mapping**.

##### 🛠 A → Use of Configuration

* In this section, you can also map:

  → **Voucher Date & Number**

  → **Party (Buyer or Consignee)**

  → **Invoice Date**, **Lading No.**, **Shipping No.**, etc.

  → Even **Cost Centres** and **Dispatch Details**
* [How to use Configuration – Learn More](https://help.suvit.io/articles/configuring-other-settings-suvit-sales-sales-return)

---

#### 💰 Step 2: GST Mapping (Tax Ledger)

Suvit will **auto-fill this** based on your last upload if available!

---

##### 🔘 Option 1: Select from Tally (if set to "No")

![3.1 no map.png](https://strapi.suvit.io/uploads/3_1_no_map_b200b0e3b3.png)

→ Choose your **Tally GST Ledger** from a dropdown.

---

##### 📄 Option 2: Select From Excel (if set to "Yes")

![3 map.png](https://strapi.suvit.io/uploads/3_map_7a3140f8fd.png)

→ Match the column from Excel where **GST Ledger Name** is written.

---

##### 🧮 GST Auto Calculation?

![2 YES AMT IMG.png](https://strapi.suvit.io/uploads/2_YES_AMT_IMG_62827e041b.png)

→ If set to **Yes**, Suvit calculates **SGST, CGST, and IGST** on its own from Tally settings.

→ Tally uses a **rate priority system** for GST calculation: [Learn More](https://help.tallysolutions.com/tally-prime/excise-for-dealers/ed-hierarchy/)

---

##### ✍️ GST Manual Calculation From Sheet

![4 gstamt.png](https://strapi.suvit.io/uploads/4_gstamt_7f8709c2d4.png)

→ If set to **No**, Suvit picks GST values from the Excel file.

→ It uses that data to fill duties & taxes and lets you add narrations if needed.

```
**Note**: SGST, CGST, and IGST Tax Ledgers must be mapped. You can also map the Round-Off Ledger.
```

---

#### 📘 Step 3: Ledger Mapping

![5 other.png](https://strapi.suvit.io/uploads/5_other_92c5b8cb3b.png)

* This is where you link other columns like:

  → **Freight Amount**

  → **Discounts**

  → **Round-off**
* Once done, click **Save & Proceed**. You're ready to push to Tally!

---

### 📦 You May Find This Useful

* Want to know how to send data to Tally? [Learn More](https://help.suvit.io/articles/how-do-we-process-or-push-sales-sales-return-data-to-tally)