/* -*- Mode: C; tab-width: 8; indent-tabs-mode: t; c-basic-offset: 8 -*- */
/*
 * gtksourceundomanager.h
 * This file is part of GtkSourceView
 *
 * Copyright (C) 1998, 1999 Alex Roberts, Evan Lawrence
 * Copyright (C) 2000, 2001 Chema Celorio, Paolo Maggi
 * Copyright (C) 2002, 2003 Paolo Maggi
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2.1 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.

 * You should have received a copy of the GNU Lesser General Public
 * License along with this library; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
 */

#ifndef __GTK_SOURCE_UNDO_MANAGER_H__
#define __GTK_SOURCE_UNDO_MANAGER_H__

#include <gtk/gtk.h>

G_BEGIN_DECLS

#define GTK_TYPE_SOURCE_UNDO_MANAGER                (gtk_source_undo_manager_get_type ())
#define GTK_SOURCE_UNDO_MANAGER(obj)                (G_TYPE_CHECK_INSTANCE_CAST ((obj), GTK_TYPE_SOURCE_UNDO_MANAGER, GtkSourceUndoManager))
#define GTK_IS_SOURCE_UNDO_MANAGER(obj)             (G_TYPE_CHECK_INSTANCE_TYPE ((obj), GTK_TYPE_SOURCE_UNDO_MANAGER))
#define GTK_SOURCE_UNDO_MANAGER_GET_INTERFACE(obj)  (G_TYPE_INSTANCE_GET_INTERFACE ((obj), GTK_TYPE_SOURCE_UNDO_MANAGER, GtkSourceUndoManagerIface))

typedef struct _GtkSourceUndoManager        	GtkSourceUndoManager;
typedef struct _GtkSourceUndoManagerIface      	GtkSourceUndoManagerIface;

struct _GtkSourceUndoManagerIface
{
	GTypeInterface parent;

	/* Interface functions */
	gboolean (*can_undo)                  (GtkSourceUndoManager *manager);
	gboolean (*can_redo)                  (GtkSourceUndoManager *manager);

	void     (*undo)                      (GtkSourceUndoManager *manager);
	void     (*redo)                      (GtkSourceUndoManager *manager);

	void     (*begin_not_undoable_action) (GtkSourceUndoManager *manager);
	void     (*end_not_undoable_action)   (GtkSourceUndoManager *manager);

	/* Signals */
	void     (*can_undo_changed)          (GtkSourceUndoManager *manager);
	void     (*can_redo_changed)          (GtkSourceUndoManager *manager);
};

GType     gtk_source_undo_manager_get_type                  (void) G_GNUC_CONST;

gboolean  gtk_source_undo_manager_can_undo                  (GtkSourceUndoManager *manager);
gboolean  gtk_source_undo_manager_can_redo                  (GtkSourceUndoManager *manager);

void      gtk_source_undo_manager_undo                      (GtkSourceUndoManager *manager);
void      gtk_source_undo_manager_redo                      (GtkSourceUndoManager *manager);

void      gtk_source_undo_manager_begin_not_undoable_action (GtkSourceUndoManager *manager);
void      gtk_source_undo_manager_end_not_undoable_action   (GtkSourceUndoManager *manager);

void      gtk_source_undo_manager_can_undo_changed          (GtkSourceUndoManager *manager);
void      gtk_source_undo_manager_can_redo_changed          (GtkSourceUndoManager *manager);

G_END_DECLS

#endif /* __GTK_SOURCE_UNDO_MANAGER_H__ */


