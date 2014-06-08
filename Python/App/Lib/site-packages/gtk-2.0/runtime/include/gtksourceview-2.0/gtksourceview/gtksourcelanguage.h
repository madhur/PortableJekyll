/* -*- Mode: C; tab-width: 8; indent-tabs-mode: t; c-basic-offset: 8; coding: utf-8 -*-
 *  gtksourcelanguage.h
 *
 *  Copyright (C) 2003 - Paolo Maggi <paolo.maggi@polito.it>
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

#ifndef __GTK_SOURCE_LANGUAGE_H__
#define __GTK_SOURCE_LANGUAGE_H__

#include <glib.h>
#include <glib-object.h>
#include <gtk/gtk.h>

G_BEGIN_DECLS

#define GTK_TYPE_SOURCE_LANGUAGE		(gtk_source_language_get_type ())
#define GTK_SOURCE_LANGUAGE(obj)		(G_TYPE_CHECK_INSTANCE_CAST((obj), GTK_TYPE_SOURCE_LANGUAGE, GtkSourceLanguage))
#define GTK_SOURCE_LANGUAGE_CLASS(klass)	(G_TYPE_CHECK_CLASS_CAST((klass), GTK_TYPE_SOURCE_LANGUAGE, GtkSourceLanguageClass))
#define GTK_IS_SOURCE_LANGUAGE(obj)		(G_TYPE_CHECK_INSTANCE_TYPE((obj), GTK_TYPE_SOURCE_LANGUAGE))
#define GTK_IS_SOURCE_LANGUAGE_CLASS(klass)	(G_TYPE_CHECK_CLASS_TYPE ((klass), GTK_TYPE_SOURCE_LANGUAGE))
#define GTK_SOURCE_LANGUAGE_GET_CLASS(obj)      (G_TYPE_INSTANCE_GET_CLASS ((obj), GTK_TYPE_SOURCE_LANGUAGE, GtkSourceLanguageClass))


typedef struct _GtkSourceLanguage		GtkSourceLanguage;
typedef struct _GtkSourceLanguageClass		GtkSourceLanguageClass;
typedef struct _GtkSourceLanguagePrivate	GtkSourceLanguagePrivate;

struct _GtkSourceLanguage
{
	GObject parent_instance;

	GtkSourceLanguagePrivate *priv;
};

struct _GtkSourceLanguageClass
{
	GObjectClass              parent_class;

	/* Padding for future expansion */
	void (*_gtk_source_reserved1) (void);
	void (*_gtk_source_reserved2) (void);
};

GType             gtk_source_language_get_type 		(void) G_GNUC_CONST;

const gchar 	 *gtk_source_language_get_id		(GtkSourceLanguage *language);

const gchar 	 *gtk_source_language_get_name		(GtkSourceLanguage *language);

const gchar	 *gtk_source_language_get_section	(GtkSourceLanguage *language);

gboolean	  gtk_source_language_get_hidden 	(GtkSourceLanguage *language);

const gchar	 *gtk_source_language_get_metadata	(GtkSourceLanguage *language,
							 const gchar       *name);

gchar		**gtk_source_language_get_mime_types	(GtkSourceLanguage *language);

gchar		**gtk_source_language_get_globs		(GtkSourceLanguage *language);

gchar		**gtk_source_language_get_style_ids 	(GtkSourceLanguage *language);

const gchar	*gtk_source_language_get_style_name	(GtkSourceLanguage *language,
							 const gchar       *style_id);

G_END_DECLS

#endif /* __GTK_SOURCE_LANGUAGE_H__ */

