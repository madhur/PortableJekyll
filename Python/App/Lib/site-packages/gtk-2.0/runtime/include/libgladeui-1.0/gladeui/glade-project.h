/* -*- Mode: C; tab-width: 8; indent-tabs-mode: t; c-basic-offset: 8 -*- */
#ifndef __GLADE_PROJECT_H__
#define __GLADE_PROJECT_H__

#include <gladeui/glade-widget.h>
#include <gladeui/glade-command.h>
#include <gladeui/glade-utils.h>
#include <gladeui/glade-xml-utils.h>


G_BEGIN_DECLS

#define GLADE_TYPE_PROJECT            (glade_project_get_type ())
#define GLADE_PROJECT(obj)            (G_TYPE_CHECK_INSTANCE_CAST ((obj), GLADE_TYPE_PROJECT, GladeProject))
#define GLADE_PROJECT_CLASS(klass)    (G_TYPE_CHECK_CLASS_CAST ((klass), GLADE_TYPE_PROJECT, GladeProjectClass))
#define GLADE_IS_PROJECT(obj)         (G_TYPE_CHECK_INSTANCE_TYPE ((obj), GLADE_TYPE_PROJECT))
#define GLADE_IS_PROJECT_CLASS(klass) (G_TYPE_CHECK_CLASS_TYPE ((klass), GLADE_TYPE_PROJECT))
#define GLADE_PROJECT_GET_CLASS(obj)  (G_TYPE_INSTANCE_GET_CLASS ((obj), GLADE_TYPE_PROJECT, GladeProjectClass))

typedef struct _GladeProjectPrivate  GladeProjectPrivate;
typedef struct _GladeProjectClass    GladeProjectClass;

typedef enum
{
	GLADE_SUPPORT_OK                   = 0,
	GLADE_SUPPORT_DEPRECATED           = (0x01 << 0),
	GLADE_SUPPORT_MISMATCH             = (0x01 << 1),
	GLADE_SUPPORT_LIBGLADE_UNSUPPORTED = (0x01 << 2),
	GLADE_SUPPORT_LIBGLADE_ONLY        = (0x01 << 3)
} GladeSupportMask;

/**
 * GladeProjectModelColumns:
 * @GLADE_PROJECT_MODEL_ICON_NAME: name of the icon for the widget
 * @GLADE_PROJECT_MODEL_ICON_NAME_COLUMN_NAME: Name of the widget
 * @GLADE_PROJECT_MODEL_ICON_NAME_COLUMN_OBJECT: the GObject of the widget
 * @GLADE_PROJECT_MODEL_ICON_NAME_N_COLUMNS: Number of columns
 *
 * The tree view columns provided by the GtkTreeModel implemented
 * by GladeProject
 *
 **/
typedef enum
{
	GLADE_PROJECT_MODEL_COLUMN_ICON_NAME,
	GLADE_PROJECT_MODEL_COLUMN_NAME,
	GLADE_PROJECT_MODEL_COLUMN_TYPE_NAME,
	GLADE_PROJECT_MODEL_COLUMN_OBJECT,
	GLADE_PROJECT_MODEL_COLUMN_MISC,
	GLADE_PROJECT_MODEL_N_COLUMNS
} GladeProjectModelColumns;

struct _GladeProject
{
	GObject parent_instance;

	GladeProjectPrivate *priv;
};

struct _GladeProjectClass
{
	GObjectClass parent_class;

	void          (*add_object)          (GladeProject *project,
					      GladeWidget  *widget);
	void          (*remove_object)       (GladeProject *project,
					      GladeWidget  *widget);
	
	void          (*undo)                (GladeProject *project);
	void          (*redo)                (GladeProject *project);
	GladeCommand *(*next_undo_item)      (GladeProject *project);
	GladeCommand *(*next_redo_item)      (GladeProject *project);
	void          (*push_undo)           (GladeProject *project,
					      GladeCommand *command);

	void          (*changed)             (GladeProject *project,
					      GladeCommand *command,
					      gboolean      forward);

	void          (*widget_name_changed) (GladeProject *project,
					      GladeWidget  *widget);
	void          (*selection_changed)   (GladeProject *project); 
	void          (*close)               (GladeProject *project);

	void          (*parse_finished)      (GladeProject *project);
};


GType          glade_project_get_type            (void) G_GNUC_CONST;

GladeProject  *glade_project_new                 (void);

GladeProject  *glade_project_load                (const gchar  *path);
gboolean       glade_project_load_from_file      (GladeProject *project, 
						  const gchar  *path);

gboolean       glade_project_save                (GladeProject *project, 
						  const gchar   *path, 
						  GError       **error);

const gchar   *glade_project_get_path            (GladeProject *project);

gchar         *glade_project_get_name            (GladeProject *project);


void           glade_project_undo                (GladeProject *project);

void           glade_project_redo                (GladeProject *project);

GladeCommand  *glade_project_next_undo_item      (GladeProject *project);

GladeCommand  *glade_project_next_redo_item      (GladeProject *project);

void           glade_project_push_undo           (GladeProject *project, 
						  GladeCommand *cmd);

GtkWidget     *glade_project_undo_items          (GladeProject *project);

GtkWidget     *glade_project_redo_items          (GladeProject *project);

void           glade_project_reset_path          (GladeProject *project);

gboolean       glade_project_get_readonly        (GladeProject *project);

const GList   *glade_project_get_objects         (GladeProject *project);

void           glade_project_add_object          (GladeProject *project, 
						  GladeProject *old_project,
						  GObject      *object);

void           glade_project_remove_object       (GladeProject *project, 
						  GObject      *object);

gboolean       glade_project_has_object          (GladeProject *project, 
						  GObject      *object);

GladeWidget   *glade_project_get_widget_by_name  (GladeProject *project, 
						  GladeWidget  *ancestor,
						  const gchar  *name);

void           glade_project_set_widget_name     (GladeProject *project, 
						  GladeWidget  *widget, 
						  const gchar  *name);

gchar         *glade_project_new_widget_name     (GladeProject *project, 
						  GladeWidget  *widget, 
						  const gchar  *base_name);

gboolean       glade_project_available_widget_name (GladeProject *project, GladeWidget  *widget,
						    const gchar  *name);

/* Selection */

gboolean       glade_project_is_selected         (GladeProject *project,
						 GObject      *object);

void           glade_project_selection_set       (GladeProject *project,
						 GObject      *object,
						 gboolean      emit_signal);

void           glade_project_selection_add       (GladeProject *project,
						 GObject      *object,
						 gboolean      emit_signal);

void           glade_project_selection_remove    (GladeProject *project,
						 GObject      *object,
						 gboolean      emit_signal);

void           glade_project_selection_clear     (GladeProject *project,
						 gboolean      emit_signal);

void           glade_project_selection_changed   (GladeProject *project);

GList         *glade_project_selection_get       (GladeProject *project);

gboolean       glade_project_get_has_selection   (GladeProject *project);

gchar         *glade_project_resource_fullpath    (GladeProject  *project,
						   const gchar   *resource);
 
gboolean       glade_project_is_loading           (GladeProject *project);
 
time_t         glade_project_get_file_mtime       (GladeProject *project);

gboolean       glade_project_get_modified         (GladeProject *project);

void           glade_project_set_format      	  (GladeProject *project, GladeProjectFormat format);

GladeProjectFormat glade_project_get_format  	  (GladeProject *project);

void           glade_project_preferences          (GladeProject *project);

void           glade_project_verify_properties    (GladeWidget  *widget);

gchar         *glade_project_verify_widget_adaptor (GladeProject       *project,
						    GladeWidgetAdaptor *adaptor,
						    GladeSupportMask   *mask);

void          glade_project_verify_project_for_ui (GladeProject  *project);

GList        *glade_project_required_libs          (GladeProject       *project);

void          glade_project_set_naming_policy      (GladeProject       *project,
						    GladeNamingPolicy   policy);

GladeNamingPolicy glade_project_get_naming_policy  (GladeProject       *project);
void          glade_project_get_target_version     (GladeProject       *project,
						    const gchar        *catalog,
						    gint               *major,
						    gint               *minor);

void          glade_project_update_signal_support_warning (GladeWidget  *widget,
							   GladeSignal  *signal);


gchar        *glade_project_display_dependencies (GladeProject *project);

void          glade_project_check_reordered (GladeProject       *project,
					     GladeWidget        *parent,
					     GList              *old_order);

void          glade_project_push_progress (GladeProject *project);
gboolean      glade_project_load_cancelled (GladeProject *project);
void          glade_project_cancel_load (GladeProject *project);

G_END_DECLS

#endif /* __GLADE_PROJECT_H__ */
