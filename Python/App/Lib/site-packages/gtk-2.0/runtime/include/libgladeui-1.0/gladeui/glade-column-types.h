/* -*- Mode: C; tab-width: 8; indent-tabs-mode: t; c-basic-offset: 8 -*- */
/*
 * Copyright (C) 2008 Juan Pablo Ugarte.
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
 *   Juan Pablo Ugarte <juanpablougarte@gmail.com>
 */
#ifndef _GLADE_COLUMN_TYPES_H_
#define _STV_CAP_H_

#include <glib.h>

G_BEGIN_DECLS

typedef struct
{
	gchar *type_name;
	gchar *column_name;
} GladeColumnType;

#define	GLADE_TYPE_COLUMN_TYPE_LIST   (glade_column_type_list_get_type())
#define GLADE_TYPE_EPROP_COLUMN_TYPES (glade_eprop_column_types_get_type())

GType        glade_column_type_list_get_type      (void) G_GNUC_CONST;
GType        glade_eprop_column_types_get_type    (void) G_GNUC_CONST;

void         glade_column_list_free               (GList *list);
GList       *glade_column_list_copy               (GList *list);

GladeColumnType *glade_column_type_new            (const gchar *type_name,
						   const gchar *column_name);
void             glade_column_type_free           (GladeColumnType *column);
GladeColumnType *glade_column_list_find_column    (GList *list, const gchar *column_name);

G_END_DECLS

#endif /* _GLADE_COLUMN_TYPES_H_ */
