# Mapping Vyapar Data in Suvit

Source: https://taxone.vyapar.com/help/articles/vyapar-mapping

[All Collection](/help)[Vyapar](/help/collections/vyapar)[Mapping Vyapar Data in Suvit](/help/articles/vyapar-mapping)

[Vyapar to Tally Mapping Stages](#vyapar-to-tally-mapping-stages)[Step 1 - Unit Mapping](#step-1-unit-mapping)[Step 2 - Item Mapping](#step-2-item-mapping)[Step 3 - Ledger Mapping](#step-3-ledger-mapping)[📌 Important Points](#-important-points)[📝 Notes](#-notes)[🔗 Next Step](#-next-step)

# Mapping Vyapar Data in Suvit

Learn how to seamlessly map units, stock items, and ledgers from Vyapar to Tally using Suvit. Follow this step-by-step guide to ensure accurate data mapping.

### Vyapar to Tally Mapping Stages

Mapping consists of **three key stages**: **Unit Mapping, Item Mapping, and Ledger Mapping**. Each step ensures accurate data transfer and prevents mismatches.

---

#### Step 1 - Unit Mapping

**1**. Verify that all **units** in Vyapar exist in the Tally company. If a unit is missing, create it in Tally with the appropriate **UQC (Unit Quantity Code)**.  
**2**. If the **unit name** in Vyapar and Tally are identical, the system will **automatically match** them.  
**3**. The **status column** will indicate whether data is mapped or **unmapped**.  
**4**. For **unmapped units**, manual mapping is required.

* A **yellow triangle** will highlight records that need selection.

![1.png](https://strapi.suvit.io/uploads/1_dc611b7698.png)

**5**. After completing the mapping, **click on Save**.

![2.png](https://strapi.suvit.io/uploads/2_6c3f8d4d09.png)

---

#### Step 2 - Item Mapping

**1**. The **status column** will display whether items are mapped or **unmapped**.

* If the **stock item name** and **GST Rate** in Vyapar match those in Tally, the system will **auto-map** them.

![3.png](https://strapi.suvit.io/uploads/3_d30a61adbe.png)

**2**. For **unmapped items**, manual mapping is required.

* The **yellow triangle** will highlight unselected records.

![4.png](https://strapi.suvit.io/uploads/4_fd8b556198.png)

**3**. Items can be mapped **one by one** or in bulk.

![5.png](https://strapi.suvit.io/uploads/5_939b227923.png)

**4**. To **create all unselected stock items**, follow these steps:

* Select all unmapped data.
* Click on the **plus (+) button** to create stock items in bulk.

![7.png](https://strapi.suvit.io/uploads/7_d0e83080ff.png)

**5**. Once the mapping is complete, **click on Save**.

---

#### Step 3 - Ledger Mapping

**1**. All **matched ledgers** will be **automatically mapped**.

![8.png](https://strapi.suvit.io/uploads/8_ec25bc33f1.png)

**2**. Any **unmapped ledgers** must be manually assigned to the correct Tally ledger.

![9.png](https://strapi.suvit.io/uploads/9_c878ba67e2.png)

**3**. If new **party names** are detected, follow these steps:

* Select all unmapped ledgers.
* Click on the **plus (+) button** to create them in bulk.

![10.png](https://strapi.suvit.io/uploads/10_c7d4331b65.png)

---

### 📌 Important Points

* Ensure the **Cash Ledger** in Vyapar is categorized under **"Cash in Hand"** to avoid mapping issues.
* Data must be **exactly the same** in Vyapar and Tally for successful mapping.
* **Case-sensitive differences and incorrect ledger types** can prevent automatic mapping.

---

### 📝 Notes

* Mapping is typically a **one-time setup**, unless new **units, items, or ledgers** are added in Vyapar.

---

### 🔗 Next Step

➡️ [How to Review and Sync Vyapar Entries in Suvit](https://help.suvit.io/articles/review-sync-vyapar-entries)