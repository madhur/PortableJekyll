/* -*- Mode: C; tab-width: 8; indent-tabs-mode: t; c-basic-offset: 8 -*- */
#ifndef __GLADE_WIDGET_H__
#define __GLADE_WIDGET_H__

#include <gladeui/glade-widget-adaptor.h>
#include <gladeui/glade-widget-action.h>
#include <gladeui/glade-signal.h>
#include <gladeui/glade-property.h>

#include <glib.h>
#include <glib-object.h>

G_BEGIN_DECLS
 
#define GLADE_TYPE_WIDGET            (glade_widget_get_type ())
#define GLADE_WIDGET(obj)            (G_TYPE_CHECK_INSTANCE_CAST ((obj), GLADE_TYPE_WIDGET, GladeWidget))
#define GLADE_WIDGET_CLASS(klass)    (G_TYPE_CHECK_CLASS_CAST ((klass), GLADE_TYPE_WIDGET, GladeWidgetClass))
#define GLADE_IS_WIDGET(obj)         (G_TYPE_CHECK_INSTANCE_TYPE ((obj), GLADE_TYPE_WIDGET))
#define GLADE_IS_WIDGET_CLASS(klass) (G_TYPE_CHECK_CLASS_TYPE ((klass), GLADE_TYPE_WIDGET))
#define GLADE_WIDGET_GET_CLASS(obj)  (G_TYPE_INSTANCE_GET_CLASS ((obj), GLADE_TYPE_WIDGET, GladeWidgetClass))

typedef struct _GladeWidgetClass  GladeWidgetClass;

struct _GladeWidget
{
	GInitiallyUnowned parent_instance;

	GladeWidgetAdaptor *adaptor; /* An adaptor class for the object type */

	GladeProject       *project; /* A pointer to the project that this 
					widget currently belongs to. */

	GladeWidget  *parent;  /* A pointer to the parent widget in the hierarchy */
	
	gchar *name; /* The name of the widget. For example window1 or
		      * button2. This is a unique name and is the one
		      * used when loading widget with libglade
		      */

	gchar *support_warning; /* A warning message for version incompatabilities
				 * in this widget
				 */
	

	gchar *internal; /* If the widget is an internal child of 
			  * another widget this is the name of the 
			  * internal child, otherwise is NULL.
			  * Internal children cannot be deleted.
			  */
	

	GObject *object; /* A pointer to the object that was created.
			  * if it is a GtkWidget; it is shown as a "view"
			  * of the GladeWidget. This object is updated as
			  * the properties are modified for the GladeWidget.
			  */
	
	GList *properties; /* A list of GladeProperty. A GladeProperty is an
			    * instance of a GladePropertyClass. If a
			    * GladePropertyClass for a gtkbutton is label, its
			    * property is "Ok". 
			    */

	GList *packing_properties; /* A list of GladeProperty. Note that these
				    * properties are related to the container
				    * of the widget, thus they change after
				    * pasting the widget to a different
				    * container. Toplevels widget do not have
				    * packing properties.
				    * See also child_properties of 
				    * GladeWidgetClass.
				    */

	GHashTable *props_hash; /* A Quick reference table to speed up calls to glade_widget_get_property()
				 */	
	GHashTable *pack_props_hash; /* A Quick reference table to speed up calls to glade_widget_get_pack_property()
				      */

	GHashTable *signals; /* A table with a GPtrArray of GladeSignals (signal handlers),
			      * indexed by its name */

	GList     *prop_refs; /* List of properties in the project who's value are `this object'
			       * (this is used to set/unset those properties when the object is
			       * added/removed from the project).
			       */

	gint               width;   /* Current size used in the UI, this is only */
	gint               height;  /* usefull for parentless widgets in the
				     * GladeDesignLayout */

	GList *actions;		/* A GladeWidgetAction list */
	
	GList *packing_actions;	/* A GladeWidgetAction list, this actions are
				 * related to the container and they are not always present.
				 */

	GladeWidget    *lock; /* The glade widget that has locked this widget down.
			       */
	GList          *locked_widgets; /* A list of widgets this widget has locked down.
					 */
	
	/* Construct parameters: */
	GladeWidget       *construct_template;
	GladeCreateReason  construct_reason;
	gchar             *construct_internal;
	guint              construct_exact : 1;


	guint visible : 1; /* Local copy of widget visibility, we need to keep track of this
			    * since the objects copy may be invalid due to a rebuild.
			    */
	guint anarchist : 1; /* Some composite widgets have internal children
			      * that are not part of the same hierarchy; hence 'anarchists',
			      * typicly a popup window or its child (we need to mark
			      * them so we can avoid bookkeeping packing props on them etc.).
			      */

	guint in_project : 1; /* Whether the widget is currently actually in the project */
};

struct _GladeWidgetClass
{
	GInitiallyUnownedClass parent_class;

	void         (*add_child)               (GladeWidget *, GladeWidget *, gboolean);
	void         (*remove_child)            (GladeWidget *, GladeWidget *);
	void         (*replace_child)           (GladeWidget *, GObject *, GObject *);

	void         (*add_signal_handler)	(GladeWidget *, GladeSignal *);
	void         (*remove_signal_handler)	(GladeWidget *, GladeSignal *);
	void         (*change_signal_handler)	(GladeWidget *, GladeSignal *, GladeSignal *);
	
	gint         (*button_press_event)      (GladeWidget *, GdkEvent *);
	gint         (*button_release_event)    (GladeWidget *, GdkEvent *);
	gint         (*motion_notify_event)     (GladeWidget *, GdkEvent *);

	gboolean     (*event)                   (GladeWidget *, GdkEvent *);
};

/*******************************************************************************
                                  General api
 *******************************************************************************/

GType                   glade_widget_get_type		    (void);

GladeWidget            *glade_widget_get_from_gobject       (gpointer          object);

void                    glade_widget_add_child              (GladeWidget      *parent,
							     GladeWidget      *child,
							     gboolean          at_mouse);

void                    glade_widget_remove_child           (GladeWidget      *parent,
							     GladeWidget      *child);

void                    glade_widget_replace                (GladeWidget      *parent,
							     GObject          *old_object,
							     GObject          *new_object);
 
void                    glade_widget_rebuild                (GladeWidget      *gwidget);
 
GladeWidget            *glade_widget_dup                    (GladeWidget      *template_widget,
							     gboolean          exact);

GList                  *glade_widget_get_signal_list        (GladeWidget      *widget);

void                    glade_widget_copy_signals           (GladeWidget      *widget,
							     GladeWidget      *template_widget);
void                    glade_widget_copy_properties        (GladeWidget      *widget,
							     GladeWidget      *template_widget,
							     gboolean          copy_parentless,
							     gboolean          exact);

void                    glade_widget_set_packing_properties (GladeWidget      *widget,
							     GladeWidget      *container);
 
GladeProperty          *glade_widget_get_property           (GladeWidget      *widget,
							     const gchar      *id_property);
 
GladeProperty          *glade_widget_get_pack_property      (GladeWidget      *widget,
							     const gchar      *id_property);

GList                  *glade_widget_dup_properties         (GladeWidget      *dest_widget,
							     GList            *template_props,
                                                             gboolean          as_load,
							     gboolean          copy_parentless,
							     gboolean          exact);

void                    glade_widget_remove_property        (GladeWidget      *widget,
							     const gchar      *id_property);
 
void                    glade_widget_show                   (GladeWidget      *widget);
 
void                    glade_widget_hide                   (GladeWidget      *widget);
 
void                    glade_widget_add_signal_handler     (GladeWidget      *widget,
							     GladeSignal      *signal_handler);
 
void                    glade_widget_remove_signal_handler  (GladeWidget      *widget,
							     GladeSignal      *signal_handler);
 
void                    glade_widget_change_signal_handler  (GladeWidget      *widget,
							     GladeSignal      *old_signal_handler,
							     GladeSignal      *new_signal_handler);
 
GPtrArray *             glade_widget_list_signal_handlers   (GladeWidget      *widget,
							     const gchar      *signal_name);
 
gboolean                glade_widget_has_decendant          (GladeWidget      *widget,
							     GType             type);
 
gboolean                glade_widget_event                  (GladeWidget      *gwidget,
							     GdkEvent         *event);

gboolean                glade_widget_placeholder_relation   (GladeWidget      *parent, 
							     GladeWidget      *widget);

GladeWidgetAction      *glade_widget_get_action             (GladeWidget *widget,
							     const gchar *action_path);

GladeWidgetAction      *glade_widget_get_pack_action        (GladeWidget *widget,
							     const gchar *action_path);

gboolean                glade_widget_set_action_sensitive   (GladeWidget *widget,
							     const gchar *action_path,
							     gboolean     sensitive);

gboolean                glade_widget_set_pack_action_sensitive (GladeWidget *widget,
								const gchar *action_path,
								gboolean     sensitive);

void                    glade_widget_remove_action          (GladeWidget *widget,
							     const gchar *action_path);

void                    glade_widget_remove_pack_action     (GladeWidget *widget,
							     const gchar *action_path);

void                    glade_widget_write                  (GladeWidget     *widget,
							     GladeXmlContext *context,
							     GladeXmlNode    *node);

void                    glade_widget_write_child            (GladeWidget     *widget,
							     GladeWidget     *child,
							     GladeXmlContext *context,
							     GladeXmlNode    *node);

void                    glade_widget_write_signals          (GladeWidget     *widget,
							     GladeXmlContext *context,
							     GladeXmlNode    *node);

void                    glade_widget_write_placeholder      (GladeWidget     *parent,
							     GObject         *object,
							     GladeXmlContext *context,
							     GladeXmlNode    *node);
	
GladeWidget            *glade_widget_read                   (GladeProject     *project,
							     GladeWidget      *parent,
							     GladeXmlNode     *node,
							     const gchar      *internal);

void                    glade_widget_read_child             (GladeWidget      *widget,
							     GladeXmlNode     *node);


void                    glade_widget_write_special_child_prop (GladeWidget     *parent, 
							       GObject         *object,
							       GladeXmlContext *context,
							       GladeXmlNode    *node);

void                  glade_widget_set_child_type_from_node (GladeWidget         *parent,
							     GObject             *child,
							     GladeXmlNode        *node);

GladeEditorProperty    *glade_widget_create_editor_property (GladeWidget      *widget,
							     const gchar      *property,
							     gboolean          packing,
							     gboolean          use_command);

gchar                  *glade_widget_generate_path_name     (GladeWidget      *widget);

gboolean                glade_widget_is_ancestor            (GladeWidget      *widget,
							     GladeWidget      *ancestor);

/*******************************************************************************
                      Project, object property references
 *******************************************************************************/
 
void                    glade_widget_add_prop_ref           (GladeWidget      *widget,
							     GladeProperty    *property);
 
void                    glade_widget_remove_prop_ref        (GladeWidget      *widget,
							     GladeProperty    *property);

GladeProperty          *glade_widget_get_parentless_widget_ref (GladeWidget  *widget);


GList                  *glade_widget_get_parentless_reffed_widgets (GladeWidget *widget);

/*******************************************************************************
            Functions that deal with properties on the runtime object
 *******************************************************************************/

void                    glade_widget_object_set_property    (GladeWidget      *widget,
							     const gchar      *property_name,
							     const GValue     *value);

void                    glade_widget_object_get_property    (GladeWidget      *widget,
							     const gchar      *property_name,
							     GValue           *value);

void                    glade_widget_child_set_property     (GladeWidget      *widget,
							     GladeWidget      *child,
							     const gchar      *property_name,
							     const GValue     *value);

void                    glade_widget_child_get_property     (GladeWidget      *widget,
							     GladeWidget      *child,
							     const gchar      *property_name,
							     GValue           *value);

/*******************************************************************************
                   GladeProperty api convenience wrappers
 *******************************************************************************/
 
gboolean                glade_widget_property_get           (GladeWidget      *widget,
							     const gchar      *id_property,
							     ...);
 
gboolean                glade_widget_property_set           (GladeWidget      *widget,
							     const gchar      *id_property,
							     ...);
 
gboolean                glade_widget_pack_property_get      (GladeWidget      *widget,
							     const gchar      *id_property,
							     ...);
 
gboolean                glade_widget_pack_property_set      (GladeWidget      *widget,
							     const gchar      *id_property,
							     ...);
 
gboolean                glade_widget_property_reset         (GladeWidget      *widget,
							     const gchar      *id_property);
 
gboolean                glade_widget_pack_property_reset    (GladeWidget      *widget,
							     const gchar      *id_property);
 
gboolean                glade_widget_property_default       (GladeWidget      *widget,
							     const gchar      *id_property);
 
gboolean                glade_widget_property_original_default (GladeWidget      *widget,
								const gchar      *id_property);
 
gboolean                glade_widget_pack_property_default  (GladeWidget      *widget,
							     const gchar      *id_property);
 
gboolean                glade_widget_property_set_sensitive (GladeWidget      *widget,
							     const gchar      *id_property,
							     gboolean          sensitive,
							     const gchar      *reason);
 
gboolean                glade_widget_pack_property_set_sensitive (GladeWidget      *widget,
								  const gchar      *id_property,
								  gboolean          sensitive,
								  const gchar      *reason);
 
gboolean                glade_widget_property_set_enabled   (GladeWidget      *widget,
							     const gchar      *id_property,
							     gboolean          enabled);
 
gboolean                glade_widget_pack_property_set_enabled (GladeWidget      *widget,
								const gchar      *id_property,
								gboolean          enabled);

 
gboolean                glade_widget_property_set_save_always (GladeWidget      *widget,
							       const gchar      *id_property,
							       gboolean          setting);
 
gboolean                glade_widget_pack_property_set_save_always (GladeWidget      *widget,
								    const gchar      *id_property,
								    gboolean          setting);

gchar                  *glade_widget_property_string        (GladeWidget      *widget,
							     const gchar      *id_property,
							     const GValue     *value);


gchar                  *glade_widget_pack_property_string   (GladeWidget      *widget,
							     const gchar      *id_property,
							     const GValue     *value);

/*******************************************************************************
                                  Accessors
 *******************************************************************************/

void                    glade_widget_set_name		    (GladeWidget      *widget,
							     const gchar      *name);
 
G_CONST_RETURN gchar   *glade_widget_get_name               (GladeWidget      *widget);

void                    glade_widget_set_internal	    (GladeWidget      *widget,
							     const gchar      *internal);
 
G_CONST_RETURN gchar   *glade_widget_get_internal           (GladeWidget      *widget);
 
GObject                *glade_widget_get_object             (GladeWidget      *widget);

void                    glade_widget_set_project	    (GladeWidget      *widget,
							     GladeProject     *project);
 
GladeProject           *glade_widget_get_project            (GladeWidget      *widget);
 
GladeWidgetAdaptor     *glade_widget_get_adaptor            (GladeWidget      *widget);
 
GladeWidget            *glade_widget_get_parent             (GladeWidget      *widget);
 
void                    glade_widget_set_parent             (GladeWidget      *widget,
							     GladeWidget      *parent);

GList                  *glade_widget_get_children	    (GladeWidget* widget);

GladeWidget            *glade_widget_get_toplevel           (GladeWidget      *widget);
 
gboolean                glade_widget_superuser              (void);
 
void                    glade_widget_push_superuser         (void);
 
void                    glade_widget_pop_superuser          (void);

void                    glade_widget_set_support_warning    (GladeWidget      *widget,
							     const gchar      *warning);

void                    glade_widget_lock                   (GladeWidget      *widget,
							     GladeWidget      *locked);
void                    glade_widget_unlock                 (GladeWidget      *widget);

void                    glade_widget_support_changed        (GladeWidget      *widget);

G_END_DECLS

#endif /* __GLADE_WIDGET_H__ */
