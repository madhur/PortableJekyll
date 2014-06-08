/* -*- Mode: C; tab-width: 8; indent-tabs-mode: t; c-basic-offset: 8 -*- */
#ifndef __GLADE_WIDGET_ADAPTOR_H__
#define __GLADE_WIDGET_ADAPTOR_H__

#include <gladeui/glade-xml-utils.h>
#include <gladeui/glade-property-class.h>
#include <gladeui/glade-editor-property.h>
#include <gladeui/glade-catalog.h>
#include <gladeui/glade-editable.h>
#include <glib-object.h>
#include <gmodule.h>
#include <gtk/gtk.h>

G_BEGIN_DECLS

#define GLADE_TYPE_WIDGET_ADAPTOR            (glade_widget_adaptor_get_type())
#define GLADE_WIDGET_ADAPTOR(obj)            (G_TYPE_CHECK_INSTANCE_CAST ((obj), GLADE_TYPE_WIDGET_ADAPTOR, GladeWidgetAdaptor))
#define GLADE_WIDGET_ADAPTOR_CLASS(klass)    (G_TYPE_CHECK_CLASS_CAST ((klass), GLADE_TYPE_WIDGET_ADAPTOR, GladeWidgetAdaptorClass))
#define GLADE_IS_WIDGET_ADAPTOR(obj)         (G_TYPE_CHECK_INSTANCE_TYPE ((obj), GLADE_TYPE_WIDGET_ADAPTOR))
#define GLADE_IS_WIDGET_ADAPTOR_CLASS(klass) (G_TYPE_CHECK_CLASS_TYPE ((klass), GLADE_TYPE_WIDGET_ADAPTOR))
#define GLADE_WIDGET_ADAPTOR_GET_CLASS(o)    (G_TYPE_INSTANCE_GET_CLASS ((o), GLADE_WIDGET_ADAPTOR, GladeWidgetAdaptorClass))

typedef struct _GladeWidgetAdaptor        GladeWidgetAdaptor;
typedef struct _GladeWidgetAdaptorPrivate GladeWidgetAdaptorPrivate;
typedef struct _GladeWidgetAdaptorClass   GladeWidgetAdaptorClass;

/**
 * GWA_IS_FIXED:
 * @obj: A #GladeWidgetAdaptor
 *
 * Checks whether this widget adaptor should be handled 
 * as a free-form container
 */
#define GWA_IS_FIXED(obj) \
        ((obj) ? GLADE_WIDGET_ADAPTOR_GET_CLASS(obj)->fixed : FALSE)

/**
 * GWA_DEPRECATED:
 * @obj: A #GladeWidgetAdaptor
 *
 * Checks whether this widget class is marked as deprecated
 */
#define GWA_DEPRECATED(obj) \
        ((obj) ? GLADE_WIDGET_ADAPTOR_GET_CLASS(obj)->deprecated : FALSE)

/**
 * GWA_LIBGLADE_UNSUPPORTED:
 * @obj: A #GladeWidgetAdaptor
 *
 * Checks whether this widget class is unsupported by Libglade
 */
#define GWA_LIBGLADE_UNSUPPORTED(obj) \
        ((obj) ? GLADE_WIDGET_ADAPTOR_GET_CLASS(obj)->libglade_unsupported : FALSE)

/**
 * GWA_LIBGLADE_ONLY:
 * @obj: A #GladeWidgetAdaptor
 *
 * Checks whether this widget class is only supported by libglade
 */
#define GWA_LIBGLADE_ONLY(obj) \
        ((obj) ? GLADE_WIDGET_ADAPTOR_GET_CLASS(obj)->libglade_only : FALSE)

/**
 * GWA_VERSION_SINCE_MAJOR:
 * @obj: A #GladeWidgetAdaptor
 *
 * Checks major version in which this widget was introduced
 */
#define GWA_VERSION_SINCE_MAJOR(obj) \
        ((obj) ? GLADE_WIDGET_ADAPTOR_GET_CLASS(obj)->version_since_major : 0)

/**
 * GWA_VERSION_SINCE_MINOR:
 * @obj: A #GladeWidgetAdaptor
 *
 * Checks minor version in which this widget was introduced
 */
#define GWA_VERSION_SINCE_MINOR(obj) \
        ((obj) ? GLADE_WIDGET_ADAPTOR_GET_CLASS(obj)->version_since_minor : 0)

/**
 * GWA_BUILDER_SINCE_MAJOR:
 * @obj: A #GladeWidgetAdaptor
 *
 * Checks major version in which this widget introduced gtkbuilder support
 */
#define GWA_BUILDER_SINCE_MAJOR(obj) \
        ((obj) ? GLADE_WIDGET_ADAPTOR_GET_CLASS(obj)->builder_since_major : 0)

/**
 * GWA_BUILDER_SINCE_MINOR:
 * @obj: A #GladeWidgetAdaptor
 *
 * Checks minor version in which this widget introduced gtkbuilder support
 */
#define GWA_BUILDER_SINCE_MINOR(obj) \
        ((obj) ? GLADE_WIDGET_ADAPTOR_GET_CLASS(obj)->builder_since_minor : 0)


/**
 * GWA_VERSION_CHECK:
 * @adaptor: A #GladeWidgetAdaptor
 * @major_version: The major version to check
 * @minor_version: The minor version to check
 *
 * Evaluates to %TRUE if @adaptor is available in its owning library version-@major_verion.@minor_version.
 *
 */
#define GWA_VERSION_CHECK(adaptor, major_version, minor_version)	\
	((GWA_VERSION_SINCE_MAJOR (adaptor) == major_version) ? \
	 (GWA_VERSION_SINCE_MINOR (adaptor) <= minor_version) : \
	 (GWA_VERSION_SINCE_MAJOR (adaptor) <= major_version))



/**
 * GWA_BUILDER_VERSION_CHECK:
 * @adaptor: A #GladeWidgetAdaptor
 * @major_version: The major version to check
 * @minor_version: The minor version to check
 *
 * Evaluates to %TRUE if @adaptor is available for use with GtkBuilder in its 
 * owning library version-@major_verion.@minor_version.
 *
 */
#define GWA_BUILDER_VERSION_CHECK(adaptor, major_version, minor_version) \
	((GWA_BUILDER_SINCE_MAJOR (adaptor) == major_version) ? \
	 (GWA_BUILDER_SINCE_MINOR (adaptor) <= minor_version) : \
	 (GWA_BUILDER_SINCE_MAJOR (adaptor) <= major_version))

/**
 * GWA_IS_TOPLEVEL:
 * @obj: A #GladeWidgetAdaptor
 *
 * Checks whether this widget class has been marked as
 * a toplevel one.
 */
#define GWA_IS_TOPLEVEL(obj) \
        ((obj) ? GLADE_WIDGET_ADAPTOR_GET_CLASS(obj)->toplevel : FALSE)

/**
 * GWA_USE_PLACEHOLDERS:
 * @obj: A #GladeWidgetAdaptor
 *
 * Checks whether this widget class has been marked to
 * use placeholders in child widget operations
 */
#define GWA_USE_PLACEHOLDERS(obj) \
        ((obj) ? GLADE_WIDGET_ADAPTOR_GET_CLASS(obj)->use_placeholders : FALSE)


/**
 * GWA_DEFAULT_WIDTH:
 * @obj: A #GladeWidgetAdaptor
 *
 * Returns: the default width to be used when this widget
 * is toplevel in the GladeDesignLayout
 */
#define GWA_DEFAULT_WIDTH(obj) \
        ((obj) ? GLADE_WIDGET_ADAPTOR_GET_CLASS(obj)->default_width : -1)


/**
 * GWA_DEFAULT_HEIGHT:
 * @obj: A #GladeWidgetAdaptor
 *
 * Returns: the default width to be used when this widget
 * is toplevel in the GladeDesignLayout
 */
#define GWA_DEFAULT_HEIGHT(obj) \
        ((obj) ? GLADE_WIDGET_ADAPTOR_GET_CLASS(obj)->default_height : -1)


/**
 * GWA_SCROLLABLE_WIDGET:
 * @obj: A #GladeWidgetAdaptor
 *
 * Checks whether this is a GtkWidgetClass with scrolling capabilities.
 */
#define GWA_SCROLLABLE_WIDGET(obj) \
        ((obj) ? GLADE_WIDGET_ADAPTOR_GET_CLASS(obj)->scrollable : FALSE)


/**
 * GWA_GET_CLASS:
 * @type: A #GType
 *
 * Shorthand for referencing glade adaptor classes from
 * the plugin eg. GWA_GET_CLASS (GTK_TYPE_CONTAINER)->post_create (adaptor...
 */
#define GWA_GET_CLASS(type)                                                      \
    (((type) == G_TYPE_OBJECT) ?                                                 \
     (GladeWidgetAdaptorClass *)g_type_class_peek (GLADE_TYPE_WIDGET_ADAPTOR) :  \
     GLADE_WIDGET_ADAPTOR_GET_CLASS (glade_widget_adaptor_get_by_type(type)))

/**
 * GWA_GET_OCLASS:
 * @type: A #GType.
 *
 * Same as GWA_GET_CLASS but casted to GObjectClass
 */
#define GWA_GET_OCLASS(type) ((GObjectClass*)GWA_GET_CLASS(type))


#define GLADE_SIGNAL_CLASS(klass) ((GladeSignalClass *)(klass))

/**
 * GSC_VERSION_CHECK:
 * @klass: A #GladeSignalClass
 * @major_version: The major version to check
 * @minor_version: The minor version to check
 *
 * Evaluates to %TRUE if @klass is available in its owning library version-@major_verion.@minor_version.
 *
 */
#define GSC_VERSION_CHECK(klass, major_version, minor_version)	\
	((GLADE_SIGNAL_CLASS (klass)->version_since_major == major_version) ? \
	 (GLADE_SIGNAL_CLASS (klass)->version_since_minor <= minor_version) : \
	 (GLADE_SIGNAL_CLASS (klass)->version_since_major <= major_version))


#define GLADE_VALID_CREATE_REASON(reason) (reason >= 0 && reason < GLADE_CREATE_REASONS)

/**
 * GladeCreateReason:
 * @GLADE_CREATE_USER: Was created at the user's request
 *                     (this is a good time to set any properties
 *                     or add children to the project; like GtkFrame's 
 *                     label for example).
 * @GLADE_CREATE_COPY: Was created as a result of the copy/paste 
 *                     mechanism, at this point you can count on glade
 *                     to follow up with properties and children on 
 *                     its own.
 * @GLADE_CREATE_LOAD: Was created during the load process.
 * @GLADE_CREATE_REBUILD: Was created as a replacement for another project 
 *                        object; this only happens when the user is 
 *                        changing a property that is marked by the type 
 *                        system as G_PARAM_SPEC_CONSTRUCT_ONLY.
 * @GLADE_CREATE_REASONS: Never used.
 *
 * These are the reasons your #GladePostCreateFunc can be called.
 */
typedef enum
{
	GLADE_CREATE_USER = 0,
	GLADE_CREATE_COPY,
	GLADE_CREATE_LOAD,
	GLADE_CREATE_REBUILD,
	GLADE_CREATE_REASONS
} GladeCreateReason;

#define GLADE_TYPE_CREATE_REASON (glade_create_reason_get_type())

/**
 * GladeSetPropertyFunc:
 * @adaptor: A #GladeWidgetAdaptor
 * @object: The #GObject
 * @property_name: The property identifier
 * @value: The #GValue
 *
 * This delagate function is used to apply the property value on
 * the runtime object.
 *
 * Sets @value on @object for a given #GladePropertyClass
 */
typedef void     (* GladeSetPropertyFunc)    (GladeWidgetAdaptor *adaptor,
					      GObject            *object,
					      const gchar        *property_name,
					      const GValue       *value);

/**
 * GladeGetPropertyFunc:
 * @adaptor: A #GladeWidgetAdaptor
 * @object: The #GObject
 * @property_name: The property identifier
 * @value: The #GValue
 *
 * Gets @value on @object for a given #GladePropertyClass
 */
typedef void     (* GladeGetPropertyFunc)    (GladeWidgetAdaptor *adaptor,
					      GObject            *object,
					      const gchar        *property_name,
					      GValue             *value);

/**
 * GladeVerifyPropertyFunc:
 * @adaptor: A #GladeWidgetAdaptor
 * @object: The #GObject
 * @property_name: The property identifier
 * @value: The #GValue
 *
 * This delagate function is always called whenever setting any
 * properties with the exception of load time, and copy/paste time
 * (basicly the two places where we recreate a hierarchy that we
 * already know "works") its basicly an optional backend provided
 * boundry checker for properties.
 *
 * Returns: whether or not its OK to set @value on @object
 */
typedef gboolean (* GladeVerifyPropertyFunc)      (GladeWidgetAdaptor *adaptor,
						   GObject            *object,
						   const gchar        *property_name,
						   const GValue       *value);

/**
 * GladeChildSetPropertyFunc:
 * @adaptor: A #GladeWidgetAdaptor
 * @container: The #GObject container
 * @child: The #GObject child
 * @property_name: The property name
 * @value: The #GValue
 *
 * Called to set the packing property @property_name to @value
 * on the @child object of @container.
 */
typedef void   (* GladeChildSetPropertyFunc)      (GladeWidgetAdaptor *adaptor,
						   GObject            *container,
						   GObject            *child,
						   const gchar        *property_name,
						   const GValue       *value);

/**
 * GladeChildGetPropertyFunc:
 * @adaptor: A #GladeWidgetAdaptor
 * @container: The #GObject container
 * @child: The #GObject child
 * @property_name: The property name
 * @value: The #GValue
 *
 * Called to get the packing property @property_name
 * on the @child object of @container into @value.
 */
typedef void   (* GladeChildGetPropertyFunc)      (GladeWidgetAdaptor *adaptor,
						   GObject            *container,
						   GObject            *child,
						   const gchar        *property_name,
						   GValue             *value);

/**
 * GladeChildVerifyPropertyFunc:
 * @adaptor: A #GladeWidgetAdaptor
 * @container: The #GObject container
 * @child: The #GObject child
 * @property_name: The property name
 * @value: The #GValue
 *
 * This delagate function is always called whenever setting any
 * properties with the exception of load time, and copy/paste time
 * (basicly the two places where we recreate a hierarchy that we
 * already know "works") its basicly an optional backend provided
 * boundry checker for properties.
 *
 * Returns: whether or not its OK to set @value on @object
 */
typedef gboolean (* GladeChildVerifyPropertyFunc) (GladeWidgetAdaptor *adaptor,
						   GObject            *container,
						   GObject            *child,
						   const gchar        *property_name,
						   const GValue       *value);


/**
 * GladeGetChildrenFunc:
 * @container: A #GObject container
 *
 * A function called to get @containers children.
 *
 * Returns: A #GList of #GObject children.
 */
typedef GList   *(* GladeGetChildrenFunc)         (GladeWidgetAdaptor *adaptor,
						   GObject            *container);

/**
 * GladeAddChildFunc:
 * @parent: A #GObject container
 * @child: A #GObject child
 *
 * Called to add @child to @parent.
 */
typedef void     (* GladeAddChildFunc)            (GladeWidgetAdaptor *adaptor,
						   GObject            *parent,
						   GObject            *child);
/**
 * GladeRemoveChildFunc:
 * @parent: A #GObject container
 * @child: A #GObject child
 *
 * Called to remove @child from @parent.
 */
typedef void     (* GladeRemoveChildFunc)         (GladeWidgetAdaptor *adaptor,
						   GObject            *parent,
						   GObject            *child);

/**
 * GladeReplaceChildFunc:
 * @container: A #GObject container
 * @old_obj: The old #GObject child
 * @new_obj: The new #GObject child to take its place
 * 
 * Called to swap placeholders with project objects
 * in containers.
 */
typedef void     (* GladeReplaceChildFunc)        (GladeWidgetAdaptor *adaptor,
						   GObject            *container,  
						   GObject            *old_obj,
						   GObject            *new_obj);


/**
 * GladeConstructObjectFunc:
 * @adaptor: A #GladeWidgetAdaptor
 * @n_parameters: amount of construct parameters
 * @parameters: array of construct #GParameter args to create 
 *              the new object with.
 *
 * This function is called to construct a GObject instance.
 * (for language bindings that may need to construct a wrapper
 * object).
 *
 * Returns: A newly created #GObject
 */
typedef GObject *(* GladeConstructObjectFunc)     (GladeWidgetAdaptor *adaptor,
						   guint               n_parameters,
						   GParameter         *parameters);



/**
 * GladePostCreateFunc:
 * @object: a #GObject
 * @reason: a #GladeCreateReason
 *
 * This function is called exactly once for any project object
 * instance and can be for any #GladeCreateReason.
 */
typedef void     (* GladePostCreateFunc)          (GladeWidgetAdaptor *adaptor,
						   GObject            *object,
						   GladeCreateReason   reason);

/**
 * GladeGetInternalFunc:
 * @parent: A #GObject composite object
 * @name: A string identifier
 *
 * Called to lookup @child in composite object @parent by @name.
 *
 * Returns: The specified internal widget.
 */
typedef GObject *(* GladeGetInternalFunc)         (GladeWidgetAdaptor *adaptor,
						   GObject            *parent,
						   const gchar        *name);

/**
 * GladeActionActivateFunc:
 * @adaptor: A #GladeWidgetAdaptor
 * @object: The #GObject
 * @action_path: The action path
 *
 * This delagate function is used to catch actions from the core.
 *
 */
typedef void     (* GladeActionActivateFunc)  (GladeWidgetAdaptor *adaptor,
					       GObject            *object,
					       const gchar        *action_path);

/**
 * GladeChildActionActivateFunc:
 * @adaptor: A #GladeWidgetAdaptor
 * @container: The #GtkContainer
 * @object: The #GObject
 * @action_path: The action path
 *
 * This delagate function is used to catch packing actions from the core.
 *
 */
typedef void     (* GladeChildActionActivateFunc) (GladeWidgetAdaptor *adaptor,
						   GObject            *container,
						   GObject            *object,
						   const gchar        *action_path);


/**
 * GladeActionSubmenuFunc:
 * @adaptor: A #GladeWidgetAdaptor
 * @object: The #GObject
 * @action_path: The action path
 *
 * This delagate function is used to create dynamically customized
 * submenus. Called only for actions that dont have children.
 *
 */
typedef GtkWidget  *(* GladeActionSubmenuFunc)  (GladeWidgetAdaptor *adaptor,
						 GObject            *object,
						 const gchar        *action_path);


/**
 * GladeDependsFunc:
 * @adaptor: A #GladeWidgetAdaptor
 * @widget: A #GladeWidget of the adaptor
 * @another: another #GladeWidget
 *
 * Checks whether @widget depends on @another to be placed earlier in
 * the glade file.
 *
 * Returns: whether @widget depends on @another being parsed first in
 * the resulting glade file.
 */
typedef gboolean (* GladeDependsFunc) (GladeWidgetAdaptor *adaptor,
				       GladeWidget        *widget,
				       GladeWidget        *another);



/**
 * GladeReadWidgetFunc:
 * @adaptor: A #GladeWidgetAdaptor
 * @widget: The #GladeWidget
 * @node: The #GladeXmlNode
 *
 * This function is called to update @widget from @node.
 *
 */
typedef void     (* GladeReadWidgetFunc) (GladeWidgetAdaptor *adaptor,
					  GladeWidget        *widget,
					  GladeXmlNode       *node);

/**
 * GladeWriteWidgetFunc:
 * @adaptor: A #GladeWidgetAdaptor
 * @widget: The #GladeWidget
 * @node: The #GladeXmlNode
 *
 * This function is called to fill in @node from @widget.
 *
 */
typedef void     (* GladeWriteWidgetFunc) (GladeWidgetAdaptor *adaptor,
					   GladeWidget        *widget,
					   GladeXmlContext    *context,
					   GladeXmlNode       *node);


/**
 * GladeCreateEPropFunc:
 * @adaptor: A #GladeWidgetAdaptor
 * @klass: The #GladePropertyClass to be edited
 * @use_command: whether to use the GladeCommand interface
 * to commit property changes
 * 
 * Creates a GladeEditorProperty to edit @klass
 *
 * Returns: A newly created #GladeEditorProperty
 */
typedef GladeEditorProperty *(* GladeCreateEPropFunc) (GladeWidgetAdaptor *adaptor,
						       GladePropertyClass *klass,
						       gboolean            use_command);

/**
 * GladeStringFromValueFunc:
 * @adaptor: A #GladeWidgetAdaptor
 * @klass: The #GladePropertyClass 
 * @value: The #GValue to convert to a string
 * @fmt: The #GladeProjectFormat the string should conform to
 * 
 * For normal properties this is used to serialize
 * property values, for custom properties (only when new pspecs are 
 * introduced) its needed for value comparisons in boxed pspecs 
 * and also to update the UI for undo/redo items etc.
 *
 * Returns: A newly allocated string representation of @value
 */
typedef gchar   *(* GladeStringFromValueFunc) (GladeWidgetAdaptor *adaptor,
					       GladePropertyClass *klass,
					       const GValue       *value,
					       GladeProjectFormat  fmt);



/**
 * GladeCreateEditableFunc:
 * @adaptor: A #GladeWidgetAdaptor
 * @type: The #GladeEditorPageType
 * 
 * This is used to allow the backend to override the way an
 * editor page is layed out (note that editor widgets are created
 * on demand and not at startup).
 *
 * Returns: A new #GladeEditable widget
 */
typedef GladeEditable *(* GladeCreateEditableFunc) (GladeWidgetAdaptor   *adaptor,
						    GladeEditorPageType   type);


/* GladeSignalClass contains all the info we need for a given signal, such as
 * the signal name, and maybe more in the future 
 */
typedef struct _GladeSignalClass GladeSignalClass; 
struct _GladeSignalClass
{
	GladeWidgetAdaptor *adaptor; /* The adaptor that originated this signal.
				      */

	GSignalQuery query;

	guint16      version_since_major; /* Version in which this signal was
					   * introduced
					   */
	guint16      version_since_minor;

	const gchar *name;         /* Name of the signal, eg clicked */
	const gchar *type;         /* Name of the object class that this signal belongs to
				    * eg GtkButton */

};

/* Note that everything that must be processed at the creation of
 * every instance is managed on the instance structure, and everywhere
 * that we want to take advantage of inheritance is handled in the class
 * structure.
 */
struct _GladeWidgetAdaptor
{
	GObject      parent_instance;

	GType        type;         /* GType of the widget */

	gchar       *name;         /* Name of the widget, for example GtkButton */


	gchar       *generic_name; /* Used to generate names of new widgets, for
				    * example "button" so that we generate button1,
				    * button2, buttonX ..
				    */
				    
	gchar       *icon_name;    /* icon name to use for widget class */
	gchar       *missing_icon; /* the name of the missing icon if it was not found */

	gchar       *title;        /* Translated class name used in the UI */

	GList       *properties;   /* List of GladePropertyClass objects.
				    * [see glade-property.h] this list contains
				    * properties about the widget that we are going
				    * to modify. Like "title", "label", "rows" .
				    * Each property creates an input in the propety
				    * editor.
				    */
	GList       *packing_props; /* List of GladePropertyClass objects that describe
				     * properties for child objects packing definition -
				     * note there may be more than one type of child supported
				     * by a widget and thus they may have different sets
				     * of properties for each type - this association is
				     * managed on the GladePropertyClass proper.
				     */
  
	GList       *signals;        /* List of GladeSignalClass objects */

        GList       *child_packings; /* Default packing property values */

	GList       *actions;        /* A list of GWActionClass */
	
	GList       *packing_actions;/* A list of GWActionClass for child objects */

	GladeWidgetAdaptorPrivate *priv;

};

struct _GladeWidgetAdaptorClass
{
	GObjectClass               parent_class;

	guint16                    version_since_major; /* Version in which this widget was */
	guint16                    version_since_minor; /* introduced.                      */

	guint16                    builder_since_major; /* Version in which this widget became */
	guint16                    builder_since_minor; /* available in GtkBuilder format      */


	guint                      deprecated : 1;          /* If this widget is currently
							     * deprecated
							     */
	guint                      libglade_unsupported : 1; /* If this widget is not supported
							      * by libglade
							      */
	guint                      libglade_only : 1;        /* If this widget is only supported
							      * by libglade
							      */

	guint                      fixed : 1;                /* If this is a Container, use free-form
							      * placement with drag/resize/paste at mouse...
							      */
	guint                      toplevel : 1;             /* If this class is toplevel */

	guint                      use_placeholders : 1;     /* Whether or not to use placeholders
							      * to interface with child widgets.
							      */

	guint                      scrollable : 1;           /* Whether this is a widget class that has
							      * klass->set_scroll_adjustments_signal != NULL (i.e.
							      * can be directly added to a GtkScrolledWindow).
							      */

	gint                       default_width;  /* Default width in GladeDesignLayout */
	gint                       default_height; /* Default height in GladeDesignLayout */

	GladeConstructObjectFunc   construct_object;  /* Object constructor
						       */

	GladePostCreateFunc        deep_post_create;   /* Executed after widget creation: 
							* plugins use this to setup various
							* support codes (adaptors must always
							* chain up in this stage of instantiation).
							*/

	GladePostCreateFunc        post_create;   /* Executed after widget creation: 
						   * plugins use this to setup various
						   * support codes (adaptors are free here
						   * to chain up or not in this stage of
						   * instantiation).
						   */

	GladeGetInternalFunc       get_internal_child; /* Retrieves the the internal child
							* of the given name.
							*/

	/* Delagate to verify if this is a valid value for this property,
	 * if this function exists and returns FALSE, then glade_property_set
	 * will abort before making any changes
	 */
	GladeVerifyPropertyFunc verify_property;
	
	/* An optional backend function used instead of g_object_set()
	 * virtual properties must be handled with this function.
	 */
	GladeSetPropertyFunc set_property;

	/* An optional backend function used instead of g_object_get()
	 * virtual properties must be handled with this function.
	 *
	 * Note that since glade knows what the property values are 
	 * at all times regardless of the objects copy, this is currently
	 * only used to obtain the values of packing properties that are
	 * set by the said object's parent at "container_add" time.
	 */
	GladeGetPropertyFunc get_property;


	GladeAddChildFunc          add;              /* Adds a new child of this type */
	GladeRemoveChildFunc       remove;           /* Removes a child from the container */
	GladeGetChildrenFunc       get_children;     /* Returns a list of direct children for
						      * this support type.
						      */


	
	GladeChildVerifyPropertyFunc child_verify_property; /* A boundry checker for 
							     * packing properties 
							     */
	GladeChildSetPropertyFunc    child_set_property; /* Sets/Gets a packing property */
	GladeChildGetPropertyFunc    child_get_property; /* for this child */
	
	GladeReplaceChildFunc        replace_child;  /* This method replaces a 
						      * child widget with
						      * another one: it's used to
						      * replace a placeholder with
						      * a widget and viceversa.
						      */
	
	GladeActionActivateFunc      action_activate;       /* This method is used to catch actions */
	GladeChildActionActivateFunc child_action_activate; /* This method is used to catch packing actions */

	GladeActionSubmenuFunc       action_submenu;       /* Delagate function to create dynamic submenus */
	                                                   /* in action menus. */
	
	GladeDependsFunc             depends; /* Periodically sort widgets in the project */

	GladeReadWidgetFunc          read_widget; /* Reads widget attributes from xml */
	
	GladeWriteWidgetFunc         write_widget; /* Writes widget attributes to the xml */

	GladeReadWidgetFunc          read_child; /* Reads widget attributes from xml */
	
	GladeWriteWidgetFunc         write_child; /* Writes widget attributes to the xml */

	GladeCreateEPropFunc         create_eprop; /* Creates a GladeEditorProperty */

	GladeStringFromValueFunc     string_from_value; /* Creates a string for a value */

	GladeCreateEditableFunc      create_editable; /* Creates a page for the editor */
};

#define glade_widget_adaptor_create_widget(adaptor, query, ...) \
    (glade_widget_adaptor_create_widget_real (query, "adaptor", adaptor, __VA_ARGS__));

#define glade_widget_adaptor_from_pclass(pclass) \
    ((pclass) ? (GladeWidgetAdaptor *)((GladePropertyClass *)(pclass))->handle : NULL)


GType                glade_widget_adaptor_get_type         (void) G_GNUC_CONST;
 

GType                glade_create_reason_get_type          (void) G_GNUC_CONST;

GList               *glade_widget_adaptor_list_adaptors    (void);

GladeWidgetAdaptor  *glade_widget_adaptor_from_catalog     (GladeCatalog         *catalog,
							    GladeXmlNode         *class_node,
							    GModule              *module);

void                 glade_widget_adaptor_register         (GladeWidgetAdaptor   *adaptor);
 
GladeWidget         *glade_widget_adaptor_create_internal  (GladeWidget          *parent,
							    GObject              *internal_object,
							    const gchar          *internal_name,
							    const gchar          *parent_name,
							    gboolean              anarchist,
							    GladeCreateReason     reason);

GladeWidget         *glade_widget_adaptor_create_widget_real (gboolean            query, 
							      const gchar        *first_property,
							      ...);


GladeWidgetAdaptor  *glade_widget_adaptor_get_by_name        (const gchar        *name);

GladeWidgetAdaptor  *glade_widget_adaptor_get_by_type        (GType               type);

GladeWidgetAdaptor  *glade_widget_adaptor_from_pspec         (GladeWidgetAdaptor *adaptor,
							      GParamSpec         *spec);

GladePropertyClass  *glade_widget_adaptor_get_property_class (GladeWidgetAdaptor *adaptor,
							      const gchar        *name);

GladePropertyClass  *glade_widget_adaptor_get_pack_property_class (GladeWidgetAdaptor *adaptor,
								   const gchar        *name);

GParameter          *glade_widget_adaptor_default_params     (GladeWidgetAdaptor *adaptor,
							      gboolean            construct,
							      guint              *n_params);

GObject             *glade_widget_adaptor_construct_object   (GladeWidgetAdaptor *adaptor,
							      guint               n_parameters,
							      GParameter         *parameters);

void                 glade_widget_adaptor_post_create        (GladeWidgetAdaptor *adaptor,
							      GObject            *object,
							      GladeCreateReason   reason);

GObject             *glade_widget_adaptor_get_internal_child (GladeWidgetAdaptor *adaptor,
							      GObject            *object,
							      const gchar        *internal_name);

void                 glade_widget_adaptor_set_property       (GladeWidgetAdaptor *adaptor,
							      GObject            *object,
							      const gchar        *property_name,
							      const GValue       *value);

void                 glade_widget_adaptor_get_property       (GladeWidgetAdaptor *adaptor,
							      GObject            *object,
							      const gchar        *property_name,
							      GValue             *value);

gboolean             glade_widget_adaptor_verify_property    (GladeWidgetAdaptor *adaptor,
							      GObject            *object,
							      const gchar        *property_name,
							      const GValue       *value);

void                 glade_widget_adaptor_add                (GladeWidgetAdaptor *adaptor,
							      GObject            *container,
							      GObject            *child);

void                 glade_widget_adaptor_remove             (GladeWidgetAdaptor *adaptor,
							      GObject            *container,
							      GObject            *child);

GList               *glade_widget_adaptor_get_children       (GladeWidgetAdaptor *adaptor,
							      GObject            *container);

gboolean             glade_widget_adaptor_has_child          (GladeWidgetAdaptor *adaptor,
							      GObject            *container,
							      GObject            *child);

void                 glade_widget_adaptor_child_set_property (GladeWidgetAdaptor *adaptor,
							      GObject            *container,
							      GObject            *child,
							      const gchar        *property_name,
							      const GValue       *value);

void                 glade_widget_adaptor_child_get_property (GladeWidgetAdaptor *adaptor,
							      GObject            *container,
							      GObject            *child,
							      const gchar        *property_name,
							      GValue             *value);

gboolean             glade_widget_adaptor_child_verify_property (GladeWidgetAdaptor *adaptor,
								 GObject            *container,
								 GObject            *child,
								 const gchar        *property_name,
								 const GValue       *value);

void                 glade_widget_adaptor_replace_child      (GladeWidgetAdaptor *adaptor,
							      GObject            *container,
							      GObject            *old_obj,
							      GObject            *new_obj);

gboolean             glade_widget_adaptor_query              (GladeWidgetAdaptor *adaptor);

G_CONST_RETURN
gchar               *glade_widget_adaptor_get_packing_default(GladeWidgetAdaptor *child_adaptor,
							      GladeWidgetAdaptor *container_adaptor,
							      const gchar        *id);

gboolean             glade_widget_adaptor_is_container       (GladeWidgetAdaptor *adaptor);

gboolean             glade_widget_adaptor_action_add         (GladeWidgetAdaptor *adaptor,
							      const gchar *action_path,
							      const gchar *label,
							      const gchar *stock,
							      gboolean important);

gboolean             glade_widget_adaptor_pack_action_add    (GladeWidgetAdaptor *adaptor,
							      const gchar *action_path,
							      const gchar *label,
							      const gchar *stock,
							      gboolean important);

gboolean             glade_widget_adaptor_action_remove      (GladeWidgetAdaptor *adaptor,
							      const gchar *action_path);

gboolean             glade_widget_adaptor_pack_action_remove (GladeWidgetAdaptor *adaptor,
							      const gchar *action_path);

GList               *glade_widget_adaptor_pack_actions_new   (GladeWidgetAdaptor *adaptor);

void                 glade_widget_adaptor_action_activate    (GladeWidgetAdaptor *adaptor,
							      GObject            *object,
							      const gchar        *action_path);

void                 glade_widget_adaptor_child_action_activate (GladeWidgetAdaptor *adaptor,
								 GObject            *container,
								 GObject            *object,
								 const gchar        *action_path);

GtkWidget           *glade_widget_adaptor_action_submenu        (GladeWidgetAdaptor *adaptor,
								 GObject            *object,
								 const gchar        *action_path);

gboolean             glade_widget_adaptor_depends            (GladeWidgetAdaptor *adaptor,
							      GladeWidget        *widget,
							      GladeWidget        *another);


void                 glade_widget_adaptor_read_widget        (GladeWidgetAdaptor *adaptor,
							      GladeWidget        *widget,
							      GladeXmlNode       *node);

void                 glade_widget_adaptor_write_widget       (GladeWidgetAdaptor *adaptor,
							      GladeWidget        *widget,
							      GladeXmlContext    *context,
							      GladeXmlNode       *node);

void                 glade_widget_adaptor_read_child         (GladeWidgetAdaptor *adaptor,
							      GladeWidget        *widget,
							      GladeXmlNode       *node);

void                 glade_widget_adaptor_write_child        (GladeWidgetAdaptor *adaptor,
							      GladeWidget        *widget,
							      GladeXmlContext    *context,
							      GladeXmlNode       *node);

GladeEditorProperty *glade_widget_adaptor_create_eprop       (GladeWidgetAdaptor *adaptor,
							      GladePropertyClass *klass,
							      gboolean            use_command);

GladeEditorProperty *glade_widget_adaptor_create_eprop_by_name (GladeWidgetAdaptor *adaptor,
								const gchar        *property_id,
								gboolean            packing,
								gboolean            use_command);

gchar               *glade_widget_adaptor_string_from_value  (GladeWidgetAdaptor *adaptor,
							      GladePropertyClass *klass,
							      const GValue       *value,
							      GladeProjectFormat  fmt);

GladeEditable       *glade_widget_adaptor_create_editable    (GladeWidgetAdaptor *adaptor,
							      GladeEditorPageType type);

GladeSignalClass    *glade_widget_adaptor_get_signal_class   (GladeWidgetAdaptor *adaptor,
							      const gchar        *name);

GladeWidgetAdaptor  *glade_widget_adaptor_get_parent_adaptor (GladeWidgetAdaptor *adaptor);

G_END_DECLS

#endif /* __GLADE_WIDGET_ADAPTOR_H__ */
