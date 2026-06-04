# How to Map Meesho Sales Sheet in Suvit

Source: https://taxone.vyapar.com/help/articles/how-to-map-meesho-sales-sheet-in-suvit

[All Collection](/help)[Frequently Asked Question](/help/collections/faqs)[How to Map Meesho Sales Sheet in Suvit](/help/articles/how-to-map-meesho-sales-sheet-in-suvit)

[Overview](#overview)[Sheet Modification](#sheet-modification)[Date Modification](#date-modification)[Sales Ledger](#sales-ledger)[Tally Settings](#tally-settings)[Accounting Allocation Setup in Tally](#accounting-allocation-setup-in-tally)[Steps to Upload Meesho Sales Sheet](#steps-to-upload-meesho-sales-sheet)[Mapping](#mapping)[Follow the below steps for Mapping:](#follow-the-below-steps-for-mapping-)[Suvit Configuration](#suvit-configuration)[Enable Required Fields in Configuration](#enable-required-fields-in-configuration)[Step 1 → Field Mapping](#step-1-field-mapping)[Step 2 → GST Mapping](#step-2-gst-mapping)[Step 3 → Ledger Mapping](#step-3-ledger-mapping)[Save Mapping](#save-mapping)[You may find this useful](#you-may-find-this-useful)

# How to Map Meesho Sales Sheet in Suvit

Learn how to correctly map Meesho sales sheets in Suvit to ensure seamless data processing and accurate accounting integration with Tally.

---

### Overview

Meesho sales sheets contain specific columns that need to be mapped correctly in Suvit to ensure smooth data processing. This guide explains the step-by-step process for mapping the Meesho sales sheet.

### Sheet Modification

![1.png](https://strapi.suvit.io/uploads/1_3384c4d57d.png)

* Filter the **Delivered** data from heading **order\_status** and copy-paste into a new sheet or delete unwanted data.

#### Date Modification

* Change the **Date** format into **DD-MM-YYYY** (use **Text to Column**).

#### Sales Ledger

![2.png](https://strapi.suvit.io/uploads/2_1e9b6ec488.png)

* Add **Sales Ledger Column** in the Excel sheet and fill the data according to the **GST Rate Applicable** (**Sales Account Ledger**).

### Tally Settings

* Before uploading, make sure **Tally Settings** is set to **Yes** for order details.
* **For Sales** → **Alt+G** (Go To) → **Create Voucher** → **F8** (Sales) → **F12** (Configure) → set **Provide Dispatch, Order, and Export details** to **Yes**.

---

#### Accounting Allocation Setup in Tally

* Tally Setting to to Maintain the **Inventory/Stock values**

|  |  |
| --- | --- |
| \*\*Steps No.\*\* | \*\*Action\*\* |
| Step 1 | Enable Accounting with Inventory in Tally Company  * Go to Gateway of Tally → F11 → Integrate Accounts with Inventory → YES → CTRL + A to save. |
| Step 2 | Enable Default Accounting Allocation in Voucher Type  * Go to Alter Voucher Type → Sales/Purchase → F12 → Allow Setting of Default Accounting Allocation → YES → CTRL + A to save. * Now in Voucher → Enable Default Accounting Allocation → Yes → CTRL + A to save. |
| Step 3 | Enable Use Inventory Allocation of Ledgers  * Go to Alter → Ledger → Sales Account (Sales Ledger Name) → F12 → Use Inventory Allocation for Ledgers → Yes → CTRL + A to save. * Now in ledger → Enable Inventory Values Are Affected → Yes → CTRL + A to save. |

---

### Steps to Upload Meesho Sales Sheet

* Login into [Suvit](https://in.suvit.io/signIn) → Click on **Explore Now** under **Data Entry Automation**.
* Select **Sales** and Click on **Bulk Upload** → Click on **Upload File** and select the **Meesho sales sheet**.
* [Click here](https://help.suvit.io/articles/uploading-sales-sales-return-data-through-an-excel-sheet) for detailed steps.

### Mapping

Mapping in **Suvit** helps streamline data entry by aligning uploaded files with the required fields in Tally. By correctly mapping columns such as **voucher numbers, dates, ledger names,** and **amounts**, it ensures accurate data transfer, minimizes errors, and automates repetitive tasks, making accounting faster and more efficient. 🚀

#### Follow the below steps for Mapping:

### Suvit Configuration

![3.png](https://strapi.suvit.io/uploads/3_fdfeb371d4.png)

* **1** → Switch to **Item Invoice**.
* **2** → Open **Configuration**.

#### Enable Required Fields in Configuration

![4.png](https://strapi.suvit.io/uploads/4_a6695041ec.png)

* **A** → Enable **State(buyer)** If required
* **B** → Enable **State(Consignee)** If required.
* **C** → Save your **Configuration Settings**.

#### Step 1 → Field Mapping

![5.png](https://strapi.suvit.io/uploads/5_eb9914b7b9.png)

* Manually map each column according to **Meesho sales format**.
* If you use the same heading every time, the system will **Auto Map** the entire data.
* Below is the sample data to map **Meesho Excel Sheet** headings in Suvit.

|  |  |
| --- | --- |
| **Meesho Sheet Heading** | **Mapped Column in Suvit** |
| order\_date | Date |
| order\_num | Order No(s) |
| sub\_order\_num | Reference No |
| quantity | Quantity |
| sup\_name | Party A/C Name |
| reseller\_state | Place of Supply |
| end\_customer\_state | State (Buyer) |
| hsn\_code | Name of Item |
| tcs\_taxable\_amount | Amount |
| end\_customer\_state\_new | State (Consignee) |
| Sales Ledger | Sales Ledger |

```
Note: Above is the sample mapping; you can change according to the requirement.
```

#### Step 2 → GST Mapping

![8.png](https://strapi.suvit.io/uploads/8_c8264481f3.png)

* **A** → This will help you choose data from **Tally** or from the **Excel sheet**. Change the settings as per the requirement.
  + By default, **Common Duties and Taxes** will be selected. Changes can be done according to the requirement.
  + Map the **GST field**. How to use multiple Duties & Taxes [Learn More](https://help.suvit.io/articles/auto-mapping-sales#step-2-gst-mapping-map-your-tax-ledger-).
* **B** → Select the **Required GST Ledger** by using the drop-down menu.
  + How **GST Auto Calculation** works [Click Here](https://help.suvit.io/articles/auto-mapping-sales#gst-auto-calculation-) for more details.
* **C** → Click **Next** for Ledger Mapping.

#### Step 3 → Ledger Mapping

![7.png](https://strapi.suvit.io/uploads/7_74ed7d0f94.png)

* This stage is **optional** for mapping.
* Map additional ledgers like **TDS, Discount, Cess,** etc. [Click Here](https://help.suvit.io/articles/how-to-use-discount-tds-cess-and-other-charges) to learn how to map them.

#### Save Mapping

* Click on **Save Mapping**. Suvit will store this mapping for future uploads.

```
- Ensure that column headers match exactly with Meesho’s sales format for every upload.
- If any discrepancies arise, manually adjust the mapping.
```

#### You may find this useful

* How to **Push Data** [Click Here](https://help.suvit.io/articles/how-do-we-process-or-push-sales-sales-return-data-to-tally#saving-and-pushing-data-to-tally) to know more.