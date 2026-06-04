# Use of General Filters

Source: https://taxone.vyapar.com/help/articles/general-filters

[All Collection](/help)[Banking](/help/collections/banking)[Use of General Filters](/help/articles/general-filters)

[1. Date-Filter](#1-date-filter)[2. Narration/Description Filter](#2-narration-description-filter)[Select Ledgers in Bulk for Similar Transactions](#select-ledgers-in-bulk-for-similar-transactions)[3. Payment/Receipt Filter](#3-payment-receipt-filter)[4. Amount Filter](#4-amount-filter)[5. Hide Tally Pushed](#5-hide-tally-pushed)[6. Blank Records](#6-blank-records)[7. Saved Records](#7-saved-records)[8. Unsaved Records](#8-unsaved-records)[Access Configuration in suvit](#access-configuration-in-suvit)[Configure Bank Allocation](#configure-bank-allocation)[Set Cheque/Instrument Number](#set-cheque-instrument-number)[Supplier/Reference Number](#supplier-reference-number)[Enable Cost Centre Tracking](#enable-cost-centre-tracking)[Set Voucher Numbering](#set-voucher-numbering)[Save Changes](#save-changes)[You May Find this Useful:](#you-may-find-this-useful-)

# Use of General Filters

Use filters like date, amount, narration, and transaction type to select ledgers. Configure settings like bank allocation, voucher number, and cost center.

##### In Suvit, you can select ledgers for transactions using various filters designed to simplify your work. Below are the filters and their applicability:

### 1. Date-Filter

![1banking26.png](https://strapi.suvit.io/uploads/1banking26_a310a47355.png)

* Filter the data by a date range you wish to work on.
* If you do not need a particular date range's data to be transferred to Tally, filter that date range and delete it from Suvit. This way, you'll only work on the relevant data.

### 2. Narration/Description Filter

![2banking27.png](https://strapi.suvit.io/uploads/2banking27_a7e28e14d4.png)

* For common transactions that need to be posted in the same ledger, search the common keyword in the narration or description (e.g., **"SMS Alert Charges"**, **"G-pay"**, etc.).
* Once the transactions are filtered, select all, and from bulk operations, set the desired ledger for the filtered transactions and save them.

#### Select Ledgers in Bulk for Similar Transactions

![3bulk ledger selected.png](https://strapi.suvit.io/uploads/3bulk_ledger_selected_e2ee6f6de6.png)

* You can filter out the transactions you wish to post in a single ledger.
* For example, in the above image
  + **A** Search the keyword **"neft"** is used in the narration. (you can search for Cash, emi, upi, neft, sms charges etc)
  + **B** Select all filtered transactions.
  + **C** Search for the Party Name in the **LEDGER** Box and select it.

### 3. **Payment/Receipt Filter**

![4transaction type.png](https://strapi.suvit.io/uploads/4transaction_type_336655dcca.png)

* Use this filter to work on specific transaction types such as **Receipts** or **Payments**.

### 4. **Amount Filter**

![5amount filter.png](https://strapi.suvit.io/uploads/5amount_filter_344ca188b8.png)

* Filter transactions within a specific amount range using this filter. This will give you the list of transactions in your desired range.

### 5. **Hide Tally Pushed**

![6hide tally push.png](https://strapi.suvit.io/uploads/6hide_tally_push_a2a5471f42.png)

* By selecting this filter, you can hide transactions already sent to Tally, helping you focus on transactions yet to be processed.

### 6. **Blank Records**

![8 blankblank records.png](https://strapi.suvit.io/uploads/8_blankblank_records_28c41e0450.png)

* This filter displays transactions where ledgers are yet to be selected and saved for sending to Tally.

### 7. Saved Records

![7saved.png](https://strapi.suvit.io/uploads/7saved_c447bf7176.png)

* This filter lists transactions with ledgers assigned but not yet sent to Tally.

### 8. Unsaved Records

![8 unsave.png](https://strapi.suvit.io/uploads/8_unsave_3e6d8ad18b.png)

* Use this filter to view transactions where ledgers were selected but not saved.
* Once ledgers are selected for all transactions, save them and send them to Tally.

### Access Configuration in suvit

* Navigate to **"Settings"** and select **"Configuration"** from the menu.

![2_setings_f269e9a0f0.png](https://strapi.suvit.io/uploads/2_setings_f269e9a0f0_8751ecd240.png)

#### [Configure Bank Allocation](https://help.suvit.io/articles/bank-allocation-guide)

* Enable the Bank Allocation feature to manage bank-related details in transactions.
* This setting ensures that bank accounts are accurately mapped for ledger entries. [Learn more.](https://help.suvit.io/articles/bank-allocation-guide)

#### [Set Cheque/Instrument Number](https://help.suvit.io/articles/enable-cheque-number-banking)

* Enable the Cheque/Instrument Number field to record details of Cheque or instruments used for payments or receipts.
* You can input Cheque numbers, transaction IDs, or instrument details for better tracking. [Learn more.](https://help.suvit.io/articles/enable-cheque-number-banking)

#### [Supplier/Reference Number](https://help.suvit.io/articles/enable-supplier-reference-number-banking)

* Activate the Supplier/Reference Number option to record the supplier invoice number or reference ID for purchases.
* This ensures proper identification of invoices during reconciliation or reporting. [Learn more.](https://help.suvit.io/articles/enable-supplier-reference-number-banking)

#### [Enable Cost Centre Tracking](https://help.suvit.io/articles/enable-cost-centre-banking)

* Turn on the Cost Centre feature to allocate expenses and revenues to specific departments, projects, or units.
* This helps in tracking profitability and controlling budgets effectively. [Learn more.](https://help.suvit.io/articles/enable-cost-centre-banking)

#### [Set Voucher Numbering](https://help.suvit.io/articles/enable-voucher-number-banking)

* Configure the Voucher Number field to manage the sequence of transaction entries in Tally.
* Choose between manual or automatic numbering based on your requirements. [Learn more.](https://help.suvit.io/articles/enable-voucher-number-banking)

#### Save Changes

* After enabling the required fields, click **"Save"** to apply the configuration settings.

### You May Find this Useful:

**Note:** Suvit also offers a unique feature for **Suggested Ledgers**, which will be discussed in the following article over [here](https://help.suvit.io/articles/suggested-ledgers).