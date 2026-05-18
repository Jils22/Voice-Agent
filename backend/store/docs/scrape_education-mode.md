# Tally in education mode

Source: https://taxone.vyapar.com/help/articles/education-mode

[All Collection](/help)[Frequently Asked Question](/help/collections/faqs)[Tally in education mode](/help/articles/education-mode)

[Understanding Failed Entries in Banking Module](#understanding-failed-entries-in-banking-module)[Error Details in the Tally.imp File.](#error-details-in-the-tally-imp-file-)[Tally 2.0](#tally-2-0)[Tally 3.0 & above](#tally-3-0-above)[Possible Solutions](#possible-solutions)

# Tally in education mode

Identify and resolve failed entries in Suvit Banking. Learn to read Tally.imp errors, check exceptions, and fix issues like missing voucher numbers or license.

### Understanding Failed Entries in Banking Module

Below image indicates that an entry has failed:

![1 entry fail in banking.png](https://strapi.suvit.io/uploads/1_entry_fail_in_banking_9baf6cf8e0.png)

1. **Red color** indicates the number of entries that have failed.
2. From here, you can cross-check the error type by visiting.[Click Here](https://help.suvit.io/articles/transaction-are-getting-fail-while-pushing-data-from-suvit-to-tally)

### Error Details in the **Tally.imp** File.

#### Tally 2.0

If error reason in blank that means Tally is in **education mode**
![Tally education mode.png](https://strapi.suvit.io/uploads/Tally_education_mode_7cba98996c.png)
The Tally.imp file provides the following details:

1. **Date and time** of the entry.
2. **Company name**.
3. **Error reason**.
4. **Error type**.

#### Tally 3.0 & above

![tally imp file 3 and above.png](https://strapi.suvit.io/uploads/tally_imp_file_3_and_above_3f19901408.png)

* In Tally 3 and above it will show in exception. Below is the Tally.imp file details:

1. **Date and time** of the entry.
2. **Company name**.
3. **Error reason**.
4. **Error type**.

##### For Tally version 3 and above check All Exception for Error reason

* **Step 1**. Press Alt+Y (Data) > All Exceptions.
* **Step 2**. The All Exceptions report appears, displaying the number of exceptions caused due to Import, Migrate/Repair, and Synchronization in Tally Prime.
  ![3 tally 5.png](https://strapi.suvit.io/uploads/3_tally_5_c04085d0a0.png)
* in Tally 3 & above it will show **Voucher No. is missing**

---

### Possible Solutions

* **Activate your Tally License.**