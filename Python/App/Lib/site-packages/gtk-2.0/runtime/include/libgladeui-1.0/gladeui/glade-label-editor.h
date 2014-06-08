/* -*- Mode: C; tab-width: 8; indent-tabs-mode: t; c-basic-offset: 8 -*- */
/*
 * Copyright (C) 2008 Tristan Van Berkom.
 *
 * This library is free software; you can redistribute it and/or modify it
 * under the terms of the GNU Lesser General Public License as
 * published by the Free Software Foundation; either version 2.1 of
 * the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public 
 * License along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
 *
 * Authors:
 *   Tristan Van Berkom <tvb@gnome.org>
 */
#ifndef _GLADE_LABEL_EDITOR_H_
#define _GLADE_LABEL_EDITOR_H_

#include <gtk/gtk.h>

G_BEGIN_DECLS

#define GLADE_TYPE_LABEL_EDITOR	            (glade_label_editor_get_type ())
#define GLADE_LABEL_EDITOR(obj)		    (G_TYPE_CHECK_INSTANCE_CAST ((obj), GLADE_TYPE_LABEL_EDITOR, GladeLabelEditor))
#define GLADE_LABEL_EDITOR_CLASS(klass)	    (G_TYPE_CHECK_CLASS_CAST ((klass), GLADE_TYPE_LABEL_EDITOR, GladeLabelEditorClass))
#define GLADE_IS_LABEL_EDITOR(obj)	    (G_TYPE_CHECK_INSTANCE_TYPE ((obj), GLADE_TYPE_LABEL_EDITOR))
#define GLADE_IS_LABEL_EDITOR_CLASS(klass)  (G_TYPE_CHECK_CLASS_TYPE ((klass), GLADE_TYPE_LABEL_EDITOR))
#define GLADE_LABEL_EDITOR_GET_CLASS(obj)   (G_TYPE_INSTANCE_GET_CLASS ((obj), GLADE_TYPE_LABEL_EDITOR, GladeLabelEditorClass))

typedef struct _GladeLabelEditor        GladeLabelEditor;
typedef struct _GladeLabelEditorClass   GladeLabelEditorClass;

typedef enum {
	GLADE_LABEL_MODE_ATTRIBUTES = 0, /* default */
	GLADE_LABEL_MODE_MARKUP,
	GLADE_LABEL_MODE_PATTERN
} GladeLabelContentMode;

typedef enum {
	GLADE_LABEL_WRAP_FREE = 0, /* default */
	GLADE_LABEL_SINGLE_LINE,
	GLADE_LABEL_WRAP_MODE
} GladeLabelWrapMode;

struct _GladeLabelEditor
{
	GtkVBox  parent;

	GladeWidget *loaded_widget; /* A handy pointer to the loaded widget ... */

	GtkWidget *embed;

	GtkWidget *attributes_radio;    /* Set pango attributes manually (attributes eprop embedded) */
	GtkWidget *markup_radio;        /* Parse the label as a pango markup string (no showing eprop) */
	GtkWidget *pattern_radio;       /* Use a pattern string to underline portions of the text
					 * (pattern eprop embedded) */

	/* These control whether to use max-width-chars or just width-chars */
	GtkWidget *width_radio;
	GtkWidget *max_width_radio;

	/* These control whether to use single-line-mode, wrap & wrap-mode or niether */
	GtkWidget *wrap_free_label; /* Set boldness on this label for a fake property */
	GtkWidget *wrap_free_radio;
	GtkWidget *single_radio;
	GtkWidget *wrap_mode_radio;

	GList *properties;         /* A list of eprops to update at load() time */

	GtkSizeGroup *appearance_group;
	GtkSizeGroup *formatting_group;
	GtkSizeGroup *wrap_group;

	gboolean loading;          /* Loading flag for loading widgets in the editor */
	gboolean modifying;        /* Flag for monitoring project changes */
};

struct _GladeLabelEditorClass
{
	GtkVBoxClass parent;
};

GType            glade_label_editor_get_type (void) G_GNUC_CONST;
GtkWidget       *glade_label_editor_new      (GladeWidgetAdaptor *adaptor,
					      GladeEditable      *editable);

G_END_DECLS

#endif  /* _GLADE_LABEL_EDITOR_H_ */
