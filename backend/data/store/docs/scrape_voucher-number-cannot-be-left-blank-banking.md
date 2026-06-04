# Voucher Number Cannot be left blank (Banking)

Source: https://taxone.vyapar.com/help/articles/voucher-number-cannot-be-left-blank-banking

[All Collection](/help)[Frequently Asked Question](/help/collections/faqs)[Voucher Number Cannot be left blank (Banking)](/help/articles/voucher-number-cannot-be-left-blank-banking)

[Overview](#overview)[Check Tally Exception Report (For Tally Version 3 and Above)](#check-tally-exception-report-for-tally-version-3-and-above-)[Follow the Steps Below](#follow-the-steps-below)[Step 1: Access Voucher Settings](#step-1-access-voucher-settings)[Step 2: Set Voucher Numbering to “Automatic”](#step-2-set-voucher-numbering-to-automatic-)[Step 3: Sync Again from Suvit to Tally](#step-3-sync-again-from-suvit-to-tally)

# Voucher Number Cannot be left blank (Banking)

When the voucher numbering method in your voucher is not set to automatic, this error occurs. Read on for the solution.

### Overview

* Bank entries are posted under **Payment**, **Receipt**, or **Contra** vouchers.
  If any of these use **Manual** or **Automatic (Manual Override)** voucher numbering instead of **Automatic**, Tally will show this error:
  **"Voucher Number cannot be left blank."**
* To check the reason for this error, refer to this guide: [Why transactions failed to sync in Tally](https://help.suvit.io/articles/transaction-s-failed-to-sync-in-tally)

![1Voucher no4.png](https://strapi.suvit.io/uploads/1_Voucher_no4_e4f88691fa.png)
*The image above shows the error from the Tally.imp file*

---

### Check Tally Exception Report (For Tally Version 3 and Above)

* To find the error reason via **All Exceptions**, follow these steps:

**Step 1**: Press **Alt+Y (Data)** → **All Exceptions**
 
**Step 2**: A report opens listing import and sync issues
 
**Step 3**: **Clear/Delete** all exception entries related to this error

![3_tally_5_c04085d0a0.png](https://strapi.suvit.io/uploads/3_tally_5_c04085d0a0_3f8c5ea8ab.png)

---

### Follow the Steps Below

#### Step 1: Access Voucher Settings

* Go to **Master Alter** in Tally.

---

#### Step 2: Set Voucher Numbering to “Automatic”

![2Voucher no5.jpg](https://strapi.suvit.io/uploads/2_Voucher_no5_ff85a94d12.jpg)

* **Important**: Take a **backup of your company** before making changes.
* Find and open **Payment**, **Receipt**, and **Contra** voucher types.
* Set all their **voucher numbering methods to Automatic**

---

#### Step 3: Sync Again from Suvit to Tally

![4 sync.png](https://strapi.suvit.io/uploads/4_sync_5b1e2060ad.png)

* After adjusting the voucher settings, sync the data again in Suvit.
* Once done, **re-push the data to Tally**.

---