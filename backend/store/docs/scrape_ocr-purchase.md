# OCR - Uploading and Processing Purchase Bills

Source: https://taxone.vyapar.com/help/articles/ocr-purchase

[All Collection](/help)[OCR](/help/collections/ocr)[OCR - Uploading and Processing Purchase Bills](/help/articles/ocr-purchase)

[How to upload a purchase invoice from an image or PDF in Suvit?](#how-to-upload-a-purchase-invoice-from-an-image-or-pdf-in-suvit-)[✅ Steps to upload Purchase Invoice (Image/PDF)](#-steps-to-upload-purchase-invoice-image-pdf-)[Step 1: Go to Transactions Section](#step-1-go-to-transactions-section)[Step 2: Click on Upload Image](#step-2-click-on-upload-image)[Step 3: Upload the File](#step-3-upload-the-file)[Step 4: Verify Uploaded Entry](#step-4-verify-uploaded-entry)[⚠️ Notes:](#-notes-)[Step 5: Verify Data](#step-5-verify-data)[Step 6: Ledger, Tax, and Finalization](#step-6-ledger-tax-and-finalization)[You May Find This Useful](#you-may-find-this-useful)

# OCR - Uploading and Processing Purchase Bills

Learn how to upload, verify, and process Purchase/Purchase Return invoices using Suvit’s OCR automation for seamless data entry and synchronization with Tally.

### **How to upload a purchase invoice from an image or PDF in Suvit?**

*You can easily upload purchase invoices in Suvit using PDF or image files. Follow the steps below to upload your invoice and map it to Tally.*

---

### ✅ Steps to upload Purchase Invoice (Image/PDF)

#### **Step 1: Go to Transactions Section**

![1 dash.png](https://strapi.suvit.io/uploads/1_dash_6eb066d6e3.png)

→ Click on the **Transactions** icon from the left menu

→ Hover on **Purchase** under the Transactions tab

→ Click on **Purchase**

#### **Step 2: Click on Upload Image**

![2 img pur.png](https://strapi.suvit.io/uploads/2_img_pur_8634a7c579.png)  
→ On the top-right corner, click on **Upload Image**

#### **Step 3: Upload the File**

![3 img.png](https://strapi.suvit.io/uploads/3_img_2d753ab2be.png)

→ Either **drag & drop** the file or click **Click to upload Image/PDF**

→ After the file loads, click **Upload**

#### **Step 4: Verify Uploaded Entry**

![4 img uploade.png](https://strapi.suvit.io/uploads/4_img_uploade_a0ac1488de.png)

→ After upload, you will see the list of invoices

→ Click on the invoice row to edit or verify the data

---

#### ⚠️ Notes:

* You can upload up to **10 invoices** at a time.
* Maximum file size supported is **5 MB**.
* Supported file types: **.pdf, .jpeg, .jpg, .png, .webp**

```
**Note:**
 Fields from the uploaded purchase invoice will be automatically detected and matched with your purchase details. You can review and correct any errors here.
```

#### Step 5: Verify Data

![6 img.png](https://strapi.suvit.io/uploads/6_img_4b94bfe115.png)

**1. Review and Select Invoice Type**

* Choose if the purchase invoice data is **"With Item"** or **"Accounting Invoice"**.

**2. Fill in Invoice Details**

* Enter the following details:
  + **Voucher Type, Number, and Date**
  + **Supplier Name and GST Number** (with additional details if required)
  + **Purchase Ledger Information**

**3. Add Item Details**

* Add purchased items with these fields:
  + Serial number, item name, quantity, rate, and amount.
* You can delete any line item if needed.

A .Configuration Options

- Use the \*\*Configuration Window\*\* to select the fields displayed during voucher entry.

- Fields include \*\*Voucher Date\*\*, \*\*Supplier Invoice No.\*\*, \*\*Item Narration\*\*, etc. Save the changes once done.

![11 img.png](https://strapi.suvit.io/uploads/11\_img\_2bbcbddc3d.png)

#### Step 6: Ledger, Tax, and Finalization

![7 img.png](https://strapi.suvit.io/uploads/7_img_0557937243.png)

**4. Edit Ledger Details**

* Add or modify **purchase ledger names and their amounts**.

**5. Add Tax Ledger Details**

* Enter tax components like **SGST, CGST, and IGST** with descriptions and amounts.

**6. Review Narration and Totals**

* Add any necessary **narration notes**.
* Review **subtotal, tax amount, and total amount**.

**7. Save and Synchronize**

* **Save & Close**: Saves the purchase invoice and closes the screen.
* **Save & Sync**: Saves the invoice and syncs it directly with Tally.

```
**Important:**
- Ensure the Suvit Tally Connector is open during synchronization.
- OCR efficiency for capturing purchase data is 50–80% during the initial entry .
```

#### You May Find This Useful

* Learn more about **Purchase and Purchase Return** [here](https://help.suvit.io/collections/purchase-and-purchase-return).