/* -*- Mode: C; tab-width: 8; indent-tabs-mode: t; c-basic-offset: 8 -*- */
/*
 * Copyright (C) 2003, 2004 Joaquin Cuenca Abela
 *
 * Authors:
 *   Joaquin Cuenca Abela <e98cuenc@yahoo.com> 
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
*/
 
#ifndef __GLADE_PLACEHOLDER_H__
#define __GLADE_PLACEHOLDER_H__

#include <gladeui/glade-widget.h>
#include <gladeui/glade-project.h>
#include <gtk/gtk.h>

G_BEGIN_DECLS

#define GLADE_TYPE_PLACEHOLDER            (glade_placeholder_get_type ())
#define GLADE_PLACEHOLDER(obj)            (G_TYPE_CHECK_INSTANCE_CAST ((obj), GLADE_TYPE_PLACEHOLDER, GladePlaceholder))
#define GLADE_PLACEHOLDER_CLASS(klass)    (G_TYPE_CHECK_CLASS_CAST ((klass), GLADE_TYPE_PLACEHOLDER, GladePlaceholderClass))
#define GLADE_IS_PLACEHOLDER(obj)         (G_TYPE_CHECK_INSTANCE_TYPE ((obj), GLADE_TYPE_PLACEHOLDER))
#define GLADE_IS_PLACEHOLDER_CLASS(klass) (G_TYPE_CHECK_CLASS_TYPE ((klass), GLADE_TYPE_PLACEHOLDER))
#define GLADE_PLACEHOLDER_GET_CLASS(obj)  (G_TYPE_INSTANCE_GET_CLASS ((obj), GLADE_TYPE_PLACEHOLDER, GladePlaceholderClass))

typedef struct _GladePlaceholder      GladePlaceholder;
typedef struct _GladePlaceholderClass GladePlaceholderClass;

struct _GladePlaceholder
{
	GtkWidget widget;

	GdkPixmap *placeholder_pixmap;
	
	GList *packing_actions;
};

struct _GladePlaceholderClass
{
	GtkWidgetClass parent_class;
};


GType        glade_placeholder_get_type   (void) G_GNUC_CONST;

GtkWidget   *glade_placeholder_new        (void);

GladeProject* glade_placeholder_get_project (GladePlaceholder *placeholder);

GladeWidget *glade_placeholder_get_parent (GladePlaceholder *placeholder);

G_END_DECLS

#endif /* __GLADE_PLACEHOLDER_H__ */
