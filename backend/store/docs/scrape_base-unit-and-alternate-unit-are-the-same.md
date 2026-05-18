# Fixing "Base Unit and Alternate Unit Are the Same" Error in Tally

Source: https://taxone.vyapar.com/help/articles/base-unit-and-alternate-unit-are-the-same

[All Collection](/help)[Frequently Asked Question](/help/collections/faqs)[Fixing "Base Unit and Alternate Unit Are the Same" Error in Tally](/help/articles/base-unit-and-alternate-unit-are-the-same)

[Exception Error Name](#exception-error-name)[Reason for the Error](#reason-for-the-error)[Solution 💡](#solution-)[Notes 📝](#notes-)

# Fixing "Base Unit and Alternate Unit Are the Same" Error in Tally

acing the "Base Unit and Alternate Unit Are the Same" error in Tally? Learn the cause and follow step-by-step instructions to fix it without resending data.

#### Exception Error Name

![1.png](https://strapi.suvit.io/uploads/1_04f066de7a.png)

* **Error Message:** ❌ "Base Unit and Alternate Unit are the same"
* This error occurs when creating a **Stock Item** in Tally, where both **Base Unit** and **Alternate Unit** are **set as the same**.

#### Reason for the Error

![2.png](https://strapi.suvit.io/uploads/2_6b10685e4d.png)

* As shown in the image, both **Base Unit** and **Alternate Unit** are the same, which causes the error.

#### Solution 💡

![3.png](https://strapi.suvit.io/uploads/3_5d5bcdec58.png)

* **Alter** the **Alternate Unit** type and **save** the changes.

### Notes 📝

* In most cases, altering the **Alternate Unit** resolves the issue.
* **If you fix the error directly from the Exception List in Suvit**, there’s no need to resend data.
* **If you delete the error and fix it manually in Tally**, follow these steps:
  + Go to **Gateway of Tally** → **Alter** → **Stock Item**
  + Select the affected **Stock Item** and make the necessary changes
  + **Go to Suvit** and **resend the Failed Data**