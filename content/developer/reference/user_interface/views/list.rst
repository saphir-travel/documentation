List
====
.. code-block:: xml

  <tree>
    ...
  </tree>

The root element of list views is ``<tree>``\ [#treehistory]_. The list view's
root can have the following attributes_:

:string:
  string_ (optional)

  View name

:create:
  boolean_ (optional)

  Disable/enable record creation on the view.

:edit:
  boolean_ (optional)

  Disable/enable record editing on the view.

  If the ``edit`` attribute is set to ``false``, the ``editable`` option will be ignored.

:delete:
  boolean_ (optional)

  Disable/enable record deletion on the view through the **Action** dropdown.

:import:
  boolean_ (optional)

  Disable/enable record import data on the view.

:export_xlsx:
  boolean_ (optional)

  Disable/enable record export data on the view.

:editable:
  string_ chooses from ``top`` or ``bottom`` (optional)

  by default, selecting a list view's row opens the corresponding
  :ref:`form view <reference/user_interface/views/form>`. The ``editable`` attributes
  makes the list view itself editable in-place.

  Valid values are ``top`` and ``bottom``, making *new* records appear respectively at
  the top or bottom of the list.

  The architecture for the inline :ref:`form view <reference/user_interface/views/form>`
  is derived from the list view. Most attributes valid on a :ref:`form view
  <reference/user_interface/views/form>`'s fields and buttons are thus accepted by list
  views although they may not have any meaning if the list view is non-editable.

  If the ``edit`` attribute is set to ``false``, the ``editable`` option **will be ignored**.

:multi_edit:
  ``1`` (optional)

  editable or not editable list can activate the multi-editing feature by defining the
  `multi_edit="1"`

:default_group_by:
  string_ :ref:`model <reference/orm/model>` field name (optional)


  whether the list view should be grouped if no grouping is specified via the action or
  the current search. Should be the name of the field to group by when no grouping is
  otherwise specified

:default_order:
  `Comma-separated values`_ (optional)

  overrides the ordering of the view, replacing the model's order (:attr:`~odoo.models.BaseModel._order` model attribute).
  The value is a comma-separated list of :ref:`fields <reference/orm/fields>`, postfixed by ``desc`` to
  sort in reverse order:

  .. code-block:: xml

    <tree default_order="sequence,name desc">
      ...
    </tree>

:decoration-{$name}:
  `python expression`_ that defines a boolean_ (optional)

  allow changing the style of a row's text based on the corresponding
  record's attributes.

  ``{$name}`` can be ``bf`` (``font-weight: bold``), ``it``
  (``font-style: italic``), or any `bootstrap contextual color`_ (``danger``,
  ``info``, ``muted``, ``primary``, ``success`` or ``warning``).

  .. code-block:: xml

    <tree decoration-danger="field_qty > field_limit">
      ...
    </tree>

:limit:
  integer_ (optional)

  the default size of a page. It must be a positive integer

:groups_limit:
  integer_ (optional)

  when the list view is grouped, the default number of groups of a page. It must be a
  position integer

:expand:
  boolean_ (optional)

  when the list view is grouped, automatically open the first level of groups if set
  to true (default: false)

Possible children elements of the list view are: ``button``, ``field``, ``groupby``,
``header`` or ``control``

.. _reference/user_interface/views/list/components:

Components
----------

.. _reference/user_interface/views/list/field:

<field>: render formatted values
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

  <tree>
    <field name="FIELD_NAME"/>
  </tree>

defines a column where the corresponding field should be displayed for
each record. Can use the following attributes:

.. rst-class:: o-definition-list

``name``
    the name of the field to display in the current model. A given name
    can only be used once per view
``string``
    the title of the field's column (by default, uses the ``string`` of
    the model's field)
``invisible``
    standard dynamic attributes based on record values. Hide the field
    if trully or if the domain result is trully.

    Fetches and stores the field, but doesn't display the column in the
    table. Necessary for fields which shouldn't be displayed but are
    used by e.g. ``@colors`` or a domain.
``readonly``
    standard dynamic attributes based on record values. If the value is
    trully or the domain result is trully, display the field in both readonly
    and edit mode, but never make it editable
``required``
    standard dynamic attributes based on record values. If the value is
    trully or the domain result is trully, generates an error and prevents
    saving the record if the field doesn't have a value
``groups``
    lists the groups which should be able to see the field
``widget``
    alternate representations for a field's display. Possible list view
    values are (among others):

    .. rst-class:: o-definition-list

    ``progressbar``
        displays ``float`` fields as a progress bar.
    ``handle``
        for ``sequence`` (or ``integer``) fields by which records are
        sorted, instead of displaying the field's value just displays a
        drag&drop icon to reorder records.
``sum``, ``avg``
    displays the corresponding aggregate at the bottom of the column. The
    aggregation is only computed on *currently displayed* records. The
    aggregation operation must match the corresponding field's
    ``group_operator``
``width`` (for ``editable``)
    when there is no data in the list, the width of a column can be forced
    by setting this attribute. The value can be an absolute width (e.g.
    '100px'). Note that when there are records in the list, we let the
    browser automatically adapt the column's widths according to their
    content, and this attribute is thus ignored.
``decoration-{$name}``
    allow changing the style of a cell's text based on the corresponding
    record's attributes.

    ``{$name}`` can be ``bf`` (``font-weight: bold``), ``it``
    (``font-style: italic``), or any `bootstrap contextual color`_ (``danger``,
    ``info``, ``muted``, ``primary``, ``success`` or ``warning``).

    Define a conditional display of a record in the style of a row's text based on the corresponding
    record's attributes.

    Values are Python expressions. For each record, the expression is evaluated
    with the record's attributes as context values and if ``true``, the
    corresponding style is applied to the row. Here are some of the other values
    available in the context:

    * ``uid``: the id of the current user,
    * ``today``: the current local date as a string of the form ``YYYY-MM-DD``,
    * ``now``: same as ``today`` with the addition of the current time.
        This value is formatted as ``YYYY-MM-DD hh:mm:ss``.

    .. code-block:: xml

        <tree decoration-info="state == 'draft'"
            decoration-danger="state == 'help_needed'"
            decoration-bf="state='busy'">
            <!-- TREE_VIEW_CONTENT -->
        </tree>

    .. warning::
        Supported values differ for the two view types. The Gantt view only supports ``success``,
        ``info``, ``warning``, ``danger`` and ``secondary`` displays. The list view supports ``bf``,
        ``it``, ``success``, ``info``, ``warning``, ``danger``, ``muted`` and ``primary`` displays.

``nolabel``
    if set to "1", the column header will remain empty. Also, the column
    won't be sortable.

.. note::

    if the list view is ``editable``, any field attribute from the
    :ref:`form view <reference/user_interface/views/form>` is also valid and will
    be used when setting up the inline form view.

.. note::

    In case of list sub-views (One2many/Many2many display in a form view),
    The attribute ``column_invisible`` can be useful to hide a column
    depending on the parent object.

    .. code-block:: xml

        <field name="product_is_late" column_invisible="[('parent.has_late_products', '=', False)]"/>

.. note:: When a list view is grouped, numeric fields are aggregated and
    displayed for each group.  Also, if there are too many records in
    a group, a pager will appear on the right of the group row. For
    this reason, it is not a good practice to have a numeric field in
    the last column, when the list view is in a situation where it can
    be grouped (it is however fine for x2manys field in a form view:
    they cannot be grouped).

.. _reference/user_interface/views/list/button:

<button>: display button to call action
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

  <tree>
    <button type="object" name="ACTION" string="LABEL"/>
    <button type="object" name="ACTION" icon="FONT_AWESOME"/>
  </tree>

.. include:: views/component_button.rst

.. _reference/user_interface/views/list/groupby:

<groupby>: custom headers when grouping
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

  <tree>
    ...
    <groupby name="FIELD_NAME">
      <BUTTONS/>
      <FIELDS/>
    </groupby>
  </tree>

defines custom headers (with buttons) for the current view when grouping
records on many2one fields. It is also possible to add `field`, inside the
`groupby` which can be used for modifiers. These fields thus belong on the
many2one comodel. These extra fields will be fetched in batch.

.. rst-class:: o-definition-list

``name``
    the name of a many2one field (on the current model). Custom header will be
    displayed when grouping the view on this field name.

.. code-block:: xml

    <groupby name="partner_id">
        <field name="name"/> <!-- name of partner_id -->
        <button type="edit" name="edit" string="Edit"/>
        <button type="object" name="my_method" string="Button1"
        invisible="[('name', '=', 'Georges')]"/>
    </groupby>

A special button (`type="edit"`) can be defined to open the many2one form view.

.. _reference/user_interface/views/list/header:

<header>: custom buttons in control panel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

  <tree>
    <header>
      <BUTTONS/>
      <FIELDS/>
    </header>
    ...
  </tree>

.. include:: header_buttons.rst

Below is an example with the status widget with some options.

.. code-block:: xml

  <header>
    <button string="Reset" type="object" name="set_draft" states="done"/>
    <field name="state" widget="statusbar" statusbar_visible="draft,posted" options="{'clickable': 1}"/>
  </header>

.. _reference/user_interface/views/list/control:

<control>: custom controls
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

  <tree>
    <control>
      <create string="LABEL"/>
      <BUTTONS/>
    </control>
    ...
  </tree>

defines custom controls for the current view.

This makes sense if the parent ``tree`` view is inside a One2many field.

Does not support any attribute, but can have children:

.. rst-class:: o-definition-list

``create``
adds a button to create a new element on the current list.

.. rst-class:: o-definition-list

.. note:: If any ``create`` is defined, it will overwrite the default
            "add a line" button.

The following attributes are supported:

.. rst-class:: o-definition-list

``string`` (required)
    The text displayed on the button.

``context``
    This context will be merged into the existing context
    when retrieving the default value of the new record.

    For example it can be used to override default values.


The following example will override the default "add a line" button
by replacing it with 3 new buttons:
"Add a product", "Add a section" and "Add a note".

"Add a product" will set the field 'display_type' to its default value.

The two other buttons will set the field 'display_type'
to be respectively 'line_section' and 'line_note'.

.. code-block:: xml

    <control>
        <create
        string="Add a product"
        />
        <create
        string="Add a section"
        context="{'default_display_type': 'line_section'}"
        />
        <create
        string="Add a note"
        context="{'default_display_type': 'line_note'}"
        />
    </control>

.. [#treehistory] for historical reasons, it has its origin in tree-type views
                later repurposed to a more table/list-type display


.. _attributes: https://en.wikipedia.org/wiki/HTML_attribute
.. _`python expression`: https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not
.. _bootstrap contextual color: https://getbootstrap.com/docs/3.3/components/#available-variations
.. _`Comma-separated values`: https://en.wikipedia.org/wiki/Comma-separated_values
.. _integer: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
.. _string: https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
.. _boolean: https://docs.python.org/3/library/stdtypes.html#boolean-values
