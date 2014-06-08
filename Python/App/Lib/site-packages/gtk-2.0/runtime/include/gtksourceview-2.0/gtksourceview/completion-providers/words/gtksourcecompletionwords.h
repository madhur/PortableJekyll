/* -*- Mode: C; tab-width: 8; indent-tabs-mode: t; c-basic-offset: 8; coding: utf-8 -*-
 * gtksourcecompletionproviderwords.h
 * This file is part of gtksourceview
 *
 * Copyright (C) 2009 - Jesse van den Kieboom
 *
 * gtksourceview is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * gtksourceview is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with gtksourceview; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin St, Fifth Floor, 
 * Boston, MA  02110-1301  USA
 */

#ifndef __GTK_SOURCE_COMPLETION_WORDS_H__
#define __GTK_SOURCE_COMPLETION_WORDS_H__

#include <gtksourceview/gtksourcecompletionprovider.h>
#include <gtk/gtk.h>

G_BEGIN_DECLS

#define GTK_TYPE_SOURCE_COMPLETION_WORDS				(gtk_source_completion_words_get_type ())
#define GTK_SOURCE_COMPLETION_WORDS(obj)		(G_TYPE_CHECK_INSTANCE_CAST ((obj), GTK_TYPE_SOURCE_COMPLETION_WORDS, GtkSourceCompletionWords))
#define GTK_SOURCE_COMPLETION_WORDS_CONST(obj)		(G_TYPE_CHECK_INSTANCE_CAST ((obj), GTK_TYPE_SOURCE_COMPLETION_WORDS, GtkSourceCompletionWords const))
#define GTK_SOURCE_COMPLETION_WORDS_CLASS(klass)	(G_TYPE_CHECK_CLASS_CAST ((klass), GTK_TYPE_SOURCE_COMPLETION_WORDS, GtkSourceCompletionWordsClass))
#define GTK_IS_SOURCE_COMPLETION_WORDS(obj)		(G_TYPE_CHECK_INSTANCE_TYPE ((obj), GTK_TYPE_SOURCE_COMPLETION_WORDS))
#define GTK_IS_SOURCE_COMPLETION_WORDS_CLASS(klass)	(G_TYPE_CHECK_CLASS_TYPE ((klass), GTK_TYPE_SOURCE_COMPLETION_WORDS))
#define GTK_SOURCE_COMPLETION_WORDS_GET_CLASS(obj)	(G_TYPE_INSTANCE_GET_CLASS ((obj), GTK_TYPE_SOURCE_COMPLETION_WORDS, GtkSourceCompletionWordsClass))

typedef struct _GtkSourceCompletionWords		GtkSourceCompletionWords;
typedef struct _GtkSourceCompletionWordsClass		GtkSourceCompletionWordsClass;
typedef struct _GtkSourceCompletionWordsPrivate		GtkSourceCompletionWordsPrivate;

struct _GtkSourceCompletionWords {
	GObject parent;
	
	GtkSourceCompletionWordsPrivate *priv;
};

struct _GtkSourceCompletionWordsClass {
	GObjectClass parent_class;
};

GType gtk_source_completion_words_get_type (void) G_GNUC_CONST;

GtkSourceCompletionWords *
		gtk_source_completion_words_new 	(const gchar              *name,
		                                         GdkPixbuf                *icon);
		
void 		gtk_source_completion_words_register 	(GtkSourceCompletionWords *words,
                                                         GtkTextBuffer            *buffer);

void 		gtk_source_completion_words_unregister 	(GtkSourceCompletionWords *words,
                                                         GtkTextBuffer            *buffer);

G_END_DECLS

#endif /* __GTK_SOURCE_COMPLETION_WORDS_H__ */
