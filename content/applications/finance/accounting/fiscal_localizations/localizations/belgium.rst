=======
Belgium
=======

Configuration
=============

:ref:`Install <general/install>` the :guilabel:`Belgium - Accounting` and the :guilabel:`Belgium -
Accounting Reports` modules to get all the features of the Belgian localization, following the
:abbr:`IFRS(International Financial Reporting Standards)` rules.

.. list-table::
   :header-rows: 1

   * - Name
     - Technical name
     - Description
   * - :guilabel:`Belgium - Accounting`
     - `l10n_be`
     - Installing this module grants you access to the basic accounting features for Belgium,
       including the Belgian taxes and Chart of accounts.
   * - :guilabel:`Belgium - Accounting Reports`
     - `l10n_be_reports`
     - Installing this module grants you access to improved accounting reports for Belgium.

.. image:: belgium/modules.png
   :align: center
   :alt: The accounting modules for the Belgian fiscal localization package on Odoo

Chart of accounts
=================

The Belgian :guilabel:`Chart of accounts` includes pre-configured accounts as described in the
:abbr:`PCMN(Plan Comptable Minimum Normalisé)`.

You can reach the :guilabel:`Chart of accounts` by going to :menuselection:`Accounting -->
Configuration --> Accounting: Chart of Accounts`.

To add a new account, click :guilabel:`Create`. A new line to fill in appears. Click
:guilabel:`Save` and then :guilabel:`Setup` to configure it further.

.. seealso::
   - Odoo Tutorial: `Chart of accounts <https://www.odoo.com/slides/slide/chart-of-accounts-1630?fullscreen=1>`_.
   - Odoo Tutorial: `Update your Chart of accounts tutorial <https://www.odoo.com/slides/slide/update-your-chart-of-accounts-1658?fullscreen=1>`_.

Taxes
=====

Default Belgian taxes are created automatically when the :guilabel:`Belgium - Accounting` and
the :guilabel:`Belgium - Accounting Reports` modules are installed.

The Belgian :guilabel:`Tax report` is available by going to :menuselection:`Accounting --> Reporting
--> Statements Reports: Tax Report`.

.. seealso::
   :doc:`../../reporting/declarations/tax_returns`.

Accounting reports
==================

Here is the list of Belgian-specific reports available on Odoo Enterprise:

- Balance sheet
- Profit & loss
- Tax report
- Partner VAT Listing

.. seealso::
   :doc:`../../getting_started/memento`.

Fee form 281.50 and form 325
=============================

Fee form 281.50
---------------

Annually, individual :guilabel:`Fee form 281.50` must be reported to the fiscal authorities.
The tag :guilabel:`281.50` must be added on the :guilabel:`Contact form` of each supplier. To do so,
go to the :guilabel:`Contacts` app, select the supplier you want to create a
:guilabel:`Fee form 281.50` for, and add the tag.

.. image:: belgium/281-50.png
   :align: center
   :alt: add the tag 281-50 on a contact form

Then, go to :menuselection:`Accounting --> Configuration --> Acounting: Chart of Accounts`. Select
the right tag on all impacted accounts, ie.: :guilabel:`281.50 - Commissions`.

Form 325
--------

You can create :guilabel:`Form 325` by going to :menuselection:`Accounting --> Reporting -->
Belgium: Create 325 form`. A new page pops up: select the right options and click
:guilabel:`Generate 325 Form`.

.. image:: belgium/create-325-form.png
   :align: center
   :alt: add the tag 281-50 on a contact form

Go to :menuselection:`Accounting --> Reporting --> Belgium: Open 325 forms` to view the
:guilabel:`325 forms` you already generated.

Disallowed expenses report
==========================

**Disallowed expenses** reflect expenses that can be deducted from your bookkeeping result but not
from your fiscal result. The :guilabel:`Disallowed Expenses Report` is available by going to
:menuselection:`Accounting --> Reporting --> Management: Disallowed Expenses`. It is generated based
on the :guilabel:`Disallowed Expenses Categories`, which allow financial results in real-time and
periodic changes. The categories are available by default based on the Belgian fiscal requirements.

You must set the :guilabel:`Current Rate` and :guilabel:`Related Account(s)` information. To do so,
go to :menuselection:`Accounting --> Configuration --> Management: Disallowed Expenses Categories`.

Let’s take an example reflecting **car expenses** and **restaurant expenses**.

Restaurant expenses
-------------------

In Belgium, 31% of **restaurants** expenses are non deductible. Set the :guilabel:`Current Rate` and
:guilabel:`Related Account(s)`.

.. image:: belgium/frais-de-restaurant.png
   :align: center
   :alt: Disallowed expenses categories

Car expenses: vehicle split
---------------------------

In Belgium, the deductible percentage varies from car to car and, therefore, should be indicated for
each vehicle. To do so, go to the :guilabel:`Fleet` app and select a vehicle. In the
:guilabel:`Tax info` tab, go to the :guilabel:`Disallowed Expenses Rate` section and click on
:guilabel:`Add a line`. Add a :guilabel:`Start Date` and a :guilabel:`%`. The amounts arrive in the
same account for all car expenses.

When you create a bill for car expenses, you can link each expense to a specific car by filling the
:guilabel:`Vehicle` column, so the right percentage is applied.

.. image:: belgium/car-expenses.png
   :align: center
   :alt: Disallowed expenses categories

The :guilabel:`vehicle split` option available in the :guilabel:`Disallowed Expenses Report` allows
you to see the rate and disallowed amount for each car.

.. image:: belgium/vehicle-split.png
   :align: center
   :alt: Disallowed expenses categories

Electronic invoicing
====================

The :guilabel:`E-FFF` and :guilabel:`Peppol BIS Billing 3.0 (UBL)` formats are enabled by default
when the :guilabel:`Belgium - Accounting` and the :guilabel:`Belgium - Accounting Reports` modules
are installed.

You can update the settings by going to :menuselection:`Accounting --> Configuration --> Journals
--> Customer Invoices --> Advanced Settings --> Electronic Invoicing`.

.. seealso::
   :doc:`../../receivables/customer_invoices/electronic_invoicing`

CODA
====

:guilabel:`CODA` is an electronic XML format used to import Belgian bank statements. You can
download CODA files from your bank and import them directly in Odoo by clicking
:guilabel:`Import Statement` from your Bank journal on your dashboard, and select the CODA file(s)
you want. This automatically creates your bank statements into your :guilabel:`Bank journal`.

.. image:: belgium/import-statement.png
   :align: center
   :alt: Import coda files

.. note::
   The :guilabel:`Belgium - Import Bank CODA Statements` module is installed by default when the
   :guilabel:`Belgium - Accounting` and the :guilabel:`Belgium - Accounting Reports` modules are
   installed.

SODA
====

:guilabel:`SODA` is an electronic XML format used to import accounting entries related to salaries.
SODA files can be imported in the :guilabel:`Miscellaneous` journal, by clicking :guilabel:`Upload`.

.. image:: belgium/soda-import.png
   :align: center
   :alt: Import soda files

Once your :guilabel:`SODA` files are imported, the entries are created automatically in your MISC
journal.

Cash discount
=============

In Belgium, the tax is calculated based on the product price after discount, whether it effectively
applies or not.

.. Seealso::
   :doc:`../../receivables/customer_invoices/cash_discounts`
