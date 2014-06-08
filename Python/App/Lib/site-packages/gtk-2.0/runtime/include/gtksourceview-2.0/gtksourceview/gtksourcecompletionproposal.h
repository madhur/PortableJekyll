/* -*- Mode: C; tab-width: 8; indent-tabs-mode: t; c-basic-offset: 8; coding: utf-8 -*-
 * gtksourcecompletionproposal.h
 * This file is part of gtksourcecompletion
 *
 * Copyright (C) 2007 - 2009 Jesús Barbero Rodríguez <chuchiperriman@gmail.com>
 * Copyright (C) 2009 - Jesse van den Kieboom <jessevdk@gnome.org>
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

#ifndef __GTK_SOURCE_COMPLETION_PROPOSAL_H__
#define __GTK_SOURCE_COMPLETION_PROPOSAL_H__

#include <glib-object.h>
#include <gdk-pixbuf/gdk-pixbuf.h>

G_BEGIN_DECLS

#define GTK_TYPE_SOURCE_COMPLETION_PROPOSAL			(gtk_source_completion_proposal_get_type ())
#define GTK_SOURCE_COMPLETION_PROPOSAL(obj)			(G_TYPE_CHECK_INSTANCE_CAST ((obj), GTK_TYPE_SOURCE_COMPLETION_PROPOSAL, GtkSourceCompletionProposal))
#define GTK_IS_SOURCE_COMPLETION_PROPOSAL(obj)			(G_TYPE_CHECK_INSTANCE_TYPE ((obj), GTK_TYPE_SOURCE_COMPLETION_PROPOSAL))
#define GTK_SOURCE_COMPLETION_PROPOSAL_GET_INTERFACE(obj)	(G_TYPE_INSTANCE_GET_INTERFACE ((obj), GTK_TYPE_SOURCE_COMPLETION_PROPOSAL, GtkSourceCompletionProposalIface))

typedef struct _GtkSourceCompletionProposal		GtkSourceCompletionProposal;
typedef struct _GtkSourceCompletionProposalIface	GtkSourceCompletionProposalIface;

struct _GtkSourceCompletionProposalIface
{
	GTypeInterface parent;
	
	/* Interface functions */
	gchar		*(*get_label)	(GtkSourceCompletionProposal *proposal);
	gchar		*(*get_markup)	(GtkSourceCompletionProposal *proposal);
	gchar		*(*get_text)	(GtkSourceCompletionProposal *proposal);
	
	GdkPixbuf	*(*get_icon)	(GtkSourceCompletionProposal *proposal);
	gchar		*(*get_info)	(GtkSourceCompletionProposal *proposal);
	
	guint		 (*hash)	(GtkSourceCompletionProposal *proposal);
	gboolean	 (*equal)	(GtkSourceCompletionProposal *proposal,
					 GtkSourceCompletionProposal *other);
	
	/* Signals */
	void		 (*changed)	(GtkSourceCompletionProposal *proposal);
};

GType 			 gtk_source_completion_proposal_get_type 	(void) G_GNUC_CONST;

gchar			*gtk_source_completion_proposal_get_label	(GtkSourceCompletionProposal *proposal);
gchar			*gtk_source_completion_proposal_get_markup	(GtkSourceCompletionProposal *proposal);
gchar			*gtk_source_completion_proposal_get_text	(GtkSourceCompletionProposal *proposal);

GdkPixbuf		*gtk_source_completion_proposal_get_icon	(GtkSourceCompletionProposal *proposal);
gchar			*gtk_source_completion_proposal_get_info	(GtkSourceCompletionProposal *proposal);

void			 gtk_source_completion_proposal_changed		(GtkSourceCompletionProposal *proposal);

guint			 gtk_source_completion_proposal_hash		(GtkSourceCompletionProposal *proposal);
gboolean		 gtk_source_completion_proposal_equal           (GtkSourceCompletionProposal *proposal,
									 GtkSourceCompletionProposal *other);

G_END_DECLS

#endif /* __GTK_SOURCE_COMPLETION_PROPOSAL_H__ */
