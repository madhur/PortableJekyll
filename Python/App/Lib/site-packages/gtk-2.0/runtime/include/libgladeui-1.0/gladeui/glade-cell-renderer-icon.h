/* -*- Mode: C; tab-width: 8; indent-tabs-mode: t; c-basic-offset: 8 -*- */
/*
 * Copyright (C) 2010 Tristan Van Berkom.
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

#ifndef __GLADE_CELL_RENDERER_ICON_H__
#define __GLADE_CELL_RENDERER_ICON_H__

#include <gtk/gtk.h>


G_BEGIN_DECLS


#define GLADE_TYPE_CELL_RENDERER_ICON			(glade_cell_renderer_icon_get_type ())
#define GLADE_CELL_RENDERER_ICON(obj)			(G_TYPE_CHECK_INSTANCE_CAST ((obj), GLADE_TYPE_CELL_RENDERER_ICON, GladeCellRendererIcon))
#define GLADE_CELL_RENDERER_ICON_CLASS(klass)		(G_TYPE_CHECK_CLASS_CAST ((klass), GLADE_TYPE_CELL_RENDERER_ICON, GladeCellRendererIconClass))
#define GLADE_IS_CELL_RENDERER_ICON(obj)		(G_TYPE_CHECK_INSTANCE_TYPE ((obj), GLADE_TYPE_CELL_RENDERER_ICON))
#define GLADE_IS_CELL_RENDERER_ICON_CLASS(klass)	(G_TYPE_CHECK_CLASS_TYPE ((klass), GLADE_TYPE_CELL_RENDERER_ICON))
#define GLADE_CELL_RENDERER_ICON_GET_CLASS(obj)         (G_TYPE_INSTANCE_GET_CLASS ((obj), GLADE_TYPE_CELL_RENDERER_ICON, GladeCellRendererIconClass))

typedef struct _GladeCellRendererIcon GladeCellRendererIcon;
typedef struct _GladeCellRendererIconClass GladeCellRendererIconClass;

struct _GladeCellRendererIcon
{
  GtkCellRendererPixbuf parent;

  guint active : 1;
  guint activatable : 1;
};

struct _GladeCellRendererIconClass
{
  GtkCellRendererPixbufClass parent_class;

  void (* activate) (GladeCellRendererIcon *cell_renderer_icon,
		     const gchar         *path);
};

GType            glade_cell_renderer_icon_get_type       (void) G_GNUC_CONST;
GtkCellRenderer *glade_cell_renderer_icon_new            (void);

gboolean        glade_cell_renderer_icon_get_active      (GladeCellRendererIcon *icon);
void            glade_cell_renderer_icon_set_active      (GladeCellRendererIcon *icon,
							  gboolean               setting);

gboolean        glade_cell_renderer_icon_get_activatable (GladeCellRendererIcon *icon);
void            glade_cell_renderer_icon_set_activatable (GladeCellRendererIcon *icon,
							  gboolean               setting);


G_END_DECLS

#endif /* __GLADE_CELL_RENDERER_ICON_H__ */
