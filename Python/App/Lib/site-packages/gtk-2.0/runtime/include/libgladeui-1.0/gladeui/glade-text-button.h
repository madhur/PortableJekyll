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
#ifndef _GLADE_TEXT_BUTTON_H_
#define _GLADE_TEXT_BUTTON_H_

#include <gtk/gtk.h>

G_BEGIN_DECLS

#define GLADE_TYPE_TEXT_BUTTON	            (glade_text_button_get_type ())
#define GLADE_TEXT_BUTTON(obj)		    (G_TYPE_CHECK_INSTANCE_CAST ((obj), GLADE_TYPE_TEXT_BUTTON, GladeTextButton))
#define GLADE_TEXT_BUTTON_CLASS(klass)	    (G_TYPE_CHECK_CLASS_CAST ((klass), GLADE_TYPE_TEXT_BUTTON, GladeTextButtonClass))
#define GLADE_IS_TEXT_BUTTON(obj)	    (G_TYPE_CHECK_INSTANCE_TYPE ((obj), GLADE_TYPE_TEXT_BUTTON))
#define GLADE_IS_TEXT_BUTTON_CLASS(klass)  (G_TYPE_CHECK_CLASS_TYPE ((klass), GLADE_TYPE_TEXT_BUTTON))
#define GLADE_TEXT_BUTTON_GET_CLASS(obj)   (G_TYPE_INSTANCE_GET_CLASS ((obj), GLADE_TYPE_TEXT_BUTTON, GladeTextTextClass))

typedef struct _GladeTextButton        GladeTextButton;
typedef struct _GladeTextButtonClass   GladeTextButtonClass;

struct _GladeTextButton
{
	GtkAlignment alignment;

	GtkWidget   *hbox;
	GtkWidget   *entry;
	GtkWidget   *button;
};

struct _GladeTextButtonClass
{
	GtkAlignmentClass parent;

	void   (*clicked)  (GladeTextButton *);
};

GType            glade_text_button_get_type (void);
GtkWidget       *glade_text_button_new      (void);

G_END_DECLS

#endif  /* _GLADE_TEXT_BUTTON_H_ */
