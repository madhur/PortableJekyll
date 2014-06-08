/* -*- Mode: C; tab-width: 8; indent-tabs-mode: t; c-basic-offset: 8 -*- */
/*
 * Copyright (C) 2001 Ximian, Inc.
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as
 * published by the Free Software Foundation; either version 2 of the
 * License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
 *
 * Authors:
 *   Naba Kumar <naba@gnome.org>
 */
 
#ifndef __GLADE_APP_H__
#define __GLADE_APP_H__

#include <gladeui/glade-editor.h>
#include <gladeui/glade-palette.h>
#include <gladeui/glade-clipboard.h>
#include <gladeui/glade-catalog.h>

G_BEGIN_DECLS

#define GLADE_TYPE_APP            (glade_app_get_type())
#define GLADE_APP(obj)            (G_TYPE_CHECK_INSTANCE_CAST ((obj), GLADE_TYPE_APP, GladeApp))
#define GLADE_APP_CLASS(klass)    (G_TYPE_CHECK_CLASS_CAST ((klass), GLADE_TYPE_APP, GladeAppClass))
#define GLADE_IS_APP(obj)         (G_TYPE_CHECK_INSTANCE_TYPE ((obj), GLADE_TYPE_APP))
#define GLADE_IS_APP_CLASS(klass) (G_TYPE_CHECK_CLASS_TYPE ((klass), GLADE_TYPE_APP))
#define GLADE_APP_GET_CLASS(o)    (G_TYPE_INSTANCE_GET_CLASS ((o), GLADE_APP, GladeAppClass))

#define GLADE_TYPE_POINTER_MODE   (glade_pointer_mode_get_type())

#define GLADE_ENV_CATALOG_PATH    "GLADE_CATALOG_PATH"
#define GLADE_ENV_MODULE_PATH     "GLADE_MODULE_PATH"

typedef struct _GladeApp         GladeApp;
typedef struct _GladeAppPrivate  GladeAppPrivate;
typedef struct _GladeAppClass    GladeAppClass;

/**
 * GladePointerMode:
 * @GLADE_POINTER_SELECT:      Mouse pointer used for selecting widgets
 * @GLADE_POINTER_ADD_WIDGET:  Mouse pointer used for adding widgets
 * @GLADE_POINTER_DRAG_RESIZE: Mouse pointer used for dragging and 
 *                             resizing widgets in containers
 *
 * Indicates what the pointer is used for in the workspace.
 */
enum _GladePointerMode
{
	GLADE_POINTER_SELECT = 0,
	GLADE_POINTER_ADD_WIDGET,
	GLADE_POINTER_DRAG_RESIZE
};
typedef enum _GladePointerMode GladePointerMode;


struct _GladeApp
{
	GObject parent_instance;
	
	GladeAppPrivate *priv;
};

struct _GladeAppClass
{
	GObjectClass parent_class;
	
	/* class methods */
	void   (*  show_properties) (GladeApp* app,
				     gboolean  raise);
	void   (*  hide_properties) (GladeApp* app);

	/* signals */
	void   (* update_ui_signal) (GladeApp    *app);
	void   (* signal_editor_created) (GladeApp *app, GladeSignalEditor *signal_editor);
};

 
GType              glade_app_get_type   (void) G_GNUC_CONST;

GladeApp*          glade_app_new        (void);

GType              glade_pointer_mode_get_type (void) G_GNUC_CONST;

GladeApp*          glade_app_get        (void);

void               glade_app_update_ui  (void);

void               glade_app_set_window (GtkWidget *window);
 
GtkWidget*         glade_app_get_window (void);

gboolean           glade_app_get_catalog_version (const gchar *name, gint *major, gint *minor);

GList             *glade_app_get_catalogs (void);

GladeCatalog      *glade_app_get_catalog (const gchar *name);

GladeEditor*       glade_app_get_editor (void);

GladePalette*      glade_app_get_palette (void);

GladeClipboard*    glade_app_get_clipboard (void);

GladeProject*      glade_app_get_project (void);

GladeProject*      glade_app_check_get_project (void);
 
void               glade_app_set_project (GladeProject *project);

GladePointerMode   glade_app_get_pointer_mode (void);
 
void               glade_app_set_pointer_mode (GladePointerMode mode);

void               glade_app_add_project (GladeProject *project);
 
void               glade_app_remove_project (GladeProject *project);
 
GList*             glade_app_get_projects (void);
 
GKeyFile*          glade_app_get_config (void);
 
gboolean           glade_app_is_project_loaded (const gchar *project_path);
 
GladeProject*      glade_app_get_project_by_path (const gchar *project_path);
 
void               glade_app_show_properties (gboolean raise);
 
void               glade_app_hide_properties (void);

 
void               glade_app_command_copy (void);
 
void               glade_app_command_cut (void);
 
void               glade_app_command_paste (GladePlaceholder *placeholder);
 
void               glade_app_command_delete (void);

void               glade_app_command_delete_clipboard (void);
 
void               glade_app_command_undo (void);
 
void               glade_app_command_redo (void);

 
gint               glade_app_config_save (void);
 
void               glade_app_set_transient_parent (GtkWindow *parent);
 
GtkWindow         *glade_app_get_transient_parent (void);
 
void               glade_app_set_accel_group (GtkAccelGroup *accel_group);

GtkAccelGroup     *glade_app_get_accel_group (void);
 
GtkWidget         *glade_app_undo_button_new (void);
 
GtkWidget         *glade_app_redo_button_new (void);

 
GList             *glade_app_get_selection (void);


/* These handle selection on a global scope and take care
 * of multiple project logic.
 */
 
gboolean           glade_app_is_selected       (GObject  *object);
 
void               glade_app_selection_set     (GObject  *object,
					        gboolean  emit_signal);
 
void               glade_app_selection_add     (GObject  *object,
					        gboolean  emit_signal);
 
void               glade_app_selection_remove  (GObject  *object,
					        gboolean  emit_signal);
 
void               glade_app_selection_clear   (gboolean  emit_signal);
 
void               glade_app_selection_changed (void);

void               glade_app_queue_selection_changed (void);

/* package paths */

const gchar       *glade_app_get_catalogs_dir  (void) G_GNUC_CONST;

const gchar       *glade_app_get_modules_dir   (void) G_GNUC_CONST;

const gchar       *glade_app_get_plugins_dir   (void) G_GNUC_CONST;

const gchar       *glade_app_get_pixmaps_dir   (void) G_GNUC_CONST;

const gchar       *glade_app_get_locale_dir    (void) G_GNUC_CONST;

const gchar       *glade_app_get_bin_dir       (void) G_GNUC_CONST;

G_END_DECLS

#endif /* __GLADE_APP_H__ */
