==================================================
Batch payments: Batch deposits (checks, cash etc.)
==================================================

A **Batch Deposit** groups multiple payments in a single batch. This allows depositing several
payments into your bank account with a single action. It can be advantageous to deposit any cash and
check transactions rapidly.

This feature lets you list several customer payments and print a deposit slip. It contains the
details of the transactions and a reference to the batch deposit. You can then select this reference
during a bank reconciliation to match the single bank statement line with all the transactions
listed in the batch deposit.

Configuration
=============

To activate the feature, go to :menuselection:`Accounting --> Configuration --> Settings -->
Customer Payments`, activate :guilabel:`Batch Payments`.

.. note::
   Your main bank accounts are automatically configured to process batch payments when you activate
   the feature.

Deposit multiple payments in batch
==================================

Record payments to deposit in batch
-----------------------------------

You can register a received payment by opening the corresponding customer invoice, and clicking on
:guilabel:`Register Payment`.
There, select the appropriate :guilabel:`Journal` linked to your bank account and select
:guilabel:`Batch Deposit` as Payment Method.

.. image:: batch/batch-payments.png
   :align: center
   :alt: Registering a customer payment as part of a Batch Deposit in Odoo Accounting

Do this step for all checks or payments you want to process in batch.

Add payments to a Batch Deposit
-------------------------------

To add the payments to a Batch Deposit, go to :menuselection:`Accounting --> Customers --> Batch
Payments`, and click on :guilabel:`New`. Next, select the Bank and Payment Method, then click on
:guilabel:`Add a line`.

.. image:: batch/batch-customer-payment.png
   :align: center
   :alt: Filling out a new Inbound Batch Payment form on Odoo Accounting

Select all payments to include in the current Batch Deposit and click on :guilabel:`Select`.

.. image:: batch/batch-lines-selection.png
   :align: center
   :alt: Selection of all payments to include in the Batch Deposit

Once done, click on :guilabel:`Validate` to finalize your Batch Deposit. You can then click on
:guilabel:`Print` to download a PDF file to include with the deposit slip.

Bank Reconciliation
-------------------

Once the bank transactions are on your database, you can reconcile the bank statement lines with the
batch payment reference. To do so, go to the Accounting dashboard and clicking on
:guilabel:`Reconcile Items` on the related bank account. In the bank statement line, the invoices
and payments are going to be matched. To display more options, open the :guilabel:`Batch Payments`
tab, and you can choose the related batch payment.

.. image:: batch/batch-reconciliation.png
   :align: center
   :alt: Reconciliation of the Batch Payment with all its transactions

.. note::
   If a check, or a payment, could not be processed by the bank and is missing, remove the related
   payment before validating the bank reconciliation.

.. seealso::
   - :doc:`recording`
   - :doc:`batch_sdd`

