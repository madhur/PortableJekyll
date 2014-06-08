/* -*- Mode: C; tab-width: 8; indent-tabs-mode: t; c-basic-offset: 8 -*- */
/*
 * Copyright (C) 2008 Tristan Van Berkom.
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
 *   Tristan Van Berkom <tvb@gnome.org>
 */
#ifndef _GLADE_EDITOR_BUTTON_H_
#define _GLADE_EDITOR_BUTTON_H_

#include <gtk/gtk.h>
#include <gladeui/glade-editable.h>


G_BEGIN_DECLS

#define GLADE_TYPE_EDITOR_TABLE	            (glade_editor_table_get_type ())
#define GLADE_EDITOR_TABLE(obj)		    (G_TYPE_CHECK_INSTANCE_CAST ((obj), GLADE_TYPE_EDITOR_TABLE, GladeEditorTable))
#define GLADE_EDITOR_TABLE_CLASS(klass)	    (G_TYPE_CHECK_CLASS_CAST ((klass), GLADE_TYPE_EDITOR_TABLE, GladeEditorTableClass))
#define GLADE_IS_EDITOR_TABLE(obj)	    (G_TYPE_CHECK_INSTANCE_TYPE ((obj), GLADE_TYPE_EDITOR_TABLE))
#define GLADE_IS_EDITOR_TABLE_CLASS(klass)  (G_TYPE_CHECK_CLASS_TYPE ((klass), GLADE_TYPE_EDITOR_TABLE))
#define GLADE_EDITOR_TABLE_GET_CLASS(obj)   (G_TYPE_INSTANCE_GET_CLASS ((obj), GLADE_TYPE_EDITOR_TABLE, GladeEditorEditorClass))

typedef struct _GladeEditorTable        GladeEditorTable;
typedef struct _GladeEditorTableClass   GladeEditorTableClass;

struct _GladeEditorTable
{
	GtkTable  parent;

	GladeWidgetAdaptor *adaptor; /* The GladeWidgetAdaptor this
				      * table was created for.
				      */

	GladeWidget *loaded_widget; /* A pointer to the currently loaded GladeWidget
				     */

	GtkSizeGroup *group; /* Group of editing widgets in the right hand column */
	
	GtkWidget *name_label; /* A pointer to the "Name:" label (for show/hide) */
	GtkWidget *name_entry; /* A pointer to the gtk_entry that holds
				* the name of the widget. This is the
				* first item _pack'ed to the table_widget.
				* We have a pointer here because it is an
				* entry which will not be created from a
				* GladeProperty but rather from code.
				*/

	GList *properties; /* A list of GladeEditorPropery items.
			    * For each row in the gtk_table, there is a
			    * corrsponding GladeEditorProperty struct.
			    */

	GladeEditorPageType type; /* Is this table to be used in the common tab, ?
				   * the general tab, a packing tab or the query popup ?
				   */

	gint rows;
};

struct _GladeEditorTableClass
{
	GtkTableClass parent;
};

GType            glade_editor_table_get_type (void);
GtkWidget       *glade_editor_table_new      (GladeWidgetAdaptor   *adaptor,
					      GladeEditorPageType   type);

G_END_DECLS

#endif  /* _GLADE_EDITOR_TABLE_H_ */
