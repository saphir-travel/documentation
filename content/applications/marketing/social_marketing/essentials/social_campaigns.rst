==========================
Social marketing campaigns
==========================

Whether the goal is to sell a new product, explain the value of a service, or advertise an upcoming
event, social marketing campaigns help companies connect with the marketplace in uniquely creative
ways.

The most effective social marketing campaigns involve multiple channels, so it is of the utmost
importance to have a reliable solution in place to help with the planning, posting, tracking, and
analyzing of content.

Campaigns page
==============

To access a complete overview of all social marketing campaigns, open the :guilabel:`Social
Marketing` application, and click :guilabel:`Campaigns` from the header menu. Doing so reveals a
separate page with every campaign (in a default :guilabel:`Kanban` view).

.. image:: social_campaigns/campaigns-page.png
   :align: center
   :alt: View of the campaigns page in the Odoo Social Marketing application.

Each stage in the :guilabel:`Kanban` view can be edited, by clicking the "gear" icon to the left of
the "+" (plus sign) - located to the right of the stage title. The "gear" icon only appears when the
cursor hovers to the left of the "+" (plus sign). When the "gear" icon is clicked, a drop-down menu
reveals the options: :guilabel:`Fold`, :guilabel:`Edit Stage`, and :guilabel:`Delete`.

.. image:: social_campaigns/campaign-stage-dropdown.png
   :align: center
   :alt: View of the campaigns page in the Odoo Social Marketing application.

Clicking :guilabel:`Fold` minimizes that specific stage's column. The stage column can be restored
by clicking the folded version of it on the main :guilabel:`Campaigns` page (in :guilabel:`Kanban`
view).

Selecting :guilabel:`Edit Stage` reveals a pop-up, in which the name (and the sequence) of the stage
can be modified. If changes are made, be sure to click :guilabel:`Save`.

Clicking :guilabel:`Delete` removes the stage entirely.

.. note::
   To add a new stage to the pipeline, side-scroll to the right on the :guilabel:`Campaigns` page,
   click :guilabel:`Add a Column`, enter in the desired information, and click :guilabel:`Add`.

.. tip::
   The same social marketing campaign information on the :guilabel:`Campaigns` page can also be
   viewed as a list, by selecting the :guilabel:`List` option (located under the :guilabel:`Search`
   bar, in the upper-right corner).

How to create social marketing campaigns
========================================

First, open the :guilabel:`Social Marketing` application, and select :guilabel:`Campaigns` from the
header menu.

On the :guilabel:`Campaigns` page, a new campaign can be created by clicking the :guilabel:`Quick
Add` plus sign ("+") icon - located at the top-right of each stage in the pipeline (visible in the
:guilabel:`Kanban` view). Or, by clicking :guilabel:`Create` in the upper-left corner of the
:guilabel:`Campaigns` page.

Both options reveal a new campaign detail window directly on the :guilabel:`Campaigns` page when
clicked.

.. image:: social_campaigns/quick-add-campaign.png
   :align: center
   :alt: View of the quick add option for campaigns in Odoo Social Marketing.

Here, a :guilabel:`Campaign Name`, :guilabel:`Responsible`, and :guilabel:`Tags` can be entered.
When all modifications are complete, click :guilabel:`Add` to add the campaign to the database.

How to edit social marketing campaigns
======================================

In order to edit a campaign in greater detail, and create/send various forms of communications
related to it, the template page for that campaign must be accessed (and modified, accordingly).
There are multiple ways to access a template page for a campaign.

- After entering the pertinent information in the :guilabel:`Quick Add` campaign drop-down, click
  :guilabel:`Edit`.
- Simply select the desired campaign from the :guilabel:`Campaigns` page (in :guilabel:`List` or
  :guilabel:`Kanban` view).
- On the :guilabel:`Campaigns` page (in :guilabel:`Kanban` view), select the "three dot" drop-down
  menu on the desired campaign, and select :guilabel:`Edit`.

Any of the above routes will reveal the campaign template page for that specific campaign.

Social marketing campaign templates
===================================

On a campaign tempate page, numerous elements can be customized/modified, and various forms of
communications can be created, modified, and sent (or scheduled). Below is a sample of a completed
campaign template.

.. image:: social_campaigns/create_campaign.png
   :align: center
   :alt: View of a sample campaign template page in Odoo Social Marketing.

.. important::
   In order for the :guilabel:`Send New Mailing` option to appear on campaign templates, make sure
   the :guilabel:`Mailing Campaigns` feature is enabled in the :guilabel:`Email Marketing` app. To
   do that, navigate to :menuselection:`Email Marketing --> Configuration --> Settings`, activate
   :guilabel:`Mailing Campaigns`, and click :guilabel:`Save`.

.. note::
   In order for the :guilabel:`Send SMS`, the Odoo :guilabel:`SMS Marketing` application must be
   installed on the database.

Adding content and communications to campaigns
==============================================

If the proper settings and applications are installed (as instructed above), there are four forms of
communication/content options that can be added to campaigns. Each of these options are displayed as
buttons in the upper-left corner of the campaign template page.

- :guilabel:`Send New Mailing`: reveals a blank email template on a separate page, in which the
  message can be fully customized in a variety of ways.
- :guilabel:`Send SMS`: reveals a blank SMS template on a separate page, in which a SMS
  communication can be created (and configured).
- :guilabel:`Send Social Post`: reveals a blank social post template on a separate page, in which a
  post can be created, and applied to social media accounts that are already connected to the
  database.
- :guilabel:`Push Notification`: reveals a similar blank social post template on a separate page,
  however, the :guilabel:`Push Notification` options are already pre-selected in the :guilabel:`Post
  on` field.

Whichever form of communication is created, once it's completed, Odoo returns to the campaign
template page, showcasing that new content in its corresponding tab (e.g. :guilabel:`Mailings`,
:guilabel:`SMS`, :guilabel:`Social Media`, and/or :guilabel:`Push Notifications`).

As content and communications are added to a campaign, tabs for those specific mediums appear, along
with a variety of analytical smart buttons (e.g. :guilabel:`Revenues`, :guilabel:`Quotations`,
:guilabel:`Leads`, etc.).

These smart buttons (located at the top of the template) display different metrics related to the
campaign, and its various communications and content. Clicking any smart button reveals a separate
page dedicated to that particular element of the campaign, allowing for quicker, more organized
analysis.

.. note::
   The Odoo :guilabel:`Social Marketing` app is integrated with other Odoo applications, such as
   :guilabel:`Sales`, :guilabel:`Invoicing`, :guilabel:`CRM`, and :guilabel:`Website`.

.. seealso::
   :doc:`./social_essentials`
