/* -*- Mode: C; tab-width: 8; indent-tabs-mode: t; c-basic-offset: 8 -*- */
#ifndef __GLADE_PROPERTY_CLASS_H__
#define __GLADE_PROPERTY_CLASS_H__

#include <glib.h>
#include <glib-object.h>
#include <gtk/gtk.h>

#include <gladeui/glade-xml-utils.h>

G_BEGIN_DECLS

/* The GladePropertyClass structure parameters of a GladeProperty.
 * All entries in the GladeEditor are GladeProperties (except signals)
 * All GladeProperties are associated with a GParamSpec.
 */
#define GLADE_PROPERTY_CLASS(gpc)     ((GladePropertyClass *) gpc)
#define GLADE_IS_PROPERTY_CLASS(gpc)  (gpc != NULL)


/**
 * GLADE_PROPERTY_CLASS_IS_TYPE:
 * gpc: A #GladePropertyClass
 * type: The #GladeEditorPageType to query
 *
 * Checks if @gpc is good to be loaded as @type
 */
#define GLADE_PROPERTY_CLASS_IS_TYPE(gpc, type)	                \
	(((type) == GLADE_PAGE_GENERAL &&                       \
	  !(gpc)->common && !(gpc)->packing && !(gpc)->atk) ||	\
	 ((type) == GLADE_PAGE_COMMON  && (gpc)->common)    ||  \
	 ((type) == GLADE_PAGE_PACKING && (gpc)->packing)   ||  \
	 ((type) == GLADE_PAGE_ATK     && (gpc)->atk)       ||  \
	 ((type) == GLADE_PAGE_QUERY   && (gpc)->query))


/**
 * GPC_VERSION_CHECK:
 * @klass: A #GladePropertyClass
 * @major_version: The major version to check
 * @minor_version: The minor version to check
 *
 * Evaluates to %TRUE if @klass is available in its owning library version-@major_verion.@minor_version.
 *
 */
#define GPC_VERSION_CHECK(klass, major_version, minor_version)		\
	((GLADE_PROPERTY_CLASS (klass)->version_since_major == major_version) ? \
	 (GLADE_PROPERTY_CLASS (klass)->version_since_minor <= minor_version) : \
	 (GLADE_PROPERTY_CLASS (klass)->version_since_major <= major_version))

/**
 * GPC_BUILDER_VERSION_CHECK:
 * @klass: A #GladePropertyClass
 * @major_version: The major version to check
 * @minor_version: The minor version to check
 *
 * Evaluates to %TRUE if @klass is available for use with GtkBuilder in its 
 * owning library version-@major_verion.@minor_version.
 *
 */
#define GPC_BUILDER_VERSION_CHECK(klass, major_version, minor_version)	\
	((GLADE_PROPERTY_CLASS (klass)->builder_since_major == major_version) ? \
	 (GLADE_PROPERTY_CLASS (klass)->builder_since_minor <= minor_version) : \
	 (GLADE_PROPERTY_CLASS (klass)->builder_since_major <= major_version))


#define GPC_OBJECT_DELIMITER ", "
#define GPC_PROPERTY_NAMELEN 512  /* Enough space for a property name I think */

typedef struct _GladePropertyClass GladePropertyClass;

struct _GladePropertyClass
{

	gpointer    handle; /* The GladeWidgetAdaptor that this property class
			     * was created for.
			     */

	guint16     version_since_major; /* Version in which this property was */
	guint16     version_since_minor; /* introduced.                       */

	guint16     builder_since_major; /* Version in which this property became */
	guint16     builder_since_minor; /* available in GtkBuilder format        */

	GParamSpec *pspec; /* The Parameter Specification for this property.
			    */

	gchar *id;       /* The id of the property. Like "label" or "xpad"
			  * this is a non-translatable string
			  */

	gchar *name;     /* The name of the property. Like "Label" or "X Pad"
			  * this is a translatable string
			  */

	gchar *tooltip; /* The default tooltip for the property editor rows.
			 */

	GValue *def;      /* The default value for this property (this will exist
			   * as a copy of orig_def if not specified by the catalog)
			   */

	GValue *orig_def; /* The real default value obtained through introspection.
			   * (used to decide whether we should write to the
			   * glade file or not, or to restore the loaded property
			   * correctly); all property classes have and orig_def.
			   */

	GList *parameters; /* list of GladeParameter objects. This list
			    * provides with an extra set of key-value
			    * pairs to specify aspects of this property.
			    *
			    * This is unused by glade and only maintained
			    * to be of possible use in plugin code.
			    */

	gint  visible_lines; /* When this pspec calls for a text editor, how many
			      * lines should be visible in the editor.
			      */

	/* For catalogs that support libglade: */
	guint    libglade_only : 1;       /* Mark special libglade virtual properties */
	guint    libglade_unsupported : 1;/* Mark properties that are not available in libglade */

	guint virt : 1; /* Whether this is a virtual property with its pspec supplied
			 * via the catalog (or hard code-paths); or FALSE if its a real
			 * GObject introspected property
			 */

	guint optional : 1; /* Some properties are optional by nature like
			     * default width. It can be set or not set. A
			     * default property has a check box in the
			     * left that enables/disables the input
			     */

	guint optional_default : 1; /* For optional values, what the default is */

	guint construct_only : 1; /* Whether this property is G_PARAM_CONSTRUCT_ONLY or not */
	
	guint common : 1;  /* Common properties go in the common tab */
	guint atk : 1;     /* Atk properties go in the atk tab */
	guint packing : 1; /* Packing properties go in the packing tab */
	guint query : 1;   /* Whether we should explicitly ask the user about this property
			    * when instantiating a widget with this property (through a popup
			    * dialog).
			    */

	
	guint translatable : 1; /* The property should be translatable, which
				 * means that it needs extra parameters in the
				 * UI.
				 */
	
	/* These three are the master switches for the glade-file output,
	 * property editor availability & live object updates in the glade environment.
	 */
	guint save : 1;      /* Whether we should save to the glade file or not
			      * (mostly just for virtual internal glade properties,
			      * also used for properties with generic pspecs that
			      * are saved in custom ways by the plugin)
			      */
	guint save_always : 1; /* Used to make a special case exception and always
				* save this property regardless of what the default
				* value is (used for some special cases like properties
				* that are assigned initial values in composite widgets
				* or derived widget code).
				*/
	guint visible : 1;   /* Whether or not to show this property in the editor &
			      * reset dialog.
			      */

	guint custom_layout : 1; /* Properties marked as custom_layout will not be included
				  * in a base #GladeEditorTable implementation (use this
				  * for properties you want to layout in custom ways in
				  * a #GladeEditable widget
				  */
	
	guint ignore : 1;    /* When true, we will not sync the object when the property
			      * changes, or load values from the object.
			      */

	guint needs_sync : 1; /* Virtual properties need to be synchronized after object
			       * creation, some properties that are not virtual also need
			       * handling from the backend, if "needs-sync" is true then
			       * this property will by synced with virtual properties.
			       */

	guint is_modified : 1; /* If true, this property_class has been "modified" from the
				* the standard property by a xml file. */

	guint themed_icon : 1; /* Some GParamSpecString properties reffer to icon names
				* in the icon theme... these need to be specified in the
				* property class definition if proper editing tools are to
				* be used.
				*/
	guint stock_icon : 1; /* String properties can also denote stock icons, including
			       * icons from icon factories...
			       */
	guint stock : 1;      /* ... or a narrower list of "items" from gtk builtin stock items.
			       */
	
	guint transfer_on_paste : 1; /* If this is a packing prop, 
				      * wether we should transfer it on paste.
				      */
	
	guint parentless_widget : 1;  /* True if this property should point to a parentless widget
				       * in the project
				       */

	gdouble weight;	/* This will determine the position of this property in 
			 * the editor.
			 */
	
	gchar *create_type; /* If this is an object property and you want the option to create
			     * one from the object selection dialog, then set the name of the
			     * concrete type here.
			     */
};


GladePropertyClass *glade_property_class_new                     (gpointer             handle);

GladePropertyClass *glade_property_class_new_from_spec           (gpointer             handle,
								  GParamSpec          *spec);

GladePropertyClass *glade_property_class_new_from_spec_full      (gpointer             handle,
								  GParamSpec          *spec,
								  gboolean             need_handle);

GladePropertyClass *glade_property_class_clone                   (GladePropertyClass  *property_class);

void                glade_property_class_free                    (GladePropertyClass  *property_class);

gboolean            glade_property_class_is_visible              (GladePropertyClass  *property_class);

gboolean            glade_property_class_is_object               (GladePropertyClass  *property_class,
								  GladeProjectFormat   fmt);

GValue             *glade_property_class_make_gvalue_from_string (GladePropertyClass  *property_class,
								  const gchar         *string,
								  GladeProject        *project,
								  GladeWidget         *widget);

gchar              *glade_property_class_make_string_from_gvalue (GladePropertyClass  *property_class,
								  const GValue        *value,
								  GladeProjectFormat   fmt);

GValue             *glade_property_class_make_gvalue_from_vl     (GladePropertyClass  *property_class,
								  va_list              vl);

void                glade_property_class_set_vl_from_gvalue      (GladePropertyClass  *klass,
								  GValue              *value,
								  va_list              vl);

GValue             *glade_property_class_make_gvalue             (GladePropertyClass  *klass,
								  ...);

void                glade_property_class_get_from_gvalue         (GladePropertyClass  *klass,
								  GValue              *value,
								  ...);

gboolean            glade_property_class_update_from_node        (GladeXmlNode        *node,
								  GModule             *module,
								  GType                object_type,
								  GladePropertyClass **property_class,
								  const gchar         *domain);

GtkAdjustment      *glade_property_class_make_adjustment         (GladePropertyClass *property_class);

gboolean            glade_property_class_match                   (GladePropertyClass *klass,
								  GladePropertyClass *comp);

gboolean            glade_property_class_void_value              (GladePropertyClass *klass,
								  GValue             *value);

gint                glade_property_class_compare                 (GladePropertyClass *klass,
								  const GValue       *value1,
								  const GValue       *value2,
								  GladeProjectFormat  fmt);

G_END_DECLS

#endif /* __GLADE_PROPERTY_CLASS_H__ */
