/* -*- Mode: C; tab-width: 8; indent-tabs-mode: t; c-basic-offset: 8 -*- */
#ifndef __GLADE_EDITOR_H__
#define __GLADE_EDITOR_H__

#include <gladeui/glade-signal-editor.h>
#include <gladeui/glade-editable.h>

G_BEGIN_DECLS


#define GLADE_TYPE_EDITOR            (glade_editor_get_type ())
#define GLADE_EDITOR(obj)            (G_TYPE_CHECK_INSTANCE_CAST ((obj), GLADE_TYPE_EDITOR, GladeEditor))
#define GLADE_EDITOR_CLASS(klass)    (G_TYPE_CHECK_CLASS_CAST ((klass), GLADE_TYPE_EDITOR, GladeEditorClass))
#define GLADE_IS_EDITOR(obj)         (G_TYPE_CHECK_INSTANCE_TYPE ((obj), GLADE_TYPE_EDITOR))
#define GLADE_IS_EDITOR_CLASS(klass) (G_TYPE_CHECK_CLASS_TYPE ((klass), GLADE_TYPE_EDITOR))
#define GLADE_EDITOR_GET_CLASS(obj)  (G_TYPE_INSTANCE_GET_CLASS ((obj), GLADE_TYPE_EDITOR, GladeEditorClass))

typedef struct _GladeEditor          GladeEditor;
typedef struct _GladeEditorClass     GladeEditorClass;

/* The GladeEditor is a window that is used to display and modify widget
 * properties. The glade editor contains the details of the selected
 * widget for the selected project
 */
struct _GladeEditor
{
	GtkVBox vbox;  /* The editor is a vbox */
	
	GtkWidget *notebook; /* The notebook widget */

	GladeWidget *loaded_widget; /* A handy pointer to the GladeWidget
				     * that is loaded in the editor. NULL
				     * if no widgets are selected
				     */

	GladeWidgetAdaptor *loaded_adaptor; /* A pointer to the loaded
					     * GladeWidgetAdaptor. Note that we can
					     * have a class loaded without a
					     * loaded_widget. For this reason we
					     * can't use loaded_widget->adaptor.
					     * When a widget is selected we load
					     * this class in the editor first and
					     * then fill the values of the inputs
					     * with the GladeProperty items.
					     * This is usefull for not having
					     * to redraw/container_add the widgets
					     * when we switch from widgets of the
					     * same class
					     */

	GtkWidget *page_widget;
	GtkWidget *page_packing;
	GtkWidget *page_common;
	GtkWidget *page_signals;
	GtkWidget *page_atk;

	GladeSignalEditor *signal_editor; /* The signal editor packed into vbox_signals
					   */

	GList *editables;     /* A list of GladeEditables. We have a widget
			       * for each GladeWidgetAdaptor and we only load
			       * them on demand
			       */
	
	GtkWidget *packing_page; /* Packing pages are dynamicly created each
				  * selection, this pointer is only to free
				  * the last packing page.
				  */

	gboolean loading; /* Use when loading a GladeWidget into the editor
			   * we set this flag so that we can ignore the
			   * "changed" signal of the name entry text since
			   * the name has not really changed, just a new name
			   * was loaded.
			   */

	gulong project_closed_signal_id; /* Unload widget when widget's project closes.
					  */
	gulong project_removed_signal_id; /* Unload widget when its removed from the project.
					   */
	gulong widget_warning_id; /* Update when widget changes warning messages.
				   */
	gulong widget_name_id;    /* Update class field when widget name changes
				   */
	GtkWidget *reset_button; /* The reset button
				  */
	
	GtkWidget *info_button; /* The actual informational button
				 */

	GtkWidget *class_field; /* The class header
				 */

	GtkWidget *warning;   /* A pointer to an icon we can show in the class
			       * field to publish tooltips for class related
			       * versioning errors.
			       */

	GtkWidget *class_icon; /* An image with the current widget's class icon.
				*/

	GtkWidget *class_label; /* A label with the current class label.
				 */

	GtkWidget *widget_label; /* A label with the current widget name.
				  */

	gboolean show_info; /* Whether or not to show an informational button
			     */
};

struct _GladeEditorClass
{
	GtkVBoxClass parent_class;

	void   (*add_signal) (GladeEditor *editor, const char *id_widget,
			      GType type_widget, guint id_signal,
			      const char *callback_name);

	void   (*gtk_doc_search) (GladeEditor *,
				  const gchar *,
				  const gchar *,
				  const gchar *);

};


GType        glade_editor_get_type           (void);

GladeEditor *glade_editor_new                (void);

GtkWidget   *glade_editor_dialog_for_widget  (GladeWidget *widget);

void         glade_editor_load_widget        (GladeEditor *editor,
					      GladeWidget *widget);

void         glade_editor_refresh            (GladeEditor *editor);

gboolean     glade_editor_query_dialog       (GladeEditor *editor,
					      GladeWidget *widget);

void         glade_editor_show_info          (GladeEditor *editor);

void         glade_editor_hide_info          (GladeEditor *editor);

void         glade_editor_search_doc_search  (GladeEditor *editor,
					      const gchar *book,
					      const gchar *page,
					      const gchar *search);
void glade_editor_set_signal_editor (GladeEditor *editor, GladeSignalEditor *signal_editor);

G_END_DECLS

#endif /* __GLADE_EDITOR_H__ */
