/* -*- Mode: C; tab-width: 8; indent-tabs-mode: t; c-basic-offset: 8; coding: utf-8 -*-
 *  gtksourcebuffer.h
 *
 *  Copyright (C) 1999,2000,2001,2002 by:
 *          Mikael Hermansson <tyan@linux.se>
 *          Chris Phelps <chicane@reninet.com>
 *          Jeroen Zwartepoorte <jeroen@xs4all.nl>
 *
 *  Copyright (C) 2003 - Paolo Maggi, Gustavo Giráldez
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

#ifndef __GTK_SOURCE_BUFFER_H__
#define __GTK_SOURCE_BUFFER_H__

#include <gtk/gtk.h>
#include <gtksourceview/gtksourcelanguage.h>
#include <gtksourceview/gtksourcemark.h>
#include <gtksourceview/gtksourcestylescheme.h>
#include <gtksourceview/gtksourceundomanager.h>

G_BEGIN_DECLS

#define GTK_TYPE_SOURCE_BUFFER            (gtk_source_buffer_get_type ())
#define GTK_SOURCE_BUFFER(obj)            (G_TYPE_CHECK_INSTANCE_CAST ((obj), GTK_TYPE_SOURCE_BUFFER, GtkSourceBuffer))
#define GTK_SOURCE_BUFFER_CLASS(klass)    (G_TYPE_CHECK_CLASS_CAST ((klass), GTK_TYPE_SOURCE_BUFFER, GtkSourceBufferClass))
#define GTK_IS_SOURCE_BUFFER(obj)         (G_TYPE_CHECK_INSTANCE_TYPE ((obj), GTK_TYPE_SOURCE_BUFFER))
#define GTK_IS_SOURCE_BUFFER_CLASS(klass) (G_TYPE_CHECK_CLASS_TYPE ((klass), GTK_TYPE_SOURCE_BUFFER))
#define GTK_SOURCE_BUFFER_GET_CLASS(obj)  (G_TYPE_INSTANCE_GET_CLASS ((obj), GTK_TYPE_SOURCE_BUFFER, GtkSourceBufferClass))

typedef struct _GtkSourceBuffer			GtkSourceBuffer;
typedef struct _GtkSourceBufferClass		GtkSourceBufferClass;
typedef struct _GtkSourceBufferPrivate		GtkSourceBufferPrivate;

struct _GtkSourceBuffer
{
	GtkTextBuffer parent_instance;

	GtkSourceBufferPrivate *priv;
};

struct _GtkSourceBufferClass
{
	GtkTextBufferClass parent_class;

	/* Signals */
	void (*undo) (GtkSourceBuffer *buffer);
	void (*redo) (GtkSourceBuffer *buffer);

	/* Padding for future expansion */
	void (*_gtk_source_reserved1) (void);
	void (*_gtk_source_reserved2) (void);
	void (*_gtk_source_reserved3) (void);
	void (*_gtk_source_reserved4) (void);
};

GType           	 gtk_source_buffer_get_type 		(void) G_GNUC_CONST;


/* Constructor */
GtkSourceBuffer	 	*gtk_source_buffer_new 			(GtkTextTagTable        *table);
GtkSourceBuffer 	*gtk_source_buffer_new_with_language 	(GtkSourceLanguage      *language);

/* Properties */
gboolean		 gtk_source_buffer_get_highlight_syntax	(GtkSourceBuffer        *buffer);
void			 gtk_source_buffer_set_highlight_syntax	(GtkSourceBuffer        *buffer,
								 gboolean                highlight);

gboolean		 gtk_source_buffer_get_highlight_matching_brackets
								(GtkSourceBuffer        *buffer);
void			 gtk_source_buffer_set_highlight_matching_brackets
								(GtkSourceBuffer        *buffer,
							       	 gboolean                highlight);

gint			 gtk_source_buffer_get_max_undo_levels	(GtkSourceBuffer        *buffer);
void			 gtk_source_buffer_set_max_undo_levels	(GtkSourceBuffer        *buffer,
							    	 gint                    max_undo_levels);

GtkSourceLanguage 	*gtk_source_buffer_get_language 	(GtkSourceBuffer        *buffer);
void			 gtk_source_buffer_set_language 	(GtkSourceBuffer        *buffer,
								 GtkSourceLanguage      *language);

gboolean		 gtk_source_buffer_can_undo		(GtkSourceBuffer        *buffer);
gboolean		 gtk_source_buffer_can_redo		(GtkSourceBuffer        *buffer);

GtkSourceStyleScheme    *gtk_source_buffer_get_style_scheme     (GtkSourceBuffer        *buffer);
void			 gtk_source_buffer_set_style_scheme     (GtkSourceBuffer        *buffer,
								 GtkSourceStyleScheme   *scheme);

/* Force highlighting */
void			 gtk_source_buffer_ensure_highlight     (GtkSourceBuffer        *buffer,
								 const GtkTextIter      *start,
								 const GtkTextIter      *end);

/* Undo/redo methods */
void			 gtk_source_buffer_undo			(GtkSourceBuffer        *buffer);
void			 gtk_source_buffer_redo			(GtkSourceBuffer        *buffer);

void			 gtk_source_buffer_begin_not_undoable_action (GtkSourceBuffer   *buffer);
void			 gtk_source_buffer_end_not_undoable_action   (GtkSourceBuffer   *buffer);

/* Mark methods */
GtkSourceMark		*gtk_source_buffer_create_source_mark	(GtkSourceBuffer        *buffer,
								 const gchar            *name,
								 const gchar            *category,
								 const GtkTextIter      *where);
gboolean		 gtk_source_buffer_forward_iter_to_source_mark
								(GtkSourceBuffer        *buffer,
								 GtkTextIter            *iter,
								 const gchar            *category);
gboolean		 gtk_source_buffer_backward_iter_to_source_mark
								(GtkSourceBuffer        *buffer,
								 GtkTextIter            *iter,
								 const gchar            *category);
GSList			*gtk_source_buffer_get_source_marks_at_iter
								(GtkSourceBuffer        *buffer,
								 GtkTextIter            *iter,
								 const gchar            *category);
GSList			*gtk_source_buffer_get_source_marks_at_line
								(GtkSourceBuffer        *buffer,
								 gint 			 line,
								 const gchar		*category);
void			 gtk_source_buffer_remove_source_marks	(GtkSourceBuffer        *buffer,
								 const GtkTextIter      *start,
								 const GtkTextIter      *end,
								 const gchar            *category);

gboolean		 gtk_source_buffer_iter_has_context_class
								(GtkSourceBuffer	*buffer,
								 const GtkTextIter	*iter,
								 const gchar            *context_class);

gchar			**gtk_source_buffer_get_context_classes_at_iter
								(GtkSourceBuffer	*buffer,
								 const GtkTextIter	*iter);

gboolean		 gtk_source_buffer_iter_forward_to_context_class_toggle
								(GtkSourceBuffer	*buffer,
								 GtkTextIter		*iter,
								 const gchar		*context_class);

gboolean		 gtk_source_buffer_iter_backward_to_context_class_toggle
								(GtkSourceBuffer	*buffer,
								 GtkTextIter		*iter,
								 const gchar		*context_class);

GtkSourceUndoManager	*gtk_source_buffer_get_undo_manager	(GtkSourceBuffer	*buffer);
void			 gtk_source_buffer_set_undo_manager	(GtkSourceBuffer	*buffer,
								 GtkSourceUndoManager	*manager);

/* private */
void			 _gtk_source_buffer_update_highlight	(GtkSourceBuffer        *buffer,
								 const GtkTextIter      *start,
								 const GtkTextIter      *end,
								 gboolean                synchronous);

GtkSourceMark		*_gtk_source_buffer_source_mark_next	(GtkSourceBuffer        *buffer,
								 GtkSourceMark          *mark, 
								 const gchar            *category);
GtkSourceMark		*_gtk_source_buffer_source_mark_prev	(GtkSourceBuffer        *buffer,
								 GtkSourceMark          *mark, 
								 const gchar            *category);

GtkTextTag		*_gtk_source_buffer_get_bracket_match_tag (GtkSourceBuffer        *buffer);

G_END_DECLS

#endif /* __GTK_SOURCE_BUFFER_H__ */
