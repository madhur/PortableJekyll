/* -*- Mode: C; tab-width: 8; indent-tabs-mode: t; c-basic-offset: 8; coding: utf-8 -*-
 *  gtksourcebuffer.c
 *
 *  Copyright (C) 2007 by:
 *		Johannes Schmid <jhs@gnome.org>
 *
 *  This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU Library General Public License as published by
 *  the Free Software Foundation; either version 2 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU Library General Public License for more details.
 *
 *  You should have received a copy of the GNU Library General Public License
 *  along with this program; if not, write to the Free Software
 *  Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
 */

#ifndef __GTKSOURCEMARK_H__
#define __GTKSOURCEMARK_H__

#include <gtk/gtk.h>

G_BEGIN_DECLS

#define GTK_TYPE_SOURCE_MARK             (gtk_source_mark_get_type ())
#define GTK_SOURCE_MARK(obj)             (G_TYPE_CHECK_INSTANCE_CAST ((obj), GTK_TYPE_SOURCE_MARK, GtkSourceMark))
#define GTK_SOURCE_MARK_CLASS(klass)     (G_TYPE_CHECK_CLASS_CAST ((klass), GTK_TYPE_SOURCE_MARK, GtkSourceMarkClass))
#define GTK_IS_SOURCE_MARK(obj)          (G_TYPE_CHECK_INSTANCE_TYPE ((obj), GTK_TYPE_SOURCE_MARK))
#define GTK_IS_SOURCE_MARK_CLASS(klass)  (G_TYPE_CHECK_CLASS_TYPE ((klass), GTK_TYPE_SOURCE_MARK))
#define GTK_SOURCE_MARK_GET_CLASS(obj)   (G_TYPE_INSTANCE_GET_CLASS ((obj), GTK_TYPE_SOURCE_MARK, GtkSourceMarkClass))

typedef struct _GtkSourceMark GtkSourceMark;
typedef struct _GtkSourceMarkClass GtkSourceMarkClass;

typedef struct _GtkSourceMarkPrivate GtkSourceMarkPrivate;

struct _GtkSourceMark
{
	GtkTextMark parent_instance;

	GtkSourceMarkPrivate *priv;
};

struct _GtkSourceMarkClass
{
	GtkTextMarkClass parent_class;

	/* Padding for future expansion */
	void (*_gtk_source_reserved1) (void);
	void (*_gtk_source_reserved2) (void);
};

GType		 gtk_source_mark_get_type (void) G_GNUC_CONST;

GtkSourceMark   *gtk_source_mark_new		(const gchar	*name, 
						 const gchar	*category);

const gchar	*gtk_source_mark_get_category	(GtkSourceMark	*mark);

GtkSourceMark	*gtk_source_mark_next		(GtkSourceMark	*mark,
						 const gchar	*category);
GtkSourceMark	*gtk_source_mark_prev		(GtkSourceMark	*mark,
						 const gchar	*category);

G_END_DECLS

#endif /* __GTKSOURCEMARK_H__ */
