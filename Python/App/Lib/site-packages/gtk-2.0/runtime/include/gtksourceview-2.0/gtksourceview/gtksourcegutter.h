/*
 * gtksourcegutter.h
 * This file is part of gtksourceview
 *
 * Copyright (C) 2009 - Jesse van den Kieboom
 *
 * gtksourceview is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2.1 of the License, or (at your option) any later version.
 *
 * gtksourceview is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this library; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
 */


#ifndef __GTK_SOURCE_GUTTER_H__
#define __GTK_SOURCE_GUTTER_H__

#include <glib-object.h>
#include <gtk/gtk.h>
#include <gdk/gdk.h>

G_BEGIN_DECLS

#define GTK_TYPE_SOURCE_GUTTER			(gtk_source_gutter_get_type ())
#define GTK_SOURCE_GUTTER(obj)			(G_TYPE_CHECK_INSTANCE_CAST ((obj), GTK_TYPE_SOURCE_GUTTER, GtkSourceGutter))
#define GTK_SOURCE_GUTTER_CLASS(klass)		(G_TYPE_CHECK_CLASS_CAST ((klass), GTK_TYPE_SOURCE_GUTTER, GtkSourceGutterClass))
#define GTK_IS_SOURCE_GUTTER(obj)		(G_TYPE_CHECK_INSTANCE_TYPE ((obj), GTK_TYPE_SOURCE_GUTTER))
#define GTK_IS_SOURCE_GUTTER_CLASS(klass)	(G_TYPE_CHECK_CLASS_TYPE ((klass), GTK_TYPE_SOURCE_GUTTER))
#define GTK_SOURCE_GUTTER_GET_CLASS(obj)	(G_TYPE_INSTANCE_GET_CLASS ((obj), GTK_TYPE_SOURCE_GUTTER, GtkSourceGutterClass))

typedef struct _GtkSourceGutter			GtkSourceGutter;
typedef struct _GtkSourceGutterClass	GtkSourceGutterClass;
typedef struct _GtkSourceGutterPrivate	GtkSourceGutterPrivate;

struct _GtkSourceGutter {
	GObject parent;

	GtkSourceGutterPrivate *priv;
};

struct _GtkSourceGutterClass {
	GObjectClass parent_class;

	void (*cell_activated) 			(GtkSourceGutter *gutter,
						 GtkCellRenderer *renderer,
						 GtkTextIter     *iter,
						 GdkEvent        *event);

	gboolean (*query_tooltip) 		(GtkSourceGutter *gutter,
						 GtkCellRenderer *renderer,
						 GtkTextIter     *iter,
						 GtkTooltip      *tooltip);
};

typedef void (*GtkSourceGutterDataFunc)		(GtkSourceGutter         *gutter,
						 GtkCellRenderer         *cell,
						 gint                     line_number,
						 gboolean                 current_line,
						 gpointer                 data);

typedef void (*GtkSourceGutterSizeFunc)		(GtkSourceGutter         *gutter,
						 GtkCellRenderer         *cell,
						 gpointer                 data);

GType gtk_source_gutter_get_type 		(void) G_GNUC_CONST;

GdkWindow *gtk_source_gutter_get_window 	(GtkSourceGutter         *gutter);

void gtk_source_gutter_insert			(GtkSourceGutter         *gutter,
						 GtkCellRenderer         *renderer,
						 gint                     position);

void gtk_source_gutter_reorder			(GtkSourceGutter	 *gutter,
                                                 GtkCellRenderer         *renderer,
                                                 gint                     position);

void gtk_source_gutter_remove			(GtkSourceGutter         *gutter,
						 GtkCellRenderer         *renderer);

void gtk_source_gutter_set_cell_data_func	(GtkSourceGutter         *gutter,
						 GtkCellRenderer         *renderer,
						 GtkSourceGutterDataFunc  func,
						 gpointer                 func_data,
						 GDestroyNotify           destroy);

void gtk_source_gutter_set_cell_size_func	(GtkSourceGutter         *gutter,
                                                 GtkCellRenderer         *renderer,
                                                 GtkSourceGutterSizeFunc  func,
                                                 gpointer                 func_data,
                                                 GDestroyNotify           destroy);

void gtk_source_gutter_queue_draw		(GtkSourceGutter         *gutter);

G_END_DECLS

#endif /* __GTK_SOURCE_GUTTER_H__ */

/* vi:ts=8 */
